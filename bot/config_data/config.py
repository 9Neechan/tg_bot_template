from dataclasses import dataclass
from environs import Env
from pydantic import PostgresDsn, RedisDsn


@dataclass
class TgBot:
    token: str  # Токен для доступа к телеграм-боту


@dataclass
class PGConfig:
    dsn: PostgresDsn
    is_echo: bool


@dataclass
class RedisConfig:
    dsn: RedisDsn


@dataclass
class Config:
    tg_bot: TgBot
    pg_db: PGConfig
    redis_db: RedisConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(token=env('BOT_TOKEN')),
        pg_db=PGConfig(dsn=env('PG_DSN'), is_echo=bool(env('IS_ECHO'))),
        redis_db=RedisConfig(dsn=env('REDIS_DSN'))
    )