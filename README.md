# Selenium for Researcher (魔改版Selenium)

> 以简化操作为宗旨，服务没有编程经验的研究者

## 安装

```
pip install Selenium4R
```

## 基本介绍

希望通过魔改使Selenium的操作更简便，让编程经验的研究者可以更方便地开发Selenium爬虫。为此，我们增强了一些常用的功能，并内置了一些异常的处理方法（当前仅支持Chrome版本）

**增加功能：**

1. 增加对POST请求的支持
2. 增加自动下载并缓存WebDriver可执行文件的功能，使Chrome更新不再是烦恼（`webdriver_manager`支持）

**调整功能：**

1. 没有定位到标签不再产生`NoSuchElementException`异常，而是返回空标签对象（`NoneElement`）；空标签对象的属性均为空，在空标签对象中定位任何对象的返回值均为空标签对象
2. 支持多种形式的`executable_path`参数，兼容ChromeDriver可执行文件路径、`chromedriver`环境变量和ChromeDriver缓存地址

**一些小改动：**

1. 移除了`find_element`和`find_elements`方法中`by`参数的默认值（ID），以免在调用方法时因为不知道存在默认值而造成困扰

**待完成功能：**

1. 调整Selenium设置方法，可通过UserOption自行设置

版本：0.0.3（当前版本暂未正式发布，下一个版本不一定会考虑兼容当前版本）

## 用法

## 作者

ChangXing 长行

## 支持

如果觉得这个项目可以帮到您，欢迎星标哦。

