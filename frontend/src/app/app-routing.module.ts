import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChessComponent } from './chess/chess.component';
import { PaperLeagueComponent } from './paper-league/paper-league.component';
import { StringValueComponent } from './string-value/string-value.component';

const routes: Routes = [
  { path: 'problem-1', component: PaperLeagueComponent },
  { path: 'problem-2', component: ChessComponent },
  { path: 'problem-3', component: StringValueComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
