from eeDAO import EmpDao 

#print("ok")

employee = {
    'eeID':'2',
    'firstName':'Pepper',
    'lastName':'Potts',
    'address':'123 Stark Towers'
}
#import the instance of the code above
#returnvalues = EmpDao.create(employee)
#print(returnvalues)

#result = EmpDao.getAll()
#print(result)

result = EmpDao.getAll()
print(result)
