import logging
from typing import Optional, MutableMapping, Any, TYPE_CHECKING

from cloudformation_cli_python_lib.interface import ProgressEvent
from cloudformation_cli_python_lib.boto3_proxy import SessionProxy
from cf_extension_core import CustomResourceHelpers, BaseHandler

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
else:
    DynamoDBServiceResource = object


# Locals
from .models import ResourceModel, ResourceHandlerRequest

# from .common import Common
from .read_handler import ReadHandler


LOG = logging.getLogger(__name__)


class CreateHandler(BaseHandler[ResourceModel, ResourceHandlerRequest]):
    def __init__(
        self,
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_name: str,
        db_resource: DynamoDBServiceResource,
        total_timeout_in_minutes: int,
    ):
        LOG.info("CreateHandler Constructor")
        assert session is not None

        super().__init__(
            session=session,
            request=request,
            callback_context=callback_context,
            type_name=type_name,
            db_resource=db_resource,
            total_timeout_in_minutes=total_timeout_in_minutes,
            cf_core_log_level=logging.DEBUG,
        )

    def execute(self) -> ProgressEvent:
        # Creation of resource
        with self.create_resource() as DB:
            if self._create_action1():
                # Get model from callback context and save to DB and return to make sure CF knows we created a resource
                saved_model = self.get_model_from_callback()
                DB.set_resource_created(
                    primary_identifier=self.validate_identifier(saved_model.GeneratedId),
                    current_model=saved_model,
                )
                return self.return_in_progress_event(message="Resource created, stabilizing", call_back_delay_seconds=4)

            # Stabilize
            # Run continuously until we can do a read
            LOG.info("Stabilizing Resource")
            pe = self.run_call_chain_with_stabilization(
                func_list=[
                    lambda: self._stabilize_resource_creation(),
                ],
                in_progress_model=self.get_model_from_callback(),
                func_retries_sleep_time=5,
            )
            if pe is not None:
                return pe

        # Creation code complete
        # Run read handler and return
        return ReadHandler(
            session=self.session,
            request=self.request,
            callback_context=self.callback_context,
            type_name=self.type_name,
            db_resource=self.db_resource,
            total_timeout_in_minutes=self.total_timeout_in_minutes,
        ).execute()

    def _create_action1(self) -> bool:
        if "_create_action1" not in self.callback_context:
            # Create Resource - hasnt been done yet

            # In ANY resource - these lines should be right next to each other.
            # Where-ever the primaryIdentifier is created/read is set, it should be set both in the
            # MODEL and the callback at the same time.

            generated_ro_id = CustomResourceHelpers.generate_id_read_only_resource(
                stack_id=self.request.stackId,
                logical_resource_id=self.request.logicalResourceIdentifier,
            )

            model = self.request.desiredResourceState
            assert model is not None
            model.GeneratedId = generated_ro_id

            self.callback_context["_create_action1"] = True
            self.save_model_to_callback(model)
            return True
        else:
            return False

    def _stabilize_resource_creation(self) -> bool:
        if "_stabilize_resource_creation" not in self.callback_context:
            LOG.info("Performing stabilization")

            # TODO: Put calls in here waiting for resource to get to desired state.

            # If desired state reached
            self.callback_context["_stabilize_resource_creation"] = True
            return True

            # if desired state not reached
            # return False
        else:
            # Already stabilized
            return True
