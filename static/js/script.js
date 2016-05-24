/**
 * Created by Andreu on 19/05/2016.
 */
$(document).ready(function () {
    //Misatges
    var time = setTimeout(eliminarAlertes, 5000);

    function eliminarAlertes() {
        var alertes = $(".alertes").slideUp();
    }
});