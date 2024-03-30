<?php
session_start();

if (false === isset($_POST['surname'], $_POST['name'], $_POST['age'])) {
    header("Location: form.php");
    exit();
}
$_SESSION['userData'] = [
    'surname' => $_POST['surname'] ?? '',
    'name' => $_POST['name'] ?? '',
    'age' => $_POST['age'] ?? ''
];
header("Location: preview.php");
