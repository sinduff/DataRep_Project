function populateTable(){
    // function to populate the table from the DB to getAll()
    //ajax getAll
    //
    
    //employee = {
        //empID:"5",
        //firstName:"Jane",
        //lastName:"Doe",
        //address:"NY, NY"                   
    //}
    employee = '';
     $.ajax({
        url:"http://127.0.0.1:5000/employees",
        method:'GET',
        data:'',
        dataType:'JSON',
        contentType: "application/json; charset=utf-8",
        success:function(result){
             //for (const item in result)
             result.forEach(addEEtoTable);
             
        },
        error:function(xhr,status,error){
            console.log("error" +error + "code"+status)
        }
    })
    //addEEtoTable(employee)
 }
function addEEtoTable(row){
    //console.log("working so far")
    const tableElem = document.getElementById("employeeTable")
    const rowElem = tableElem.insertRow(-1)
    rowElem.setAttribute("id",row.eeID)
    //rowElem.setAttribute("id",employee.firstName)
    const cell1 = rowElem.insertCell(0);
    cell1.innerHTML = row.eeID;
    const cell2 = rowElem.insertCell(1);
    cell2.innerHTML = row.firstName;
    const cell3 = rowElem.insertCell(2);
    cell3.innerHTML = row.lastName;
    const cell4 = rowElem.insertCell(3);
    cell4.innerHTML = row.address;
    const cell5 = rowElem.insertCell(4);
    cell5.innerHTML = '<button onclick="showUpdate(this)">Update</button>';
    const cell6 = rowElem.insertCell(5);
    cell6.innerHTML = '<button onclick="doDelete(this)">Delete</button>';
    }
 populateTable()