from aiogram.utils import executor
import logging
from handlers import client, extra, callback, admin
from config import dp

callback.register_hendler_culback(dp)
client.register_mesage_handler_client(dp)
admin.reqister_admin_hundlers(dp)

extra.reqister_extra(dp)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

