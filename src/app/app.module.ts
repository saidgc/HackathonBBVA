
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';

import { HeaderComponent } from './header/header.component';
import { TarjetasComponent } from './tarjetas/tarjetas.component';
import { RegistroFisicaComponent } from './registro-fisica/registro-fisica.component';
import { RegistraPersonaMoralComponent } from './registra-persona-moral/registra-persona-moral.component';
import { RegistroNoConvencionalesComponent} from './registro-no-convencionales/registro-no-convencionales.component';
import { DashboardComponent } from './dashboard/dashboard.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    TarjetasComponent,
    RegistroFisicaComponent,
    RegistraPersonaMoralComponent,
    RegistroNoConvencionalesComponent,
    DashboardComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})



export class AppModule { }
