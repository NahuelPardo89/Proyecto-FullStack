import { Component } from '@angular/core';
import { BreakpointObserver, Breakpoints } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map, shareReplay } from 'rxjs/operators';

@Component({
  selector: 'app-dashboard-nav',
  templateUrl: './dashboard-nav.component.html',
  styleUrls: ['./dashboard-nav.component.css']
})
export class DashboardNavComponent {

  isAdmin: boolean = false;
  

  isAdminToggle() {
    this.isAdmin = !this.isAdmin
  }

  isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
    .pipe(
      map(result => result.matches),
      shareReplay()
    );

  constructor(private breakpointObserver: BreakpointObserver) {
    this.loadAdminStatus();
  }

  loadAdminStatus() {
    const userItem = localStorage.getItem('user');
    if (userItem) {
      const usuario = JSON.parse(userItem);
      this.isAdmin = usuario.is_staff;
      
    }
  }

}
