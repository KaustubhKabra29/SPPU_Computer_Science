<?php
function display_query($Query, $SubQuery,$Result_Type) {
	$con=mysqli_connect("localhost","root","iiit123","moviedb");
	
	//display the query
	echo "<div class='panel panel-default'><div class='panel-body'>" . $Query . "</div></div>";
	echo "<div class='panel panel-default'><div class='panel-body'>" . $SubQuery . "</div></div>";
	
	//query the database
	$result = mysqli_query($con, $Query);

	if($result)
	{
	echo "Success";
	$result = mysqli_query($con, $SubQuery);
	} else{
	
	$result = mysqli_query($con, $SubQuery);
	if($result){
	if($Result_Type == "addactor"){
		echo "\n Person with the same details exists. Same person is added to Actors list";}
	elseif($Result_Type == "adddire"){
		echo "\n Person with the same details exists. Same person is added to Directors list";}
	
	} else{ echo "Failed"; }
	}

	echo "<table class='table'>";
	
	switch($Result_Type) {
		case "year_search":
			echo "<tr><th>Title</th> <th>Release Date</th> <th>Language</th> <th>Certification</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","Release_Date","Language","Certification"), $row);
			}
			break;

		case "actor":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>Movie</th> <th>Certification</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","Title","Certification"), $row);
			}
			break;

		case "Dire":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>Movie</th> <th>Direction Type</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","Title","Direction_Type"), $row);
			}
			break;


		case "ycoll":
			echo "<tr><th>Movie</th> <th>Release Date</th> <th>Budget</th> <th>Revenue</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","Release_Date","Budget","Overall_Worldwide_Collections"), $row);
			}
			break;

		case "DirCumAct":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>Gender</th> <th>DOB</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","Gender","DOB"), $row);
			}
			break;

		case "mvr":
			echo "<tr><th>Title</th> <th>Language</th> <th>Certification</th> <th>Rating</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","Language","Certification","Rating"), $row);
			}
			break;
		

		default:
			break;
	}
	echo "</table>";

	mysqli_close($con);
}

function display_row($fields, $row) {
	echo "<tr>";
	foreach ($fields as $field) {
		echo "<td>" . $row[$field] . "</td>";
  	}
  	echo "</tr>";
}
?>



	
