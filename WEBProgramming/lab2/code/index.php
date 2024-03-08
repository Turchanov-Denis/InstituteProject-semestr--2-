<?php
header('Content-type: text/plain');
// task1 
echo "\n--------------task1-------------\n";
/* Imagine a lot of code here */
$very_bad_unclear_name = "15 chicken wings";
// Write your code here:
$order = &$very_bad_unclear_name;
$order .= "cat";
// Don't change the line below
echo "Your order is: $order.";
echo "\n \n";


// task2
echo "\n--------------task2-------------\n";
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
echo "\n--------------task11-------------\n";
$numLanguages = 4;
$month = 11;
$days = $month * 16;
$daysPerLanguage = $days / $numLanguages;
echo "average days : $daysPerLanguage days\n";
echo "\n \n";


// task12
echo "\n--------------task12-------------\n";
echo 8 ** 2;
echo "\n \n";


// task13
echo "\n--------------task13-------------\n";
$myNum = 233;
$answer = $myNum;
$answer += 2;
$answer *= 2;
$answer -= 2;
$answer /= 2;
$answer -= $myNum;
echo "$answer \n";


// task14
echo "\n--------------task14-------------\n";
$a = 10;
$b = 3;
echo $a % $b;
echo "\n";
//
if (0 == $a % $b) {
    echo "divide ";
    echo $a / $b;
    echo "\n";
} else {
    echo "not divide, remainder of the division: ";
    echo $a % $b;
    echo "\n";
}
//
$st = pow(2, 10);
$s = sqrt(245);
$randomList = [4, 2, 5, 19, 13, 0, 10];
$ww = 0;
foreach ($randomList as $value) {
    $ww += pow($value, 2);
}
$ww = sqrt($ww);
//
$n0 = round(sqrt(349), 0);
$n1 = round(sqrt(349), 1);
$n2 = round(sqrt(349), 2);

$numC = ceil(sqrt(587));
$numF = floor(sqrt(587));
$arr = [
    "ceil" => $numC,
    "floor" => $numF,
];
//
$arr = [4, -2, 5, 19, -130, 0, 10];
$min = min($arr);
$max = max($arr);
//
echo rand(1, 100);
echo "\n";
$ArrayOfRandNum = [];
for ($i = 0; $i < 10; $i++) {
    $arrayOfRandom[$i] = rand(1, 100);
}
echo "\n";
//
$a = 111;
$b = 222;
$res = abs($a - $b);
echo $res;
echo "\n";
// alternative
$a = -111;
$b = 2;
$res = abs($a - $b);
echo $res;

$arrayOfNum = [1, 2, -1, -2, 3, -3];
$newArr = [];
foreach ($arrayOfNum as $value) {
    $value = abs($value);
    array_push($newArr, $value);
}
echo "abs ";
print_r($newArr);
echo "\n";
//
$ControlNum = rand(1, 1000);
$i = 1;
$arr = [];
while ($i <= $ControlNum) {
    if (0 === $ControlNum % $i) {
        array_push($arr, $i);
    }
    $i++;
}
echo " number of divide: $ControlNum";
print_r($arr);

$arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
$ans = 0;
$counter = 0;
foreach ($arr1 as $value) {
    if ($ans > 10) {
        break;
    }
    $ans += $value;
    $counter++;
}
echo "counter: $counter";


// task15
echo "\n--------------task15-------------\n";
function printStringReturnNumber()
{
    echo "Hello, world!\n";
    return strlen("Hello, world!");
}
$myNum = printStringReturnNumber();
echo "$myNum\n";


// task16
echo "\n--------------task16-------------\n";
function increaseEnthusiasm($item){
    return "$item". "!";
}
$string = "Random string";
echo increaseEnthusiasm($string). "\n";
//

function repeatThreeTimes($item){
    return "$item". "$item". "$item";
}
echo RepeatThreeTimes($string). "\n";
//

echo increaseEnthusiasm(RepeatThreeTimes($string)). "\n";
//

function cut($str, $NumOfSimbols = 10){
    return substr_replace($str, "", $NumOfSimbols, strlen($str) - $NumOfSimbols);
}
echo cut($string, 3). "\n";
//
function printArray($arr, $i = 0){
    echo $arr[$i]. "\n";
    if(array_key_last($arr) > $i){
        printArray($arr, ++$i);
    }
}
printArray($arr1);
echo "\n";
//
function sumOfNumbers(int $n){
    $sum = 0;
    while($n != 0 ){
        $sum += $n % 10;
        $n = intdiv($n, 10);
    }
    if($sum >= 10){
        $sum = sumOfNumbers($sum);
    }
    return $sum;
}
echo sumOfNumbers(99991). "\n";
// task17
echo "\n--------------task17-------------\n";
