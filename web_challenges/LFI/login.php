<?php

   $file = $_GET['file'];
   if(isset($file))

   {

       include("$file");

   }

   else

   {

       include("auth.php");

   }
   ?>
