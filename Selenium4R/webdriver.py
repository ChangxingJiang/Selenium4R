import os
import time
from typing import List

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

from .common.JavaScriptLibrary import JavaScriptLibrary
from .webelement import NodeElement
from .webelement import NoneElement


class Chrome(WebDriver):
    """Chrome浏览器驱动"""

    def __init__(self, use_chrome_account=None, cache_path=None,
                 executable_path="chromedriver", port=0, options=None, service_args=None,
                 desired_capabilities=None, service_log_path=None, keep_alive=True):
        """创建Chrome浏览器驱动实例

        启动服务，然后创建一个新的Chrome浏览器驱动实例

        用户参数：
        :param use_chrome_account: 本地Chrome浏览器中已登录的Google账号用户文件路径
        :param cache_path: 缓存地址(可能缓存ChromeDriver可执行文件和常用JavaScript库)

        原生参数：
        :param executable_path: Chrome浏览器的可执行文件路径 (默认 = 自动安装ChromeDriver)
        :param port: Chrome浏览器运行的端口 (默认 = 自动寻找一个空闲端口)
        :param options: ChromeOptions (设置参数实例)
        :param service_args: 服务参数
        :param desired_capabilities: 非浏览器功能设置
        :param service_log_path: Chrome浏览器服务日志路径
        :param keep_alive: 是否将ChromeRemoteConnection设置为 "HTTP keep-alive"
        """

        # 处理缓存地址
        self.cache_path = cache_path
        if not cache_path or not os.path.isdir(cache_path):
            self.cache_path = os.path.abspath("../Selenium4R2")
        if not os.path.exists(self.cache_path):
            os.makedirs(self.cache_path)
        if not os.path.exists(os.path.join(self.cache_path, "libraries")):
            os.makedirs(os.path.join(self.cache_path, "libraries"))

        # 设置options参数 (设置参数实例)
        if not options:
            options = Options()  # 构造Selenium控制的Chrome浏览器的设置对象

        # 移除浏览器中的“Chrome正受到自动测试软件的控制”标签
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # 配置Selenium忽略证书错误
        options.add_argument("--ignore-certificate-errors")

        # 设置Chrome浏览器的Google账号用户文件地址
        if use_chrome_account:
            options.add_argument("user-data-dir=" + use_chrome_account)

        # 下载并缓存ChromeDriver可执行文件
        if executable_path == "chromedriver" and "chromedriver" in os.environ:  # 处理读取环境变量的情况
            executable_path = os.environ["chromedriver"]
        if os.path.isfile(executable_path) and "river" in os.path.basename(executable_path):  # ChromeDriver可执行文件为路径的情况
            pass
        else:
            executable_path = ChromeDriverManager(path=cache_path).install()

        # 启动Selenium控制的Chrome浏览器
        super().__init__(executable_path=executable_path, port=port, options=options, service_args=service_args,
                         desired_capabilities=desired_capabilities, service_log_path=service_log_path,
                         keep_alive=keep_alive)

        # 移除网页中的window.navigator.webdriver属性
        self.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
        })

    def find_element(self, by=None, value=None) -> WebElement:
        """依据定位策略定位指定一个标签"""
        try:
            return NodeElement(super().find_element(by, value))
        except Exception as e:
            print("未找到标签:" + by + "=" + value + "(异常:" + e.__class__.__name__ + ")")
            return NoneElement()

    def find_elements(self, by=None, value=None) -> List[WebElement]:
        """依据定位策略定位符合条件的所有标签"""
        try:
            return [NodeElement(element) for element in super().find_elements(by, value)]
        except Exception as e:
            print("未找到标签:" + by + "=" + value + "(异常:" + e.__class__.__name__ + ")")
            return []

    def execute_script(self, script, *args):
        """执行JavaScript脚本代码"""
        try:
            converted_args = list(args)

            if self.w3c:
                command = Command.W3C_EXECUTE_SCRIPT
            else:
                command = Command.EXECUTE_SCRIPT

            return self.execute(command, {
                'script': script,
                'args': converted_args})['value']

        except Exception as e:
            print("执行JavaScript脚本代码失败:" + script + "(异常:" + e.__class__.__name__ + ")")
            return None

    def load_javascript_library(self, name: str):
        """载入JavaScript库"""
        if javascript_source := JavaScriptLibrary(self.cache_path).get(name):
            self.execute_script(javascript_source)

    def post(self, url, params=None, payload=False):
        """执行POST请求

        :param url: 请求的目标Url
        :param params: 请求传参
        :param payload: False为使用FormData传参(默认)，True为使用PayLoad传参
        :return: 请求的返回值
        """
        self.load_javascript_library("JQuery")  # 在当前页面中加载JQuery库

        # 将传参转换为Js对象
        if params:
            self.execute_script("window.req_data = %s;" % str(params))
        else:
            self.execute_script("window.req_data = {};")

        # 生成两种不同的传参方法的Ajax请求的Js代码
        if payload:  # 处理PayLoad传参方法
            js_ajax = "$.ajax('%s',{method:'POST',contentType:'application/json;charset=utf-8',data:JSON.stringify(window.req_data),success:function(res){window.req_res=res}});"
        else:  # 处理FormData传参方法
            js_ajax = "$.ajax('%s',{method:'POST',contentType:'application/x-www-form-urlencoded;charset=UTF-8',data:window.req_data,success:function(res){window.req_res=res}});"
        self.execute_script(js_ajax % url)

        # 等待Ajax请求的时间
        time.sleep(3)

        # 获取Ajax请求的结果
        return self.execute_script("return window.req_res;")
