import { Component, OnInit } from '@angular/core';
import { ResponseWrapper } from '../models/response-wrapper';
import { ResolverService } from '../services/resolver.service';

@Component({
  selector: 'app-chess',
  templateUrl: './chess.component.html',
  styleUrls: ['./chess.component.css']
})
export class ChessComponent implements OnInit {

  input: string;
  output: string;

  constructor(
    private service: ResolverService
  ) { }

  ngOnInit(): void {
  }

  resolve(): void {
    this.service.resolveChessProblem(this.input).subscribe((response: ResponseWrapper) => {
      this.output = response.response;
    });
  }

}
