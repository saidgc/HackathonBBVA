import { Component, OnInit } from '@angular/core';

// import { HttpClient } from '@angular/common/https';
// import { HttpErrorResponse } from '@angular/common/https';
import { HttpClient } from '@angular/common/http';
import { HttpClientModule } from '@angular/common/http';
import { Http, Response } from '@angular/http';

import {HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-matematico',
  templateUrl: './matematico.component.html',
  styleUrls: ['./matematico.component.css']
})
export class MatematicoComponent implements OnInit {
  constructor(private httpService: HttpClient) { }

      // ADD CHART OPTIONS. 
      pieChartOptions = {
        responsive: true
    }

    pieChartLabels =  ['JAN', 'FEB', 'MAR', 'APR', 'MAY'];
  
    // CHART COLOR.
    pieChartColor:any = [
        {
            backgroundColor: ['rgba(30, 169, 224, 0.8)',
            'rgba(255,165,0,0.9)',
            'rgba(139, 136, 136, 0.9)',
            'rgba(255, 161, 181, 0.9)',
            'rgba(255, 102, 0, 0.9)'
            ]
        }
    ]

    pieChartData:any = [
      { 
          data: []
      }
    ];

  ngOnInit() {
    this.httpService.get('./assets/sales.json', {responseType: 'json'}).subscribe(
      data => {
          this.pieChartData = data as any [];	 // FILL THE CHART ARRAY WITH DATA.
      },
      (err: HttpErrorResponse) => {
          console.log (err.message);
      }
    );
  }

  onChartClick(event) {
    console.log(event);
  }
  
  

}


