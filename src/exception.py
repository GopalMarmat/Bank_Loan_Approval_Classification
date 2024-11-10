import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("error_log.log"),  # Log to a file
        logging.StreamHandler()                # Log to console
    ]
)

# Error message function to detail error information
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        f"Error occurred in script: [{file_name}] "
        f"at line [{exc_tb.tb_lineno}] with message: [{str(error)}]"
    )
    return error_message

# CustomException class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# Test the CustomException
if __name__ == "__main__":
    try:
        # Example of code that could throw an error
        x = 1 / 0  # This will raise a ZeroDivisionError
    except Exception as e:
        # Raise CustomException with details
        custom_exception = CustomException("An error occurred", sys)
        logging.error(custom_exception)
        print(custom_exception)
