from config import bot, dp
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keybords.client_kb import start_markup

async def info(massage: types.Message):
    await massage.answer('Сам разбирайся')


async def start_hundler(massage: types.Message):
    await bot.send_message(chat_id=massage.from_user.id, text=f'салам хозяин {massage.from_user.first_name}', reply_markup=start_markup)

async def quiz_1(massage: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next1', callback_data='button_call_1')
    markup.add(button_call_1)
    questions = 'город кр'
    answers = [
        'ош',
        'бишкек',
        'токмок',
        'fdfd'
        'dfdf'
    ]
    await bot.send_poll(
        chat_id=massage.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='стыдно не знать',
        open_period=5,
        reply_markup=markup
    )

def register_mesage_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_hundler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(info, commands=['info'])
