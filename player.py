class Player:

    def __init__(self, chat_id, name):
        self.__chat_id = chat_id
        self.__name = name
        self.__point = 0
        self.__chards = None
        self.__isReading = False

    def addChard(self, chard):
        self.__chards.append(chard)

    def addPoint(self):
        self.__point += 1
        return self.__point

    def getPoint(self):
        return self.__point

    def removeChard(self, chard):
        self.__chards.remove(chard)

    def setIsReading(self, isReading):
        self.__isReading = isReading
