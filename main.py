import asyncio


from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties


from Config.config import Config, load_config


async def main():
    config: Config = load_config()

    bot = Bot(
        token=config.bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    dp = Dispatcher()

if __name__ == "__main__":
    asyncio.run(main())
    