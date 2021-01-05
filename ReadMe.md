# Data Representation and Querying
## Project 2020 
### Submited by Sinéad Duffy, Student ID - 10016151

## Introduction
The brief for this project was to work with API's and have the data they interfaced with displayed via a web interface.  There was two options that were available, namely;
1. A web application project
2. A third party API project

The author evaluated both options and has chosen to undertake option 1, namely the **Web application project**.

As per the project brief, a git-hub file was created, and a link was shared for submission.  The server.py and eeDAO.py files use CRUD operations to complete the updates to the server and database respectively.  CRUD operations used for the purpose of the project are:

[![N|Solid](\CRUD Operations.GIF]

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
2. **def create** - provides the structure to create a new record.  The SQL command to create a new record, using the 'INSERT INTO'  command is included here.
3. **def getAll** - returns all the data from the database
4. **def ConvertToDict** - converts the returned data (which is a tupple) from the database into a dictionary object called 'employee{}'.  The program iterates through the results, and for every column name returend, it converts it to a array.
5. **def findByID** - searches the database for a specific id number, and returns to the user.
6. **def update** - provides to code to update an existing record in the database
7. **def delete** - provides the code to allow a user to delete an existing record in a database.

### 3. server.py
The server.py program creates a flask server, which will allow the database to interact with a web based interface.  The flask module is imported at the start of the program, as well as a link to the EmpDAO, which was created in the eeDAO.py file above. 

The relevant sections of the program are outlined below.

1. **@app.route()** - defines the route to the relevant files to access for the server.
2. **@app.route('/employees')** - calls the function getAll from the file eeDAO.py.  The link is tested using curl statements, each of which are included above each of the @app.route statements. 0
3. **@app.route('/employees/1')** - calls the findById function, and returns the database record equal to the id number at the end of the statement.
4. **@app.route('/employees', methods=['POST'])** - using the POST method, this function calls the create function and is used to create a new record for the database.
5. **@app.route('/employees/<int:eeID>', methods=['PUT'])** -updates the selected record by using the PUT method.  The function findByID is called, and filter through the arguments passed to it to update the selected fileds.  An error message is also built to alert the user if the requested record was not contained in the database.
6. **@app.route('/employees/<int:eeID>', methods=['DELETE'])** - deletes the selected record from the database using the DELETE method.  The method calls the delete function from the EmpDAO program.

### 4. index.html
The index file is stored in the folder called 'staticfolder', and is referenced at the start of the server.py file.  Indeed, without running the server.py file, the link to the database will not be created, and an error will be displayed.

The purpose fo this file is to act as an interface between the MySQL server and the end user.

The Index.html file consists of one html page, with two tables, the first table with the id of 'createUpdateForm', is encased in <div> tags, which have been set to 'none'.  This means that nothing is displayed.  The <div> tags also hold a table with a number of rows down the left hand of the page.  The input boxes are lined to a function in the index.js file.

One of the rows in this table is a drop box which is filled with the 3 input choices for gender.  The author ran out of time, and was not able to finish the connect to the database correctly.  All other input forms are linked to the database.

Further down the the program is a second set of <div> tags which hold a second table.  This table is visible to the user once the page is loaded.

Within the <script>, there is a call to an index.js file.  The author has chosen to place the functions for this program in an javascript file for clarity.  The file is called by referencing the file itself.

### 5. index.js
The index.js file contains the functions that display the data from the MySQL database and the connection with the Flask server in the server.py file.

At the start of the file is an empty array which holds the values as the pass from the html file to the functions.  The functions are outlined below.

1. **function showCreate** - links to the 'create' button at the top of the html page.  When clicked, the button displays the hidden table at the top of the code.  The table displaying the data from the database is hidden once this button is clicked.
2. **function showUpdate** - this function reads in the data on the line on which the update button is resting via the 'thisElem' variable.  The function reads in the data, then passes it to another function called populateForm.  The values are passed through the empty array defined at the start.
3. **function populateForm** - this function takes in the variable 'eeUpdate', and updates the input fields with the values relating to the corresponding fields in the database.
4. **function doCreate** on the hidden page, a 'create' button is placed.  When this button is selected, it interfaces with the flask server using ajax, and 'POSTs' the new record via the function populateTable.  Error handling is also included and will display the error code if necessary.
5. **function showDisplay** - referened above, the function shows the hidden create button when the create option is selected.
6. **function doUpate** references the function getEEFromForm where the details that have been updated are stored, and passed to another function called updateServer.
7. **function updateServer** the employee details are passed to the function, which in turns use ajax to 'PUT' the updated dated details into the database.  Error handling is also included.
8. **function updateTableRow** function to update the row of the selected employee details
9. **function doDelete** passes through the id of the selected row, and then, using the 'DELETE' method passed through ajax, deletes the relevant record
from the database****
10. **function getEEFromForm** an empty array is created and is filled with the values of the row of the table that was selected.  the function is called in the  doUpate function
11. **function populateTable**  the first thing this function does is clear the table of any data that may have been loaded.  It passed through a blank emploee reference, and uses ajax to interface with the database using a 'GET' method.  Ultimately, this function gets the data from the database and populates the second table in the Index.html file.  This is the table that is shown to the user when they first load the html file.
12. **function populateGenderList** as with populateTable above, this function interacts with the database, specificly the 'gendertype' table and loads the data into the update form.
13. **function addEEtoTable** creates a new row in the table, and then loads the data form the table to the correct field.  The function populateTable at the end of the function, then takes the data and passes it into the table for display.
14. **function goBack** displays on the 'create' page, and brings the user back to the index page.  Other code is included here to go back a page, but this will bring the user to the last page used, not the index page.

### 6. ReadMe.md
This readme file outlines the details of the code and functions that are held there.

### 7. requirements.txt
This file outlines the running oder of the different programs.  Unless the code is run in specific order, the program will not run.

#### Conclusion
Generally the program runs, however, the addition of the second table and time constraints have not allowed the author to get database link working correctly.

### Refrenences
1. Lecture Materials by Andrew Beatty
2. W3Schools - specifcally'
 1. SQL
 2. Html
 3. Bootstrap
 4. Javascript
3. Oracle - documents relating to SQL commands
4. Real Python - Flask by Example – Project Setup