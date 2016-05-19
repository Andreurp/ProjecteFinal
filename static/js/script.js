/**
 * Created by Andreu on 19/05/2016.
 */
$(document).ready(function () {
    var time = setTimeout(eliminarAlertes, 5000);

    function eliminarAlertes() {
        var alertes = $(".alertes").slideUp();
    }
    
    //quatitat pruducte + o -
    // This button will increment the value
    $('.qtyplus').click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        fieldName = $(this).attr('field');
        // Get its current value
        var currentVal = parseInt($('input[name=' + fieldName + ']').val());
        // If is not undefined
        if (!isNaN(currentVal)) {
            // Increment
            $('input[name=' + fieldName + ']').val(currentVal + 1);
        } else {
            // Otherwise put a 0 there
            $('input[name=' + fieldName + ']').val(0);
        }
        $.post('update_session/', $(this).closest('tr').find('#id').html(), $(this).closest('form').find('.qty').val())
    });

    // This button will decrement the value till 0
    $(".qtyminus").click(function (e) {
        // Stop acting like a button
        e.preventDefault();
        // Get the field name
        fieldName = $(this).attr('field');
        // Get its current value
        var currentVal = parseInt($('input[name=' + fieldName + ']').val());
        // If it isn't undefined or its greater than 0
        if (!isNaN(currentVal) && currentVal > 0) {
            // Decrement one
            $('input[name=' + fieldName + ']').val(currentVal - 1);
        } else {
            // Otherwise put a 0 there
            $('input[name=' + fieldName + ']').val(0);
        }
        $.post('update_session/', $(this).closest('tr').find('#id').html(), $(this).closest('form').find('.qty').val())
    });
});