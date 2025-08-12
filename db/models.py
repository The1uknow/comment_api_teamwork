from sqlalchemy import (Integer, String, DateTime, Column, Boolean, ForeignKey)
from sqlalchemy.orm import relationship
from db import Base
from datetime import datetime




class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement = True, primary_key = True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    birthday = Column(String, nullable=False)
    city = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


class UserPost(Base):
    __tablename__ = 'userposts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    main_text = Column(String, max_length = 256)
    reg_date = Column(DateTime, default=datetime.now())

    user_id_fk = relationship(User, lazy = 'subquery')


class PostPhoto(Base):
    __tablename__ = 'photos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    photo_path = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('userposts.id'), nullable = False)
    reg_date = Column(DateTime, default=datetime.now())

    post_id_fk = relationship(UserPost, lazy='subquery')



class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    post_id = Column(Integer, ForeignKey('userposts.id'), nullable = False)
    text = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    user_id_fk = relationship(User, lazy='subquery')
    post_id_fk = relationship(User, lazy='subquery')
