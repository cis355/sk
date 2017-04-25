<?php 
	update("led1.txt");
	update("led2.txt");
	update("led3.txt");
	
	function update($filename) {
		$myfile = fopen($filename, "w") or die("Unable to open file!");
		fputs($myfile,"0");
		fclose($myfile);
	}
?>