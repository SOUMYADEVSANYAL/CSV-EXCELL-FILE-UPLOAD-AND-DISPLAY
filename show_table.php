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

    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "student_db";

    $conn = new mysqli($servername, $username, $password,$dbname);
    $query="SHOW TABLES";
    $result = mysqli_query($conn, $query);
    $row = mysqli_fetch_all($result);

?>
  <body>
    <div class="container" style="margin-top: 10em;">
      <div class="row align-items-center">
        <div class="col-sm-1"></div>
        <div class="col-sm-10">
          <h1 class="text_heading text-center" style="margin-bottom: 50px;">
            Table : -
          </h1>
          <table class="table table-hover table-dark">
            <thead>
              <tr>
                <th scope="col" class="text-center">
                  Name of the table existing
                </th>
              </tr>
            </thead>
            <tbody class="text-center">
              <?php
				foreach ($row as $value) {
        echo "<tr><td>$value[0]<td><tr>";}
			  ?>
            </tbody>
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
