from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import logging
import math


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Salam aleikym {message.from_user.first_name}!")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Дальше", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "За кого вы болеете?"
    answers = [
        'за Конора',
        'за Макгрегора',
        'Садыр Нургожоевич - лучший',
        'за Путина',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="Кумтор - наш!!!",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Какой римской цифры не существует?"
    answers = [
        '1000',
        '10000',
        '0',
        '1000000',
        '100000',
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=True,
        type='quiz',
        correct_option_id=2,
        explanation="И ты , Брут?",
        open_period=10,

    )


@dp.message_handler(commands=['mem'])
async def mem_photo(message: types.Message):
    photo = open('media/photo_2022-10-18_11-34-48.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)
    else:
        await bot.send_message(message.from_user.id, message.text)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
