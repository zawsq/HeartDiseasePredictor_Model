import logging
from logging import StreamHandler

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Add console handler for real-time output in the terminal
console_handler = StreamHandler()
console_handler.setFormatter(
    logging.Formatter('[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s')
)
logger.addHandler(console_handler)

# Test logging
if __name__ == "__main__":
    logger.info("Logging has started successfully.")
