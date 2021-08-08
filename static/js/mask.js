$(function(){
    $('#input').on('focus',function(){
        $('#mask').addClass('mask')
    })

    $('#input').on('blur',function(){
        $('#mask').removeClass('mask')
    })
});