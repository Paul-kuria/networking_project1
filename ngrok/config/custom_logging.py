import sys

from config.config import configuration
from loguru import logger


def setup_logger():
    logger.remove()  # Remove any default handlers

    # Console handler with colors & more information
    console_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )

    logger.add(sink=sys.stdout, format=console_format, level=configuration.LOG_LEVEL)

    # File handler with roation, backtrace, retention
    logfile_path: str = f"{configuration.logs_directory}/{{time:YYYY-MM-DD}}-app.log"
    file_format: str = (
        "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}.{function}:{line} | {message}"
    )
    rotation: str = "1 day"
    backtrace: bool = True
    level: str = configuration.LOG_LEVEL  # Use log level from your config
    retention: str = "7 days"

    logger.add(
        sink=logfile_path,
        format=file_format,
        rotation=rotation,
        backtrace=backtrace,
        level=level,
        retention=retention,
    )
    return logger


logger = setup_logger()
