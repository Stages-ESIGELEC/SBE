<?php
// Data basis setting's connection
$servername = "localhost";
$username = "root"; //sbe
$password = ""; //projetsbe
$dbname = "sbe";

//Creating the connection
$conn = new mysqli($servername, $username, $password, $dbname);


// Verifying the connection
if ($conn->connect_error) {
    die("Échec de la connexion : " . $conn->connect_error);
}

// Getting the form's informations
$nom = $_POST['nom'];
$secteur = $_POST['secteur'];
$type = $_POST['type'];
$adresse = $_POST['adresse'];

// Preparing and executing the SQL query 
$sql_structure = "INSERT INTO structure (nom,adresse,type,secteur) VALUES ('$nom','$adresse','$secteur','$type')";
$conn->query($sql_structure);

// Closing the connection
$conn->close();

?>
