import asyncio
import logging

from aiogram import Bot, Dispatcher
from key import api
from app.hendlers import router

logging.basicConfig(level=logging.DEBUG,
                    filename='logging.log',
                    format = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s",
                    datefmt='%d/%m/%Y %I:%M:%S',
                    encoding='utf-8',
                    filemode='w')

bot = Bot(token=api)
dp = Dispatcher()

logging.info('info')
logging.warning('warning')
logging.error('error')

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())