from config import bot, Dispatcher
from aiogram import types
from config import ADMINS

async def ban(massage: types.Message):
    if massage.chat.type != 'private':
        if massage.from_user.id not in ADMINS:
            await massage.answer('Ты не админ!')
        elif not massage.text.startswith('pin'):
            await massage.answer('чтоб закрепить Команда должна начинаться на !pin')
        elif not massage.reply_to_message(massage.chat.id, massage.from_user.id):
            await massage.answer('Команда должна быть ответом на сообщение!')
        else:
            await bot.kick_chat_member(massage.chat.id, massage.reply_to_message.from_user.id)
            await massage.answer(f'{massage.reply_to_message.from_user.full_name} был кикнут')
    else:
        await massage.answer('Пиши в группе!')

def reqister_admin_hundlers(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')