# tests/test_logging.py
from loguru import logger

def test_log_output():
    logger.trace("This is trace message")  # 仅在LOG_LEVEL=TRACE时显示
    logger.debug("Debug information")
    logger.info("System running normally")
    logger.warning("Low disk space")
    logger.error("Failed to connect database")
    logger.critical("System crash imminent!")