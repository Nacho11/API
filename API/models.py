from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

#Restaurant Table
class Restaurant(Base):
    __tablename__ = 'restaurant'
    id = Column(Integer, primary_key=True)
    menus = relationship("Menu")
    restaurant_name = Column(String)

    @property
    def serialize(self):
        return {
        'restaurant_name': self.restaurant_name,
        'id': self.id
        }

#Menu Table
class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    restaurant_name = Column(Integer, ForeignKey('restaurant.restaurant_name'))
    menu_type = Column(String)
    menu_items = relationship("MenuItem")

    @property
    def serialize(self):
        return {
        'menu_type': self.menu_type,
        'restaurant_name': self.restaurant_name,
        'id': self.id
        }

#Menu Item Table
class MenuItem(Base):
    __tablename__ = 'menuitem'
    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    menu_id = Column(Integer, ForeignKey('menu.id'))

    @property
    def serialize(self):
        return {
        'item_name': self.item_name,
        'menu_id' : self.menu_id,
        'id' : self.id
        }

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.create_all(engine)
