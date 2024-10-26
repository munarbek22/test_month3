from asyncore import dispatcher
from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
import config

class fsm_order(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    contact = State()
    submit = State()

async def start_order(message: types.Message):
    await message.answer('Введите артикул товара: ')
    await fsm_order.product_id.set()

async def load_product_id(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['product_id'] = message.text
    await message.answer('Введите размер товара: ')
    await fsm_order.next()

async def load_size(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text
    await message.answer('Введите количество: ')
    await fsm_order.next()

async def load_quantity(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['quantity'] = message.text
    await message.answer('Введите ваши контакты:  ')
    await fsm_order.next()

async def load_contact(message: types.Message, state=FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text
    await message.answer(f'Верны ли данные:\n'
                         f'Артикул - {data["product_id"]}\n'
                         f'Размер - {data["size"]}\n'
                         f'Количество - {data["quantity"]}\n'
                         f'Ваши контакты - {data["contact"]}')
    await fsm_order.next()

async def submit(message: types.Message, state=FSMContext):
    if message.text.lower() == 'да':
        async def send_message(message: types.Message, state: FSMContext):
            data = await state.get_data()
            order = (f'Артикул - {data["product_id"]}\n'
                 f'Размер - {data["size"]}\n'
                 f'Количество - {data["quantity"]}\n'
                 f'Ваши контакты - {data["contact"]}')

            for staff_id in config.staff:
                await Bot.send_message(staff_id, order)

            await message.answer("Ваш заказ отправлен!")
            await state.finish()


def register_order_handler(dp: Dispatcher):
    dp.register_message_handler(start_order, commands=['order'])
    dp.register_message_handler(load_product_id, state=fsm_order.product_id)
    dp.register_message_handler(load_size, state=fsm_order.size)
    dp.register_message_handler(load_quantity, state=fsm_order.quantity)
    dp.register_message_handler(load_contact, state=fsm_order.quantity)
    dp.register_message_handler(submit, state=fsm_order.submit)


