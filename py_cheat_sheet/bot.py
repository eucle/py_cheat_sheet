import asyncio

from aiogram import Bot, Dispatcher
from loguru import logger

from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers
from keyboards.main_menu import set_main_menu


async def main():
    logger.info("Bot started.")

    config: Config = load_config()

    bot = Bot(
        token=config.tg_bot.token,
    )
    dp = Dispatcher()

    await set_main_menu(bot)
    logger.info("Main menu set.")

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    logger.info("Handlers are ready.")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
