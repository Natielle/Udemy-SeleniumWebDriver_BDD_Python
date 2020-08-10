__author__ = 'Reinaldo Mateus Rossetti Junior'
from helpers.driver import WebDriver
from modules.process_and_files import Process


def set_browser(browser):

    browser = browser.lower()
    if browser == "firefox":
        set_job("server_firefox.bat")
        desired_capabilities = {'browserName': 'firefox', 'marionette': True}
        command_executor = "http://127.0.0.1:5559/wd/hub"
        driver = WebDriver(desired_capabilities=desired_capabilities, command_executor=command_executor)
        return driver

    elif browser == "chrome":
        set_job("node_chrome.bat")
        desired_capabilities = {'browserName': 'chrome'}
        command_executor = "http://127.0.0.1:5556/wd/hub"
        driver = WebDriver(desired_capabilities=desired_capabilities, command_executor=command_executor)
        return driver

    elif browser == "ie":
        #set_job("server_IE.bat")
        desired_capabilities = {'browserName': 'ie'}
        #command_executor = "http://127.0.0.1:5555/wd/hub" , command_executor=command_executor
        driver = WebDriver(desired_capabilities=desired_capabilities)
        return driver


def set_job(browser):
    test = Process()
    test.run_process("",browser)
