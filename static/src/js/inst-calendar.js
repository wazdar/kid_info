import {Calendar} from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import interaction from '@fullcalendar/interaction';
import timegrid from '@fullcalendar/timegrid';
import {get_presence, getCookie, modal_spiner} from './ultis';


document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('institution_calendar');

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

            // your event source
            {
                events: [ // put the array in the `events` property
                    {
                        title: 'Mały Januszek',
                        start: '2020-05-01',
                        color: '#21ff37',
                    },                    {
                        title: 'Duży januszek',
                        start: '2020-05-01',
                        color: '#ff6161'
                    },                    {
                        title: 'event1',
                        start: '2020-05-01',
                        color: '#ff6161'
                    },                    {
                        title: 'event1',
                        start: '2020-05-01',
                        color: '#ff6161'
                    },
                    {
                        title: 'event1',
                        start: '2020-05-01',
                        color: '#ff6161'
                    },                    {
                        title: 'event1',
                        start: '2020-05-01',
                        color: '#ff6161'
                    },                    {
                        title: 'event1',
                        start: '2020-05-01',
                        color: 'red',
                    },                    {
                        title: 'event1',
                        start: '2020-05-01',
                        color: 'red',
                    },

                ],

            }

            // any other event sources...

        ]
    });


    calendar.render()


});