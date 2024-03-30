<?php
// Вывод данных пользователя из сессии
session_start();
if (isset($_SESSION['userData'])) {
    echo "<h2>Данные пользователя:</h2>";
    foreach ($_SESSION['userData'] as $key => $value) {
        echo "<p>$key: $value</p>";
    }
    unset($_SESSION['userData']);
}
