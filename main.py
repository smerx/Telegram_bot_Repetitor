import telebot
from telebot import types

bot = telebot.TeleBot('5775270269:AAEg14NbCA473jc6ClWg93aX3QCRgJ4LrTY')
keyboard = types.InlineKeyboardMarkup()  # клавиатура меню
key_inf_pay = types.InlineKeyboardButton(text='Информация по оплате', callback_data='inf_pay')
keyboard.add(key_inf_pay)  # добавляем кнопку в клавиатуру
key_promo = types.InlineKeyboardButton(text='Скидки и промокоды', callback_data='promo')
keyboard.add(key_promo)
key_timetable = types.InlineKeyboardButton(text='Расписание', callback_data='timetable')
keyboard.add(key_timetable)

@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "/start":
        question = "Доброго времени суток! Что бы вы хотели? "
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(message):
    if message.data == "inf_pay": #call.data это callback_data
        bot.send_message(message.message.chat.id, 'Дата последней оплаты (08.09.2022), осталось 8 занятий. ')
        bot.send_message(message.from_user.id, text="Что-то ещё?", reply_markup=keyboard)
    elif message.data == "promo":
        bot.send_message(message.message.chat.id, 'Преведи друга и получи 3000 рублей на карту. ')
        bot.send_message(message.from_user.id, text="Что-то ещё?", reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
