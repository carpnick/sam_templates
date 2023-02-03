import logging
from typing import Any, MutableMapping, Optional
from cloudformation_cli_python_lib.interface import (
    Action,
    ProgressEvent,
)
from cloudformation_cli_python_lib.resource import Resource
from cloudformation_cli_python_lib.boto3_proxy import SessionProxy
import cf_extension_core as core


# Locals
from .models import ResourceHandlerRequest, ResourceModel
from {{cookiecutter.project_name}}.create_handler import CreateHandler
from {{cookiecutter.project_name}}.read_handler import ReadHandler
from {{cookiecutter.project_name}}.delete_handler import DeleteHandler
from {{cookiecutter.project_name}}.update_handler import UpdateHandler


# Use this logger to forward log messages to CloudWatch Logs.
LOG = logging.getLogger(__name__)
TYPE_NAME = "{{cookiecutter.resource_name}}"

resource = Resource(TYPE_NAME, ResourceModel)
test_entrypoint = resource.test_entrypoint


@resource.handler(Action.CREATE)
def create_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    return CreateHandler(
        session=session,
        request=request,
        callback_context=callback_context,
        type_name=TYPE_NAME,
        db_resource=core.generate_dynamodb_resource(session_proxy=session),
        total_timeout_in_minutes=2,  # Should match Schema value - unit test validated - https://shorturl.at/gHK46
    ).execute()


@resource.handler(Action.UPDATE)
def update_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    return UpdateHandler(
        session=session,
        request=request,
        callback_context=callback_context,
        type_name=TYPE_NAME,
        db_resource=core.generate_dynamodb_resource(session_proxy=session),
        total_timeout_in_minutes=2,  # Should match Schema value - unit test validated - https://shorturl.at/gHK46
    ).execute()


@resource.handler(Action.DELETE)
def delete_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    return DeleteHandler(
        session=session,
        request=request,
        callback_context=callback_context,
        type_name=TYPE_NAME,
        db_resource=core.generate_dynamodb_resource(session_proxy=session),
        total_timeout_in_minutes=2,  # Should match Schema value - unit test validated - https://shorturl.at/gHK46
    ).execute()


@resource.handler(Action.READ)
def read_handler(
    session: Optional[SessionProxy],
    request: ResourceHandlerRequest,
    callback_context: MutableMapping[str, Any],
) -> ProgressEvent:
    return ReadHandler(
        session=session,
        request=request,
        callback_context=callback_context,
        type_name=TYPE_NAME,
        db_resource=core.generate_dynamodb_resource(session_proxy=session),
        total_timeout_in_minutes=2,  # Should match Schema value - unit test validated - https://shorturl.at/gHK46
    ).execute()
