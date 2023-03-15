# import typing
# from typing import MutableMapping, Any
# from cloudformation_cli_python_lib.interface import OperationStatus
# from {{cookiecutter.project_name}}.models import ResourceModel
# from {{cookiecutter.project_name}}.read_handler import ReadHandler
# from {{cookiecutter.project_name}}.handlers import TYPE_NAME
from pytest_mock import MockFixture


def test_read_success(mocker: MockFixture) -> None:
    s = mocker.MagicMock()
    assert s is not None
