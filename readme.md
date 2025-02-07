#页面元素定位方法

1、fill文本框输入，例如：登录文本框
page.fill('input[type="text"]', username)    
page.fill('input[type="password"]', str(password))
- xpath写法
//input[@type="text"]  
遇到文本框没有提示词的，可以直接拿xpath
page.fill('//*[@id="el-id-4305-243"]','点检')
- 查看页面中该文本数量
page.get_by_text("状态监视").count()    
- class写法定位
假设<div data-v-76680a84="" class="avatar-img">
page.locator（".avatar-img"）

2、f12定位组件后，ctrl+f查找该参数是否唯一
举例：账号输入框，显示为type="text"
先断电调试启动登录页
在搜索框输入xpath表达式：//input[@type="text"]，查询后看后面显示共一个，表示唯一
再去IDE中对表达式进行求值，输入page.locator('//input[@type="text"]').fill("superadmin")
然后求值，提示none，说明是成功的，会在页面中的账号输入框中写入superadmin

3、大写的一般是类的名称，小写的是函数或者方法

4、断言 expect（软断言，会自动等待）  assert（判断逻辑，断言失败立即终止测试）
可以采用getbytext
expect(page.get_by_text("状态监视")).to_be_visible()  判断页面中是否有"状态监视"这四个字
同理，可以作为判断是否新增成功，弹出的“提交成功”弹窗
toHaveCount(1)，断言某个元素的数量正好等于1

5、将跑用例录屏
在pytest.ini中加参数   --video=on
会生成一个视频，直接丢进新开的浏览器播放

6、录制用例编译出代码
在终端输入  playwright open  
可以一定程度上辅助定位元素，但不是百分百都有用

7、点击次数
遇到需要双击才能跳转的，使用click(click_count=2)，默认1
page.get_by_text("6号").click(click_count=2)  #点击次数
或者是dblclick

8、出现页面性能加载过慢无法断言成功
加一个参数wait_until="networkidle"，在500毫秒之内都没新的请求才会退出这个操作
实例：page.goto("#/login",wait_until="networkidle") 
9、悬浮
可以用来验证登录账号是否和个人中心一致
page.locator('.avatar-img').hover()
expect(page.get_by_text("小葵花")).to_be_visible()

10、下拉框选择
一般就是先定位下拉框，找下class是不是唯一，点击后再去写一条选择的语句
page.get_by_text("历史回放").click()  
expect(page.get_by_text("回放机构状态")).to_be_visible()
page.locator(".el-select__selection").click()  
page.get_by_text("7号").click()

11、input定位灰色提示词
可以定位输入框中的提示语
page.get_by_placeholder("模糊搜索关键词(回车查询)").fill("电源断路器")

12、失焦
像新增的功能，选择时间后可以用失焦
page.get_by_placeholder("模糊搜索关键词(回车查询)").blur()

13、switch 开关（开启/关闭）
常用xpath，查看页面元素，看是不是唯一的，
page.locator（“xpath书写"）.click（）

14、上传附件
通常是定位点击上传的范围
[图片]
用xpath书写：input[@type="file"]
page.locator('//input[@type="file"]').set_input_files('pytest.ini') #这块是上传当前项目根路径下的文件
断言是否上传成功，expect(page.get_by_text("pytest.ini上传成功")).to_be_visible()

15、下载

16、拖拽

17、角色定位
1、常规角色定位，定位后的父级显示role=，用于点击后的二次确认弹窗
page.get_by_role("dialog")
2、复选框的定位也可以使用角色定位，用于断言是否选中，假设选中，checked=True，count就为0
page.get_by_role("checkbox",name="全部",checked=True).count()
3、使用set_checked（True/Flase），表示点击后再点击

18、重复组件如何精准定位
1、观察重复组件有无大范围的相同名称，定位后采用关键词定位
2、使用count()来校验数量
3、进行常规的模拟操作
案列：任务看板中有多个新建，无法定位
page.locator(".panel").filter(has_text="维修").get_by_text("新建").click()
expect(page.get_by_text("新建任务")).to_be_visible()  #断言是否真的触发了新建
是否可见：to_be_visible()

19、根据文本定位
文本定位(包含，如果是精准定位要加exact=True）
page.get_by_text("登录").click()
page.get_by_text("请选择",exact=True).click()
断言时可以采用expect(page.locator(".panel")).to_have_count(3)

20、根据标签定位
#适用于没有提示文字的表单输入框
原理是表单的结构是组合形式，字段和输入框使用的lable：forID是一样的；相当于直接定位输入框
page.get_by_label("项目").fill("测试")   
#常规的一般都会有提示文字，所以直接用placeholder

21、回车查询
page.keyboard.press('Enter')


22、css选择器
id：locator.(""). 
class： 
如果某个div class="6666"
css可以直接用.6666，在html中找到

23、xpath选择器
单斜杠/ 代表是层级
双斜杠// 代表是全局

//input[@id='hahahaha']
只有属性才需要@

像网页中某个值，是div的
//div[text()="关键词"]

如果是包含关系，可以用contains
//div[contains(text(),"关键词")]

逻辑运算找元素
1、并列
//div[@data][text()='']

2、不包含 not

3、管道符 |
可以让两个元素都被找到

##轴定位
1、parent，父节点
如果一个大框里有很多子类，你先找到了子类，然后用/parent::div，就可以找到这个子类上面紧邻的一个div
//div[@class=]/parent::div

2、ancestor，祖先节点
除了能找到父节点，也能找的父节点的父节点
//div[@class=]/ancestor::div

3、following，找到当前元素之后的所有节点，位置比它低
//div[@class=]/following::*，所有的之后节点都会算上

4、following-sibling，找到当前元素之后的所有兄弟节点，就是在同个父节点下的
例子：li一般有很多个，如果用following-sibling，就能找到同个模块下所有的li

//li[@data-index="5"]/following-sibling::li

5、preceding ，找到当前元素之前的节点，位置比他高
6、preceding-sibling，和following同理，找到元素之前的兄弟节点

7、last(),用在兄弟节点较多的情况，寻找倒数第一个元素
//li[@aria-lable="查看更多"][last()]，如果是倒数第二个[last()-1],没有first，直接用[1]



24、filter过滤器
如果按照行，提取相同元素，多行的情况，可以提取关键词
page.locator('共同元素').filter(has_text="工业品") #这时候是把含有工业品那一行获取到
.get_by_role("link")#用角色找link .all_text_contents #这是个求值得到link这个列表的内容 [-1]=="关键词"#找到这个列表的最后一个

#has_not_text  
#has  包含那个locator   has=page.locator("//a[text()='关键词']") 

25、and or  visible
page.get_by_text("关键词").and_(page.get_by_role("link")) #既满足前半部分，又满足后半部分

page.get_by_text("关键词").and_(page.get_by_role("link")).or_(page.locator("#qq"))
拆分开：locator1=page.get_by_text("关键词").and_(page.get_by_role("link"))
       locator2=or_(page.locator("#qq"))
意思就是，先找1，如果没有就找2
如果是用是否可见，is_to_be_visible,其中一个找到就是true
如果是用to_have_count,返回最终匹配到的 Locator 的数量。

26、visible 可见的  想定位显示的
page.get_by_text("关键词").locator("visible=true")  #过滤掉我们看不见的元素

27、nth 
page.locator('[@aria-lable="查看更多"]').nth(0) 和first同理  nth(-1)=last

28、frame
 