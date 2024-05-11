from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вишневе-Київ"),
            KeyboardButton(text="Київ-Вишневе"),
        ],
        [
            KeyboardButton(text="Повна(Вишневе-Київ)"),
            KeyboardButton(text="Повна(Київ-Вишневе)"),
        ]
    ],
    resize_keyboard=True
)