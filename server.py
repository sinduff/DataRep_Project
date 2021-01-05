
from flask import Flask, url_for, request, redirect, abort, jsonify
from eeDAO import EmpDao 

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello, the webpage is working"

#set a variable for nextID for update tests
nextID = 3

#curl http://127.0.0.1:5000/employees
@app.route('/employees')
def getAll():
    return jsonify(EmpDao.getAll())
    
#curl http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:eeID>')
def findById(eeID):
    return jsonify(EmpDao.findByID(eeID)) 
    
#curl -X "POST" -H "Content-Type:application/json" -d "{\"eeID\":\3,\"firstName\":\"test\",\"lastName\":\"test\",\"address\":\"test\"}" http://127.0.0.1:5000/employees

#curl -X "POST" -H "Content-Type:application/json" -d "{\"eeID\":\2,\"firstName\":\"testCreate\",\"lastName\":\"testCreate\",\"address\":\"testCreate\",\"genderType\":\"Unknown\"}" http://127.0.0.1:5000/employees
@app.route('/employees', methods=['POST'])
def create():
    employee = {
       #"eeID": nextID,
        "firstName":request.json["firstName"],
        "lastName": request.json["lastName"],
        "address": request.json["address"],
        "genderType": request.json["genderType"],
    }
    return jsonify(EmpDao.create(employee))

#curl -X "PUT" -d "{\"firstName\":\"Steve\",\"lastName\":\"Rogers\"}" -H "Content-Type:application/json" http://127.0.0.1:5000/employees/4
@app.route('/employees/<int:eeID>', methods=['PUT'])
def update(eeID): 
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

#curl -X "DELETE" http://127.0.0.1:5000/employees/1
@app.route('/employees/<int:eeID>', methods=['DELETE'])
def delete(eeID): 
    EmpDao.delete(eeID)
    return jsonify({"done":True})
    #error check to make sure the searched for employee exists
 
if __name__ == "__main__":
    app.run(debug=True)