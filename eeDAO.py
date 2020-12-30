import mysql.connector
from mysql.connector import cursor

class EmpDao:
    db = ""
    def __init__(self):
         self.db = mysql.connector.connect(
            host = 'localhost',
            user= 'root',
            password = '',
            database ='hrSystem'
        )
    #check to make sure code is working
    #print ("connection made")

    def create(self, employee):
        cursor = self.db.cursor()
        values = [
        #   employee['eeID'],  ... removed to allow for auto increment
            employee['firstName'],
            employee['lastName'],
            employee['genderType'],
            employee['address'],
        ]
        sql = "insert into employees (eeID, firstName, lastName, genderType, address) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql,values)
        
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "SELECT employees.eeID, employees.firstName, employees.lastName, employees.address, genderinfo.genderType FROM genderinfo INNER JOIN employees ON genderinfo.genderType=employees.genderType"
        cursor.execute(sql)
        results = cursor.fetchall()
        #convert tupple of data from results into an array
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        return returnArray

    def convertToDict(self,result):
        colnames = ['eeID', 'firstName', 'lastName', 'address', 'genderType']
        employee = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value
            return employee

    def findByID(self,eeID):
        cursor = self.db.cursor()
        sql = "select * from employees where eeID = %s"
        values = [ eeID ]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)
    
    def update(self,employee):
        cursor = self.db.cursor()
        sql = "update employees set firstName = %s, lastName= %s, genderType= %s, address= %s  where eeID =%s"
        values = [
            employee['firstName'],
            employee['lastName'],
            employee['genderType'],
            employee['address'],
            employee['eeID']
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return employee
            
    def delete(self,eeID):
        cursor = self.db.cursor()
        sql = "delete from employees where eeID = %s"
        values = [ eeID ]
        cursor.execute(sql, values)
        return {}

EmpDao = EmpDao()

