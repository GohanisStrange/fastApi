from sqlalchemy import Column , Integer , DateTime , ForeignKey, String, Boolean, Float
from sqlalchemy.orm import relationship

from database import Base

class Bake(Base):
    __tablename__ = 'deserts'
    bakery_products_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    bake_date = Column(DateTime)
    price = Column(String)

class Cupcakes(Base):
    __tablename__ = 'cupcakes'
    cupcake_id = Column(String, ForeignKey('deserts.bakery_products_id'))
    cupcake_amount = Column(String,nullable=False)
    cupcake_price = Column(String,ForeignKey('deserts.price'))
    cupcake_taste = Column(String)
    cupcake_date = Column(DateTime)


class Bakers(Base):
    __tablename__ = 'bakers'
    bakery_id = Column(String, primary_key=True, autoincrement=True)
    bakery_location = Column(String)
    bakery_name = Column(String)

