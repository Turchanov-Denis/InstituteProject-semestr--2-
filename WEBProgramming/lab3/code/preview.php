<?php
// Вывод данных пользователя из сессии
session_start();
if (isset($_SESSION['userData'])) {
    echo "<h2>User data:</h2>";
    foreach ($_SESSION['userData'] as $key => $value) {
        echo "<p>$key: $value</p>";
    }
    unset($_SESSION['userData']);
}

if (isset($_SESSION['userArray'])) {
    echo "<h2>User Array Data:</h2><ul>";
    foreach ($_SESSION['userArray'] as $key => $value) {
        echo "<li>$key: $value</li>";
    }
    unset($_SESSION['userArray']);
}
