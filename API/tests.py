import httplib2
import json
import sys

print('Running Tests')
address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':  ")
if address == '':
    address = 'http://localhost:5000'


#These are the tests for version 2
#Making a POST request for Restaurant with location
print("Making a POST request to restaurant")
try:
    url = address + "/restaurant?name=Zappos+Cafe+1&location=Las+Vegas"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 10 failed. Could not make a POST request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 10 PASSED. Succesfully made POST request to /restaurant")

#Making a GET request to retrieve all the restaurant based on a location
print("Making a GET request to restaurant with location as a parameter")
try:
    url = address + "/restaurant?location=Las+Vegas"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 11 failed. Could not make a GET request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 11 PASS. Succesfully made GET request to /restaurant")

#Making a DELETE request with restaurant name and location
print("Making a DELETE request to restaurant with arguments name and location")
try:
    url = address + "/restaurant?name=Zappos+Cafe+1&location=Las+Vegas"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 12 failed. Could not make a DELETE request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 12 PASS. Succesfully made DELETE request to /restaurant")

#Making a POST request to /restaurant/menu with restaurant name, location and menu type
#This will create a new record in menu table with values
# restaurant_id = restaurant ID for Zappos Cafe 1
# location = Provided Location
# menu_type = Provided Menu Type
print("Making a POST request to menu with given restaurant name, location and menu type")
try:
    url = address + "/restaurant?name=Zappos+Cafe+1&location=Las+Vegas"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    #The restaurant must be present to add the menu
    url = address + "/restaurant/menu?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 13 failed. Could not make a POST request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 13 PASS. Succesfully made POST request to /restaurant/menu")

#Making a GET request to /restaurant/menu with restaurant name and location
#This will retrieve all the menus for the given restaurant in the given location
print("Making a GET request to menu with given restaurant name and location")
try:
    url = address + "/restaurant/menu?name=Zappos+Cafe+1&location=Las+Vegas&type=Dinner"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    # Adding additional data above
    url = address + "/restaurant/menu?name=Zappos+Cafe+1&location=Las+Vegas"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 14 failed. Could not make a GET request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 14 PASS. Succesfully made GET request to /restaurant/menu")

#Making a DELETE request to delete a given menu from a restaurant
print("Making a DELETE request to menu with given restaurant name, location and menu_type")
try:
    url = address + "/restaurant/menu?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 15 Failed. Could not make a DELETE request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 15 PASS. Succesfully made DELETE request to /restaurant/menu")

#Making a POST request to menu item to add a new item for a restaurant in a paraticular location, given menu_type and price
print("Making a POST request to menu item with given restaurant name, location, menu type, item name and price")
try:
    url = address + "/restaurant?name=Zappos+Cafe+1&location=Las+Vegas"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    url = address + "/restaurant/menu?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    #The restaurant and menu must be present to add the item
    url = address + "/restaurant/menu/item?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch&item=Pasta&price=30"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 16 Failed. Could not make a POST request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 16 PASS. Succesfully made POST request to /restaurant/menu/item")

#Making a GET request to menu item to retrieve the details of items from a menu type in a restaurant at given location
print("Making a GET request to menu item to display all the details of an item")
try:
    url = address + "/restaurant/menu/item?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 17 Falied. Could not make a GET request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 17 PASSED. Succesfully made GET request to /restaurant/menu/item")

#Making a PUT request to update the price of an item
print("Making a PUT request to update the price of a menu item")
try:
    url = address + "/restaurant/menu/item?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch&item=Pasta&price=50"
    h = httplib2.Http()
    resp, result = h.request(url, 'PUT')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 18 Failed. Could not make a PUT request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 18 PASSED. Succesfully made PUT request to /restaurant/menu/item")

#Making a DELETE request to menu item with given restaurant name, location, menu type and item
print("Making a DELETE request to delete an item from menu item")
try:
    url = address + "/restaurant/menu/item?name=Zappos+Cafe+1&location=Las+Vegas&type=Lunch&item=Pasta"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 19 failed. Could not make a DELETE request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 19 PASSED. Succesfully made DELETE request to /restaurant/menu/item")
