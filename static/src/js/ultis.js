export function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export function modal_spiner() {
    return `

          <div class="modal-dialog modal-dialog-centered">        
              <div class="modal-content p-4">
                <div class="d-flex justify-content-center">
  <div class="spinner-border" role="status">
    <span class="sr-only">Loading...</span>
  </div>
</div>
              </div>
           </div>
      </div>
   `
};

export function get_presence(children_id) {
    $.post("/dashboard/kids/presence/get", {
        csrfmiddlewaretoken: getCookie('csrftoken'),
        'id': children_id
    }, function (data) {

    }).done(function () {

        }
    );
}