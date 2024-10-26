import sqlite3
from itertools import product

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store 
    """).fetchall()
    conn.close()
    return products


async def sendall_products(callback_query: types.CallbackQuery):
    products = fetch_all_products()
    if products:
        for product in products:
            caption = (f'Верные ли данные: \n'
                       f'Название - {product["name_product"]}\n'
                       f'Категория - {product["category"]}\n'
                       f'Размер - {product["size"]}\n'
                       f'Цена - {product["price"]}\n'
                       f'Артикул - {product["article"]}\n'
            )


            await callback_query.message.answer_photo(
                photo=product['photo'],
                caption=caption
            )
    else:
        await callback_query.message.answer('Товар нет!')

def register_send_handler(dp: Dispatcher):
    dp.register_callback_query_handler(sendall_products, command=['product'])