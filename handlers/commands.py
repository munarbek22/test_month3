from aiogram import types, Dispatcher
import os
from config import bot

async def start_command_handler(message: types.Message):
    await message.answer('Привет!')

async def info_command_handler(message: types.Message):
    await message.answer('Бот умеет принимать заказы')

def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command_handler, commands=['start'])
    dp.register_message_handler(info_command_handler, commands=['info'])