import logging
import os
import traceback
import inspect
from pathlib import Path
from datetime import datetime


def setup_logger():
    logger = logging.getLogger("mcp_x")

    # Check if LOGGING_PATH environment variable is set
    logging_path = os.getenv("LOGGING_PATH")

    if os.getenv("LOGGING_PATH"):
        log_dir = Path(logging_path)
        log_dir.mkdir(parents=True, exist_ok=True)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        log_file = log_dir / f"spotify_mcp_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        error_log_file = log_dir / f"spotify_mcp_errors_{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.log"
        error_file_handler = logging.FileHandler(error_log_file)
        error_file_handler.setFormatter(formatter)
        error_file_handler.setLevel(logging.ERROR)

        # Configure logger with both handlers
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        logger.addHandler(error_file_handler)
    else:
        # Use default logging configuration
        logger.setLevel(logging.INFO)

    return logger
