# pylint: disable=W0613,W0703, E0611, C0103
"""
Initial file called from Cloud Formation via Lambda
"""

import logging
import json
from crhelper import CfnResource
from {{cookiecutter.project_name}}_function.input import InputObject


##################################################################################
# START BOILER PLATE
# Do this until this is merged: https://github.com/aws-cloudformation/custom-resource-helper/pull/28
class MyCfnResource(CfnResource): # pylint: disable=C0115
    def _wait_for_cwlogs(self, sleep=0):
        return

helper = MyCfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')


def lambda_handler(event, context):
    """
    Integration with CloudFormation using the helper

    :param event:
    :param context:
    :return:
    """
    assert len(event['Records']) == 1, "Got too many or too few records in the request"
    myrequest = json.loads(event['Records'][0]['Sns']['Message'])
    helper(myrequest, context)


try:
    # Init code goes here
    logger = logging.getLogger(__name__)

except Exception as exc:
    helper.init_failure(exc)

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
    new_input = InputObject(event["ResourceProperties"]) #pylint: disable=W0612

    ##TODO: Put in your implementation logic here to create a new resource. # pylint: disable=W0511

    # Always return an ID or ARN or checksum.
    # This return value equals the PhysicalResourceId for your resource you created
    return new_input.arn()


@helper.update
def handle_update(event, context):
    """
    Create the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Update")

    new_input = InputObject(event["ResourceProperties"])

    # Go review the InputObject.new_resource_required method and make sure you have filled it out
    if InputObject.new_resource_required(InputObject(event["OldResourceProperties"]), new_input):

        logger.info("Detected new resource is required, performing create instead")
        new_physical_resource_id = handle_create(event, context)
        return new_physical_resource_id


    logger.info("Update allowed, no new resource is required, performing update")

    # TODO: Put in your implementation logic here for performing a resource Update. # pylint: disable=W0511

    # Return same resource id that was passed to us since we only updated it.
    return event['PhysicalResourceId']


@helper.delete
def handle_delete(event, context):
    """
    Deletes the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Delete")

    new_input = InputObject(event["ResourceProperties"])  # pylint: disable=W0612

    # Only delete if PhysicalResourceId is something we generated
    if event['PhysicalResourceId'] != new_input.arn():
        logger.info("Not deleting, not our generated ID")
        return

    # TODO: Put in your implementation logic here to delete the resource. # pylint: disable=W0511
    # Do not return anything from this method.
