import { Component, OnInit } from '@angular/core';
import { InstalacionesService } from '../../services/instalaciones.service';

@Component({
  selector: 'app-instalaciones',
  templateUrl: './instalaciones.component.html',
  styleUrls: ['./instalaciones.component.css']
})
export class InstalacionesComponent implements OnInit {
  
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
