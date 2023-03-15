import logging
from typing import Optional, MutableMapping, Any, TYPE_CHECKING

from cloudformation_cli_python_lib.interface import ProgressEvent
from cloudformation_cli_python_lib.boto3_proxy import SessionProxy
from cf_extension_core import BaseHandler, CustomResourceHelpers

if TYPE_CHECKING:
    from mypy_boto3_dynamodb.service_resource import DynamoDBServiceResource
else:
    DynamoDBServiceResource = object


# Locals
from .models import ResourceModel, ResourceHandlerRequest

# from .common import Common
from .read_handler import ReadHandler

LOG = logging.getLogger(__name__)


class UpdateHandler(BaseHandler[ResourceModel, ResourceHandlerRequest]):
    def __init__(
        self,
        session: Optional[SessionProxy],
        request: ResourceHandlerRequest,
        callback_context: MutableMapping[str, Any],
        type_name: str,
        db_resource: DynamoDBServiceResource,
        total_timeout_in_minutes: int,
    ):
        LOG.info("UpdateHandler Constructor")
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
        desired_state = self.request.desiredResourceState
        assert desired_state is not None

        # get the primary identifier
        primary_identifier = self.validate_identifier(desired_state.GeneratedId)

        # Update of resource
        with self.update_resource(primary_identifier=primary_identifier) as DB:
            # Get naked resource identifier
            resource_identifier = CustomResourceHelpers.get_naked_resource_identifier_from_string(
                primary_identifier=primary_identifier
            )
            LOG.debug(resource_identifier)

            # Read DB Model
            db_model: ResourceModel = DB.read_model(ResourceModel)

            # Handle inconsistencies of AWS Framework and CF to guarantee contract
            self._set_variables(desired_state=desired_state, db_model=db_model)

            # Perform update
            self._update_action_1()
            # self._update_action_2()
            # etc

            # Stabilize
            pe = self.run_call_chain_with_stabilization(
                func_list=[lambda: self._update_stabilization()],
                in_progress_model=desired_state,
                func_retries_sleep_time=5,
            )
            if pe is not None:
                return pe

            # Using wherever the most up to date model is, update the DB Tier
            saved_model = self.get_model_from_callback()
            DB.update_model(updated_model=saved_model)

        # Run read handler and return
        return ReadHandler(
            session=self.session,
            request=self.request,
            callback_context=self.callback_context,
            type_name=self.type_name,
            db_resource=self.db_resource,
            total_timeout_in_minutes=self.total_timeout_in_minutes,
        ).execute()

    def _update_action_1(self) -> None:
        if "_update_action_1" not in self.callback_context:
            # TODO - API Code to update the resource
            self.callback_context["_update_action_1"] = True

    def _set_variables(self, desired_state: ResourceModel, db_model: ResourceModel) -> None:
        # CreateOnly Properties MUST be the same in an UPDATE
        # Lets guarantee that by pulling from DB tier and setting them.
        # This also solves if AWS framework has any inconsistencies with the Contract tests.
        # It also forces honoring of contract - no matter what end user puts in.
        # This might yield unexpected results but it guarantees following the contract the developer intended.
        # We could make this better user facing by doing a comparison and outputting an error, but since
        # contract test randomly break this - it is hard to do a one size fits all implementation.

        # TODO: fill out variables here
        pass

        # Apparently non-create-only properties are not guaranteed if they dont change?
        # So if we need the RO property set - we should do it here.  Just not the Primary Identifier, that is provided
        # TODO: fill out variables here

    def _update_stabilization(self) -> bool:
        if "_update_stabilization" not in self.callback_context:
            # TODO: Put calls in here waiting for resource to get to desired state.

            # If desired state reached
            self.callback_context["_update_stabilization"] = True
            return True

            # if desired state not reached
            # return False

        else:
            # If more stabilization is needed by another method in call chain
            return True
