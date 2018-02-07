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
    location = request.args.get('location', '')
    name = request.args.get('name', '')
    if request.method == "GET":
        return getAllRestaurants(location)
    elif request.method == "POST":
        return createRestaurant(name, location)
    elif request.method == "DELETE":
        return deleteRestaurant(name, location)

@app.route("/restaurant/menu", methods=["GET", "POST", "DELETE"])
def restaurantMenuFunction():
    name = request.args.get('name', '')
    location = request.args.get('location', '')
    menu_type = request.args.get('type', '')
    if request.method == "GET":
        return getMenu(name, location)
    elif request.method == "POST":
        return addMenu(name, location, menu_type)
    elif request.method == "DELETE":
        return deleteMenu(name, location, menu_type)

@app.route("/restaurant/menu/item", methods=["GET", "POST", "PUT", "DELETE"])
def menuItemFunction():
    name = request.args.get('name', '')
    location = request.args.get('location', '')
    menu_type = request.args.get('type', '')
    item = request.args.get('item', '')
    price = request.args.get('price', '')
    if request.method == 'GET':
        return getItems(name, location, menu_type)
    elif request.method == 'POST':
        return addItems(name, location, menu_type, item, price)
    elif request.method == 'DELETE':
        return deleteItem(name, location, menu_type, item)
    elif request.method == "PUT":
        return updateItem(name, location, menu_type, item, price)

def getAllRestaurants(location):
    if location != '':
        restaurant = session.query(Restaurant).filter_by(location=location).all()
    else:
        restaurant = session.query(Restaurant).all()
    return jsonify(Restaurants=[i.serialize for i in restaurant])

def createRestaurant(name, location):
    restaurant = Restaurant(restaurant_name=name, location=location)
    session.add(restaurant)
    session.commit()
    return jsonify(Restaurant = restaurant.serialize)

def deleteRestaurant(name, location):
    restaurant = session.query(Restaurant).filter_by(restaurant_name=name, location=location).all()
    session.delete(restaurant[0])
    session.commit()
    return "Removed Restaurant with name %s" % name

def getMenu(name, location):
    query = (session.query(Restaurant, Menu).join(Menu).filter(Restaurant.restaurant_name==name, Restaurant.id == Menu.restaurant_id)).all()
    list_of_menus = []
    for each in query:
        rest, menu = each
        list_of_menus.append(menu)
    return jsonify(Menus=[i.serialize for i in list_of_menus])

def addMenu(name, location, menu_type):
    restaurant = session.query(Restaurant).filter_by(restaurant_name=name, location=location).all()
    rest_id = restaurant[0].id
    menu = Menu(restaurant_id=rest_id, menu_type=menu_type)
    session.add(menu)
    session.commit()
    return jsonify(Menu = menu.serialize)

def deleteMenu(name, location, menu_type):
    query = (session.query(Restaurant, Menu).join(Menu).filter(Restaurant.restaurant_name==name, Restaurant.id == Menu.restaurant_id, Menu.menu_type == menu_type)).one()
    rest, menu = query
    session.delete(menu)
    session.commit()
    return "Removed the menu with type %s in restaurant %s" % (name, menu_type)

def getItems(name, location, menu_type):
    query = (session.query(Restaurant, Menu, MenuItem)
    .join(Menu)
    .join(MenuItem)
    .filter(Restaurant.restaurant_name==name, Restaurant.location==location, Restaurant.id == Menu.restaurant_id, Menu.menu_type == menu_type, MenuItem.menu_id == Menu.id)).all()
    list_of_items = []
    for each in query:
        rest, menu, item = each
        list_of_items.append(item)
    return jsonify(Items=[i.serialize for i in list_of_items])

def addItems(name, location, menu_type, item, price):
    query = (session.query(Restaurant, Menu).join(Menu).filter(Restaurant.restaurant_name==name, Restaurant.location==location, Restaurant.id == Menu.restaurant_id, Menu.menu_type == menu_type)).one()
    rest, menu = query
    item = MenuItem(item_name=item, menu_id=menu.id, price=price)
    session.add(item)
    session.commit()
    return jsonify(MenuItem = item.serialize)

def deleteItem(name, location, menu_type, item):
    query = (session.query(Restaurant, Menu, MenuItem)
    .join(Menu)
    .join(MenuItem)
    .filter(Restaurant.restaurant_name==name, Restaurant.location == location, Restaurant.id == Menu.restaurant_id, Menu.menu_type == menu_type, MenuItem.menu_id == Menu.id, MenuItem.item_name == item)).one()
    rest, menu, item = query
    session.delete(item)
    session.commit()
    return "Removed the item %s from the menu %s in the restaurant %s" % (name, menu_type, item)

def updateItem(name, location, menu_type, item, price):
    query = (session.query(Restaurant, Menu, MenuItem)
    .join(Menu)
    .join(MenuItem)
    .filter(Restaurant.restaurant_name==name, Restaurant.location == location, Restaurant.id == Menu.restaurant_id, Menu.menu_type == menu_type, MenuItem.menu_id == Menu.id, MenuItem.item_name == item)).one()
    rest, menu, item = query
    item.price = price
    session.add(item)
    session.commit()
    return "Updated the price of the item %s on the menu %s in the restaurant %s to %s" % (item, menu_type, name, price)

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
