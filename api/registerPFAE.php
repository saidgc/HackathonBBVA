<?php
    //registerPFAE
    //Este servico agrega un amigo
    
    /* Parametros:
        - RFC
        - Nombre
        - ApellidoP
        - ApellidoM
        - email
        - password
    
       Devuelve a la APP un un JSON con {status, msg}
       
       Lista de status:
       - 0      No execution
       - 200 	Success
       - 600	Datos faltantes
    */

    $myfile = fopen("PFAE.csv", "r+") or die("No se pudo abrir el archivo!");
    while(!feof($myfile)) {
        $data = fgets($myfile);
        if($data != ""){
            //El archivo esta vacio y hay que llenarlo
            //	Validación de rfc
            $rfc = "";
            if(!isset($_REQUEST[rfc]) || trim($_REQUEST[rfc]) == ""){
                $json[status] 	= 600;
                $json[msg]			= "Campo de rfc vacio";
                echo json_encode($json);
                exit;
            }
            else
            {
                $rfc = $_REQUEST[rfc];
            }
            //	Validación de nombre
            $nombre = "";
            if(!isset($_REQUEST[nombre]) || trim($_REQUEST[nombre]) == ""){
                $json[status] 	= 600;
                $json[msg]			= "Campo de nombre vacio";
                echo json_encode($json);
                exit;
            }
            else
                $nombre = $_REQUEST[nombre];
            //	Validación de ApellidoP
            $ApellidoP = "";
            if(!isset($_REQUEST[ApellidoP]) || trim($_REQUEST[ApellidoP]) == ""){
                $json[status] 	= 600;
                $json[msg]			= "Campo de ApellidoP vacio";
                echo json_encode($json);
                exit;
            }
            else
                $ApellidoP = $_REQUEST[ApellidoP];
            //	Validación de ApellidoM
            $ApellidoM = "";
            if(!isset($_REQUEST[ApellidoM]) || trim($_REQUEST[ApellidoM]) == ""){
                $json[status] 	= 600;
                $json[msg]			= "Campo de ApellidoM vacio";
                echo json_encode($json);
                exit;
            }
            else
                $ApellidoM = $_REQUEST[ApellidoM];
            //	Validación de email
            $email = "";
            if(!isset($_REQUEST[email]) || $_REQUEST[email] == "" || !filter_var($_REQUEST[email],FILTER_VALIDATE_EMAIL)){
                $json[status] 	= 600;
                $json[msg]		= "El email no existe o es incorrecto"; 
                echo json_encode($json);
                exit;
            }
            else{
                $email = $_REQUEST[email];
            //Validacion de password
            $password = "";
            if(!isset($_GET[password]) || $_GET[password] == ""){
                $json[status] 	= 600;
                $json[msg]		= "Campo de password vacio";
                echo json_encode($json);
                exit;
            }
            else
                $password = $_GET[password];

            $PFAE = $nombre . "," . $ApellidoP . "," . $ApellidoM . "," . $email . "," . $password;
            fwrite($myfile, $PFAE); 
            $json[status] 	= 200;
            $json[msg]		= "PFAE registrada correctamente";
            echo json_encode($json);
            exit;
        }
      }


?>