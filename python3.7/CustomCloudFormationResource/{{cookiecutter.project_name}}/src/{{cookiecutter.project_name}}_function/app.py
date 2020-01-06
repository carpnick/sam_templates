# pylint: disable=W0613,W0703, E0611, C0103
"""
Initial file called from Cloud Formation via Lambda
"""

import logging
from crhelper import CfnResource


##################################################################################
# START BOILER PLATE
helper = CfnResource(json_logging=False, log_level='DEBUG', boto_level='CRITICAL')


def lambda_handler(event, context):
    """
    Integration with CloudFormation using the helper

    :param event:
    :param context:
    :return:
    """
    helper(event, context)


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

    ##TODO: Put in your implementation logic here. # pylint: disable=W0511

@helper.update
def handle_update(event, context):
    """
    Create the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Update")

    ##TODO: Put in your implementation logic here. # pylint: disable=W0511


@helper.delete
def handle_delete(event, context):
    """
    Deletes the resource.  Initially called  by CloudFormation
    :param event:
    :param context:
    :return:
    """
    logger.info("Got Delete")

    ##TODO: Put in your implementation logic here. # pylint: disable=W0511
