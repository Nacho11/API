from flask import Flask, request, jsonify
from models import Restaurant, Menu, MenuItem, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///restaurants.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route("/restaurant", methods=["GET", "POST", "DELETE"])
def restaurantFunction():
    if request.method == "GET":
        return getAllRestaurants()
    elif request.method == "POST":
        name = request.args.get('name', '')
        return createRestaurant(name)
    elif request.method == "DELETE":
        name = request.args.get('name', '')
        return deleteRestaurant(name)

@app.route("/restaurant/menu", methods=["GET", "POST", "DELETE"])
def restaurantMenuFunction():
    name = request.args.get('name', '')
    menu_type = request.args.get('type', '')
    if request.method == "GET":
        return getMenu(name)
    elif request.method == "POST":
        return addMenu(name, menu_type)
    elif request.method == "DELETE":
        return deleteMenu(name, menu_type)

@app.route("/restaurant/menu/item", methods=["GET", "POST", "DELETE"])
def menuItemFunction():
    name = request.args.get('name', '')
    menu_type = request.args.get('type', '')
    item = request.args.get('item', '')
    if request.method == 'GET':
        return getItems(name, menu_type)
    elif request.method == 'POST':
        return addItems(name, menu_type, item)
    elif request.method == 'DELETE':
        return deleteItem(name, menu_type, item)


def getAllRestaurants():
    restaurant = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurant])

def createRestaurant(name):
    restaurant = Restaurant(restaurant_name=name)
    session.add(restaurant)
    session.commit()
    return jsonify(Restaurant = restaurant.serialize)

def deleteRestaurant(name):
    restaurant = session.query(Restaurant).filter_by(restaurant_name=name).all()
    #print(restaurant)
    session.delete(restaurant[0])
    session.commit()
    return "Removed Restaurant with name %s" % name

def getMenu(name):
    #restaurant_id = session.query(Restaurant).filter_by(restaurant_name=name).one()
    menus = session.query(Menu).filter_by(restaurant_name=name).all()
    return jsonify(Menus=[i.serialize for i in menus])

def addMenu(name, menu_type):
    #restaurant_id = session.query(Restaurant).filter_by(restaurant_name=name).one()
    menu = Menu(restaurant_name=name, menu_type=menu_type)
    session.add(menu)
    session.commit()
    return jsonify(Menu = menu.serialize)

def deleteMenu(name, menu_type):
    menu = session.query(Menu).filter_by(restaurant_name=name, menu_type=menu_type).all()
    session.delete(menu[0])
    session.commit()
    return "Removed the menu with type %s in restaurant %s" % (name, menu_type)

def getItems(name, menu_type):
    menu = session.query(Menu).filter_by(restaurant_name=name, menu_type=menu_type).one()
    print(menu)
    items = session.query(MenuItem).filter_by(menu_id=menu.id).all()
    return jsonify(Items=[i.serialize for i in items])

def addItems(name, menu_type, item):
    menu = session.query(Menu).filter_by(restaurant_name=name, menu_type=menu_type).one()
    item = MenuItem(item_name=item, menu_id=menu.id)
    session.add(item)
    session.commit()
    return jsonify(MenuItem = item.serialize)

def deleteItem(name, menu_type, item):
    menu = session.query(Menu).filter_by(restaurant_name=name, menu_type=menu_type).all()
    item = session.query(MenuItem).filter_by(menu_id=menu[0].id, item_name=item).one()
    session.delete(item)
    session.commit()
    return "Removed the item %s from the menu %s in the restaurant %s" % (name, menu_type, item)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5004)
