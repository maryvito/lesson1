from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, ephem, datetime, re, telegram

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

def planet(bot, update, args):
    #d = datetime.datetime.now()
    #dd = strftime('%Y/%m/%d')
     
    user_text = args[0] 
    if user_text == "mars":
        planet = ephem.Mars('2017/06/03')
    elif user_text == "mercury":
        planet = ephem.Mercury ('2017/06/03') 
    elif user_text == "venus":
        planet = ephem.Venus('2017/06/03')
    elif user_text == "jupiter":
        planet = ephem.Jupiter('2017/06/03') 
    elif user_text == "saturn":
        planet = ephem.Saturn ('2017/06/03')
    elif user_text == "uranus":
        planet = ephem.Uranus('2017/06/03')
    elif user_text == "neptune":
        planet = ephem.Neptune('2017/06/03')
        
    update.message.reply_text(ephem.constellation(planet)[0])

def word_count(bot, update, args):
    
    if args[0] == '' or args[0] == "":
        update.message.reply_text(str(len(args))+ ' слова')
    else:
        update.message.reply_text('0 слов')

def calc(bot, update, args):

    expr = args[0]
    if expr[-1] != '=' :
        result = "Выражение некорректно"
    else:
        expr = expr[:-1]
        operations = '+-*/'
        for op in operations:
            if op in expr:
                numbers = expr.split(op)
                a = int(numbers[0])
                b = int(numbers[1])
                c = op
                if c == '+':
                    result = a + b
                elif c == '-':
                    result = a - b
                elif c == '*':
                    result = a * b
                elif c == '/':
                    if b == 0: 
                        result = "деление на ноль"
                    else:
                        result = a / b
                break


    update.message.reply_text(str(result))

def calc_pro(bot, update, args):
    custom_keyboard = [['1', '2'], 
                      ['*', '-']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(reply_markup)
    
    #bot.send_message(chat_id=chat_id, 
                     # text="Custom Keyboard Test", 
                     # reply_markup=reply_markup)
    


def main():
    updater = Updater("394450546:AAH3yjqcvOdl0oxOJBJv7Euj8kHttzdXFis")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet, pass_args = True))
    dp.add_handler(CommandHandler("calc", calc, pass_args = True))
    dp.add_handler(CommandHandler("calcpro", calc_pro, pass_args = True))

    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    updater.start_polling()
    updater.idle()



main()
