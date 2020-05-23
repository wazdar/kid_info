import {getCookie} from './ultis';

$(function () {

    function create_msg(from_parent, text, date) {
        if (!from_parent) {
            return `
            <div class="outgoing_msg">
                <div class="sent_msg">
                <p>${text}</p>
                <span class="time_date"> ${date.toDateString()} | ${date.toLocaleTimeString()}</span></div>
            </div>
            `
        } else {
            var img = (from_parent === "mother") ?
                '/static/dashboard/img/mother.png'
                :
                '/static/dashboard/img/father.png'

            return `
                <div class="incoming_msg">
                <div class="incoming_msg_img">
                <img
                src=${img}
                
                ></div>
                <div class="received_msg">
                <div class="received_withd_msg">
                <p>${text}</p>
                <span class="time_date"> ${date.toDateString()} | ${date.toLocaleTimeString()}</span></div>
                </div>
            </div>
            `
        }


    }

    function get_msg(element){
        $('.active_chat').removeClass('active_chat');
        $(element).addClass('active_chat')
        var chat = $('.msg_history'),
            id = $(element).data('id');

        chat.empty()

        $.ajax({
            type: 'get',
            url: '/dashboard/message/msg',
            data: {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                id: id
            },
            beforeSend: function () {

            },
            success: function (response) {
                response.map(function (element) {
                    var date = new Date(element.datetime)
                    chat.append(create_msg(element.from_parent, element.text, date))
                })


            },

            complete: function () {
                $('#child_id').val(id)
                $('.type_msg').show();
            }
        });
    }


    $('.chat_list').click(function () {
        get_msg(this)
    })

    $('.msg_send_btn').click(function () {
        var msg = $('.write_msg').val(),
            id = $('#child_id').val()
        $.post(
            '/dashboard/message/msg',
            {
                csrfmiddlewaretoken: getCookie('csrftoken'),
                'text': msg,
                'id': id,
            },
            function (data) {
                console.log(data)
            }

        ).done(function () {
            $('.write_msg').val('')
            get_msg($('.active_chat'))
        })
    })

})