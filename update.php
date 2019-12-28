<?php
	$table_name=$_POST['table_name'];
    $student_roll=$_POST['student_roll'];
    $student_name=$_POST['student_name'];
    $email=$_POST['email'];
	$new_roll_number=$_POST['student_roll1'];
    $cmd="java UpdateManualAll ".$table_name." ".$student_roll." ".$email." ".$new_roll_number." ".$student_name;
    $output = shell_exec($cmd);
    #echo "<pre>$output</pre><br>";
?>
<META HTTP-EQUIV="Refresh" CONTENT="0; URL=index.html">