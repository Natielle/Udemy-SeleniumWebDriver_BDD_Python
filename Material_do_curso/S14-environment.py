from helpers.browser import set_browser
from helpers.page import PageBase
from time import sleep

"""
def before_all(context):
    context.driver = set_browser("chrome")
    context.page = PageBase(context.driver)
"""

def before_feature(context, feature):
    if "ignore" in feature.tags:
        feature.skip(reason="Feature not complete.")


def before_scenario(context, scenario):
    if "ignore" in scenario.tags:
        scenario.skip(reason="Bug in Test.")


def after_all(context):
    sleep(7)
    context.page.close_browser()


def before_scenario(context, scenario):
    if "chrome" in scenario.tags:
        context.driver = set_browser("chrome")
    elif "firefox" in scenario.tags:
        context.driver = set_browser("firefox")
    elif "ie" in scenario.tags:
        context.driver = set_browser("ie")

    context.page = PageBase(context.driver)


def after_step(context, step):
    if step.status == "failed":
        context.driver.get_screenshot_as_file \
            ('C:\\testlink_automation\\reports\\ \
            {}_{}.png'.format(step.name, step.status))
