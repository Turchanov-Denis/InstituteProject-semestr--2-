<?php session_start(); ?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <div id="root">
        <h1>Sell your product</h1>
        <form action="./publish.php" method="post">
            <label for="category">Select the category</label>
            <select name="category" id="category" required>
                <option value="cars">cars</option>
                <option value="phones">phones</option>
                <option value="other">other</option>
            </select>
            <label for="email">Your contact email</label>
            <input type="email" name="email" required>
            <label for="title">Product title</label>
            <input type="text" name="title" required>
            <label for="description">Description</label>
            <textarea name="description" cols="60" rows="4" required></textarea>
            <button type="submit">Publish</button>
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
                require('vendor/autoload.php');
                $client = new Google_Client();
                $client->setApplicationName('WebLab4');
                $client->setScopes(['https://www.googleapis.com/auth/spreadsheets']);
                $client->setAccessType('offline');
                $client->setAuthConfig('client_credentials.json');

                $service = new \Google\Service\Sheets($client);
                $spreadsheetId = "1Ai50d9Tgna-4UQupehqZTw29L8lhrPoXY6NhMDZjBZQ";
                $listName = "List1";
                
                $rows = $service->spreadsheets_values->get($spreadsheetId, $listName)->getValues();
                foreach ($rows as $row) {
                    echo "<tr>";
                    foreach ($row as $cell) {
                        echo "<td>$cell</td>";
                    }
                    echo "</tr>";
                }
                ?>
            </tbody>
        </table>
    </div>
</body>

</html>