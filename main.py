from aiogram.utils import executor
from config import dp
import logging

from handlers import client, callback, extra, fsmAdminMenu, admin
from database.bot_dp import sql_create


async def on_startup(_):
    sql_create()


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsmAdminMenu.register_handlers_fsmmenu(dp)

extra.register_handlers_extra(dp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
