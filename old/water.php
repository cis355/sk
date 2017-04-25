<?php 	
	$level = $_GET['level'];
	$filename = "water.txt";
	$myfile = fopen($filename, "w") or die("Unable to open file!");
	fputs($myfile,(string)$level);
	fclose($myfile);
	//echo (($value + 1) % 2);
	
?>