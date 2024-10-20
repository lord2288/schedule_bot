from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.pars_exel import KURSES

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=KURSES[0]), KeyboardButton(text=KURSES[1]), KeyboardButton(text=KURSES[2])]
])