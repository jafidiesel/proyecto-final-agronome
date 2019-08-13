import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',

})
export class TableComponent implements OnInit {

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
