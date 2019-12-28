<?php
//DONT TOUCH FROM HERE
$target_dir = "";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
// checking if file already exists
if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}
if($imageFileType != "xlsx") {
	echo "Sorry, only CSV files are allowed.";
    $uploadOk = 0;
}
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
        // echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
// YOU CAN TOUCH FROM HERE
$table_name = $_POST["table"];
$file_name = $_FILES["fileToUpload"]["name"];

$cmd = "python create_dynamic_table.py ".$table_name." ".$file_name;
$output = shell_exec($cmd);

$cmd = "python excell_value_insert.py ".$table_name." ".$file_name;
$output = shell_exec($cmd);

// echo "<pre>$output</pre>\n";
$cmd = "java DeleteFile ".$file_name;
$output = shell_exec($cmd);
// echo "<pre>$output</pre>";
?>
<META HTTP-EQUIV="Refresh" CONTENT="0; URL=index.html">
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
  <body>
    <div class="container" style="margin-top: 10em;">
      <div class="row align-items-center">
        <div class="col-sm-3"></div>
        <div class="col-sm-6">
          <h1 style="margin-bottom: 10px;">
            CSV File Uploaded.<br></br>
          </h1>
          <form>
            <div class="form-group">
              <!-- <label for="exampleInputName" class="text_heading" -->
                <!-- >Table Name</label -->
              <!-- > -->
              <!-- <input -->
                <!-- type="text" -->
                <!-- class="form-control bg-dark" -->
                <!-- id="exampleInputName" -->
                <!-- aria-describedby="emailHelp" -->
                <!-- placeholder="Enter Name" -->
                <!-- style="color: white;" -->
              <!-- /> -->
              <br />
              <br />
              
              
            <!-- <button type="submit" class="btn btn-outline-warning"> -->
              <!-- Submit -->
            <!-- </button> -->
          </form>
        </div>
        <div class="col-sm-3 fixed-bottom">
                <!-- <button -->
                <!-- type="button" -->
                <!-- class="btn btn-outline-info" -->
                <!-- style="margin-bottom: 25px;" -->
                <!-- onclick="location.href='index.html'" -->
              <!-- > -->
                <!-- Home Page -->
              <!-- </button> -->
        </div>
      </div>
    </div>
  </body>
</html>
<META HTTP-EQUIV="Refresh" CONTENT="5; URL=index.html">