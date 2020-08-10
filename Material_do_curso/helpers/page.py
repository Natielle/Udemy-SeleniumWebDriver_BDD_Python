from time import sleep

import requests
from selenium.webdriver import ActionChains
from helpers.errors import WaitForElementError
from selenium.common.exceptions import NoAlertPresentException

#TODO create WaitForElementError class
"""
Class PageBase about talk by Dakota Smith at the Houston Python Web meetup on March 2nd 2015.
author: https://github.com/dakotasmith/page-object-examples
"""


class PageBase(object):

    timeout_seconds = 20
    sleep_interval = .25

    def __init__(self, driver):
        self.driver = driver
        self.WebElement = ""

    @property
    def referrer(self):
        return self.driver.execute_script('return document.referrer')

    def sleep(self, seconds=None):
        if seconds:
            sleep(seconds)
        else:
            sleep(self.sleep_interval)

    def find_element_by_locator(self, locator):
        return self.driver.find_element_by_locator(locator)

    def find_elements_by_locator(self, locator):
        return self.driver.find_elements_by_locator(locator)

    def wait_for_available(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_element_available(locator):
                break
            self.sleep()
        else:
            raise WaitForElementError('Wait for available timed out')
        return True

    def wait_for_visible(self, locator):
        for i in range(self.timeout_seconds):
            if self.driver.is_visible(locator):
                return True
            self.sleep()
        else:
            raise WaitForElementError('Wait for visible timed out')

    def wait_for_hidden(self, locator):
        for i in range(self.timeout_seconds):

            if self.driver.is_visible(locator):
                self.sleep()
            else:
                break
        else:
            raise WaitForElementError('Wait for hidden timed out')
        return True

    def wait_for_alert(self):
        for i in range(self.timeout_seconds):
            try:
                alert = self.driver.switch_to_alert()
                if alert.text:
                    break
            except NoAlertPresentException:
                pass
            self.sleep()
        else:
            raise NoAlertPresentException(msg='Wait for alert timed out')
        return True

    def _dispatch(self, l_call, l_args, d_call, d_args):
        pass

    def open(self, page_url):
        self.driver.set_page_load_timeout(30)
        request = requests.get(page_url)
        status_code = int(request.status_code)
        response_time = requests.get(page_url).elapsed.total_seconds()
        if status_code > 200:
            print("Pagina com error!\n status code: {}\n response time: {}".format(request.status_code, response_time))
            raise("Error")
        else:
            print("Pagina Carregada!\n status code: {}\n response time: {}".format(request.status_code, response_time))
            self.driver.get(page_url)
        return self.page_has_loaded()

    def submit(self, element):

        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_element_by_locator(element))
        actions.click(self.find_element_by_locator(element))
        actions.perform()
        return self.page_has_loaded()

    def close_browser(self):
        self.driver.close()
        self.driver.quit()

    def page_has_loaded(self):
        print("Checking if {} page is loaded.".format(self.driver.current_url))
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def type(self, element, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element_by_locator(element).click()
            if clear_first:
                self.find_element_by_locator(element).clear()
            self.find_element_by_locator(element).send_keys(value)
        except AttributeError:
            print('%s page does not have "%s" locator' % (self, element))
            return False
        return True


    def change_frame(self, frame):
        self.driver.switch_to.frame(frame)
