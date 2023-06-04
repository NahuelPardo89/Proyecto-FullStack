import { User } from "./user.interface";

export interface JwtResponse {
  user: User;
  refresh: string;
  access: string;
}