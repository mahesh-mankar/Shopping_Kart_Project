import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        file = logging.FileHandler("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Logs\\logfile.log")
        formats = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file.setFormatter(formats)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return logger
