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
    def create(self, employee):
        cursor = self.db.cursor()
        sql = "insert into employees (eeID, firstName, lastName, address) values (%s,%s,%s,%s)"
        values = [
            employee['eeID'],
            employee['firstName'],
            employee['lastName'],
            employee['address'],
        ]
        cursor.execute(sql,values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = "select * from employees"
        cursor.execute(sql)
        results = cursor.fetchall()
        #conver tupple from results into an array
        returnArray = []
            #sanity check
        print(results)
        for result in results:
            #call the funtion convertToDict
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        
        return returnArray

    def convertToDict(self,result):
        #convert the tupple to ino a dict object called 'employee{}'
        colnames = ['eeID', 'firstName', 'lastName', 'address']
        employee = {}

        #iterate through the results, and for every colName, covert to []
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                employee[colName] = value
            return employee

    def findbyID



#make a new instace of the class to get the code to run
EmpDao = EmpDao()

