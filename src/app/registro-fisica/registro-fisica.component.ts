import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-registro-fisica',
  templateUrl: './registro-fisica.component.html',
  styleUrls: ['./registro-fisica.component.css']
})
export class RegistroFisicaComponent implements OnInit {
  rfc = 'paho';
  constructor() { }

  ngOnInit() {
  }
  print() {
    console.log(this.rfc.toString());
    console.log(this.rfc);
  }

  changeRfc($event) {
    this.rfc = $event.target.value;
    if (this.rfc.length >= 13)
      this.validarInput(this.rfc);
  }

  rfcValido(rfc, aceptarGenerico = true) {
    const re = /^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$/;
    let validado = rfc.match(re);

    if (!validado)  //Coincide con el formato general del regex?
      return false;

    //Separar el dígito verificador del resto del RFC
    const digitoVerificador = validado.pop(),
      rfcSinDigito = validado.slice(1).join(''),
      len = rfcSinDigito.length,

      //Obtener el digito esperado
      diccionario = "0123456789ABCDEFGHIJKLMN&OPQRSTUVWXYZ Ñ",
      indice = len + 1;
    var suma,
      digitoEsperado;

    if (len == 12) suma = 0
    else suma = 481; //Ajuste para persona moral

    for (var i = 0; i < len; i++)
      suma += diccionario.indexOf(rfcSinDigito.charAt(i)) * (indice - i);
    digitoEsperado = 11 - suma % 11;
    if (digitoEsperado == 11) digitoEsperado = 0;
    else if (digitoEsperado == 10) digitoEsperado = "A";

    //El dígito verificador coincide con el esperado?
    // o es un RFC Genérico (ventas a público general)?
    if ((digitoVerificador != digitoEsperado)
      && (!aceptarGenerico || rfcSinDigito + digitoVerificador != "XAXX010101000"))
      return false;
    else if (!aceptarGenerico && rfcSinDigito + digitoVerificador == "XEXX010101000")
      return false;
    return rfcSinDigito + digitoVerificador;
  }

  validarInput(input) {
    let rfc = input.trim().toUpperCase();
    let resultado = document.getElementById('resultado');
    let valido;
    var rfcCorrecto = this.rfcValido(rfc);

    if (rfcCorrecto) {
      valido = "Válido";
      resultado.classList.add("ok");
    } else {
      valido = "Inválido"
      resultado.classList.remove("ok");
    }

    resultado.innerText = valido;
  }

}
