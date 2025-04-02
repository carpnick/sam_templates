# from typing import MutableMapping, Any
# from {{cookiecutter.project_name}}.update_handler import UpdateHandler
# from {{cookiecutter.project_name}}.handlers import TYPE_NAME
from pytest_mock import MockFixture


def test_update_fail_in_context(mocker: MockFixture) -> None:
    s = mocker.MagicMock()
    assert s is not None


def test_update_success(mocker: MockFixture) -> None:
    s = mocker.MagicMock()
    assert s is not None
