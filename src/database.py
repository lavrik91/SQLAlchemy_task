
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
from config import settings




# синхронное подключение к бд
sync_engine = create_engine(settings.DB_URL)

sync_session = sessionmaker(sync_engine)


class Base(DeclarativeBase):
    pass
    # repr_cols_num = 3
    # repr_cols = tuple()
    #
    # def __repr__(self):
    #     """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
    #     cols = []
    #     for idx, col in enumerate(self.__table__.columns.keys()):
    #         if col in self.repr_cols or idx < self.repr_cols_num:
    #             cols.append(f"{col}={getattr(self, col)}")
    #
    #     return f"<{self.__class__.__name__} {', '.join(cols)}>"



