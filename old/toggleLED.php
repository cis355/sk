<?php 	
	$led = $_GET['led'];
	
	if ($led == 1) update("led1.txt");	
	if ($led == 2) update("led2.txt");
	if ($led == 3) update("led3.txt");
	
	function update($filename) {	
		//echo $filename . "<br />";
		$myfile = fopen($filename, "r") or die("Unable to open file!1");
		$value = fgets($myfile);
		fclose($myfile);
		$myfile = fopen($filename, "w") or die("Unable to open file!2");
		if($value==1) fputs($myfile,"0");
		else fputs($myfile,"1");
		fclose($myfile);
		echo (($value + 1) % 2);
	}
	
?>