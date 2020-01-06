# pylint: disable=W0621, W0613

""" Sample Integration Tests"""


import pytest
from lambda_local.context import Context
from {{ cookiecutter.project_name }}_function import app


# https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requesttypes.html
@pytest.fixture()
def cf_create_event():
    """ Generates Cloudformation Create Event"""

    return {
        "RequestType": "Create",
        "ResponseURL": "https://devnull-as-a-service.com/dev/null",
        "StackId": "arn:aws:cloudformation:us-west-2:1111111111:stack/...",
        "RequestId": "...",
        "LogicalResourceId": "localexecutioncall",
        "ResourceType": "Custom::hello_world",
        "ResourceProperties": {}
    }

@pytest.fixture()
def cf_delete_event():
    """ Generates Cloudformation Create Event"""

    return {
        "RequestType": "Delete",
        "ResponseURL": "https://devnull-as-a-service.com/dev/null",
        "StackId": "arn:aws:cloudformation:us-west-2:1111111111:stack/...",
        "RequestId": "...",
        "LogicalResourceId": "localexecutioncall",
        "ResourceType": "Custom::hello_world",
        "ResourceProperties": {}
    }

def test_delete_lambda_handler(cf_delete_event, mocker):
    """ Delete Lambda Integration Test"""

    app.lambda_handler(cf_delete_event, Context(60)._activate())  # pylint: disable=W0212

def test_create_lambda_handler(cf_create_event, mocker):
    """ Create Lambda Integration Test"""

    app.lambda_handler(cf_create_event, Context(60)._activate())  # pylint: disable=W0212
