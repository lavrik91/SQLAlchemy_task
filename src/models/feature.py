from sqlalchemy import Column, Integer, Float, ForeignKey, String, CheckConstraint, Text
from sqlalchemy.orm import relationship, validates

from database import Base


class GitTestModel(Base):
    __tablename__ = 'git_tests'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    text = Column(Text)