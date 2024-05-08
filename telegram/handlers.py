from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
import sys
# sys.path.append('..')
# print(sys.path)

from keyboard import start_kb
from parser.main_train import info_road

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Шо ти голова", reply_markup=start_kb)


@router.message(lambda message: "Вишневе" in message.text or "Київ" in message.text)
async def start(message: types.Message):

    if message.text == "Вишневе-Київ":
        data_info_road = info_road()

    elif message.text == "Повна(Вишневе-Київ)":
        data_info_road = info_road(all_info=True)

    elif message.text == "Київ-Вишневе":
        data_info_road = info_road(index_url=1)

    elif message.text == "Повна(Київ-Вишневе)":
        data_info_road = info_road(index_url=1, all_info=True)

    text = ""
    for i in data_info_road:
        text += f"<u>{i.get('time')} | {i.get('road')} | {i.get('num')}</u>\n\n"

    await message.answer(text, reply_markup=start_kb)
