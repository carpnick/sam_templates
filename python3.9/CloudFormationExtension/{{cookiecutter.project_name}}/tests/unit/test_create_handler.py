# from typing import MutableMapping, Any
# from {{cookiecutter.project_name}}.create_handler import CreateHandler
# from {{cookiecutter.project_name}}.handlers import TYPE_NAME
from pytest_mock import MockFixture


def test_create_fail_in_context(mocker: MockFixture) -> None:
    s = mocker.MagicMock()
    assert s is not None


def test_create_success(mocker: MockFixture) -> None:
    s = mocker.MagicMock()
    assert s is not None
