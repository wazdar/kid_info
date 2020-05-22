import {Calendar} from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import interaction from '@fullcalendar/interaction';
import timegrid from '@fullcalendar/timegrid';
import {get_presence, getCookie, modal_spiner} from './ultis';


document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('parent-calendar');
    if (calendarEl) {
        function send_presence(children_id, presence, date_start, date_end = null) {
            $.ajax({
                type: 'post',
                url: '/dashboard/kids/presence/set',
                data: {
                    csrfmiddlewaretoken: getCookie('csrftoken'),
                    id: children_id,
                    presence: presence,
                    date_start: date_start,
                    date_end: date_end,
                },
                beforeSend: function () {
                    $('#myModal').html(modal_spiner())
                },
                success: function (response) {
                    $('#myModal').modal('hide');
                    $('#myModal').detach();
                    calendar.refetchEvents();
                },

                error: function (data) {

                }
            });
        }


        function showModal(date1, date2 = null) {

            var modal = `
        <div class="modal fade" id="myModal" role="dialog">
          <div class="modal-dialog modal-dialog-centered">        
              <div class="modal-content">
                <div class="btn-group" role="group">
                     <button id="btn_yes" class="btn btn-success">Obecny</button>         
                     <button id="btn_no" class="btn btn-danger" onclick="">Nieobecny</button>         
                </div>
              </div>
           </div>
      </div>`;

            $("body").append(modal);
            $('#myModal').modal('show')

            $('#btn_yes').click(function () {
                send_presence(CHILDREN_ID, true, date1, date2);

            });
            $('#btn_no').click(function () {
                send_presence(CHILDREN_ID, false, date1, date2)
            });
        }

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
                showModal(info.dateStr);
            },
            select: function (info) {

                if (info.end.getDate() !== info.start.getDate() + 1) {
                    showModal(info.startStr, info.endStr);
                }
            },
            eventSources: [
                {
                    url: '/dashboard/kids/presence/get',
                    method: 'POST',
                    extraParams: {
                        csrfmiddlewaretoken: getCookie('csrftoken'),
                        id: CHILDREN_ID,
                    },
                    failure: function () {
                        alert('Bład pobierania danych');
                    },
                }
            ]
        });
        calendar.render()
    }
});