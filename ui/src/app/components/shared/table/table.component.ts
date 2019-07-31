import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',

})
export class TableComponent implements OnInit {

  @Input() tableData: any[];
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
  }

}
