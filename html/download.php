<?php
print_r("test");

$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

// Check if image file is a actual image or fake image
// if(isset($_POST["submit"])) {
//   $check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
//   if($check !== false) {
//     echo "File is an image - " . $check["mime"] . ".";
//     $uploadOk = 1;
//   } else {
//     echo "File is not an image.";
//     $uploadOk = 0;
//   }
// }

//$config['allowed_types'] = 'svg';
//$config['allowed_types'] = 'png';

// Check if file already exists
if (file_exists($target_file)) {
  echo "Sorry, file already exists.";
  $uploadOk = 0;
}

// Check file size
if ($_FILES["fileToUpload"]["size"] > 200000) {
  echo "Sorry, your file is too large.";
  $uploadOk = 0;
}
echo $_FILES;
// Allow certain file formats
if($imageFileType != "svg") {
  echo "Sorry, only SVG files are allowed.";
  $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
  echo "Sorry, your file was not uploaded.";
// if everything is ok, try to upload file
} else {
  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
    echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
    //header("Location: http://localhost/spacetracking");
  } else {
    echo "Sorry, there was an error uploading your file.";
  }
}
//header("Location: http://localhost/spacetracking");
?>
<!DOCTYPE html>
<html>
<head>
    <title>Beispiel für WebAPP über jQuery Mobile</title>
    <meta charset="UTF-8" />
    <meta name="author" content="https://www.html-seminar.de/" />
	<link rel="stylesheet"  href="jquery.mobile/demos/css/themes/default/jquery.mobile-1.2.0.css" />
	<link rel="stylesheet" href="jquery.mobile/demos/docs/_assets/css/jqm-docs.css" />
	<script src="jquery.mobile/demos/js/jquery.js"></script>
	<script src="jquery.mobile/demos/docs/_assets/js/jqm-docs.js"></script>
	<script src="jquery.mobile/demos/js/jquery.mobile-1.2.0.js"></script>
    <meta name="apple-mobile-web-app-capable" content="yes" />
    <meta name="viewport" content="width=device-width, initial-scale=1,maximum-scale=1" />
    <!-- ICONS -->
    <!-- eigene CSS-Defintionen -->
    <link href="css/design.css" type="text/css" rel="stylesheet" />
</head>
<body>
<h1>erste Webapp</h1>
</body>
</html>