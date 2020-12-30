#sample code from rest_server.py in Wk08 Lab
from flask import Flask, url_for, request, redirect, abort, jsonify
from eeDAO import EmpDao 

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

#set a variable for nextID
nextID = 3

#get all values in the table employees
#curl http://127.0.0.1:5000/employees
@app.route('/employees')
def getAll():
    #to return all the ee's in the database
    #return jsonify([])
    return jsonify(EmpDao.getAll())
    

#find by id - one ee in database
#curl http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:eeID>')
def findById(eeID):
    #to return the ee with eeID of the EE of id number 1
    #return jsonify([])
    return jsonify(EmpDao.findByID(eeID))
    
#create a new entry into the database
#curl -X "POST" -H "Content-Type:application/json" -d "{\"eeID\":\3,\"firstName\":\"test\",\"lastName\":\"test\",\"address\":\"test\"}" http://127.0.0.1:5000/employees
# to check it worked .. curl http://127.0.0.1:5000/employees
#test for 2nd table
#curl -X "POST" -H "Content-Type:application/json" -d "{\"eeID\":\2,\"firstName\":\"testCreate\",\"lastName\":\"testCreate\",\"address\":\"testCreate\",\"genderType\":\"Unknown\"}" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def create():
    #sanity check to make sure flask link is working
    #return "used by create method"
    employee = {
       #"eeID": nextID,
        "firstName":request.json["firstName"],
        "lastName": request.json["lastName"],
        "address": request.json["address"],
        "genderType": request.json["genderType"],
    }
    return jsonify(EmpDao.create(employee))


#update
#curl -X "PUT" -d "{\"firstName\":\"Steve\",\"lastName\":\"Rogers\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees/4
#PUT FUNCTION RETURNS AN EMPTY  JSON OBJECT
@app.route('/employees/<int:eeID>', methods=['PUT'])
def update(eeID): 
    #sanity check to make sure flask link is working
    #return "used by update method"
    foundEEs = EmpDao.findByID(eeID)
    print(foundEEs)
    if len(foundEEs)==[]:
        return jsonify({}), 404
    currentEE = foundEEs
    if 'firstName' in request.json:
        currentEE['firstName'] = request.json['firstName']
    if 'lastName' in request.json:
        currentEE['lastName'] = request.json['lastName']
    if 'address' in request.json:
        currentEE['address'] = request.json['address']    
    if 'genderType' in request.json:
        currentEE['genderType'] = request.json['genderType']
    EmpDao.update(currentEE)
    return jsonify(currentEE)

#delete
#curl -X "DELETE" http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:eeID>', methods=['DELETE'])
def delete(eeID):
    #sanity check to make sure flask link is working
    #return "served by Delete method"
    
    EmpDao.delete(eeID)
    return jsonify({"done":True})

#ERROR CHECK FOR IF THE BOOK DOES NOT EXIST

if __name__ == "__main__":
    app.run(debug=True)