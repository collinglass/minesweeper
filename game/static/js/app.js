jQuery(document).ready(function ($) { // wait until the document is ready
	function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');


	var all_images = $('.unrevealed');
	all_images.click(function(){
		var postdata = {
			'x': $(this).attr('data-x'),
			'y': $(this).attr('data-y'),
			'csrfmiddlewaretoken': csrftoken
		};
		var board_id = $(this).attr('data-board');
		$.ajax({
			url: '/game/'+board_id+'/',
			type: "POST",
			data: postdata,
			statusCode: {
				404: function() {
					alert( "Page not found" );
				},
				200: function() {
					window.location.assign('/game/'+board_id+'/');
				}
			}
		});
		window.alert(board_id);
	}); // End onclick
});