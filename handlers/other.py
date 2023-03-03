from aiogram import types, Dispatcher
from aiogram.types import Message

from create_bot import bot


# @dp.message_handler()
async def echo_send(message: types.Message):
    # if message.text == 'Привет':
    await message.answer('И тебе привет!')

    # await message.answer(message.text)
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)


async def send_voice(message: types.Message):
    audio = open("Congratulations.mp3", 'rb')
    await message.answer_voice(audio)


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send, commands=['Привет'])
