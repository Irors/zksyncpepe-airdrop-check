from loguru import logger
from sys import stderr

def add_logger():
    logger.remove()
    logger.add(
        stderr,
        format="<bold><blue>{time:HH:mm:ss}</blue> | <level>{level}</level> | <level>{message}</level></bold>"
    )

