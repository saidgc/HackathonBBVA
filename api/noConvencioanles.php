<?php
    //variablesNoConvencioanles
    //Este servico agrega un amigo
    
    /* Parametros:
        - direccion?
        - sertificaciones? (0/1)
        - economiaZona?
        - noClientes?
        - noClientesEsperados?
        - costoAdquisicionClientes?
        - landinfPage? (0/1)
        - domainAge?
        - BBVA?
    
       Devuelve a la APP un un JSON con {status, msg}
       
       Lista de status:
       - 0      No execution
       - 200 	Success
       - 600	Datos faltantes
    */

    $myfile = fopen("moral.csv", "r+") or die("No se pudo abrir el archivo!");
    while(!feof($myfile)) {
        $data = fgets($myfile);
        if($data != ""){
            //El archivo esta vacio y hay que llenarlo
            //	Validación de direccion
            $direccion = "";
            if(!isset($_REQUEST[direccion]) || trim($_REQUEST[direccion]) == ""){
                //Es opcional
            }
            else
            {
                $direccion = $_REQUEST[direccion];
            }
            //	Validación de sertificaciones
            $sertificaciones = "";
            if(!isset($_REQUEST[sertificaciones]) || trim($_REQUEST[sertificaciones]) == ""){
                //Es opcional
            }
            else
            {
                $sertificaciones = $_REQUEST[sertificaciones];
            }
            //	Validación de economiaZona
            $economiaZona = "";
            if(!isset($_REQUEST[economiaZona]) || trim($_REQUEST[economiaZona]) == ""){
                //Es opcional
            }
            else
            {
                $economiaZona = $_REQUEST[economiaZona];
            }
            //	Validación de noClientes
            $noClientes = "";
            if(!isset($_REQUEST[noClientes]) || trim($_REQUEST[noClientes]) == ""){
                //Es opcional
            }
            else
            {
                $noClientes = $_REQUEST[noClientes];
            }
            //	Validación de noClientesEsperados
            $noClientesEsperados = "";
            if(!isset($_REQUEST[noClientesEsperados]) || trim($_REQUEST[noClientesEsperados]) == ""){
                //Es opcional
            }
            else
            {
                $noClientesEsperados = $_REQUEST[noClientesEsperados];
            }
            //	Validación de costoAdquisicionClientes
            $costoAdquisicionClientes = "";
            if(!isset($_REQUEST[costoAdquisicionClientes]) || trim($_REQUEST[costoAdquisicionClientes]) == ""){
                //Es opcional
            }
            else
            {
                $costoAdquisicionClientes = $_REQUEST[costoAdquisicionClientes];
            }
            //	Validación de landinfPage
            $landinfPage = "";
            if(!isset($_REQUEST[landinfPage]) || trim($_REQUEST[landinfPage]) == ""){
                //Es opcional
            }
            else
            {
                $landinfPage = $_REQUEST[landinfPage];
            }
            //	Validación de domainAge
            $domainAge = "";
            if(!isset($_REQUEST[domainAge]) || trim($_REQUEST[domainAge]) == ""){
                //Es opcional
            }
            else
            {
                $domainAge = $_REQUEST[domainAge];
            }
            //	Validación de BBVA
            $BBVA = "";
            if(!isset($_REQUEST[BBVA]) || trim($_REQUEST[BBVA]) == ""){
                //Es opcional
            }
            else
            {
                $BBVA = $_REQUEST[BBVA];
            }

            $PFAE = $direccion . "," . $sertificaciones . "," . $economiaZona . "," . $noClientes . "," . $noClientesEsperados . "," . $costoAdquisicionClientes . "," . $landinfPage . "," . $domainAge . "," . $BBVA ;
            fwrite($PFAE); 
            $json[status] 	= 200;
            $json[msg]		= "PFAE registrada correctamente";
            echo json_encode($json);
            exit;
        }
      }


?>