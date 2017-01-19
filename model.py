import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as declarative
from zope.sqlalchemy import ZopeTransactionExtension as ZTE

DBSession = orm.scoped_session(orm.sessionmaker(extension=ZTE()))
Base = declarative.declarative_base()

class login(Base):
    __tablename__ = "login"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.Unicode(100), nullable=False)
    email = sa.Column(sa.Unicode(100), nullable=False)
