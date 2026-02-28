import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from src.config import LOG_LEVEL, LOG_DIR

def setup_logger(name : str) -> logging.Logger:
    LOG_DIR.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        #console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        #File handler
        file_handler = RotatingFileHandler(
            LOG_DIR / f"{name}.log",
            maxBytes=5_000_000,
            backupCount=3,
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger