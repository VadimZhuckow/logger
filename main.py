from loguru import logger

logger.add("debug.log", format="{time} {level} {message}",
           level="DEBUG", rotation="10 MB", compression='zip', serialize=True)


# for _ in range(1000):
#     logger.debug('debug message (debug)')
# logger.info('info message (info)')
# logger.error('error message (error)')


def divide(a, b):
    return a / b


@logger.catch
def main():
    divide(1, 0)


if __name__ == '__main__':
    main()
