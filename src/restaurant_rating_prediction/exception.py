import sys
from src.restaurant_rating_prediction.logger import logging


def error_message_detail(error, error_detail: sys):
    _,_, error_tb = error_detail.exc_info()
    file_name = error_tb.tb_frame.f_code.co_filename
    error_msg = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, error_tb.tb_lineno,str(error))

    return error_msg


class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_msg = error_message_detail(error_message,error_detail)
        logging.error(self.error_msg)
    def __str__(self):
        return self.error_msg
