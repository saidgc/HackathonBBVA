
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HeaderComponent } from './header/header.component';
import { TarjetasComponent } from './tarjetas/tarjetas.component';

 
const routes: Routes = [
  
];



@NgModule({

  imports: [

    RouterModule.forRoot(
      routes,  
      {anchorScrolling: 'enabled',
        enableTracing: true}
    )
  ],
  
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
