import logging
from typing import Optional, MutableMapping, Any, TYPE_CHECKING

from cloudformation_cli_python_lib.interface import ProgressEvent
from cloudformation_cli_python_lib.boto3_proxy import SessionProxy
from cf_extension_core import BaseHandler

# Locals
from .models import ResourceModel, ResourceHandlerRequest

LOG = logging.getLogger(__name__)

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
else:
    DynamoDBServiceResource = object


class DeleteHandler(BaseHandler[ResourceModel, ResourceHandlerRequest]):
    def __init__(
        self,
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_name: str,
        db_resource: DynamoDBServiceResource,
        total_timeout_in_minutes: int,
    ):
        LOG.info("DeleteHandler Constructor")
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
        # Validates a row exists - otherwise fail out with a NotFound
        assert self.request.desiredResourceState is not None
        identifier = self.validate_identifier(self.request.desiredResourceState.GeneratedId)

        with self.delete_resource(primary_identifier=identifier) as DB:
            # Use DB Model
            db_model: ResourceModel = DB.read_model(model_type=ResourceModel)

            if self._delete_resource():
                self.save_model_to_callback(db_model)
                return self.return_in_progress_event(message="Resource deleted, stabilizing", call_back_delay_seconds=1)

            # Stabilize
            LOG.info("Stabilizing resource deletion")
            pe = self.run_call_chain_with_stabilization(
                func_list=[
                    lambda: self._stabilize_resource_deletion(),
                ],
                in_progress_model=db_model,
                func_retries_sleep_time=5,
            )
            if pe is not None:
                return pe
            LOG.info("Resource Stabilization completed")

            # Now we can mark deletion since it is stabilized
            DB.set_resource_deleted()

            return self.return_success_delete_event()

    def _delete_resource(self) -> bool:
        if "_delete_resource" not in self.callback_context:
            # TODO: Code to delete the resource

            self.callback_context["_delete_resource"] = True

            return True
        else:
            return False

    def _stabilize_resource_deletion(self) -> bool:
        if "_stabilize_resource_deletion" not in self.callback_context:
            # TODO: Put calls in here waiting for resource to get to desired state.

            # If desired state reached
            self.callback_context["_stabilize_resource_deletion"] = True
            return True

            # if desired state not reached
            # return False

        else:
            # If more stabilization is needed by another method in call chain
            return True
