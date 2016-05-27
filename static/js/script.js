/**
 * Created by Andreu on 19/05/2016.
 */
$(document).ready(function () {
    //Misatges
    var time = setTimeout(eliminarAlertes, 5000);

    function eliminarAlertes() {
        var alertes = $(".alertes").slideUp();
    }

    <!-- Kick off Filterizr -->
    $(function () {
        //Initialize filterizr with default options
        $('.filtr-container').filterizr();
    });
});