import inspect
import logging


class LogGen:
    @staticmethod
    def loggen():
        classname = inspect.stack()[1][3]
        logger = logging.getLogger(classname)
        file = logging.FileHandler("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Logs\\logfile.log")
        formats = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        file.setFormatter(formats)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
