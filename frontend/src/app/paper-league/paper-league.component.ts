import { Component, OnInit } from '@angular/core';
import { ResponseWrapper } from '../models/response-wrapper';
import { ResolverService } from '../services/resolver.service';

@Component({
  selector: 'app-paper-league',
  templateUrl: './paper-league.component.html',
  styleUrls: ['./paper-league.component.css']
})
export class PaperLeagueComponent implements OnInit {

  input: string;
  output: string;

  constructor(
    private service: ResolverService
  ) { }

  ngOnInit(): void {
  }

  resolve(): void {
    this.service.resolvePaperLeagueProblem(this.input).subscribe((response: ResponseWrapper) => {
      this.output = response.response;
    });
  }

}
