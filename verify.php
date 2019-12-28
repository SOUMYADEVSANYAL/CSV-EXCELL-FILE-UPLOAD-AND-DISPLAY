<?php
$table_name = $_POST["table"];
$cmd = "java EmailVerify ".$table_name;
$output = shell_exec($cmd);
?>
<META HTTP-EQUIV="Refresh" CONTENT="0; URL=index.html">