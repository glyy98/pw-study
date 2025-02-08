from playwright.sync_api import Page,expect,sync_playwright

#同步方法，pw实例只允许一个
def pw_baidu():
    #一共四层，一个pw会对一个browser，一个browser会对多个上下文
    pw = sync_playwright().start()    #创建一个pw的实例
    browser = pw.chromium.launch(headless=fasle) #选择浏览器
    context =browser.new_context()  #创建上下文，设置分辨率大小
    page = context.new_page()   #page层，后面定位元素会用到

    page.goto(url="")   #打开网页

如果有两个案例同时跑，pw1_baidu、pw2_baidu，那就是存在两个pw实例， 
但在一个session里面只允许出现一个实例，再去用的时候需要给它关掉，需要在用例尾部加上，pw.stop()
如果是同步方法，就是用这个操作


pw_baidu()  #直接运行


#异步方法，pw可以有多个
def pw_baidu():
    with sync_playwright() as pw:   #创建一个pw的实例
        browser = pw.chromium.launch(headless=fasle) #选择浏览器
        context =browser.new_context()  #创建上下文，设置分辨率大小
        page = context.new_page()   #page层，后面定位元素会用到
        page.goto(url="")   #打开网页
        #这里没有关闭，也可以让两个案例分别跑起来。
        #因为这个with可以帮助，在用例跑完/失败后，将用例退出来
        