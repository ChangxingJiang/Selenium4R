from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class MyElement(WebElement):
    def __init__(self, element: "WebElement"):
        super().__init__(element.parent, element.id, element._w3c)

    def find_element_by_id(self, id_, default=None):
        return self.find_element(by=By.ID, value=id_, default=default)

    def find_elements_by_id(self, id_, default=None):
        return self.find_elements(by=By.ID, value=id_, default=default)

    def find_element_by_xpath(self, xpath, default=None):
        return self.find_element(by=By.XPATH, value=xpath, default=default)

    def find_elements_by_xpath(self, xpath, default=None):
        return self.find_elements(by=By.XPATH, value=xpath, default=default)

    def find_element_by_link_text(self, link_text, default=None):
        return self.find_element(by=By.LINK_TEXT, value=link_text, default=default)

    def find_elements_by_link_text(self, text, default=None):
        return self.find_elements(by=By.LINK_TEXT, value=text, default=default)

    def find_element_by_partial_link_text(self, link_text, default=None):
        return self.find_element(by=By.PARTIAL_LINK_TEXT, value=link_text, default=default)

    def find_elements_by_partial_link_text(self, link_text, default=None):
        return self.find_elements(by=By.PARTIAL_LINK_TEXT, value=link_text, default=default)

    def find_element_by_name(self, name, default=None):
        return self.find_element(by=By.NAME, value=name, default=default)

    def find_elements_by_name(self, name, default=None):
        return self.find_elements(by=By.NAME, value=name, default=default)

    def find_element_by_tag_name(self, name, default=None):
        return self.find_element(by=By.TAG_NAME, value=name, default=default)

    def find_elements_by_tag_name(self, name, default=None):
        return self.find_elements(by=By.TAG_NAME, value=name, default=default)

    def find_element_by_class_name(self, name, default=None):
        return self.find_element(by=By.CLASS_NAME, value=name, default=default)

    def find_elements_by_class_name(self, name, default=None):
        return self.find_elements(by=By.CLASS_NAME, value=name, default=default)

    def find_element_by_css_selector(self, css_selector, default=None):
        return self.find_element(by=By.CSS_SELECTOR, value=css_selector, default=default)

    def find_elements_by_css_selector(self, css_selector, default=None):
        return self.find_elements(by=By.CSS_SELECTOR, value=css_selector, default=default)

    def find_element(self, by=None, value=None, default=None):
        """依据定位策略定位指定一个标签"""
        try:
            return MyElement(super().find_element(by, value))
        except Exception as e:
            print("未找到标签:" + by + "=" + value + "(异常:" + e.__class__.__name__ + ")")
            return default

    def find_elements(self, by=None, value=None, default=None):
        """依据定位策略定位符合条件的所有标签"""
        try:
            return [MyElement(element) for element in super().find_elements(by, value)]
        except Exception as e:
            print("未找到标签:" + by + "=" + value + "(异常:" + e.__class__.__name__ + ")")
            return default if default is not None else []
