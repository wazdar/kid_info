import {Calendar} from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import interaction from '@fullcalendar/interaction';
import timegrid from '@fullcalendar/timegrid';


document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('parent-calendar');

    function addModal() {
        var modal = `
    <div class="modal fade" id="myModal" role="dialog">
      <div class="modal-dialog modal-dialog-centered">        
          <div class="modal-content">
            <div class="btn-group" role="group">
                 <button id="btn_yes" class="btn btn-success">Obecny</button>         
                 <button class="btn btn-danger">Nieobecny</button>         
            </div>
          </div>
       </div>
  </div>`;


        $("body").append(modal);
        $('#myModal').modal('show')

    }


    function send_presence(children_id, presence, date_start, date_end = null,) {
        console.log(children_id, presence, date_start, date_end)

    }

    var present = null;
    var calendar = new Calendar(calendarEl, {
        plugins: [dayGridPlugin, timegrid, interaction],
        locales: 'pl',
        selectable: true,
        header: {
            left: 'prev,next today',
            center: 'title',
            right: ''
        },
        dateClick: function (info) {
            addModal()
            $('#btn_yes').click(function () {
                $('#myModal').modal('hide').remove()
                present = true

            })
            send_presence(CHILDREN_ID, present, info.dateStr)

        },
        select: function (info) {

            if (info.end.getDate() !== info.start.getDate() + 1) {
                alert('selected :) ');
            }
        },
        events: [
            {
                start: '2020-05-03',
                end: '2020-05-05',
                rendering: 'background',
                color: '#1a8bff'
            },
            {
                start: '2020-05-06',
                end: '2020-05-08',
                rendering: 'background',
                color: '#ff6161'
            }
        ]
    });

    calendar.render();
});