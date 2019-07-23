jQuery(document).ready(function($) {

    $(".clickable-row").click(function() {
        window.location = $(this).data("url");
    });

    // Modals
    var modals = document.querySelectorAll('.modal');
    var modalsInstances = M.Modal.init(modals);

    // Datepicker
    var datepickers = document.querySelectorAll('.datepicker');
    var datepickerOptions = {"format": "dd/mm/yyyy",
                             "minDate": new Date(),
                             "i18n": {
                                months: ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
                                weekdaysShort: ['Dim', 'Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam'],
                                today: 'aujourd\'hui',  
                                clear: 'effacer',
                                cancel: "annuler"
                             }
                            }
    var datepickerInstances = M.Datepicker.init(datepickers, datepickerOptions);

});

