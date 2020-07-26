<!DOCTYPE html>
<html>
<head>
    <title>jQuery MOBILE</title>
    <meta name="viewport" content="width=device-width, height=device-height, initial-scale=1.0"/>
    <link rel="stylesheet" href="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.css" />
    <script src="http://code.jquery.com/jquery-1.9.1.min.js"></script>
    <script src="http://code.jquery.com/mobile/1.3.2/jquery.mobile-1.3.2.min.js"></script> 
</head>
<body>
    <div data-role="page" id="second">
        <div data-theme="a" data-role="header">
            <h3>Page 2</h3>
        </div>

        <div data-role="content">
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
        </div>
    </div>
</body>
</html>