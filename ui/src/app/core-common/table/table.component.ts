import { Component, OnInit, Input } from '@angular/core';
import { faEdit, faPowerOff, faEye } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',

})
export class TableComponent implements OnInit {
  
  faEdit = faEdit;
  faPowerOff = faPowerOff;
  faEye = faEye;


  @Input() tableData: any[];
  tableDataHeader : any[];
  tableDataRow : any[];
  tableLong: number;
  @Input() tableCss: any;
  @Input() hasLinks: any;

  dummyTableData: any[] = [
    0,
    1,
    2,
    3,
    4,
  ];

  constructor() { 
  }
  
  ngOnInit() {
    this.tableDataHeader = this.tableData.slice(0,1);
    this.tableDataRow = this.tableData.slice(1,this.tableData.length);
  }

}
