from django.http import HttpResponse
from bs4 import BeautifulSoup
import threading, requests, random, time, urllib.parse
# from selenium import webdriver
from twilio.rest import Client

agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)'
    ]

def func_baiduyun(request):
    try:
        kw = request.GET.get('kw')
        list_src = []
        url = 'http://i.ashvsash.top/' + kw
        header1 = {'User-Agent': random.choice(agent_list)}

        res1 = requests.get(url, headers=header1).content.decode("utf-8", "ignore")
        soup1 = BeautifulSoup(res1, 'lxml')
        for a in soup1.select('#post_content img'):
            list_src.append('<img style="float:left;margin-right:25px;width: 250px;" src=' + a['src'] + '>')
        for b in soup1.select('#link-report span'):
            list_src.append('<div style="font-size:17px;line-height:1.5;">' + b.text + '</div>')
        for c in soup1.select('h2 span a'):
            list_src.append('<br>' + '<strong style="font-size:18px;line-height:1.5;">' + c['href'] + '</strong>')
        for d in soup1.select('h2 span'):
            list_src.append('&nbsp;&nbsp;&nbsp;<strong style="font-size:18px;line-height:1.5;">' + d.text[-9::] + '</strong>')

        # 创建chrome参数对象
        # options = webdriver.ChromeOptions()
        # options.add_argument('--no-sandbox') # 解决DevToolsActivePort文件不存在的报错
        # options.add_argument('window-size=1600x900') # 指定浏览器分辨率
        # options.add_argument('--disable-gpu') # 谷歌文档提到需要加上这个属性来规避bug
        # options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
        # options.add_argument('blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
        # options.add_argument('--headless') # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败

        # def same(tag):
            # url2 = tag['href']
            # browser = webdriver.Chrome(options=options)
            # browser = webdriver.Chrome(options=options, executable_path='/usr/chromedriver')
            # browser.get(url2)
            # btn = browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/ul[2]/li[3]/a')
            # btn.click()
            # time.sleep(0.5)
            # xiazai = browser.find_element_by_xpath('/html/body/div[6]/div[2]/div[3]/a')
            # xiazai.click()
            # browser.switch_to.window(browser.window_handles[1])
            # list_src.append(('<div>' + tag['title'] + '</div><br>'))
            # list_src.append('<h4>' + browser.current_url + '</h4>')
            # browser.quit()

        # def one():
        #     res1 = requests.get(url, headers=header1).content.decode("utf-8", "ignore")
        #     soup1 = BeautifulSoup(res1, 'lxml')
        #     for a in soup1.select('#post_content img')[4:10:6]:
        #         same(a)
        #
        # def two():
        #     res2 = requests.get(url, headers=header2).content.decode("utf-8", "ignore")
        #     soup2 = BeautifulSoup(res2, 'lxml')
        #     for b in soup2.select('.user-share-list a')[5:10:6]:
        #         same(b)
        #
        # def three():
        #     res3 = requests.get(url, headers=header3).content.decode("utf-8", "ignore")
        #     soup3 = BeautifulSoup(res3, 'lxml')
        #     for c in soup3.select('.user-share-list a')[6:10:6]:
        #         same(c)
        #
        # def four():
        #     res4 = requests.get(url, headers=header4).content.decode("utf-8", "ignore")
        #     soup4 = BeautifulSoup(res4, 'lxml')
        #     for d in soup4.select('.user-share-list a')[7:10:6]:
        #         same(d)
        #
        # def five():
        #     res5 = requests.get(url, headers=header5).content.decode("utf-8", "ignore")
        #     soup5 = BeautifulSoup(res5, 'lxml')
        #     for e in soup5.select('.user-share-list a')[8:10:6]:
        #         same(e)
        #
        # def six():
        #     res6 = requests.get(url, headers=header6).content.decode("utf-8", "ignore")
        #     soup6 = BeautifulSoup(res6, 'lxml')
        #     for f in soup6.select('.user-share-list a')[9:10:6]:
        #         same(f)
        #
        # t1 = threading.Thread(target=one)
        # t2 = threading.Thread(target=two)
        # t3 = threading.Thread(target=three)
        # t4 = threading.Thread(target=four)
        # t5 = threading.Thread(target=five)
        # t6 = threading.Thread(target=six)
        #
        # t1.start()
        # t2.start()
        # t3.start()
        # t4.start()
        # t5.start()
        # t6.start()
        # t1.join()
        # t2.join()
        # t3.join()
        # t4.join()
        # t5.join()
        # t6.join()

        if len(list_src):
            return HttpResponse(list_src)
        else:
            return HttpResponse('<h3>对不起，没找到相关资源~</h3>')
    except Exception as e:
        return HttpResponse(e)

