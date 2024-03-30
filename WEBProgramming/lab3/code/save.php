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
$desc = $_POST['description'];
$filePath = "categories/{$category}/{$title}.txt";
if (false === file_put_contents($filePath, $desc)) {
    throw new Exception(message: "Something went wrong.");
}
redirectToHome();
