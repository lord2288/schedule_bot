import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from key import api

bot = Bot(token=api)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'{message.chat.id}')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())