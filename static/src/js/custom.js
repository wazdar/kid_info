import {getCookie} from './ultis';

$(function () {


    $('[data-toggle="sidebar"]').click(function (event) {
        event.preventDefault();
        $('.app').toggleClass('sidebar-toggle');
    });

    function validateEmail(email) {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    }

    $('[data-toggle="inv_parent"]').on('click', function (event) {
        event.stopPropagation();
        event.preventDefault();

        var button = $(this),
            form = button.closest('form'),
            container = $(form.parent('.dropdown-menu').get(0)),
            data = form.serializeArray();

        var loading = `
        <div class="text-center" style="padding-bottom:1rem">
          <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>`;

        $('.text-danger').remove();


        if (validateEmail(data[3].value)) {
            $.ajax({
                type: 'post',
                url: '/account/invite',
                data: form.serializeArray(),
                beforeSend: function () {
                    container.html(loading);
                },
                success: function (response) {
                    container.html('<div class="mb-3"><small class="text-success m-auto">Zaproszienie wysłano</small></div>');
                    container.parent().append(`
                        <button type="button"
                        class="btn btn-sm btn-warning float-right ml-1"
                        data-id="${response.id}"
                        data-toggle="cancle_inv"
                        >
                            <i class="fa fa-trash"></i> Anuluj
                        </button>
                    `)
                },

                error: function (data) {
                    container.append('<div class="mb-3"><small class="text-danger m-auto">${data}</small></div>')
                }
            });
        } else {
            container.append('<div class="mb-3"><small class="text-danger" >Podaj poprawny email</small></div>')
        }

    })

    $(document).on('click', '[data-toggle="cancle_inv"]', function () {
        var button = $(this),
            id = button.data('id');

        $.post('/account/invite/cancel', {
            id: id,
            csrfmiddlewaretoken: getCookie('csrftoken'),
        }, function () {
        }).done(function (data) {
            button.remove()
        }).fail(function (data) {
            console.log(data.responseText)
        })

    })
})