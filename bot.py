from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def main():
    updater = Updater("394450546:AAH3yjqcvOdl0oxOJBJv7Euj8kHttzdXFis")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    updater.start_polling()
    updater.idle()



main()
