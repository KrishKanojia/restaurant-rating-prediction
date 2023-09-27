from src.restaurant_rating_prediction.logger import logging
from src.restaurant_rating_prediction.exception import CustomException
import sys


if __name__ == "__main__":
    try:
        1/0
    except Exception as e:
        logging.info("Custom Exception Occured")
        raise CustomException(e,sys)