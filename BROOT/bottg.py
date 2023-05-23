import telebot
from telebot import types
import set
import EGE

bot = telebot.TeleBot(set.api_token)


@bot.message_handler(commands=['start'])
def start(message):
    #########################################################################
    print(message.chat.id)
    print(message.from_user)
    file = open("log.txt", "+a")
    file.write(str(message.from_user)+"\n")
    file.close()

    #########################################################################



    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! ".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])

def wetwlenie(message):
    if message.text == "👋 Поздороваться":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("10")
        btn2 = types.KeyboardButton("20")
        btn3 = types.KeyboardButton("30")
        btn4 = types.KeyboardButton("40")
        btn5 = types.KeyboardButton("50")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Какое количество желаете?".format(
                         message.from_user), reply_markup=markup)
    elif message.text == "❓":
        bot.send_message(message.chat.id, text="Create by Instructor")

    elif int(message.text) == 10:
        for i in range(0,10):
            data = EGE.users_search(i)
            id = data['id']
            first_name = data['first_name']
            last_name = data['last_name']
            photo = data['photo']
            bot.send_message(message.chat.id, f'[{first_name} {last_name} '
                                              f' ]({photo})', parse_mode='Markdown')
            bot.send_message(message.chat.id, text=f"https://vk.com/id{id}")
    elif int(message.text) == 20:
        for i in range(0, 20):
            data = EGE.users_search(i)
            id = data['id']
            first_name = data['first_name']
            last_name = data['last_name']
            photo = data['photo']
            bot.send_message(message.chat.id, f'[{first_name} {last_name} '
                                              f' ]({photo})', parse_mode='Markdown')
            bot.send_message(message.chat.id, text=f"https://vk.com/id{id}")
    elif int(message.text) == 30:
        for i in range(0, 30):
            data = EGE.users_search(i)
            id = data['id']
            first_name = data['first_name']
            last_name = data['last_name']
            photo = data['photo']
            bot.send_message(message.chat.id, f'[{first_name} {last_name} '
                                              f' ]({photo})', parse_mode='Markdown')
            bot.send_message(message.chat.id, text=f"https://vk.com/id{id}")
    elif int(message.text) == 40:
        for i in range(0, 40):
            data = EGE.users_search(i)
            id = data['id']
            first_name = data['first_name']
            last_name = data['last_name']
            photo = data['photo']
            bot.send_message(message.chat.id, f'[{first_name} {last_name} '
                                              f' ]({photo})', parse_mode='Markdown')
            bot.send_message(message.chat.id, text=f"https://vk.com/id{id}")
    elif int(message.text) == 50:
        for i in range(0, 50):
            data = EGE.users_search(i)
            id = data['id']
            first_name = data['first_name']
            last_name = data['last_name']
            photo = data['photo']
            bot.send_message(message.chat.id, f'[{first_name} {last_name} '
                                              f' ]({photo})', parse_mode='Markdown')
            bot.send_message(message.chat.id, text=f"https://vk.com/id{id}")


# @bot.message_handler(content_types=['text'])
# def search(message):
#     if int(message.text) == 10:
#         for i in range(10):
#             data = EGE.users_search(i)
#             id = data['id']
#             first_name = data['first_name']
#             last_name = data['last_name']
#             photo = data['photo']
#             bot.send_message(message.chat.id, f'[{first_name} {last_name} '
#                                               f' ]({photo})', parse_mode='Markdown')
#             bot.send_message(message.chat.id, text=f"https://vk.com/id{id}")
#     # bot.send_message(message.chat.id, text=f"{photo}")
bot.polling(none_stop=True)