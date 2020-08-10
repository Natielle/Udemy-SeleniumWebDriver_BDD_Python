from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement


class WebElement(SeleniumWebElement):
    def __init__(self, element):
        super(WebElement, self).__init__(element.parent, element.id)

    def find_element_by_locator(self, locator):
        locator_type, locator_value = locator.split('=', 1)
        if locator_type == 'class':
            return WebElement(self.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            return WebElement(self.find_element_by_css_selector(locator_value))
        elif locator_type == 'id':
            return WebElement(self.find_element_by_id(locator_value))
        elif locator_type == 'link':
            return WebElement(self.find_element_by_link_text(locator_value))
        elif locator_type == 'name':
            return WebElement(self.find_element_by_name(locator_value))
        elif locator_type == 'link':
            return WebElement(self.find_element_by_partial_link_text(locator_value))
        elif locator_type == 'tag':
            return WebElement(self.find_element_by_tag_name(locator_value))
        elif locator_type == 'xpath':
            return WebElement(self.find_element_by_xpath(locator_value))
        else:
            raise Exception('Invalid locator')

    def find_elements_by_locator(self, locator):
        locator_type, locator_value = locator.split('=')
        if locator_type == 'class':
            elements = self.find_elements_by_class_name(locator_value)
        elif locator_type == 'css':
            elements = self.find_elements_by_css_selector(locator_value)
        elif locator_type == 'id':
            elements = self.find_elements_by_id(locator_value)
        elif locator_type == 'link':
            elements = self.find_elements_by_link_text(locator_value)
        elif locator_type == 'name':
            elements = self.find_elements_by_name(locator_value)
        elif locator_type == 'link':
            elements = self.find_elements_by_partial_link_text(locator_value)
        elif locator_type == 'tag':
            elements = self.find_elements_by_tag_name(locator_value)
        elif locator_type == 'xpath':
            elements = self.find_elements_by_xpath(locator_value)
        else:
            raise Exception('Invalid locator')

        return [WebElement(e) for e in elements]

    def is_element_present(self, locator):
        try:
            self.find_element_by_locator(locator)
            return True
        except NoSuchElementException:
            return False

    def is_visible(self, locator):
        if self.is_element_present(locator):
            if self.find_element_by_locator(locator).is_displayed():
                return True
            else:
                return False
        else:
            return False

    def is_element_available(self, locator):
        if self.is_visible(locator):
            return True
        else:
            return False