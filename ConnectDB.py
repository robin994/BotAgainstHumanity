import mysql.connector
import logging
from . import Card

logging.getLogger().setLevel(logging.INFO)


class ConnectDB:

    def __init__(self):
        self.cnx = self.__connectdb()

    def __connectdb(self):
        logging.info("ConnectionDB : Avvio connessione DB")
        config = {
            'user': 'root',
            'password': 'root',
            'host': '127.0.0.1',
            'database': 'cah_db',
            'raise_on_warnings': True
        }

        cnx = mysql.connector.connect(**config)
        logging.info("ConnectionDB : connessione stabilita DB")
        return cnx

    def __sendQuery(self, query):
        cnxcursor = self.cnx.cursor()
        cnxcursor.execute(query)
        result = cnxcursor.fetchall()
        return result

    def getChards(self, language):
        query = "SELECT id, type, text FROM chards WHERE LANGUAGE = " + language
        chards = self.__sendQuery(query)
        toReturn = None
        for actualchard in chards:
            logging.info('actualchard: ' + actualchard)
            toReturn.append(Card(actualchard[0], actualchard[1], actualchard[2]))
        return toReturn

    def getAllCards(self):
        query = self.__sendQuery("SELECT id, type, text FROM chards")
        cards = self.__sendQuery(query)
        toReturn = None
        for actualcard in cards:
            logging.info('actualchard: ' + actualcard)
            toReturn.append(Card(actualcard[0], actualcard[1], actualcard[2]))
        return toReturn

    def getLanguage(self):
        query = self.__sendQuery("SELECT id, type, text FROM chards")
        chards = self.__sendQuery(query)
        toReturn = None
        for actualchard in chards:
            logging.info('actualchard: ' + actualchard)
            toReturn.append(Card(actualchard[0], actualchard[1], actualchard[2]))
        return toReturn
