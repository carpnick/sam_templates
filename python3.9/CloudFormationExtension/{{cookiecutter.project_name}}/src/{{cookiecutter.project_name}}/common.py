from typing import Optional, TYPE_CHECKING
import logging

from cloudformation_cli_python_lib.boto3_proxy import SessionProxy
import cloudformation_cli_python_lib.exceptions as exceptions
from {{cookiecutter.project_name}}.models import ResourceModel


# if TYPE_CHECKING:
#     from mypy_boto3_identitystore import Client as IdentityStoreClient
# else:
#     IdentityStoreClient: object

LOG = logging.getLogger(__name__)


class Common:
    @staticmethod
    def hello_world(session: Optional[SessionProxy], model: Optional[ResourceModel], type_name: str) -> str:
        assert session is not None
        assert model is not None

        myreturn = session.client("sts").get_caller_identity()
        LOG.info(str(myreturn))
