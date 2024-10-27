import app.pars_exel as pars_exel

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.pars_exel import button_all_year1, button_all_year2, button_all_year34

DAYS = ['На сегодня', 'На завтра']


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Начать')],
     [KeyboardButton(text='О авторе')]
])


year = (ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=pars_exel.KURSES[0]), KeyboardButton(text=pars_exel.KURSES[1]),
     KeyboardButton(text=pars_exel.KURSES[2])]
]))

group1 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=button_all_year1()[0]), KeyboardButton(text=button_all_year1()[1])],
    [KeyboardButton(text=button_all_year1()[2]), KeyboardButton(text=button_all_year1()[3])]
])

group2 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=button_all_year2()[0]), KeyboardButton(text=button_all_year2()[1])],
    [KeyboardButton(text=button_all_year2()[2]), KeyboardButton(text=button_all_year2()[3])]
])

group34 = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=button_all_year34()[0]), KeyboardButton(text=button_all_year34()[1])],
    [KeyboardButton(text=button_all_year34()[2]), KeyboardButton(text=button_all_year34()[3])]
])

def num_group(year: str, group: str) -> ReplyKeyboardMarkup:
    buttons = []
    button_row = []  # Список для одной строки кнопок
    for i in pars_exel.button_num_group(year, group):
        button_row.append(KeyboardButton(text=i))
        if len(button_row) == 2:
            buttons.append(button_row)
            button_row = []  # Очищаем строку для следующей пары кнопок
    if button_row:
        buttons.append(button_row)
    button_markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)  # Создаем клавиатуру с кнопками
    return button_markup  # Возвращаем клавиатуру

def day_button(group: str) -> ReplyKeyboardMarkup:
    button_markup = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text=f'{DAYS[0]}  {group}'), KeyboardButton(text=f'{DAYS[1]}  {group}')],
        [KeyboardButton(text='Назад')]

    ])
    return button_markup

