
from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "secure_users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(320), unique=True, nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )


class Calculation(Base):
    __tablename__ = "calculations"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, index=True
    )

    a: Mapped[float] = mapped_column(
        Float, nullable=False
    )

    b: Mapped[float] = mapped_column(
        Float, nullable=False
    )

    type: Mapped[str] = mapped_column(
        String(10), nullable=False
    )

    result: Mapped[float | None] = mapped_column(
        Float, nullable=True
    )
