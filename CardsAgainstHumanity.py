import time, threading, logging, random
from . import player
from . import ConnectDB


class CardsAgainstHumanity():

    def addPlayer(self, player):
        self.__players.append(player)

    def __init__(self, player, lang):
        self.__answers = None
        self.__players = player
        self.__cards = ConnectDB().getCards(lang)
        for chard in self.__cards:
            if chard.getType() == 1:
                self.__whiteCards.append(chard)
            else :
                self.__blackCards.append(chard)

    def pickCard(self, type):
        if type == 1:
            toReturn = self.__whiteCards[random.randint(0, len(self.__cards))]
            if toReturn.getPicked():
                self.pickCard(self)
            else:
                toReturn.setPicked(True)
                return toReturn
        else:
            toReturn = self.__blackCards[random.randint(0, len(self.__cards))]
            if toReturn.getPicked():
                self.pickCard(self)
            else:
                toReturn.setPicked(True)
                return toReturn

    def prepareGame(self):
        for player in self.__players:
            counter = 0
            while counter < 10:
                player.addChard(self.pickCard(1))
        self.isPLaying = random.randint(0, len(self.__players))

    def getNextBlackChard(self):
        return self.pickCard(0)

    def getNextWhiteChard(self):
        return self.pickCard(1)


    def startGame(self):
        self.prepareGame()


    def getAnswers(self):
        return self.__answers

    def addAnswers(self, answer):
        self.__answers.append(answer)

    def clearAnswers(self):
        self.__answers.clear()