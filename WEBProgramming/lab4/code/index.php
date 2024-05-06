<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div id="form">
    <h3>Create</h3>
        <form action="save.php" method="post">
            <label for="email">Email</label>
            <input type="email" name="email" required>
            <label for="category">Category</label>
            <select name="category" required>
                <?php
                $categories = scandir("./categories/");
                foreach ($categories as $category) {
                    if ('.' != $category && '..' != $category) {
                        echo "<option value=\"$category\">$category</option>";
                    }
                }
                ?>
            </select>
            <label for="title">Title</label>
            <input type="text" name="title" required>
            <label for="description">Description</label>
            <textarea rows="3" name="description"></textarea>
            <input type="submit" value="save">
        </form>
    </div>
    <div id="table">
        <h3>Table</h3>
        <table>
            <thead>
                <th>Category</th>
                <th>Title</th>
                <th>Email</th>
                <th>Description</th>
            </thead>
            <tbody>
            <?php
                for ($i = 2; $i < count($categories); $i++) {
                    $category = $categories[$i];
                    $emails = scandir("./categories/{$category}");
                    for ($j = 2; $j < count($emails); $j++) {
                        $email = $emails[$j];
                        $categories = scandir("./categories/{$category}/{$email}");
                        for ($k = 2; $k < count($categories); $k++) {
                            $title = $categories[$k];
                            $desc = file_get_contents("./categories/{$category}/{$email}/{$title}");
                            $categoryDisplay = ucfirst($category);
                            $formattedTitle = substr($title, 0, strlen($title) - 4);
                            echo "<tr>";
                            echo "<td>$categoryDisplay</td>";
                            echo "<td>$formattedTitle</td>";
                            echo "<td>$email</td>";
                            echo "<td>$desc</td>";
                            echo "</tr>";
                        }
                    }
                }
                ?>
            </tbody>
        </table>
    </div>
</body>

</html>