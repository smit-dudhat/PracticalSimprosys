# from database.config import Base
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


product_category = Table('product_category',
                        Base.metadata,
                        Column('product_id',Integer, ForeignKey('Product.id'),primary_key=True),
                        Column('category_id',Integer, ForeignKey('Cateogry.id'),primary_key=True))


class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class Product(Base):
    __tablename__ = 'Product' 
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    status = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    category = relationship(('Category'), secondary=False)
