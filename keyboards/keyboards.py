from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


from lexicon.lexicon import LEXICON_RU


button_create_habit = KeyboardButton(text=LEXICON_RU["button_create_habit"])
button_change_habit = KeyboardButton(text=LEXICON_RU["button_change_habit"])
button_list_habit = KeyboardButton(text=LEXICON_RU["button_list_habit"])

start_kb_builder = ReplyKeyboardBuilder()

start_kb_builder.row(button_create_habit, button_change_habit, button_list_habit, width=1)

start_kb: ReplyKeyboardMarkup = start_kb_builder.as_markup(
    one_time_keyboard=False, resize_keyboard=True
)