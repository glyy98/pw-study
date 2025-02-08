#效率
1、并发：pytest-xdist/执行端-单机/多机
2、避免强制等待
3、预置数据和数据准备方式：ui/接口

#稳定
1、根据被测对象设计的等待-函数（方法）级/
2、重试机制-用例级（失败了就多执行几次）/函数（方法）级【对某个动作做重试机制】
3、隔离+闭环-自带隔离（尽量不让用例之间有关系）/设计能自愈的自动化用例

#功能
1、登录持久化-并发下的登录处理/登录状态的判断和处理
2、user data的持久化-减少数据请求量-使用命令行参数控制
3、多context的使用-用户交互（a提交审批-b收到通知）
4、数据类的使用-数据层-标准化/数据的处理更灵活/方便从其他渠道收集数据做数据驱动
5、其他功能
全局mock
全局接口监听
不定期弹窗处理
har记录和分析
基于locust的性能测试


#维护
1、pom封装
basepage封装：1、pom类基本框架的定义 2、表格 3、表单 4、通用封装
baselocators的封装：常见的locator封装
各个页面的封装：元素定位/方法/细粒度（需要根据业务去分析）

2、中文标识符
模块/类/函数(方法)/变量/   可以汉化

3、日志和报告
allure的植入
截图录像和tracing-log策略
console日志下的输出

4、配置
配置文件（pytest.ini）
pytest命令行参数-官方/自定义

5、持续集成
Jenkins的对接
企业通讯工具的对接（飞书）