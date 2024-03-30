<?php
session_start();
if (false === isset($_POST['text'])) {
    header("Location: form.php");
    exit();
}
$text = $_POST['text'];
$wordsCount = str_word_count($text);
$charsCount = strlen(preg_replace('/\s+/', '', $text));
$_SESSION['message'] = "Word Count: $wordsCount, Character Count (excluding spaces): $charsCount";
header("Location: form.php");
