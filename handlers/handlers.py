from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import start_kb


user_router = Router()


@user_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=start_kb)


@user_router.message(Command(commands="help"))
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])


@user_router.message(F.text == LEXICON_RU["button_create_habit"])
async def start_command(message: Message):
    user_username = message.from_user.username
    await message.reply(f"Ваш ID: {user_username}")
