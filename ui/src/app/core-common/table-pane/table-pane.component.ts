import { Component, OnInit, Input,  } from '@angular/core';
import { Observable } from 'rxjs';
import { faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-table-pane',
  templateUrl: './table-pane.component.html'
})
export class TablePaneComponent implements OnInit {
  selectedOption: string;
  @Input() titleText: string;
  @Input() rows: Observable<string>;
  @Input() buttonAddText: string;
  @Input() optionsDropdown = []; // Todas las opciones para mostrarle en el dropdown
  @Input() optionsList = []; // Las opciones que tiene realmente el parametro
  @Input() output =[]
  
  faTrashAlt = faTrashAlt;

  mockedData = [
    "noche",
    "mañana",
  ];


  constructor() {
  }
  
  ngOnInit() {
    this.rows.subscribe(
      (result:any) => {
        for (let index = 0; index < result.length; index++) {
          const element = result[index];
          this.optionsDropdown.push(element);
          
        }
      },
      error => console.log(error)
    );
    console.log(this.rows);
  }

  agregarItem(){
    this.optionsList.push( this.selectedOption );
    this.output.push( this.selectedOption );
    console.log(this.optionsList);
  }

  quitarItem(itemARemover){
    this.optionsList.forEach( (item, index) => {
      if(item === itemARemover) {
        this.optionsList.splice(index,1);
        this.output.splice(index,1);
      }
    });
    console.log(this.optionsList);
  }


}
