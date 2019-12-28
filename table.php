<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
      crossorigin="anonymous"
    />
    <link rel="stylesheet" href="myStyleSheet.css" />
    <title>Document</title>
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
  <body>
    <div class="container" style="margin-top: 10em;">
      <div class="row align-items-center">
        <div class="col-sm-1"></div>
        <div class="col-sm-10">
          <h1 class="text_heading" style="margin-bottom: 50px;">
            Table Data : -
          </h1>
          <table class="table table-hover table-dark">
            <thead>
              <tr>
                <th scope="col">Name</th>
                <th scope="col">Roll Number</th>
                <th scope="col">Email</th>
              </tr>
            </thead>
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
                    echo "<div class='text_heading text-center'><h1>No data to show</h1></div>";
                }
                
                ?>
          </table>
        </div>
        <div class="col-sm-3 fixed-bottom">
          <button
            type="button"
            class="btn btn-outline-info"
            style="margin-bottom: 25px;"
            onclick="location.href='index.html'"
          >
            Home Page
          </button>
        </div>
      </div>
    </div>
  </body>
</html>