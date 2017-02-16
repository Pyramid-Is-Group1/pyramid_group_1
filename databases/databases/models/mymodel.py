from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class Students(Base):
	__tablename__ = 'students'
	id = Column(Integer, primary_key=True)


class Faculty(Base):
	__tablename__ = 'Faculty'
	id = Column(Integer, primary_key=True)
	name = Column(Text)
	department = Column(Text)
	password = Column(Text)
	
Index('my_index', MyModel.name, unique=True, mysql_length=255)

