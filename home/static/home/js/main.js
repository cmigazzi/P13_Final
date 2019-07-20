jQuery(document).ready(function($) {

    $(".clickable-row").click(function() {
        window.location = $(this).data("url");
    });

    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems);

});

