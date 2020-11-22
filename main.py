import sys
import time, telepot, threading, logging
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


logging.getLogger().setLevel(logging.INFO)

def prepareGame():
    #TODO: da preimpostare
    return 1


def startgame(chat_id, timeToGo):
    print("Avvio gioco")
    bot.sendMessage(chat_id, 'Heylà')
    logging.info("Main    : Creo il thread")

    logging.info("Main    : Avvio il thread")
    timer = threading.Timer(timeToGo, forcestart, args=[chat_id])
    timer.start()
    logging.info("Main    : Processo terminato")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Accedi', callback_data='Access')]
    ])
    bot.sendMessage(chat_id,
                    'Il gioco sta per iniziare avete 2 minuti per accedere alla partita. Premi il tasto "accedi" per '
                    'entrare in partita',
                    reply_markup=keyboard)


def forcestart(chat_id):
    logging.info("Main    : forzo avvio partita")
    # TODO: Stop thread timer
    bot.sendMessage(chat_id, " gioco avviato")


def addChard(msg):
    logging.info("Main    : aggiungo carta")


def on_chat_message(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        if '/startgame' in txt:
            #TODO: Check if there is already a game istance
            timeToGo = 2
            startgame(chat_id, timeToGo)
        elif '/help' in txt:
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco:\n - /start\n - /hey')
        elif '/endgame' in txt:
            # TODO: create end game
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco:\n - /start\n - /hey')
        elif '/forcestart' in txt:
            forcestart()
        elif '/addChard' in txt:
            addChard()
        else:
            bot.sendMessage(chat_id, 'Mi spiace {}, non capisco\nUsa /help per sapere cosa posso fare!'.format(name))


def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print("Callback Query:", query_id, from_id, query_data)


bot = telepot.Bot('1465603402:AAH9ST1L3F8Mq4LHGSx93SoyB4Mm2grWJXQ')
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
