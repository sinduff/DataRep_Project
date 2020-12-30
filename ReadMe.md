# Data Representation and Querying
## Project 2020 
### Submited by Sinéad Duffy, Student ID - 10016151

## Introduction
The brief for this project was to work with API's and have the data they interfaced with displayed via a web interface.  There was two options that were available, namely;
1. A web application project
2. A third party API project

The author evaluated both options and has chosen to undertake option 1, namely the **Web applicaiton project**.

As per the project brief, a git-hub file was created, and a link was shared for submission.

The project conists of a number of files, namely

1. initdb.sql
2. eeDAO.py
3. server.py
4. /staticpages/index.html
5. /staticpages/index.js
6. ReadMe.md
7. requirements.txt

The structure and outline of the programmes will be outlined in the following sections.

### 1. initdb.sql
The initdb.sql file outlines how the two tables were created in MySQL.  The two tables created are;
1. **employees** - contains employee data for a databae called **hrSystem**.  The table had a number of columns namely;
	a.	empNo - this was an auto incremental number and the primary key of the table.
	b.	firstName - the first name of the employee
	c.	lastName - the last name of the employee
	d.	address - the address of the employee
	e.	genderType - this column was added later, and links to the second table, genderInfo
	
2. **genderInfo** - outlines possible genders allowable in the system, namely
	a.	genderNo	number of entries in the table
	b.	genderType	the possible types of gender i.e. Male / Female / Unknown

### 2. eeDAO.py
This file, provides the link between the database, and the flask server.  The program creates a class called EmpDAO with a number of functions that allow the program to interact with the MySQL database.  The functions contain SQL code to query the database, and this is faciliated by the command *cursor.execute*, which relates to the **mysql.connector** library imported at the start of the program.  The functions created are; 

1. **def __init__ **- links to the database, and provide the address, passwords, database name etc.
2. **def create** - provides the structure to create a new record
3. **def getAll** - returns all the data from the database
4. **def ConvertToDict** - converts the returned data (which is a tupple) from the database into a dictionary object called 'employee{}'.  The program iterates through the results, and for every column name returend, it converts it to a array.
5. **def findByID** - searches the database for a specific id number, and returns to the user.
6. **def update** - provides to code to update an existing record in the database
7. **def delete** - provides the code to allow a user to delete an existing record in a database.

### 3. server.py
The server.py program creates a flask server, which will allow the database to interact with a web based interface.  The flask module is imported at the start of the program, as well as a link to the EmpDAO, which was created in the eeDAO.py file above. 

The relevant sections of the program are outlined below.

1. **app** - defines the route to the relevant files to access for the server.













