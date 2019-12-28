<?php
    $table_name=$_POST['table_name'];
    $student_name=$_POST['student_name'];
    $student_roll=$_POST['student_roll'];
    $email=$_POST['email'];
    $cmd="java InsertManual ".$table_name." ".$email." ".$student_roll." ".$student_name;  //edit here the java class name
    $output = shell_exec($cmd);
    echo "<pre>$output</pre><br>"
?>
<META HTTP-EQUIV="Refresh" CONTENT="0; URL=index.html">