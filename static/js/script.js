/**
 * Created by Andreu on 19/05/2016.
 */
$(document).ready(function () {
    //Misatges
    var time = setTimeout(eliminarAlertes, 5000);

    function eliminarAlertes() {
        var alertes = $(".alertes").slideUp();
    }

    //$("#zoom_01").elevateZoom();
    
    //Numero productes en el carro

    /*$('.afegir').on('click', function() {
        var num = $('.badge').html();
        num += 1;
        $('.badge').html(num)

    });*/



    //Select stock

    /*$('.selectpicker').change(function(){
        var url = $('.afegir').attr('href')
        var varlor = $('.selectpicker').val()

        var url_final = url + varlor
    });*/
});