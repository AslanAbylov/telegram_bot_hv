from aiogram import Bot, Dispatcher
from decouple import config

TOKEN = config('TOKEN')
ADMINS = [5429202367, ]

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
