from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('/home/subhodeep/Documents/python/automation_testing/chromedriver')
driver.get("file:///home/subhodeep/Documents/minor-project/test/index.html")

driver.implicitly_wait(30)

driver.maximize_window()

element_to_hover = driver.find_element_by_xpath("/html/body/nav/div/button")
hover = ActionChains(driver).move_to_element(element_to_hover)
hover.perform()

driver.close()