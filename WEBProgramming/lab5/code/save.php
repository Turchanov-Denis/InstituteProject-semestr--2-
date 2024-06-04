<?php
function redirectToHome(): void {
    header('Location: /');
    exit();
}

function validateInput(array $data): bool {
    $requiredFields = ['email', 'category', 'title', 'description'];
    foreach ($requiredFields as $field) {
        if (empty($data[$field])) {
            return false;
        }
    }
    return true;
}

if (!validateInput($_POST)) {
    redirectToHome();
}

$mysqli = new mysqli('db', 'root', 'helloworld', 'web');
if ($mysqli->connect_errno) {
    printf('Failed to connect to MySQL: %s\n', $mysqli->connect_error);
    exit();
}

$email = $_POST['email'];
$category = $_POST['category'];
$title = $_POST['title'];
$description = $_POST['description'];

$stmt = $mysqli->prepare("INSERT INTO ad (email, title, description, category) VALUES (?, ?, ?, ?)");
if ($stmt) {
    $stmt->bind_param('ssss', $email, $title, $description, $category);
    $stmt->execute();
    $stmt->close();
} else {
    printf('Failed to prepare statement: %s\n', $mysqli->error);
}

$mysqli->close();
redirectToHome();
?>
