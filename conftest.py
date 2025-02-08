import pytest
from playwright.sync_api import Page,expect,sync_playwright

#这个conftest是pw默认存放装饰器的文件，公共的。跟这个文件同级或者子级，都可以调用这里面的装饰器
@pytest.fixture()  
def cecece():
    print("开始")
    yield        #用例开始前先执行输出【开始】，用例结束后，再执行输出【结束】
    print("结束") 

