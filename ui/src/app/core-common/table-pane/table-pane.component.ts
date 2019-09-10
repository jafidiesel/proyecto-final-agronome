import { Component, OnInit, Input,  } from '@angular/core';

@Component({
  selector: 'app-table-pane',
  templateUrl: './table-pane.component.html'
})
export class TablePaneComponent implements OnInit {
  selectedOption: string;
  @Input() titleInput: string;
  @Input() rows: [];
  @Input() buttonAdd;
  @Input() optionsDropdown; // Todas las opciones para mostrarle en el drowdown
  @Input() optionsList; // Las opciones que tiene realmente el parametro


  mockedData = [
    { name: "Noche", value: 1 },
    { name: "Madrugada", value: 2 }
  ];


  constructor() {
    this.optionsDropdown = this.mockedData;
    this.optionsList = this.mockedData;
  }

  ngOnInit() {
  }

  agregarOpcion(){
    this.optionsList.push( JSON.stringify(this.selectedOption) );
    console.log(this.optionsList);
    console.log(this.optionsList);



  }


}
