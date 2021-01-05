let formValues = [];

function showCreate() {
	//find the div for 'display' @ line 37 and show
	document.getElementById('display').style.display = "none";
	document.getElementById('update-button').style.display = "block";
	document.getElementById('update-button').style.display = "none";
	document.getElementById('create-update').style.display = "block";
}

function showUpdate(thisElem) {
	//function to read the data in the row to be updated
	populateForm(formValues[thisElem]);

	//hide or show the buttons
	document.getElementById('display').style.display = "none";
	document.getElementById('update-button').style.display = "block";
	document.getElementById('create-button').style.display = "none";
	document.getElementById('create-update').style.display = "block";
}

function populateForm(eeUpdate) {
	//same code as function getEEFromForm
	var form = document.getElementById('createUpdateForm');

	form.querySelector('input[name="eeID"]').value = eeUpdate.eeID;
	form.querySelector('input[name="eeID"]').disabled = true;

	form.querySelector('input[name="firstName"]').value = eeUpdate.firstName;
	form.querySelector('input[name="lastName"]').value = eeUpdate.lastName;
	//form.querySelector('input[name="genderType"]').value = eeUpdate.genderType;
	form.querySelector('input[name="address"]').value = eeUpdate.address;
}

function doCreate() {
	//find the div for 'display' @ line 37 and show
	let EE = getEEFromForm();
	//code to put the data to the server
	$.ajax({
		url: "http://127.0.0.1:5000/employees",
		method: 'POST',
		//convert data to a string to allow it to be passed to the DB
		data: JSON.stringify(EE),
		dataType: 'JSON',
		contentType: "application/json; charset=utf-8",
		success: function (result) {
			console.log(result);
			showDisplay();
			populateTable();
		},
		error: function (xhr, status, error) {
			console.log("error " + error);
		}
	});
	
}

function showDisplay() {
	//find the div for 'display' @ line 37 and show
	document.getElementById('display').style.display = "block";
	document.getElementById('create-update').style.display = "none";
}

function doUpdate() {
	let EE = getEEFromForm();
	//update server
	console.log(EE, "doUpdate");
	updateServer(EE);
}

function updateServer(employee) {
	//ajax call to the server
	$.ajax({
		url: "/employees/" + employee.empID, //EE.eeID,
		method: "PUT",
		//convert data to a string to allow it to be passed to the DB
		data: JSON.stringify(employee),
		dataType: 'JSON',
		contentType: "application/json; charset=utf-8",
		success: function (result) {
			console.log(result);
			populateTable();
			showDisplay();
		},
		error: function (xhr, status, error) {
			console.log("error " + error);
		}
	});
}

function updateTableRow(EE) {
	console.log("updating table");
}

function doDelete(thisElem) {
	let id = formValues[thisElem].eeID;
	console.log(id);
	$.ajax({
		url: "/employees/" + id,
		method: "DELETE",
		data: "",
		dataType: "JSON",
		contentType: "application/json; charset=utf-8",
		success: function (result) {
			populateTable();
		},
		error: function (xhr, status, error) {
			//console.log()
			console.log("error " + error);
		}
	});
}

function getEEFromForm() {
	var form = document.getElementById('createUpdateForm');
	var EE = {};
	//commented out this as the primary key is auto incremented and code won't update unless it's blank
	EE.empID = form.querySelector('input[name="eeID"]').value;
	EE.firstName = form.querySelector('input[name="firstName"]').value;
	EE.lastName = form.querySelector('input[name="lastName"]').value;
	EE.genderType = form.querySelector('input[name="genderType"]').value;
	EE.address = form.querySelector('input[name="address"]').value;
	//sanity check for doCreate() function
	console.log(EE);
	return EE;
}

function populateTable() {
    //code to clear the table before starting to load in the data
	const tableElem = document.getElementById("employeeTable");
	tableElem.innerHTML = '';
    
    employee = '';
	$.ajax({
		url: "http://127.0.0.1:5000/employees",
		method: 'GET',
		data: '',
		dataType: 'JSON',
		contentType: "application/json; charset=utf-8",
		success: function (result) {
			formValues = result;
			formValues.forEach((fe, indx) => addEEtoTable(fe, indx));
		},
		error: function (xhr, status, error) {
			console.log("error" + error + "code" + status);
		}
	});
}

function populateGenderList (){
	//code to clear the table before starting to load in the data
	const tableElem = document.getElementById("employeeTable");
	tableElem.innerHTML = '';
	
	// Populate the dropdown list in the Update / create form
	gender = '';
	$.ajax({
		url: "http://127.0.0.1:5000/genderinfo",
		method: 'GET',
		data: '',
		dataType: 'JSON',
		contentType: "application/json; charset=utf-8",
		success: function (result) {
			formValues = result;
			formValues.forEach((fe, indx) => addEEtoTable(fe, indx));
		},
		error: function (xhr, status, error) {
			console.log("error" + error + "code" + status);
		}
	});
}

function addEEtoTable(EE, indx) {
    const tableElem = document.getElementById("employeeTable");
    //add a new row to the table
	const rowElem = tableElem.insertRow(-1);
	rowElem.setAttribute("id", EE.eeID);

	const cell1 = rowElem.insertCell(0);
	cell1.innerHTML = EE.eeID;
	const cell2 = rowElem.insertCell(1);
	cell2.innerHTML = EE.firstName;
	const cell3 = rowElem.insertCell(2);
	cell3.innerHTML = EE.lastName;
	const cell4 = rowElem.insertCell(3);
	cell4.innerHTML = EE.genderType;
	const cell5 = rowElem.insertCell(4);
	cell5.innerHTML = EE.address;
	const cell6 = rowElem.insertCell(5);
	cell6.innerHTML = `<button type="button" class="btn btn-secondary"  onclick="showUpdate(${indx})">Update</button>`;
	const cell7 = rowElem.insertCell(6);
	cell7.innerHTML = `<button type="button" class="btn btn-secondary" onclick="doDelete(${indx})">Delete</button>`;
}
populateTable();

function goBack(){
	//log to console
	//console.log("in goBack")
	
	//go back to the previous page .. returns to homepage
	//window.history.back();
	//window.history.go(-1);

	//returns to home page of the project
	window.location.href = 'http://127.0.0.1:5000/index.html';
}