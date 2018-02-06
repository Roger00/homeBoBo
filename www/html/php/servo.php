<?php
    header('Content-Type: application/json');

    $aResult = array();

    if( !isset($_POST['functionname']) ) { $aResult['error'] = 'No function name!'; }

    if( !isset($_POST['arguments']) ) { $aResult['error'] = 'No function arguments!'; }

    if( !isset($aResult['error']) ) {

        switch($_POST['functionname']) {
            case 'servo_update':
               if( !is_array($_POST['arguments']) || (count($_POST['arguments']) < 1) ) {
                   $aResult['error'] = 'Error in arguments!';
               }
               else {
                   $aResult['result'] = servo_update($_POST['arguments'][0]);
               }
               break;

            default:
               $aResult['error'] = 'Not found function '.$_POST['functionname'].'!';
               break;
        }

    }

    echo json_encode($aResult);

  function add($a,$b){
    $c=$a+$b;
    return $c;
  }

// chdir('/home/pi/scripts/servo');
function servo_update($direction) {
	if ($direction==='LEFT') {
		echo system('python ./servo_left.py');
	} else {
		echo system('python ./servo_right.py');
	}
}

?>
