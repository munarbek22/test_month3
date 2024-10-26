import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()

async def sql_create():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_STORE)
async def sql_insert_store(name_product, category, size, price, product_id, photo):
    cursor.execute(queries.INSERT_STORE, (
        name_product, category, size, price, product_id, photo
    ))
db.commit()