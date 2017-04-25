<?php
    $filename = $_GET['file'] . ".txt";
    
    // If $_GET['value'] is set...
    if (isset($_GET['value'])) { 
        // set the contents of the file to $_GET['value']
        $myfile = fopen($filename,"w") or die("Unable to write to file!");
        fputs($myfile,$_GET['value']);
    } else {
        // else, toggle the value of the file between 1 and 0.
        $myfile = fopen($filename,"r") or die("Unable to read file!");
        $value = fgets($myfile);
        fclose($myfile);        
        $myfile = fopen($filename,"w") or die("Unable to write to file!");
        fputs($myfile,(($value+1)%2));
        fclose($myfile);
    }
?>