# example with caching postgerql for speed up requests
# https://github.com/MasterGroosha/advanced-telegram-bots/blob/master/08_Databases/02-sqlalchemy-orm/bot/middlewares/track_all_users.py

import asyncio
import logging
import sys
import os

from sqlalchemy import text

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.base import DefaultKeyBuilder

from fluentogram import TranslatorHub

# Добавляем корневой каталог проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bot.config_data.config import load_config
from bot.dialogs.start.dialogs import start_dialog
from bot.dialogs.menu.dialogs import menu_dialog
from bot.dialogs.admin.dialogs import admin_dialog
from bot.dialogs.generation.dialogs import looks_catalog_dialog, generation_menu_dialog, fitting_dialog
from bot.handlers.commands import commands_router
from bot.handlers.other import other_router
from bot.middlewares.i18n import TranslatorRunnerMiddleware
from bot.utils.i18n import create_translator_hub
from bot.db import Base
from bot.middlewares.session import DbSessionMiddleware
from bot.utils.db import SessionLocal, engine


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
           '%(lineno)d - %(name)s - %(message)s'
)

logger = logging.getLogger(__name__)


async def main() -> None:
    # laod config
    conf = load_config()

    # Хранилище переводов
    translator_hub: TranslatorHub = create_translator_hub()

    # Redis FSM storage
    storage = RedisStorage.from_url(conf.redis_db.dsn, key_builder=DefaultKeyBuilder(with_destiny=True))

    # Проверка соединения с СУБД
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

    # Создание таблиц
    async with engine.begin() as connection:
        # Если ловите ошибку "таблица уже существует", раскомментируйте следующую строку:
        #await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    # setup bot
    bot = Bot(
        token=conf.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    # await bot.delete_webhook(drop_pending_updates=True)

    dp = Dispatcher(storage=storage)
    dp.include_router(commands_router)
    dp.include_router(other_router)
    dp.include_routers(start_dialog)

    # Подключение мидлварей
    #dp.message.middleware(DbSessionMiddleware(SessionLocal)) # DB
    #dp.callback_query.middleware(DbSessionMiddleware(SessionLocal)) # DB
    dp.update.middleware(DbSessionMiddleware(SessionLocal)) # DB
    
    dp.update.middleware(TranslatorRunnerMiddleware()) # i18n

    setup_dialogs(dp)
    await dp.start_polling(bot, _translator_hub=translator_hub)


asyncio.run(main())