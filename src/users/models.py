from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class User(Base):
    __tablename__ = "user"

    id:              Mapped[int]          = mapped_column(primary_key=True)
    email:           Mapped[str]          = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]          = mapped_column()

    registered_at:   Mapped[datetime]     = mapped_column(default=datetime.now, index=True)
    updated_at:      Mapped[datetime]     = mapped_column(default=datetime.now, onupdate=datetime.now, index=True)

  