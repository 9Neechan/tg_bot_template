from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert 
from sqlalchemy.ext.asyncio import AsyncSession

from bot.db.models import User


async def insert_user(
        session: AsyncSession,
        tg_id: int,
        num_fittings: int | None = 15,
        sex: str | None = 'ru',
        language: str | None = None, 
):
    stmt = insert(User).values(
        {
            'tg_id': tg_id,
            'sex': sex,
            'language': language,
            'num_fittings': num_fittings,
        }
    )
    stmt = stmt.on_conflict_do_nothing(index_elements=['tg_id'])
    await session.execute(stmt)
    await session.commit()


async def update_user_language(session: AsyncSession, tg_id, lang):
    stmt = select(User).where(User.tg_id == tg_id)
    result = await session.execute(stmt)
    user = result.scalar()
    user.language = lang
    await session.commit()


async def update_user_sex(session: AsyncSession, tg_id, sex):
    stmt = select(User).where(User.tg_id == tg_id)
    result = await session.execute(stmt)
    user = result.scalar()
    user.sex = sex
    await session.commit()


async def update_user_fittings(session: AsyncSession, tg_id, num_fittings):
    stmt = select(User).where(User.tg_id == tg_id)
    result = await session.execute(stmt)
    user = result.scalar()
    user.num_fittings = num_fittings
    await session.commit()


async def get_value_from_users(session: AsyncSession, tg_id, find_column):
    stmt = select(User).filter_by(tg_id = tg_id)
    result = await session.execute(stmt)
    row = result.scalar_one_or_none()
    if row:
        return getattr(row, find_column, None)
    
    return None