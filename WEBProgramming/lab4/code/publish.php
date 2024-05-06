<?php
require_once 'vendor/autoload.php';
if (true === isset($_POST['email'], $_POST['category'], $_POST['title'], $_POST['description'])) {
    $client = new Google_Client();
    $client->setApplicationName('WebLab4');
    $client->setScopes(['https://www.googleapis.com/auth/spreadsheets']);
    $client->setAccessType('offline');
    $client->setAuthConfig('client_credentials.json');

    $service = new \Google\Service\Sheets($client);
    $spreadsheetId = "1Ai50d9Tgna-4UQupehqZTw29L8lhrPoXY6NhMDZjBZQ";
    $listName = "List1";

    $email = $_POST['email'];
    $category = $_POST['category'];
    $title = $_POST['title'];
    $description = $_POST['description'];
    $payload = [[$email, $category, $title, $description]];
    $body = new \Google\Service\Sheets\ValueRange(['values' => $payload]);
    $opts = array('valueInputOption' => 'USER_ENTERED');

    $service->spreadsheets_values->append($spreadsheetId, $listName, $body, $opts);
}
header('Location: /index.php');
exit();
