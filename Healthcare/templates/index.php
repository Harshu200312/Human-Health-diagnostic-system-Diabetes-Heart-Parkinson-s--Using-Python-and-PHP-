<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "root";
$database = "ashwini";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Extract data from the POST request
$urination = $_POST['urination'];
$thirst = $_POST['thirst'];
$weightLoss = $_POST['weightLoss'];
$hunger = $_POST['hunger'];
$fatigue = $_POST['fatigue'];
$vision = $_POST['vision'];
$tingling = $_POST['tingling'];
$sores = $_POST['sores'];
$infections = $_POST['infections'];
$familyHistory = $_POST['familyHistory'];
$age = $_POST['age'];
$response = $_POST['response'];

// Prepare SQL statement to insert data into database
$sql = "INSERT INTO DiabetesData (urination, thirst, weight_loss, hunger, fatigue, vision, tingling, sores, infections, family_history, age, response) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);

if (!$stmt) {
    die("Error preparing SQL statement: " . $conn->error);
}

$stmt->bind_param("ssssssssssss", $urination, $thirst, $weightLoss, $hunger, $fatigue, $vision, $tingling, $sores, $infections, $familyHistory, $age, $response);

// Execute SQL statement
if ($stmt->execute()) {
    echo json_encode(array("message" => "Data stored successfully"));
} else {
    echo json_encode(array("error" => "Error storing data: " . $conn->error));
}

// Close statement and connection
$stmt->close();
$conn->close();
?>




</div>
</div>