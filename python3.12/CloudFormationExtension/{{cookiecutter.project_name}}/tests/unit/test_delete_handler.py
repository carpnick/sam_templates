# from typing import MutableMapping, Any
# from cloudformation_cli_python_lib.interface import OperationStatus
# from {{cookiecutter.project_name}}.delete_handler import DeleteHandler
# from {{cookiecutter.project_name}}.handlers import TYPE_NAME
from pytest_mock import MockFixture


def test_delete_success(mocker: MockFixture) -> None:
    s = mocker.MagicMock()
    assert s is not None
