<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Form</title>
</head>
<form action="count-word-chars.php" method="post">
    <textarea name="text" rows="4" cols="50"></textarea><br>
    <input type="submit" value="Count Words and Characters">
</form>

<?php if (isset($_SESSION['message'])) : ?>
    <p><?php echo $_SESSION['message'];
        unset($_SESSION['message']); ?></p>
<?php endif; ?>

<body>

</body>

</html>