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
$catInt = 1;
echo "$catInt";
echo "\n";
$catFloat = 3.14;
echo $catFloat;
echo "\n";

echo $catInt * 4 + 8;
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
if (0 === $a % $b) {
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
    if (10 < $ans) {
        break;
    }
    $ans += $value;
    $counter++;
}
echo "counter: $counter";


// task15
echo "\n--------------task15-------------\n";
function printStringReturnNumber(): int
{
    echo "Hello, world!\n";
    return strlen("Hello, world!");
}
$myNum = printStringReturnNumber();
echo "$myNum\n";


// task16
echo "\n--------------task16-------------\n";
function increaseEnthusiasm(string $item): string
{
    return "$item" . "!";
}
$string = "Random string";
echo increaseEnthusiasm($string) . "\n";
//

function repeatThreeTimes(string $item): string
{
    return "$item" . "$item" . "$item";
}
echo RepeatThreeTimes($string) . "\n";
//

echo increaseEnthusiasm(RepeatThreeTimes($string)) . "\n";
//

function cut(string $str, int $NumOfSimbols = 10): string
{
    return substr_replace($str, "", $NumOfSimbols, strlen($str) - $NumOfSimbols);
}
echo cut($string, 3) . "\n";
//
function printArray($arr, $i = 0)
{
    echo $arr[$i] . "\n";
    if (array_key_last($arr) > $i) {
        printArray($arr, ++$i);
    }
}
printArray($arr1);
echo "\n";
//
function sumBeforeSimple(int $n): int
{
    $sum = 0;
    while ($n != 0) {
        $sum += $n % 10;
        $n = intdiv($n, 10);
    }
    if (10 <= $sum) {
        $sum = sumBeforeSimple($sum);
    }
    return $sum;
}
echo sumBeforeSimple(991) . "\n";
// task17
echo "\n--------------task17-------------\n";
$arr17 = [];
for ($i = 0; $i < 10; $i++) {
    $arr17[$i] = str_repeat("x", $i + 1);
}
var_dump($arr17);
//
function arrayFill($item, int $n)
{
    $tmp_arr = [];
    for ($i = 0; $i < $n; $i++) {
        $tmp_arr[$i] = $item;
    }
    return $tmp_arr;
}
$arr171 =  arrayFill('x', 5);
var_dump($arr171);
//
$array172 = [[1, 2, 3], [4, 5], [6]];
$sum = 0;
foreach ($array172 as $subArray) {
    foreach ($subArray as $value) {
        $sum += $value;
    }
}
echo "Sum of array: $sum\n";

$arr172 = [];
$count = 1;
for ($i = 0; $i < 3; $i++) {
    $temp = [];
    for ($j = 0; $j < 3; $j++) {
        $temp[] = $count;
        $count++;
    }
    $arr172[] = $temp;
}
print_r($arr172);

$arr173 = [2, 5, 3, 9];
$result = ($arr173[0] * $arr173[1]) + ($arr173[2] * $arr173[3]);
echo "Result of operations: $result\n";

$user = [
    'name' => 'Mary',
    'surname' => 'Johnson',
    'patronymic' => '-'
];
echo $user['surname'] . ' ' . $user['name'] . ' ' . $user['patronymic'] . "\n";

$date = [
    'year' => date('Y'),
    'month' => date('m'),
    'day' => date('d')
];
echo "{$date['year']}-{$date['month']}-{$date['day']}\n";

$arr = ['a', 'b', 'c', 'd', 'e'];
echo "Number of elements: " . count($arr) . "\n";
echo "Last element: " . end($arr) . "\n";
echo "Second-to-last: " . $arr[count($arr) - 2] . "\n";

// task18
echo "\n--------------task18-------------\n";

function checkSum(int $num1, int $num2): bool
{
    return (10 < $num1 + $num2) ? true : false;
}

function checkEq(int $num1, int $num2): bool
{
    return ($num1 === $num2) ? true : false;
}

// if (0 === $test) echo 'correct';

$age = 21;
if ($age < 10 || $age > 99) {
    echo "out of range (10,99)";
} else {
    $digitSum = array_sum(str_split($age));
    if (9 >= $digitSum) {
        echo "single-digit";
    } else {
        echo "two-digit";
    }
}
echo "\n";
$arr18 = [0, 0, 0];
if (3 === count($arr18)) {
    echo "Sum of array: " . array_sum($arr18);
}

// task19
echo "\n--------------task19-------------\n";
for ($i = 1; $i <= 20; $i++) {
    for ($j = 1; $j <= $i; $j++) echo 'x';
    echo "\n";
}

// task20
echo "\n--------------task20-------------\n";

$array20 = [1, 2, 3, 4];
$average = array_sum($array20) / count($array20);

$sum20 = array_sum(range(1, 100));

$array201 = [4, 9, 16, 25];
$squareRoots = array_map('sqrt', $array201);

$alphArray = array_combine(range('a', 'z'), range(1, 26));

$string = '1234567890';
$sumOfPairs = array_sum(str_split($string, 2));
