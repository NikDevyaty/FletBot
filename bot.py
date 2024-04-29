import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.types import Message, WebAppInfo
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from motor.motor_asyncio import AsyncIOMotorClient

# from handlers import setup_message_routers
# from callbacks import setup_callbacks_routers

# from middlewares import CheckUser


# from config_reader import config
def webapp_builder() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="lets Click!",
        web_app=WebAppInfo(url="https://f8cd-185-97-201-64.ngrok-free.app"),
    )
    return builder.as_markup()


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.reply("Click Click", reply_markup=webapp_builder())


async def main() -> None:
    bot = Bot(
        "7000256880:AAHidXEOByPasXkppLRL5ZseH74fLQGolYw", parse_mode=ParseMode.HTML
    )
    dp = Dispatcher()

    # cluster = AsyncIOMotorClient(config.DATABASE_URL.get_secret_value())
    # db = cluster.anonimdb

    # dp.message.middleware(CheckUser())

    # message_routers = setup_message_routers()
    # callback_routers = setup_callbacks_routers()
    dp.include_router(router)
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
