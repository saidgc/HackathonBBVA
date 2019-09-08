import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-registro-no-convencionales',
  templateUrl: './registro-no-convencionales.component.html',
  styleUrls: ['./registro-no-convencionales.component.css']
})
export class RegistroNoConvencionalesComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }



  certificacion = '';
  certificaciones = [];

  partner = '';
  partners = [];


  agrega () {
    this.certificaciones.push(this.certificacion);
  }

  elimina( value ){
    this.certificaciones.splice(value, 1);
  }

  agregaP () {
    this.partners.push(this.partner);
  }

  eliminaP( value ){
    this.partners.splice(value, 1);
  }



}
