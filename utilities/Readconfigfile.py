import configparser

config = configparser.RawConfigParser()

config.read("C:\\Users\\LENOVO\\PycharmProjects\\pythonProject\\Shopping_Kart\\Configuration\\config.ini")


class ReadValues:

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password

