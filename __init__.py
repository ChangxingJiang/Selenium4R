"""
魔改版Selenium（当前仅支持Chrome版）

希望让Selenium的操作更简便，更适合没有软件工程经验的研究者；增强了一些常用功能，并内置了一些异常的处理方法

功能增强：
1. 支持POST请求
2. 自动下载适应当前系统和Chrome版本的ChromeDriver文件（webdriver_manager包支持）

修改内容：
1. 没有定位到标签不再返回异常，而是返回None
"""

from .WebDriver import Chrome
from .common.JavaScriptLibrary import JavaScriptLibrary
