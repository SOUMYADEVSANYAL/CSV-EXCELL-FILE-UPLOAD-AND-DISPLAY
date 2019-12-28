<html>
<head>
	<!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" >
    <!-- jQuery library -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Table Data</title>
</head>
<?php

$table_name=$_POST['table_name'];
$con=mysqli_connect("localhost","root","","student_db") or die(mysqli_error($con));
$query = "SELECT * FROM ".$table_name;
$data = mysqli_query($con,$query);
$total = mysqli_num_rows($data);

if($total !=0)
{

    ?>
    <body class='container'>
    <table class="table table-striped">
                <th>Name</th>
                <th>Roll_Number</th>
                <th>Email</th>
                
    <?php
                while($result = mysqli_fetch_assoc($data))
                {
                    echo "
                        <tr>
                            <td hidden>".$result['id']."</td>
                            <td>".$result['Name']."</td>
                            <td>".$result['Roll_Number']."</td>
                            <td>".$result['Email']."</td>
                        </tr>
                         ";
                    
    }}
                else
                {
                    echo "<div class='container'><h1>No data to show</h1></div>";
                }
                
                ?>
    </table>
    </body>
    </html>