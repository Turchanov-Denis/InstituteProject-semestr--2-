<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <form action="save.php" method="post">
        <label for="email">Email</label>
        <input type="email" name="email" required>
        <label for="category">Category</label>
        <select name="category" required>
            <option value="cars">Cars</option>
            <option value="other">Other</option>
        </select>
        <label for="title">Title</label>
        <input type="text" name="title" required>
        <label for="description">Description</label>
        <textarea rows="3" name="description"></textarea>
    </form>
</body>

</html>