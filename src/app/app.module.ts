import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ChartsModule } from 'ng2-charts';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { FisicoComponent } from './fisico/fisico.component';
import { MatematicoComponent } from './matematico/matematico.component';

@NgModule({
  declarations: [
    AppComponent,
    FisicoComponent,
    MatematicoComponent
  ],
  imports: [
    BrowserModule,
    ChartsModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
