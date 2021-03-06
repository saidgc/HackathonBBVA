
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HeaderComponent } from './header/header.component';
import { TarjetasComponent } from './tarjetas/tarjetas.component';
import { RegistraPersonaMoralComponent } from './registra-persona-moral/registra-persona-moral.component';
import { RegistroFisicaComponent } from './registro-fisica/registro-fisica.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { RegistroNoConvencionalesComponent } from './registro-no-convencionales/registro-no-convencionales.component';



const routes: Routes = [
  { path: '',   redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: TarjetasComponent },
  { path: 'registraMoral', component: RegistraPersonaMoralComponent },
  { path: 'registraFisica', component: RegistroFisicaComponent },
  
  { path: 'dashboard', component: DashboardComponent },
  { path: 'registronoc', component: RegistroNoConvencionalesComponent }
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
