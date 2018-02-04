import httplib2
import json
import sys

print('Running Tests')
address = input("Please enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000':  ")
if address == '':
    address = 'http://localhost:5000'

#Making a POST request to restaurant
print("Making a POST request to restaurant")
try:
    url = address + "/restaurant?name=Zappos+Cafe"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    obj = json.loads(result)
    restaurantID = obj['Restaurant']['id']
    if resp['status'] != '200':
        raise Exception("Received an unsuccessful status code of %s" % resp['status'])

except Exception as err:
    print("Test 1 failed. Could not make POST request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 1 PASS: Succesfully Made POST request to /restaurant ")

#Making a GET request to restaurant
print("Making a GET request to restaurant")
try:
    url = address + "/restaurant"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    obj = json.loads(result)
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 2 failed. Could not make GET request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 2 PASS: Succesfully Made GET request to /restaurant")

#Making a DELETE request to restaurant
print("Making a DELETE request to restaurant")
try:
    url = address + "/restaurant?name=Zappos+Cafe"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 3 Failed. Could not make DELETE request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 3 PASS: Succesfully Made DELETE request to /restaurant")

#Making a POST request to Menu
print("Making a POST request to menu")
try:
    url = address + "/restaurant/menu?name=Zappos+Cafe&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    obj = json.loads(result)
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 4 Failed. Could not make POST request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 4 PASS: Succesfully Made POST request to /restaurant/menu")

#Making a GET request to Menu
print("Making a GET request to Menu")
try:
    url = address + "/restaurant/menu?name=Zappos+Cafe"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    obj = json.loads(result)
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 5 Failed. Could not make GET request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 5 PASSED: Succesfully made GET request to /restaurant/menu")

#Making a DELETE request to Menu
print("Making a DELETE request to Menu")
try:
    url = address + "/restaurant/menu?name=Zappos+Cafe&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 6 failed. Could not make DELETE request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 6 PASSED: Succesfully made DELETE request to /restaurant/menu")

#Making a POST request to Menu Item
print("Making a POST request to menu item")
try:
    #Adding the Zappos Cafe with Lunch menu into the database so that the menu item can be added
    url = address + "/restaurant/menu?name=Zappos+Cafe&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    url = address + "/restaurant/menu/item?name=Zappos+Cafe&type=Lunch&item=Pasta"
    h = httplib2.Http()
    resp, result = h.request(url, 'POST')
    obj = json.loads(result)
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 7 failed. Could not make POST request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 7 PASSED: Succesfully made POST request to /restaurant/menu/item")

#Making a GET request to Menu Item
print("Making a GET request to menu item")
try:
    url = address + "/restaurant/menu/item?name=Zappos+Cafe&type=Lunch"
    h = httplib2.Http()
    resp, result = h.request(url, 'GET')
    obj = json.loads(result)
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 8 failed. Could not make a GET request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 8 PASSED: Succesfully made GET request to /restaurant/menu/item")

#Making a DELETE request to Menu Item
print("Making a DELETE request to menu item")
try:
    url = address + "/restaurant/menu/item?name=Zappos+Cafe&type=Lunch&item=Pasta"
    h = httplib2.Http()
    resp, result = h.request(url, 'DELETE')
    if resp['status'] != '200':
        raise Exception("Received an unsuccesful status code of %s" % resp['status'])

except Exception as err:
    print("Test 9 failed. Could not make a DELETE request to web server")
    print(err.args)
    sys.exit()
else:
    print("Test 9 PASS: Succesfully made DELETE request to /restaurant/menu/item")
