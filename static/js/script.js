/**
 * Created by Andreu on 19/05/2016.
 */
$(document).ready(function () {
    var time = setTimeout(eliminarAlertes, 5000);

    function eliminarAlertes() {
        var alertes = $(".alertes").slideUp();
    }

    $('.selectpicker').selectpicker({
        style: 'btn-info',
        size: 4
    });
});