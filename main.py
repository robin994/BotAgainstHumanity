import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        name = msg["from"]["first_name"]
        txt = msg['text']
        if '/start' in txt:
            bot.sendMessage(chat_id, 'ciao {}, sono un bot molto stupido!'.format(name))
        elif '/hey' in txt:
            bot.sendMessage(chat_id, 'Heylà')
        elif '/help' in txt:
            bot.sendMessage(chat_id, 'Ecco i comandi che capisco:\n - /start\n - /hey')
        else:
            bot.sendMessage(chat_id, 'Mi spiace {}, non capisco\nUsa /help per sapere cosa posso fare!'.format(name))

def on_callback_query(msg):
  query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
  print('Callback Query:', query_id, from_id, query_data)



bot = telepot.Bot('1465603402:AAFl6HCxzVKlWPdK6A33PNEsjm-6KZ_ebvw')
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)
