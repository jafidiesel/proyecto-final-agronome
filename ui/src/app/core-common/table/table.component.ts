import { Component, OnInit, Input, EventEmitter, Output } from '@angular/core';
import { faEdit, faPowerOff, faEye,faTrashAlt } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',

})
export class TableComponent implements OnInit {
  
  faEdit = faEdit;
  faPowerOff = faPowerOff;
  faEye = faEye;
  faTrashAlt = faTrashAlt;


  @Input() tableData: any[];
  tableDataHeader : any[];
  tableDataRow : any[];
  tableLong: number;
  @Input() tableCss: any;
  @Input() hasLinks: any;
  @Output() eventClick = new EventEmitter();


  constructor() { 
  }
  
  ngOnInit() {
    this.tableDataHeader = this.tableData.slice(0,1);
    this.tableDataRow = this.tableData.slice(1,this.tableData.length);
  }

  clickEvent(parametro){
    this.eventClick.emit(parametro);
  }

}
