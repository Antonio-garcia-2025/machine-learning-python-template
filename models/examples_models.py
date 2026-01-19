from sqlalchemy.orm import declarativeBase
from sqlalchemy import string
from sqlalchemy.orm import Mapped, mapped_column

Base = declarativeBase()

class ExampleModel(Base):
    _tablename_ = 'example_table'
    id: Mapped[int] =  mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)

