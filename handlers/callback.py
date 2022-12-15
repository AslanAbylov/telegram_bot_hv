from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
from aiogram import types, Dispatcher

#
# @dp.callback_query_handler(text='button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next2', callback_data='button_call_2')
    markup.add(button_call_2)
    question = 'кто я'
    answers = [
        '1',
        '2',
        '3',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='гадал',
        open_period=5,
        reply_markup=markup
    )

# @dp.callback_query_handler(text='button_call_2')
async def quiz_3(call: types.CallbackQuery):
    questions = 'атвичай'
    answers = [
        '5',
        '7',
        '10',
        '0',
    ]
    photo = open('media/photo_2022-12-09_17-50-06.jpg', 'rb')
    await bot.send_photo(chat_id=call.from_user.id, photo=photo)

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=questions,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='norm'
    )

def register_hendler_culback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button_call_1')
    dp.register_callback_query_handler(quiz_3, text='button_call_2' )