def func_xunlei(request):
    try:
        kw = request.GET.get('kw')
        list_src = []
        kw = kw.encode('gbk')
        kw = urllib.parse.quote(kw)
        url = 'http://s.ygdy8.com/plus/so1.php?typeid=1&keyword=' + kw

        header1 = {'User-Agent': random.choice(agent_list)}
        header2 = {'User-Agent': random.choice(agent_list)}
        header3 = {'User-Agent': random.choice(agent_list)}

        def one():
            res = requests.get(url, headers=header1).content.decode("gb2312", "ignore")
            soup = BeautifulSoup(res, 'lxml')
            for a in soup.select('table a')[:6:3]:
                url1 = 'http://s.ygdy8.com' + a['href']
                res1 = requests.get(url1, headers=header1).content.decode("gb2312", "ignore")
                soup1 = BeautifulSoup(res1, 'lxml')
                for x in soup1.select('tbody a'):
                    list_src.append('<h4>' + x['href'] + '</h4>')

        def two():
            res = requests.get(url, headers=header2).content.decode("gb2312", "ignore")
            soup = BeautifulSoup(res, 'lxml')
            for b in soup.select('table a')[1:6:3]:
                url2 = 'http://s.ygdy8.com' + b['href']
                res2 = requests.get(url2, headers=header2).content.decode("gb2312", "ignore")
                soup2 = BeautifulSoup(res2, 'lxml')
                for y in soup2.select('tbody a'):
                    list_src.append('<h4>' + y['href'] + '</h4>')

        def three():
            res = requests.get(url, headers=header3).content.decode("gb2312", "ignore")
            soup = BeautifulSoup(res, 'lxml')
            for c in soup.select('table a')[2:6:3]:
                url3 = 'http://s.ygdy8.com' + c['href']
                res3 = requests.get(url3, headers=header3).content.decode("gb2312", "ignore")
                soup3 = BeautifulSoup(res3, 'lxml')
                for z in soup3.select('tbody a'):
                    list_src.append('<h4>' + z['href'] + '</h4>')


        t1 = threading.Thread(target=one)
        t2 = threading.Thread(target=two)
        t3 = threading.Thread(target=three)
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

        if len(list_src):
            tips = ['复制对应链接后，即可下载>>><br><br>']
            return HttpResponse(tips + list_src)
        else:
            return HttpResponse('<h3>对不起，没找到相关资源~</h3>')

    except Exception as e:
        return HttpResponse(e)

def func_msg_send(request):
    try:
        account_sid = "AC23182fc8f960f3dc4065ff43f711aae1"
        auth_token = "3856a081437690db6d3afd8c203ee862"
        client = Client(account_sid, auth_token)

        first_name = request.POST.get('fn')
        last_name = request.POST.get('ln')
        e_mail = request.POST.get('em')
        mobile = request.POST.get('mb')
        msg = request.POST.get('msg')
        all_msg = "留言人：" + last_name + first_name + "Email：" + e_mail + "手机号：" + mobile + "内容：" + msg

        client.messages.create(to="+8617608289726", from_="+14803515539", body=all_msg)
        time.sleep(3)
        return HttpResponse( "<script>alert('留言成功！！！我们会尽快查阅您的留言！'); window.location.href='https://www.pantays.com'; </script>")

    except Exception as e:
        return HttpResponse(e)