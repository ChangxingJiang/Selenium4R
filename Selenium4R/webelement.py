from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class NodeElement(WebElement):
    """非空DOM标签对象"""

    def __init__(self, element: "WebElement"):
        super().__init__(element.parent, element.id, element._w3c)

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


class NoneElement(WebElement):
    """空DOM标签对象"""

    def __init__(self):
        super().__init__(None, None)

    def __repr__(self):
        return "NoneElement"

    def __bool__(self):
        return False

    @property
    def tag_name(self):
        return None

    @property
    def text(self):
        return None

    def click(self):
        pass

    def submit(self):
        pass

    def clear(self):
        pass

    def get_property(self, name):
        return ""

    def get_attribute(self, name):
        return ""

    def is_selected(self):
        return False

    def is_enabled(self):
        return False

    def find_element_by_id(self, id_):
        return NoneElement()

    def find_elements_by_id(self, id_):
        return NoneElement()

    def find_element_by_name(self, name):
        return NoneElement()

    def find_elements_by_name(self, name):
        return NoneElement()

    def find_element_by_link_text(self, link_text):
        return NoneElement()

    def find_elements_by_link_text(self, link_text):
        return NoneElement()

    def find_element_by_partial_link_text(self, link_text):
        return NoneElement()

    def find_elements_by_partial_link_text(self, link_text):
        return NoneElement()

    def find_element_by_tag_name(self, name):
        return NoneElement()

    def find_elements_by_tag_name(self, name):
        return NoneElement()

    def find_element_by_xpath(self, xpath):
        return NoneElement()

    def find_elements_by_xpath(self, xpath):
        return NoneElement()

    def find_element_by_class_name(self, name):
        return NoneElement()

    def find_elements_by_class_name(self, name):
        return NoneElement()

    def find_element_by_css_selector(self, css_selector):
        return NoneElement()

    def find_elements_by_css_selector(self, css_selector):
        return NoneElement()

    def send_keys(self, *value):
        pass

    def is_displayed(self):
        return False

    @property
    def location_once_scrolled_into_view(self):
        return None

    @property
    def size(self):
        return {"height": 0, "width": 0}

    def value_of_css_property(self, property_name):
        return None

    @property
    def location(self):
        return None

    @property
    def rect(self):
        return None

    @property
    def screenshot_as_base64(self):
        return None

    @property
    def screenshot_as_png(self):
        return None

    def screenshot(self, filename):
        return False

    @property
    def parent(self):
        return None

    @property
    def id(self):
        return None

    def __eq__(self, element):
        return element is None or element.__class__.__name__ == "NoneElement"

    def __ne__(self, element):
        return not self.__eq__(element)

    def find_element(self, by=By.ID, value=None):
        return NoneElement()

    def find_elements(self, by=By.ID, value=None):
        return []

    def __hash__(self):
        return hash(self)
