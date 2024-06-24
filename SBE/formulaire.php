<?php
// Paramètres de connexion à la base de données
$servername = "localhost";
$username = "root"; //sbe
$password = ""; //projetsbe
$dbname = "sbe";

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $dbname);


// Vérifier la connexion
if ($conn->connect_error) {
    die("Échec de la connexion : " . $conn->connect_error);
}

// Récupérer les données du formulaire
$nom = $_POST['nom'];
$secteur = $_POST['secteur'];
$type = $_POST['type'];
$adresse = $_POST['adresse'];

// if ($_SERVER["REQUEST_METHOD"] == "POST") {
//     // Vérifier si des options ont été sélectionnées
//     if(isset($_POST['options']) && !empty($_POST['options'])) {
//         // Récupérer les options sélectionnées
//         $options_selectionnees = $_POST['options'];

//         // Traiter les options sélectionnées
//         foreach($options_selectionnees as $option) {
//             echo $option . "<br>"; // Vous pouvez traiter chaque option comme nécessaire
//         }
//     } else {
//         echo "Aucune option sélectionnée.";
//     }
// }



        // if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        //     $nom = $_POST['nom'] ?? 'Nom non fourni';
        //     echo "Le nom est : " . htmlspecialchars($nom);
        // } else {
        //     echo "Aucune donnée envoyée.";
        // }




// Préparer et exécuter la requête SQL
$sql_structure = "INSERT INTO structure (nom,adresse,type,secteur) VALUES ('$nom','$adresse','$secteur','$type')";
$conn->query($sql_structure);

// // Préparer et exécuter la requêter SQL pour la liste déroulante des zones géographiques
// $sql_zone_geographique = "SELECT zone_geographique FROM service";
// $conn->query($sql_zone_geographique);

// Créer la liste déroulante





// if ($conn->query($sql_statu_administratif) === TRUE) {
//     echo "Nouveau record créé avec succès";
// } else {
//     echo "Erreur : " . $sql_statu_administratif . "<br>" . $conn->error;
// }

// Fermer la connexion
$conn->close();

?>
