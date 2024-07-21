from loguru import logger

logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG")


logger.debug('debug message (debug)')
logger.info('info message (info)')
logger.error('error message (error)')

