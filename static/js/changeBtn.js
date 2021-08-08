$(function(){
    $('#changeBtn').on('click',function(){
        $('#controls').removeClass('disappear')
        $('#changeBtn').attr('class','disappear')
        $('#changeBtn2').attr('class','appear')
    })

    $('#changeBtn2').on('click',function(){
        $('#controls').addClass('disappear')
        $('#changeBtn').attr('class','appear')
        $('#changeBtn2').attr('class','disappear')
    })

    $('#weatherControls').on('click',function(){
        $('#weatherItem').removeClass('disvisible')
       
    })

    $('#onlineWeb').on('click',function(){
        $('#players').removeClass('disvisible')
       
    })

    $('#skinsButton').on('click',function(){
        $('#changeSkins').removeClass('disvisible')
       
    })

    $('#clearAll').on('click',function(){
        $('#weatherItem').addClass('disvisible')
        $('#players').addClass('disvisible')
        $('#changeSkins').addClass('disvisible')
       
    })
    
})

