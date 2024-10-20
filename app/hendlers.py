import app.keybords as kb

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'{message.chat.id}', reply_markup=kb.main)

@router.message(F.text.in_(['1 курс', '2 курс', '3, 4 курс']))
async def cmd_start(message: Message):
    if message.text == '1 курс':
        print(1)
    elif message.text == '2 курс':
        print(2)
    elif message.text == '3, 4 курс':
        print(3,4)
    else:
        print('error')
