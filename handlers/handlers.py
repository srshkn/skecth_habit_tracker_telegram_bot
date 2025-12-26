from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import start_kb

user_router = Router()


@user_router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU["/start"], reply_markup=start_kb)
