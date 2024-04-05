from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey
from datetime import datetime
from environ import DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USERNAME

db_url = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = create_engine(url=db_url)
Session = scoped_session(sessionmaker(autoflush=False, bind=engine))
session = Session()


Base = declarative_base()

# Base.metadata = Session.query_property()
