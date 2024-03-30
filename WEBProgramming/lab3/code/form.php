<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Form</title>
</head>

<body style="display: flex; ">
    <div style="padding: 100px;">
        <form action="count-word-chars.php" method="post">
            <textarea name="text" rows="4" cols="50"></textarea><br>
            <input type="submit" value="Count Words and Characters">
        </form>

        <?php if (isset($_SESSION['message'])) : ?>
            <p><?php echo $_SESSION['message'];
                unset($_SESSION['message']); ?></p>
        <?php endif; ?>
    </div>

    <!-- Form for saving user data -->
    <div style="padding: 100px;">
        <form action="save-user-data.php" method="post">
            Surname: <input type="text" name="surname"><br>
            Name: <input type="text" name="name"><br>
            Age: <input type="number" name="age"><br>
            <input type="submit" value="Save User Data">
        </form>
    </div>

</body>

</html>