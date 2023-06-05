import { Component, OnDestroy, OnInit } from '@angular/core';

import { Subscription } from 'rxjs';
import { User } from 'src/app/modules/auth/interfaces/user.interface';
import { AuthService } from 'src/app/modules/auth/services/auth.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css']
})
export class NavComponent implements OnInit, OnDestroy {
  user: User | null = null;
  subscription!: Subscription;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    this.subscription = this.authService.currentUser.subscribe(user => {
      this.user = user;
    });
  }

  logout() {
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
      console.log('entra')
      this.authService.logout(refreshToken).subscribe(() => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user');
        this.user = null;
      });
    }
  }

  ngOnDestroy(): void {
    this.subscription.unsubscribe();
  }
}

