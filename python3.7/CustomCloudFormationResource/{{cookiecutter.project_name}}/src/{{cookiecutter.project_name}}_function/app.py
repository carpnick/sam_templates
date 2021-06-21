# pylint: disable=W0613,W0703, E0611, C0103
"""
Initial file called from Cloud Formation via Lambda
"""

import logging
from crhelper import CfnResource
import eliza_cf_custom_resource_common
from {{cookiecutter.project_name}}_function.input import InputObject

logger = logging.getLogger(__name__)
eliza_cf_custom_resource_common.resource_default_logging_config()

##################################################################################
# START BOILER PLATE
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL', sleep_on_delete=0)

def lambda_handler(event, context):
    """
    Integration with CloudFormation using the helper
    """
    eliza_cf_custom_resource_common.resource_entrypoint(helper, event, context)

# END BOILER PLATE
##################################################################################


@helper.create
def handle_create(event, context):
    """
    Create the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Create")

    if eliza_cf_custom_resource_common.item_exists_successful(helper=helper, event=event):
        return
    else:
        with eliza_cf_custom_resource_common.resource_create(event=event) as DB:


            new_input = InputObject(event["ResourceProperties"]) #pylint: disable=W0612

            ##TODO: Put in your implementation logic here to create a new resource. # pylint: disable=W0511

            # This return value equals the PhysicalResourceId for your resource you created
            # This should be set in the implementation above as soon as the resource is created
            #  even if you are waiting for the resource to stabilize
            event['PhysicalResourceId'] = "None"

            DB.db_set_item_helper_data(helper.Data)


@helper.update
def handle_update(event, context):
    """
    Create the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Update")

    if eliza_cf_custom_resource_common.item_exists_successful(helper=helper, event=event):
        return
    else:
        # Parse params
        old_input = InputObject(event["OldResourceProperties"]) #pylint: disable=W0612
        new_input = InputObject(event["ResourceProperties"]) #pylint: disable=W0612

        #Choose one of the following based on your resource:
        #Choose one of the following based on your resource:

        # #Case 1 - Both create a new one and updating an existing one is supported
        # with eliza_cf_custom_resource_common.resource_update(event=event) as DB:
        #     if InputObject.new_resource_required(old_input, new_input):
        #         logger.info("Detected new resource is required, performing create instead")
        #         myevent = DB.set_update_is_a_replacement()
        #         handle_create(myevent, context)
        #     else:
        #         logger.info("Update allowed, no new resource is required, performing update")
        #         myevent = DB.set_update_is_update_only()
        #
        #         #Generate clients, class implemenation logics here.
        #         #TODO: If your custom resource does not have a method of is_in_desired_state, create one.  Sample can be found in sample repository # pylint: disable=W0511
        #         if impl.is_in_desired_state(helper=helper, new_input=new_input):
        #             DB.db_set_item_helper_data(helper.Data)
        #             #Nothing to do
        #         else:
        #             impl.update_route(new_input)
        #             DB.db_set_item_helper_data(helper.Data)

        # ############################################################################################################

        # #Case 2 - Create a new one is supported and updating an existing one is not supported
        # with eliza_cf_custom_resource_common.resource_update(event=event) as DB:
        #     if InputObject.new_resource_required(old_input, new_input):
        #         logger.info("Detected new resource is required, performing create instead")
        #         myevent = DB.set_update_is_a_replacement()
        #         handle_create(myevent, context)
        #     else:
        #         myevent = DB.set_update_is_update_only()
        #         impl = MyImplClass()
        #         if impl.is_in_desired_state(helper=helper, new_input=new_input):
        #             DB.db_set_item_helper_data(helper.Data)
        #             #Nothing to do
        #         else:
        #             logger.info("Update not supported, raising exception")
        #             raise NotImplementedError("Cannot update - No update API exists")
        #
        #   ##
        #   #Or if there is no way to rollback properly (aka an update is always net new - ACM as an example)
        #   ##
        #   with eliza_cf_custom_resource_common.resource_update(event=event) as DB:
        #       myevent = DB.set_update_is_a_replacement()
        #       logger.info("Detected new resource is required, performing create instead")
        #       handle_create(myevent, context)
        #
        # ############################################################################################################

        # #Case 3 - Create a new one is not supported and updating an existing one is supported
        # with eliza_cf_custom_resource_common.resource_update(event=event) as DB:
        #     if InputObject.new_resource_required(old_input, new_input):
        #         logger.info("Cannot create a new resource, raising an exception...")
        #         raise NotImplementedError("Cannot update - Cannot create a new instance of resource.  Please undeploy and redeploy manually")
        #     else:
        #         logger.info("Update allowed, no new resource is required, performing update")
        #         myevent = DB.set_update_is_update_only()
        #
        #         #Generate clients, class implemenation logics here.
        #         #TODO: If your custom resource does not have a method of is_in_desired_state, create one.  Sample can be found in sample repository # pylint: disable=W0511
        #         if impl.is_in_desired_state(helper=helper, new_input=new_input):
        #             DB.db_set_item_helper_data(helper.Data)
        #             #Nothing to do
        #         else:
        #             impl.update_route(new_input)
        #             DB.db_set_item_helper_data(helper.Data)

        # ############################################################################################################

        # #Case 4 - Create a new one is not supported and updating an existing one is not supported
        # with eliza_cf_custom_resource_common.resource_update(event=event) as DB:
        #     if impl.is_in_desired_state(helper=helper, new_input=new_input):
        #         myevent = DB.set_update_is_update_only()
        #         DB.db_set_item_helper_data(helper.Data)
        #     else:
        #         raise NotImplementedError("Cannot update - Please undeploy and redeploy manually.  Neither updating or creating a new one is supported.  Is a singleton only") # pylint: disable=C0301

        # ############################################################################################################

        # #Case 5 - There is no difference between doing an update and creating a new one - IE think read only custom resources.  These have static HARD CODED returned physical resource id's like "NONE" # pylint: disable=C0301

        # with eliza_cf_custom_resource_common.resource_update(event=event) as DB:
        #     logger.info("Update allowed, no new resource is required, performing update")
        #     my_event = DB.set_update_is_update_only()
        #     handle_create(my_event, context)


@helper.delete
def handle_delete(event, context):
    """
    Deletes the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Delete")

    with eliza_cf_custom_resource_common.resource_delete(event=event) as DB:

        # If the params are invalid, the resource never created so no rows should exist - not adding any validation for now.
        if InputObject.params_are_invalid(event["ResourceProperties"]):
            logger.info("Params are invalid, assuming nothing to delete since invalid parameters cannot run properly anyways")
            return

        new_input = InputObject(event["ResourceProperties"]) # pylint: disable=W0612

        #TODO: Implementation logic

        # New implementation
        if DB.db_item_exists():
            logger.info("New delete code activated")
            #TODO: Delete logic
        else:
            # So this gets activated when a create fails with/without dynamo code.
            # This is by design. If the row doesnt exist, it means we stack/resource do not own the resource
            logger.info("Non-Dynamo DB delete code activated")

            # Only delete if PhysicalResourceId is something we generated.  If generated by crhelper, do not continue deletion.
            if eliza_cf_custom_resource_common.resource_is_generated_physical_resource_id(event):
                logger.info("Not deleting, not our generated ID: %s", event['PhysicalResourceId'])
                return

            #TODO: Delete logic
