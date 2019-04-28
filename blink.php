<?php
$servername="localhost";
$user = "root";
$dbname="ahack";

$conn = mysqli_connect($servername,$user,"",$dbname);
$result = mysqli_query($conn,"SELECT path from anomaly");

while($row=$result->fetch_assoc()){
echo "$row['path']";
}
$conn->close();
?>