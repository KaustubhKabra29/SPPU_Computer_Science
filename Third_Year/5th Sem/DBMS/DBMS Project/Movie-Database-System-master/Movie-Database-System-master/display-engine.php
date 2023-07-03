<?php
function display_query($Query, $Result_Type) {
	$con=mysqli_connect("localhost","root","iiit123","moviedb");
	
	//display the query
	echo "<div class='panel panel-default'><div class='panel-body'>" . $Query . "</div></div>";
	
	//query the database
	$result = mysqli_query($con, $Query);

	if($result)
	{
	echo "Success";
	} else{
	echo "Failed";
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
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>Shows</th> <th>Certification</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","Title","Certification"), $row);
			}
			break;

		case "Dire":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>Shows</th> <th>Direction Type</th></tr>";
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

		case "movie":
			echo "<tr><th>Movie</th> <th>FirstName</th> <th>LastName</th> <th>DOB</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","First_Name","Last_Name","DOB"), $row);
			}
			break;
		case "actordetails":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>DOB</th> <th>Gender</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","DOB","Gender"), $row);
			}
			break;


		case "dirdetails":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>DOB</th> <th>Gender</th><th>DirectionType</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","DOB","Gender","Direction_Type"), $row);
			}
			break;

		case "movdetails":
			echo "<tr><th>Movie</th> <th>Certification</th> <th>Language</th> <th>Released ON</th><th>Duration</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","Certification","Language","Release_Date","Duration"), $row);
			}
			break;


		case "tvdetails":
			echo "<tr><th>TV Show</th> <th>Air Channel</th> <th>Language</th> <th>Start Date</th><th>Certification</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","Air_Channel","Language","Start_date","Certification"), $row);
			}
			break;
		
		case "rvwdetails":
			echo "<tr><th>Show Title</th> <th>User</th> <th>Reviwed Date</th> <th>Review Description</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","User_Id","Reviwed_Date","Review_Description"), $row);
			}
			break;

		case "genre":
			echo "<tr><th>Show Title</th> <th>Genre</th> <th>Rating</th> <th>Certification</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("Title","Name","Rating","Certification"), $row);
			}
			break;

		case "persondet":
			echo "<tr><th>FirstName</th> <th>LastName</th> <th>DOB</th> <th>Gender</th></tr>";
			while($row = mysqli_fetch_array($result)) {
			        display_row(array("First_Name","Last_Name","DOB","Gender"), $row);
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



	
