from eeDAO import EmpDao 

#print("ok")

employee3 = {
    'eeID':'3',
    'firstName':'Steve',
    'lastName':'Rogers',
    'address':'Washington DC'
}
#import the instance of the code above
#returnvalues = EmpDao.create(employee2)
#print(returnvalues)

result = EmpDao.getAll()
print(result)

result = EmpDao.findByID(employee3['eeID'])
print("find By ID :")
print(result)

returnvalue = EmpDao.update(employee3)
print(result)

#to see the changed employee data
result = EmpDao.findByID(employee3['eeID'])
print(result)

result = EmpDao.delete(employee3['eeID'])
print(result)

#to check that the employee has been deleted
result = EmpDao.getAll()
print(result)
