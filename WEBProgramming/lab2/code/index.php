<?php
header('Content-type: text/plain');
// task1 
/* Imagine a lot of code here */
$very_bad_unclear_name = "15 chicken wings";


// Write your code here:
$order = &$very_bad_unclear_name;
$order .= "cat";

// Don't change the line below
echo "Your order is: $order.";
echo "\n \n";
// task2
$catI = 1;
echo "$catI";
echo "\n";
$catF = 3.14;
echo $catF;
echo "\n";

echo $catI * 4 + 8;
echo "\n";

$lastMonth = 1187.23;
$thisMonth = 1089.98;
echo "last month I spent more on: " . $lastMonth - $thisMonth;
echo "\n \n";
// task11
$numLanguages = 4;
$month = 11;
$days = $month * 16;
$daysPerLanguage = $days / $numLanguages;
echo "average days : $daysPerLanguage days\n";
echo "\n \n";
// task12
echo 8**2;
echo "\n \n";
// task13
$myNum = 233;
$answer = $myNum;
$answer += 2;
$answer *= 2;
$answer -= 2;
$answer /= 2;
$answer -= $myNum;
echo"$answer \n";
// task14
