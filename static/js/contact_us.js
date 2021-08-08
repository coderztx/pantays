$(function(){
    // 监视对应input框，聚焦则移动text文本内容
    $('#input1').on('focus',function(){
        $('#text1').css({
            'top': '-35px',
            'left': '-10px'
        })
    })

    $('#input2').on('focus',function(){
        $('#text2').css({
            'top': '-35px',
            'left': '-10px'
        })
    })

    $('#input3').on('focus',function(){
        $('#text3').css({
            'top': '-35px',
            'left': '-10px'
        })
    })

    $('#input4').on('focus',function(){
        $('#text4').css({
            'top': '-35px',
            'left': '-10px'
        })
    })

    $('#input5').on('focus',function(){
        $('#text5').css({
            'top': '-35px',
            'left': '-10px'
        })
    })

    // 监视对应input框，聚焦则改变line的高度
    $('#input1').on('focus',function(){
        $('#line1').css({
            'height': '100%'
        })
    })

    $('#input2').on('focus',function(){
        $('#line2').css({
            'height': '100%'
        })
    })

    $('#input3').on('focus',function(){
        $('#line3').css({
            'height': '100%'
        })
    })

    $('#input4').on('focus',function(){
        $('#line4').css({
            'height': '100%'
        })
    })

    $('#input5').on('focus',function(){
        $('#line5').css({
            'height': '100%'
        })
    })
    
     // 监视对应input框，失去焦点后，判断是否为空值，为空则恢复text的位置
    $("#input1").on('blur',function() {
        if ($("#input1").val() == ""){ 
            $("#text1").css({
                'top': '0',
                'left': '0'
            }); 
        }
    })

    $("#input2").on('blur',function() {
        if ($("#input2").val() == ""){ 
            $("#text2").css({
                'top': '0',
                'left': '0'
            }); 
        }
    })

    $("#input3").on('blur',function() {
        if ($("#input3").val() == ""){ 
            $("#text3").css({
                'top': '0',
                'left': '0'
            }); 
        }
    })

    $("#input4").on('blur',function() {
        if ($("#input4").val() == ""){ 
            $("#text4").css({
                'top': '0',
                'left': '0'
            }); 
        }
    })

    $("#input5").on('blur',function() {
        if ($("#input5").val() == ""){ 
            $("#text5").css({
                'top': '0',
                'left': '0'
            }); 
        }
    })
     
     // 监视对应input框，失去焦点后，判断是否为空值，为空则恢复line的位置
    $("#input1").on('blur',function() {
        if ($("#input1").val() == ""){ 
            $("#line1").css({
                'height':'2px'
            }); 
        }
    })

    $("#input2").on('blur',function() {
        if ($("#input2").val() == ""){ 
            $("#line2").css({
                'height':'2px'
            }); 
        }
    })

    $("#input3").on('blur',function() {
        if ($("#input3").val() == ""){ 
            $("#line3").css({
                'height':'2px'
            }); 
        }
    })

    $("#input4").on('blur',function() {
        if ($("#input4").val() == ""){ 
            $("#line4").css({
                'height':'2px'
            }); 
        }
    })

    $("#input5").on('blur',function() {
        if ($("#input5").val() == ""){ 
            $("#line5").css({
                'height':'2px'
            }); 
        }
    })

    // 监听改变样式的点击事件
    $("#change_style").on('click',function() {
        $('body').css({'background':'#03080a'})
        $('h2').css({'color':'#45f3ff'})
        $('.inputBox').css({'color':'#45f3ff'})
        $('input').css({'color':'#000'})
        $('textarea').css({'color':'#000'})
        $('.line').css({'background':'#45f3ff'})
        $('button').css({'color':'#000','background':'#45f3ff'})
    })

});