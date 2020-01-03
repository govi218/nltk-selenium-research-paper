from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.webelement import FirefoxWebElement

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=r'/home/gov/bin/geckodriver')

with open('sitelist', 'r') as sites:
    for site in sites:
        driver.get(site)
        curr_line = ""
        try:
            elem = driver.find_element_by_xpath("//strong[text()='Contributors']/following::div")
            print('element.get_attribute(\'value\'): {0}'.format(elem.get_attribute('innerHTML')))
            curr_line += "{0}".format(elem.get_attribute('innerHTML'))
        except NoSuchElementException:
            print("Excepted: ", site)
        with open('contrib_blob', 'a+') as contribs:
            contribs.write(curr_line + '\n')

print("Headless Firefox Initialized")
driver.quit()
