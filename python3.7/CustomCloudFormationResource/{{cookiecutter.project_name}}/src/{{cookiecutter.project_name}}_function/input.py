# pylint: disable=R0903, C0103, R0201

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

        # TODO: Put in all parameters that you are expecting - with defaults if necessary # pylint: disable=W0511,  C0301
        # IE - self.idp_name = parameters["IDPName"]
        print()

    def arn(self):
        """
                Returns the ARN for this resource based on input parameters
                :return:
                """
        delimeter = "::"

        # return self.input_param + delimeter + self.input_param2
        # TODO: Only add parameters that are immutable here. # pylint: disable=W0511,  C0301
        # TODO: AKA - if a new resource needs to be created because of the parameter, then it needs to go in here, otherwise no. # pylint: disable=W0511,  C0301
        return delimeter


    @staticmethod
    def params_are_invalid(parameters):
        """Theory"""
        try:
            InputObject(parameters)
            logger.info("Params are valid")
            return False
        except Exception: #pylint: disable=W0703
            logger.info("Params are invalid")
            return True


    @staticmethod
    def new_resource_required(old_input, new_input):  # pylint: disable=W0613
        """
        Compare the old parameters to the new parameters and determine if a new resource needs to be created
        for this custom resource
        :param old_input:
        :param new_input:
        :return:
        """  # pylint: disable=W0511,  C0301

        """
        #Example Implementation
        if old_input.arn() == new_input.arn():
            return True	   #Can be updated

        else:
            return True # Cant be updated
        """  # pylint: disable=W0105

        return False
