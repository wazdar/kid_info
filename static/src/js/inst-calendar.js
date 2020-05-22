import {Calendar} from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import interaction from '@fullcalendar/interaction';
import timegrid from '@fullcalendar/timegrid';
import {get_presence, getCookie, modal_spiner} from './ultis';


document.addEventListener('DOMContentLoaded', function () {
    var institution_calendar = document.getElementById('institution_calendar');
    if (institution_calendar) {
        var calendar = new Calendar(institution_calendar, {

            plugins: [dayGridPlugin,],
            locales: 'pl',
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
                    url: '/dashboard/kids/presence/get-all',
                    method: 'POST',
                    extraParams: {
                        csrfmiddlewaretoken: getCookie('csrftoken'),
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