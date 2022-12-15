from config import bot, Dispatcher
from aiogram import types

async def filter_words(massage: types.Message):
    if massage.chat.type != 'private':
        bad_words = ['java', 'html', 'skript']
        username = f'{massage.from_user.username}' if massage.from_user.username is not None else massage.from_user.full_name
        for i in bad_words:
            if i in massage.text.lower():
                await bot.delete_message(massage.chat.id, massage.message_id)
                await massage.answer(f'не матерись @{username}, сам ты {massage.text}')

    if massage.text.startswith('.pin'):
        await bot.pin_chat_message(massage.chat.id, massage.message_id)

    if massage.text == 'dice':
        a = await bot.send_dice(massage.chat.id, emoji='🎯')
        print(a)

def reqister_extra(dp: Dispatcher):
    dp.register_message_handler(filter_words)