import time

import telepot
from telepot.loop import MessageLoop

MAMANOMATOR_BOT_TOKEN = "392500649:AAHW-3XqFF6wGR4HVFC5pVzlw8_98ohTE2k"
ERROR_UNKNOWN_COMMAND = "I don't know what you want. Please use /name."
ERROR_NAME_USAGE = "Missing something? Use like this: /name MyName"
bot = telepot.Bot(MAMANOMATOR_BOT_TOKEN)


name_to_id = {
    u"ShayNehmad": "206341521"
}


def main():
    try:
        bot_server_logic()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print 'Stopping ...'


def bot_server_logic():
    MessageLoop(bot, handle).run_as_thread()
    print 'Listening ...'


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text'].split(" ")[0]

    if command == "/name":
        try:
            name = msg['text'].split(" ")[1]

            if name_to_id.has_key(name):
                bot.sendMessage(
                    chat_id,
                    "{0}'s ID is {1}.".format(name, name_to_id.get(name)))
            else:
                bot.sendMessage(
                    chat_id,
                    "Sorry, I don't know who {0} is.".format(name))
        except IndexError:
            bot.sendMessage(chat_id, ERROR_NAME_USAGE)
    else:
        bot.sendMessage(chat_id, ERROR_UNKNOWN_COMMAND)


if __name__ == '__main__':
    main()
