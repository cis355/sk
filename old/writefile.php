<?php 
$myfile = fopen("ledfile.txt", "r") or die("Unable to open file!");
$value = fgets($myfile);
fclose($myfile);
$myfile = fopen("ledfile.txt", "w") or die("Unable to open file!");
if($value==1) fputs($myfile,"0");
else fputs($myfile,"1");
fclose($myfile);

?>