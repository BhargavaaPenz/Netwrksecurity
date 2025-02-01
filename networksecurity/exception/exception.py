import sys
sys.path.append("/Users/bhargavaa/Documents/Learn Python/NETWORKSEC")
from networksecurity.logging import logger

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()
        self.line_number=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
def __str__(self):
    return f"Error occured in python script name [{self.file_name}] line number [{self.line_number}] error message [{self.error_message}]"

if __name__=="__main__":
    try:
        logger.logging.info("Try block entered") 
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)
