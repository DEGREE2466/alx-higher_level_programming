#!/usr/bin/python3
'''
    Module that defines the classes for the tables
'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
        Creates table for states with id and name
    '''
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
