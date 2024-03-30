<?php
function redirectToHome(): void
{
    header('Location: /');
    exit();
}
if (false === isset($_POST['email'], $_POST['category'], $_POST['title'], $_POST['description'])) {
    redirectToHome();
}

$category = $_POST['category'];
$title = $_POST['title'];
$email = $_POST['email'];
$desc = $_POST['description'];

$dirName = "./categories/{$category}/{$email}";
if (false === mkdir($dirName)) {
    throw new Exception("Cannot create user folder");
}

$filePath = "{$dirName}/{$title}.txt";
if (false === file_put_contents($filePath, $desc)) {
    throw new Exception(message: "Something went wrong.");
}
redirectToHome();
