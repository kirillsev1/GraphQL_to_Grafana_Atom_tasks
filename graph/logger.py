import logging


def init_logger(name):
    """Function which initialises logger.

    Args:
        name: str - name of application in log file.
    """
    logger = logging.getLogger(name)
    FORMAT = '%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s'
    logger.setLevel(logging.DEBUG)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    sh.setLevel(logging.DEBUG)
    sh.setLevel(logging.DEBUG)
    logger.addHandler(sh)
    logger.debug('logger was initialized')
