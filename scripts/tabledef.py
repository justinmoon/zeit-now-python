# -*- coding: utf-8 -*-
import os
import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    # return create_engine(os.environ['DATABASE_URI'], connect_args={'sslmode':'require'})
    return create_engine(os.environ['DATABASE_URI'])


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(512))
    email = Column(String(50))

    def __repr__(self):
        return '<User %r>' % self.username


engine = db_connect()  # Connect to database
Base.metadata.create_all(engine)  # Create models
