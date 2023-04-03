<?php
$weaponsTable = array("rock", "paper", "scissors");
echo "Choose rock, paper, or scissors: ";

$computerNum = rand(0,2);

$inputString = trim(fgets(STDIN));  // 표준 입력에서 한 줄을 읽어옴

$myWeaponNum = array_search($inputString, $weaponsTable);

if ($myWeaponNum === false) {  // 유효하지 않은 입력값 처리
    echo "Invalid input!\n";
} else {
	if ($myWeaponNum == $computerNum) {
		echo "Hummm.... Tie!!";
	} else if (($myWeaponNum + 1) % 3 == $computerNum) {
		echo "Sorry, you lost.";
	} else {
		echo "Congratulations! You won!";
	}
	echo " The computer chose {$weaponsTable[$computerNum]}.\n";
}
?>
