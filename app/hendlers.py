import app.pars_exel as pars_exel
import app.keybords as kb

from aiogram import F, Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

class Reg(StatesGroup):
    year = State()
    group = State()
    num_group = State()
    day = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Здравтсвуйте {message.chat.username}', reply_markup=kb.main)

@router.message(F.text == 'Начать')
async def start_Reg(message: Message, state: FSMContext):
    await state.set_state(Reg.year)
    await message.answer(f'Выберите курс', reply_markup=kb.year)



@router.message(Reg.year)
async def group(message: Message, state: FSMContext):
    await state.update_data(year=message.text)
    if message.text == '1 курс':
        await message.answer(f'{message.chat.id}', reply_markup=kb.group1)
    elif message.text == '2 курс':
        await message.answer(f'{message.chat.id}', reply_markup=kb.group2)
    elif message.text == '3, 4 курс':
        await message.answer(f'{message.chat.id}', reply_markup=kb.group34)
    await state.set_state(Reg.group)

@router.message(Reg.group)
async def first_second(message: Message, state: FSMContext):
    await state.update_data(group=message.text)
    data = await state.get_data()
    await message.answer(f'{message.chat.id}', reply_markup=kb.num_group(data['year'], data['group']))
    await state.set_state(Reg.num_group)

@router.message(Reg.num_group)
async def first_second(message: Message, state: FSMContext):
    await state.update_data(num_group=message.text)
    await message.answer(f'Выберите день/дни расписания', reply_markup=kb.day_button(message.text))
    await state.clear()

@router.message(F.text.startswith('На '))
async def first_second(message: Message):
    if message.text.split('  ')[0] == 'На сегодня':
        messag = ''
        name = pars_exel.the_schedule_for_today(message.text, pars_exel.kours(message.text))
        if len(name) != 1:
            for i in range(len(name[1])):
                messag += f'{name[0][i]} - {name[1][i]} {name[2][i]} {name[3][i]}\n'

            await message.answer(messag)
        else:
            await message.answer(name[0])

    elif message.text.split('  ')[0] == 'На завтра':
        messag = ''
        name = pars_exel.Tomorrows_schedule(message.text, pars_exel.kours(message.text))
        if len(name) != 1:
            for i in range(len(name[2])):
                messag += f'{name[0][i]} - {name[1][i]} {name[2][i]} {name[3][i]}\n'

            await message.answer(messag)
        else:
            await message.answer(name[0])

@router.message(F.text == 'Назад')
async def first_second(message: Message):
    await message.answer(f'Здравтсвуйте {message.chat.username}', reply_markup=kb.main)

@router.message(F.text == 'О Авторе')
async def first_second(message: Message, bot:Bot):
    photo = FSInputFile(path='photo_2024-01-17_12-10-48.jpg')
    await bot.send_photo(message.chat.id, photo=photo)
    await message.answer(text=pars_exel.text)
