import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { tap, catchError } from 'rxjs/operators';
import { Observable, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ResolverService {

  headers = new HttpHeaders()
    .set('Content-Type', 'application/json')
    .set('Accept', 'application/json');
  httpOptions = { headers: this.headers };
  url: string;

  constructor(private http: HttpClient) { }

  resolvePaperLeagueProblem(data: string) {
    return this.http.post(`${environment.server_url}/solve/paper_league`, { data: data }, this.httpOptions).pipe(catchError(this.handleError));
  }

  resolveChessProblem(data: string) {
    return this.http.post(`${environment.server_url}/solve/chess`, { data: data }, this.httpOptions).pipe(catchError(this.handleError));
  }

  resolveStringValueProblem(data: string) {
    return this.http.post(`${environment.server_url}/solve/string_value`, { data: data }, this.httpOptions).pipe(catchError(this.handleError));
  }

  private handleError(error: any) {
    console.error(error);
    return throwError(error);
  }
}
