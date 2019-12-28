<?php

$con=mysqli_connect("localhost","root","","student_db") or die(mysqli_error($con));
$student_roll = $_POST['student_roll'];
$table_name=$_POST['table_name'];
$query = "DELETE FROM $table_name where Roll_Number='$student_roll'";
$data = mysqli_query($con,$query);
if($data)
{
	echo "<font color='green'>Record Deleted";
	?>
	<META HTTP-EQUIV="Refresh" CONTENT="0; URL=index.html">
	<?php
}
else
{
	die(mysqli_error($con));
}

?>