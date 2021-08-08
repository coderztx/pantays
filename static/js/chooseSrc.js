$(function(){
    var $formItem = $('#formItem');
    var $baiduyun = $('#baiduyun');
    var $input = $('#input');
    var $douban = $('#douban');
    var $xunlei = $('#xunlei');
    var $zimu = $('#zimu');

    // 点击豆瓣按钮后执行的函数
    function douBanClick(){
        $formItem.attr('action','https://search.douban.com/movie/subject_search')
        $input.attr('name','search_text')
        $input.attr('placeholder','豆瓣搜索')
        $douban.addClass('selected')
        $baiduyun.removeClass('selected')
        $xunlei.removeClass('selected')
        $zimu.addClass('disappear')
        $zimu.removeClass('selected')

    }

    // 点击百度云按钮后执行的函数
    function baiDuYunClick(){
        $formItem.attr('action','/search/baiduyun')
        $input.attr('name','kw')
        $input.attr('placeholder','百度云链接搜索')
        $baiduyun.addClass('selected')
        $douban.removeClass('selected')
        $xunlei.removeClass('selected')
        $zimu.addClass('disappear')
        $zimu.removeClass('selected')
    
    }

    // 点击迅雷按钮后执行的函数
    function xunLeiClick(){
        $formItem.attr('action','/search/xunlei')
        $input.attr('name','kw')
        $input.attr('placeholder','迅雷资源搜索')
        $xunlei.addClass('selected')
        $douban.removeClass('selected')
        $baiduyun.removeClass('selected')
        $zimu.removeClass('disappear')
        $zimu.removeClass('selected')
        
    }

    function ziMu(){
        $formItem.attr('action','http://www.zimuku.la/search')
        $input.attr('name','q')
        $input.attr('placeholder','影片字幕下载')
        $zimu.addClass('selected')
        $xunlei.removeClass('selected')
        
         
    }

// 设置事件，点击对应元素后，调用对应函数
    $baiduyun.on('click',baiDuYunClick);
    $douban.on('click',douBanClick);
    $xunlei.on('click',xunLeiClick);
    $zimu.on('click',ziMu);
});
