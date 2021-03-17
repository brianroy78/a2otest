import { Component, OnInit } from '@angular/core';
import { ResponseWrapper } from '../models/response-wrapper';
import { ResolverService } from '../services/resolver.service';


@Component({
  selector: 'app-string-value',
  templateUrl: './string-value.component.html',
  styleUrls: ['./string-value.component.css']
})
export class StringValueComponent implements OnInit {

  input: string;
  output: string;

  constructor(
    private service: ResolverService
  ) { }

  ngOnInit(): void {
  }

  resolve(): void {
    this.service.resolveStringValueProblem(this.input).subscribe((response: ResponseWrapper) => {
      this.output = response.response;
    });
  }

}
