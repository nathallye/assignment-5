<?php
  if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $a_value = escapeshellarg($_POST['a_value']);
    $b_value = escapeshellarg($_POST['b_value']);
    $c_value = escapeshellarg($_POST['c_value']);
    $d_value = escapeshellarg($_POST['d_value']);
    $e_value = escapeshellarg($_POST['e_value']);

    $command = "python3 data_management.py $a_value $b_value $c_value $d_value $e_value";
    $result = shell_exec($command);

    echo $result;
  }
?>
