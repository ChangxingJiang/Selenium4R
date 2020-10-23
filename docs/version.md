## V0.1.2 (Beta)

> 发布时间：2020.10.23

**调整功能**

1. 空标签对象（`NoneElement`对象）的`get_property`方法和`get_attribute`不再返回`None`而是返回空字符串（`""`），使返回值与Selenium统一

## V0.1.0 - V0.1.1 (Beta)

> 发布时间：2020.10.16

**调整功能**

1. 没有定位到标签不再产生`NoSuchElementException`异常，而是返回指定的空标签对象（`NoneElement`对象），在继续使用该标签对象时不会报错而是返回指定的默认值

## V0.0.1 - V0.0.3 (Beta)

> 发布时间：2020.10.14

**增加功能**

1. 增加对POST请求的支持
2. 增加自动下载并缓存WebDriver可执行文件的功能，使Chrome更新不再是烦恼（`webdriver_manager`支持）
3. 没有定位到标签不再返回异常，而是返回指定的默认值
4. 支持多种形式的`executable_path`参数，兼容ChromeDriver可执行文件路径、`chromedriver`环境变量和ChromeDriver缓存地址
5. 移除了`find_element`和`find_elements`方法中`by`参数的默认值（ID），以免在调用方法时因为不知道存在默认值而造成困扰

