<?php
session_start();
if (false === isset($_POST['arrayName'], $_POST['arrayAge'], $_POST['salary'], $_POST['hobby'],)) {
    header("Location: form.php");
    exit();
}

$_SESSION['userArray'] = [
    'name' => $_POST['arrayName'] ?? '',
    'age' => $_POST['arrayAge'] ?? '',
    'salary' => $_POST['salary'] ?? '',
    'hobby' => $_POST['hobby'] ?? ''
];


header("Location: preview.php");
