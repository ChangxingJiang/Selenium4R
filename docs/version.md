## V0.0.1 - V0.0.3

> 【Demo】第一个发布版本

**增强功能：**

1. 增加对POST请求的支持
2. 增加自动下载并缓存WebDriver可执行文件的功能，使Chrome更新不再是烦恼（`webdriver_manager`支持）

**调整功能：**

1. 没有定位到标签不再返回异常，而是返回指定的默认值
2. 支持多种形式的`executable_path`参数，兼容ChromeDriver可执行文件路径、`chromedriver`环境变量和ChromeDriver缓存地址

**一些小改动：**

1. 移除了`find_element`和`find_elements`方法中`by`参数的默认值（ID），以免在调用方法时因为不知道存在默认值而造成困扰