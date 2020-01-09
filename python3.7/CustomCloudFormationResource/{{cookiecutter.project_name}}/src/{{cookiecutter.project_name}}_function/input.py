# pylint: disable=R0903

"""
Input object class for parsing parameters from the Custom CF Resource event
"""
import logging

logger = logging.getLogger(__name__)


class InputObject:
    """
    Object to hold all the parameters
    """

    def __init__(self, parameters): # pylint: disable=W0613
        """
        Constructor
        :param parameters:
        """

        # TODO: Put in all parameters that you are expecting - with defaults if necessary # pylint: disable=W0511
        # IE - self.idp_name = parameters["IDPName"]
        print()


    @staticmethod
    def new_resource_required(old_input, new_input):  # pylint: disable=W0613
        """
        Compare the old parameters to the new parameters and determine if a new resource needs to be created
        for this custom resource
        :param old_input:
        :param new_input:
        :return:
        """

        """
        #Example Implementation
        if old_input.idp_name == new_input.idp_name:
            return False

        return True
        """  # pylint: disable=W0105

        return False
