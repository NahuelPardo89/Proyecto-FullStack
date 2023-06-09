import { Component, OnInit } from '@angular/core';
import { InstalacionesService } from './service/instalaciones.service';

@Component({
  selector: 'app-instalaciones',
  templateUrl: './instalaciones.component.html',
  styleUrls: ['./instalaciones.component.css']
})
export class InstalacionesComponent implements OnInit {
  //creamos e inicializamos el array de instalaciones
  instalaciones: any[] = [];
  
  constructor(private instalacionesService: InstalacionesService) {
    this.instalaciones = [];
  }

  ngOnInit() {
    this.instalacionesService.getInstalaciones()
      .subscribe(instalaciones => {
        this.instalaciones = instalaciones;
      });
  }
}
