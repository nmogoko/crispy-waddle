# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app import db

Base = declarative_base()
metadata = Base.metadata


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String(100))
    created_at = Column(DateTime)


class ContentCalendar(db.Model):
    __tablename__ = 'content_calendar'

    content_calendar_id = Column(Integer, primary_key=True)
    content_calendar_date = Column(Date)
    task_title = Column(String)
    user_id = Column(ForeignKey('users.id'))
    status = Column(Enum('Done', 'NotDone', name='daily_tasks_list_status'))
    created_at = Column(DateTime)

    user = relationship('User')


class DailyTasksList(db.Model):
    __tablename__ = 'daily_tasks_list'

    task_id = Column(Integer, primary_key=True)
    task_title = Column(String)
    user_id = Column(ForeignKey('users.id'))
    status = Column(Enum('Done', 'NotDone', name='daily_tasks_list_status'))
    created_at = Column(DateTime)

    user = relationship('User')


class MovieList(db.Model):
    __tablename__ = 'movie_list'

    movie_id = Column(Integer, primary_key=True)
    movie_title = Column(String)
    user_id = Column(ForeignKey('users.id'))
    status = Column(Enum('Watched', 'NotWatched', name='movie_list_status'))
    created_at = Column(DateTime)

    user = relationship('User')


class QuickNote(db.Model):
    __tablename__ = 'quick_notes'

    quick_notes_id = Column(Integer, primary_key=True)
    quick_notes_title = Column(String)
    user_id = Column(ForeignKey('users.id'))
    status = Column(Enum('Done', 'NotDone', name='quick_notes_status'))
    created_at = Column(DateTime)

    user = relationship('User')


class ReadingList(db.Model):
    __tablename__ = 'reading_list'

    book_id = Column(Integer, primary_key=True)
    book_title = Column(String)
    user_id = Column(ForeignKey('users.id'))
    status = Column(Enum('Read', 'Unread', name='reading_list_status'))
    created_at = Column(DateTime)

    user = relationship('User')
