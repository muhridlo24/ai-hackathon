

$(document).ready(function(){
    $("table.meeting-notes-table").DataTable({
        fixedColumns:{
            left:3,
            right:get_fixed_columns()
        },
        autoWidth: true,
        fixedHeader: true,
        serverSide: true,
        scrollCollapse: true,
        scrollX: true,
        scrollY: '50vh',
        responsive: true,
        ajax: {
          url: 'data',
          type: 'GET',
          data: function (data) {
            // Customize the AJAX request parameters with filtering criteria
            data.dcr_status = sessionStorage.getItem('dcr_status');
            // Add any other parameters as needed for filtering
            delete data.columns;
          },
        },  
        columnDefs: [
          {width:"8px",target:0},
            {width:"150px",target:1},
            {width:"150px",target:2},
            {width:"150px",target:3},
            {width:"150px",target:4},
            {width:"100px",target:5},
            {width:"150px",target:6},
        ],
        columns: [
            {
                visible: false,
                data: 'id'
            },
            {
                className:"bg-white tx-center",
                data: 'meeting_title'
            },
            {
                className:"bg-white tx-center",
                data: 'project_id__project_name'
            },
            {
                className:"bg-white tx-center",
                data: 'group_id__group_name'
            },
            {
                className:"bg-white tx-center",
                data: 'meeting_date'
            },
            {
              className:"bg-white tx-center",
              data: 'transcript'
            },
            {
              visible:true,
              data: null,
              className: 'dt-center editor-delete bg-white',
              render: function(data,type,row){ 
                if(!data['isAuthorized']['delete']){
                  return '';
                }
                return '<div style="width:100%;height:100%;"><a href="#modal_delete_dcr" data-toggle="modal" style="color:red;"><ion-icon name="trash" title="Delete DCR"></ion-icon></a></div>';
              }
              ,
              // defaultContent: '<div style="width:100%;height:100%;"><a href="#modal_delete_record" data-toggle="modal" style="color:red;"><ion-icon name="trash" title="Delete DCR"></ion-icon></a></div>',
              orderable: false
            }
        ],
        language: {
          searchPlaceholder: 'Search...',
          sSearch: '',
          lengthMenu: '_MENU_ items/page',
        },
        dom: 'lfrtip',
        "rowCallback":function(row,data,index){
        }
    })
})