class Card:

    def getText(self):
        return self.__text

    def getId(self):
        return self.__id

    def getType(self):
        return self.__type

    def setText(self, text):
        self.__text = text

    def setId(self, id):
        self.__id = id

    def setType(self, type):
        self.__type = type

    def getLanguage(self):
        return self.__language

    def setLanguage(self, language):
        self.__language = language

    def getPicked(self):
        return self.__picked

    def setPicked(self, bool):
        self.__picked = bool

    def __init__(self, id, type, text, language):
        self.__text = text
        self.__id = id
        self.__type = type
        self.__language = language
        self.__picked = False
