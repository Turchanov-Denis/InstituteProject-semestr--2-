<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Task1</title>
</head>

<body>
    <h1>Regular expression</h1>
    <h2> subtask1</h2>
    <?php
    $str = 'ahb acb aeb aeeb adcb axeb';
    $regexp = '/a..b/';
    ?>

    <div>Example string: <?php echo $str; ?></div>
    <div>Regular expression: <?php echo $regexp; ?></div>
    <?php
    $matches = [];
    $count = preg_match_all('/a..b/', $str, $matches);
    ?>
    <div>Total matches: <?php echo $count ?></div>
    <div>
        <p>
            Matching strings:<br>
            <?php
            foreach ($matches[0] as $match) {
                echo "$match<br>";
            }
            ?>
        </p>
    </div>

    <h2> subtask2</h2>
    <p>Given a string with integers 'a1b2c3'. Using a regular expression, transform the formula so that instead of these numbers there are their cubes.</p>
    <div>
        <?php
        $str = 'a1b2c3';
        $result = preg_replace_callback('/\d+/', function ($matches) {
            return $matches[0] ** 3;
        }, $str);
        ?>
        <p>Result: <?php echo $result ?></p>
    </div>
</body>

</html>