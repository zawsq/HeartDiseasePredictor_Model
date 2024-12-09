import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

# Define log file directory and filename
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Log file name with timestamp for the current day
LOG_FILE = f"log_{datetime.now().strftime('%m_%d_%Y')}.log"
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Setting up the rotating file handler
log_handler = RotatingFileHandler(
    LOG_FILE_PATH,
    maxBytes=10 * 1024 * 1024,  # Maximum size (10 MB)
    backupCount=5,  # Keep 5 backup files
)

log_handler.setFormatter(
    logging.Formatter('[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s')
)

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

# Optional: Add console handler for real-time output in the terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter('[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(console_handler)

# Test logging
if __name__ == "__main__":
    logger.info("Logging has started successfully.")