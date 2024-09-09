from sqlalchemy import BigInteger, String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from bot.db import Base
from bot.db.models.mixins import TimestampMixin


class User(TimestampMixin, Base):
    __tablename__ = "users"

    tg_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    sex: Mapped[str | None] = mapped_column(String, nullable=True)#False)
    language: Mapped[str | None] = mapped_column(String, nullable=True)#False)
    num_fittings: Mapped[int | None] = mapped_column(Integer, nullable=True)#False)
    # created_at добавляется из миксина