<?php
    $table_name = $_POST['table_name'];
    $cmd = "java CreateTable ".$table_name;  //edit the name
    $output = shell_exec($cmd);
    #echo "<pre>$output</pre><br>";
?>
<META HTTP-EQUIV="Refresh" CONTENT="2; URL=index.html">

