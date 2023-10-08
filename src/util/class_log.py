import logging
from logging.handlers import TimedRotatingFileHandler

class Log():

    def __new__(cls, *args, **kwargs):
        return super(Log, cls).__new__(cls)

    def __init__(self):
        return

    def build(self, name, log_path, storage_days = 7, console_handler = True):
        logger = logging.getLogger(name)
        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s', datefmt = '%d/%m/%Y %H:%M:%S')
        fileHandler = TimedRotatingFileHandler(f"{log_path}{name}.log", when = 'midnight', backupCount = storage_days)
        fileHandler.setLevel(logging.DEBUG)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        if console_handler:
            consoleHandler = logging.StreamHandler()
            consoleHandler.setLevel(logging.DEBUG)
            logger.addHandler(consoleHandler)
        return logger
    

if __name__ == '__main__':
    log_manager = Log()
    log = log_manager.build('testLog', './', 7, 0)
    log.info('test')