from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from bot.config_data.config import load_config


conf = load_config()

# connect to PG
engine = create_async_engine(
    url=str(conf.pg_db.dsn),  
    echo=conf.pg_db.is_echo
)

# Создание асинхронной сессии
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)