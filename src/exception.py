import logging
import sys

class CustomException(Exception):
    """Custom Exception class for more informative errors."""
    def __init__(self, message, error_details: sys):
        super().__init__(message)
        self.error_details = error_details

    def __str__(self):
        _, _, exc_tb = self.error_details.exc_info()
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"{self.args[0]} occurred in {file_name} at line {line_number}"