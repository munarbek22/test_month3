from aiogram import executor
import logging
from config import dp, bot
from handlers import commands, FSM_store
from db import db_main

async def on_startup(_):
    await db_main.sql_create()

FSM_store.register_handlers_store(dp)
commands.register_handlers_commands(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)