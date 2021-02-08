from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
desired_cap = {
 'os_version': '10',
 'resolution': '1920x1080',
 'browser': 'Chrome',
 'browser_version': 'latest',
 'os': 'Windows',
 'browserstack.debug': True,
 'name': 'BStack-[Python] Sample Test',
 'build': 'Azure CI integration',
 'browserstack.user': os.getenv("BROWSERSTACK_USERNAME"),
 'browserstack.key': os.getenv("BROWSERSTACK_ACCESS_KEY"),
 'browserstack.local': os.getenv("BROWSERSTACK_LOCAL"),
 'browserstack.localIdentifier': os.getenv("BROWSERSTACK_LOCAL_IDENTIFIER")
}
driver = webdriver.Remote(
    command_executor='https://hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("BrowserStack")
elem.submit()
print(driver.title)
# Setting the status of test as 'passed' or 'failed' based on the condition; if title of the web page starts with 'BrowserStack'
if (driver.title[:12]=="BrowserStack"):
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Title matched!"}}')
else:
	driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Title not matched"}}')
driver.quit() 