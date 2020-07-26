<?php
echo $_FILES;
/**
 * Check to see if POST was used and that its content length is less than the value in post_max_size
 */
$requestType = $_SERVER['REQUEST_METHOD'];
if($requestType != 'POST'){
    echo 'Request type was ' . $requestType . ' - File uploads will only work with POST. Are you using method="post" in your form element?<br>';
    exit;
} else{
    
    if(isset($_SERVER['CONTENT_TYPE'])){
        $contentType = strtolower($_SERVER['CONTENT_TYPE']);
        if(!stristr($contentType, 'multipart/form-data')){
            echo 'Could not find multipart/form-data in Content-Type. Did you use enctype="multipart/form-data" in your form element?<br>';
        }
    }
    
    if(isset($_SERVER['CONTENT_LENGTH'])){
        $postSize = $_SERVER['CONTENT_LENGTH'];
        $maxPostSize = ini_get('post_max_size');
        if($maxPostSize == 0){
            echo 'post_max_size is set to 0 - unlimited.<br>';
        } else{
            if(strlen($maxPostSize) > 1){
                $lastChar = substr($maxPostSize, -1);
                $maxPostSize = substr($maxPostSize, 0, -1);
                if($lastChar == 'G'){
                    $maxPostSize = $maxPostSize * 1024 * 1024 * 1024;
                }
                if($lastChar == 'M'){
                    $maxPostSize = $maxPostSize * 1024 * 1024;
                }
                if($lastChar == 'K'){
                    $maxPostSize = $maxPostSize * 1024;
                }
                if($postSize > $maxPostSize){
                    echo 'The size of the POST request (' . $postSize . ' bytes) exceeded the limit of post_max_size (' . $maxPostSize . ' bytes) in your php.ini file<br>';
                    exit;
                }
            } else{
                if($postSize > $maxPostSize){
                    echo 'The size of the POST request (' . $postSize . ' bytes) exceeded the limit of post_max_size (' . $maxPostSize . ' bytes) in your php.ini file<br>';
                    exit;
                }
            }
            
        }
    } else{
        echo 'CONTENT_LENGTH not found. Make sure that your POST request is smaller than the ' . ini_get('post_max_size') . ' post_max_size in php.ini<br>';
    }
}


$tempFolder = ini_get('upload_tmp_dir');
if(strlen(trim($tempFolder)) == 0){
    echo 'upload_tmp_dir was blank. No temporary upload directory has been set in php.ini<br>';
    exit;
} else{
    echo 'upload_tmp_dir is set to: ' . $tempFolder . '<br>';
}

if(!is_dir($tempFolder)){
    echo 'The temp upload directory specified in upload_tmp_dir does not exist: ' . $tempFolder . '<br>';
    exit;
} else{
    echo $tempFolder . ' is a valid directory<br>';
}

if(!is_writable($tempFolder)){
    echo 'The temp upload directory specified in upload_tmp_dir is not writeable: ' . $tempFolder . '<br>';
    echo 'Does PHP have permission to write to this directory?<br>';
    exit;
} else{
    echo $tempFolder . ' is writeable<br>';
}

$write = file_put_contents($tempFolder . '/' . uniqid(). '.tmp', 'test');
if($write === false){
    echo 'PHP could not create a file in ' . $tempFolder . '<br>';
    exit;
} else{
    echo 'PHP successfully created a test file in: ' . $tempFolder . '<br>';
}

if(ini_get('file_uploads') == 1){
    echo 'The file_uploads directive in php.ini is set to 1, which means that your PHP configuration allows file uploads<br>';
} else{
    echo 'The file_uploads directive in php.ini has been set to 0 - Uploads are disabled on this PHP configuration.<br>';
    exit;
}

if(empty($_FILES)){
    echo 'The $_FILES array is empty. Is your form using method="post" and enctype="multipart/form-data"? Did the size of the file exceed the post_max_size in PHP.ini?';
    exit;
} else{
    foreach($_FILES as $file){
        if($file['error'] !== 0){
            echo 'There was an error uploading ' . $file['name'] . '<br>';
            switch($file['error']){
                case 1:
                    echo 'Size exceeds the upload_max_filesize directive in php.ini<br>';
                    break;
                case 2:
                    echo 'Size exceeds the MAX_FILE_SIZE field in your HTML form<br>';
                    break;
                case 3:
                    echo 'File was only partially uploaded<br>';
                    break;
                case 4:
                    echo 'No file was selected by the user<br>';
                    break;
                case 6:
                    echo 'PHP could not find the temporary upload folder<br>';
                    break;
                case 7:
                    echo 'PHP failed to write to disk. Possible permissions issue?<br>';
                    break;
                case 8:
                    echo 'A PHP extension prevented the file from being uploaded.<br>';
                    break;
                default:
                    echo 'An unknown error occured: ' . $file['error'] . '<br>';
                    break;
            }
        } else{
            echo $file['name'] . ' was successfully uploaded to ' . $file['tmp_name'] . '<br>';
        }
    }
}


$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
print_r($target_file);
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
header("Location: http://localhost/spacetracking");
?>
