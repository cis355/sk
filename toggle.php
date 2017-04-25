<?php
    $filename = $_GET['file'] . ".txt";
    $myfile = fopen($filename,"r") or die("Unable to read file!");
	$value = fgets($myfile);
	fclose($myfile);
	
	$myfile = fopen($filename,"w") or die("Unable to write to file!");
	if (strcmp($filename, "food.txt")==0) {
		$contents = $_GET['contents'];
		fputs($myfile,$contents);
	}
	else {
		fputs($myfile,(($value+1)%2));
	}
    fclose($myfile);
?>