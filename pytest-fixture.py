#pytest， 测试用例以test开头，可以用命令行执行

import pytest
from playwright.sync_api import Page,expect,sync_playwright

@pytest.fixture()  #现在这个装饰器只能在当前这个文件使用，其他文件是无法调用
def cecece():
    print("开始")
    yield        #用例开始前先执行输出【开始】，用例结束后，再执行输出【结束】
    print("结束")

@pytest.mark.only  #only自定义命名
def test_pw_select(page:Page,cecece): #调用装饰器，直接把方法名放进用例的参数中
    print('')

