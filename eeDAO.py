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

    #function to create data as a json / dict object
    #updated for auto increment
    def create(self, employee):
        cursor = self.db.cursor()
        values = [
        #   employee['eeID'],
            employee['firstName'],
            employee['lastName'],
            employee['genderType'],
            employee['address'],
        ]
        #query for one table
        sql = "insert into employees (eeID, firstName, lastName, genderType, address) values (%s,%s,%s,%s,%s)"
        
        #sql code to query two tables with an inner join statement
        #sql = "SELECT employees.eeID, employees.firstName, employees.lastName, employees.address, genderinfo.genderType FROM genderinfo INNER JOIN employees ON genderinfo.genderType=employees.genderType"
        cursor.execute(sql,values)
        
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        #sql = "select * from employees"
        sql = "SELECT employees.eeID, employees.firstName, employees.lastName, employees.address, genderinfo.genderType FROM genderinfo INNER JOIN employees ON genderinfo.genderType=employees.genderType"
        cursor.execute(sql)
        results = cursor.fetchall()
        #conver tupple from results into an array
        returnArray = []
            #sanity check
        #print(results)
        for result in results:
            #call the funtion convertToDict
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        
        return returnArray

    def convertToDict(self,result):
        #convert the tupple to ino a dict object called 'employee{}'
        colnames = ['eeID', 'firstName', 'lastName', 'address', 'genderType']
        employee = {}

        #iterate through the results, and for every colName, covert to []
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
        
        #convert the returned value into a dict object
        return self.convertToDict(result)
    
    def update(self,employee):
        cursor = self.db.cursor()
        #sql code to query 1 table
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



#make a new instace of the class to get the code to run
EmpDao = EmpDao()

