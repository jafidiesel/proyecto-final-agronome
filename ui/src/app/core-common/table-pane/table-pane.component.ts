import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-table-pane',
  templateUrl: './table-pane.component.html'
})
export class TablePaneComponent implements OnInit {
  @Input() titleInput: string;
  @Input() rows: [];
  @Input() buttonAdd;
  
  selectedOption: string;
  printedOption: string;

  options = [
    { name: "Noche", value: 1 },
    { name: "Madrugada", value: 2 }
  ]
  print() {
    this.printedOption = this.selectedOption;
    console.log("My input: ", this.selectedOption);
  }


  constructor() { }

  ngOnInit() {
  }
  
  agregarOpcion(parametro: string){
    this.rows.push(parametro);

  }


}
