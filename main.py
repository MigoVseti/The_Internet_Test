from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/")
#1
driver.find_element(By.LINK_TEXT, "Form Authentication").click()
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("ABC")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("ABC")
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example form:nth-child(3) button.radius:nth-child(3) > i.fa.fa-2x.fa-sign-in").click()

driver.get("https://the-internet.herokuapp.com/")
#2
driver.find_element(By.LINK_TEXT, "Drag and Drop").click()
source_element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
target_element = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]")
actions = ActionChains(driver)
actions.click_and_hold(source_element)
actions.move_to_element(target_element)
actions.release()
actions.perform()

driver.get("https://the-internet.herokuapp.com/")
#3
driver.find_element(By.LINK_TEXT, "Infinite Scroll").click()
start_time = time.time()
while time.time() - start_time < 5:
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(0.1)

driver.get("https://the-internet.herokuapp.com/")
#4
driver.find_element(By.LINK_TEXT, "Key Presses").click()
driver.find_element(By.CSS_SELECTOR, "#target").send_keys(Keys.CONTROL)
driver.find_element(By.CSS_SELECTOR, "#target").send_keys(Keys.ESCAPE)

driver.get("https://the-internet.herokuapp.com/")
#5
driver.find_element(By.LINK_TEXT, "Horizontal Slider").click()
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(1) div.sliderContainer:nth-child(3) > input:nth-child(1)").click()
actions = ActionChains(driver)
actions.send_keys(Keys.ARROW_RIGHT)
actions.perform()

driver.get("https://the-internet.herokuapp.com/")
#6
driver.find_element(By.LINK_TEXT, "Hovers").click()
actions = ActionChains(driver)
avatar = driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(2) div.figure:nth-child(5) > img:nth-child(1)")
link = driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(2) div.figure:nth-child(5) div.figcaption:nth-child(2) > a:nth-child(2)")
actions.move_to_element(avatar)
actions.click(link)
actions.perform()

driver.get("https://the-internet.herokuapp.com/")
#7
driver.find_element(By.LINK_TEXT, "Dropdown").click()
driver.find_element(By.CSS_SELECTOR, "#dropdown").click()
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(1) select:nth-child(2) > option:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(1) select:nth-child(2) > option:nth-child(3)").click()

driver.get("https://the-internet.herokuapp.com/")
#8
driver.find_element(By.LINK_TEXT, "Checkboxes").click()
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(1) form:nth-child(2) > input:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example:nth-child(1) form:nth-child(2) > input:nth-child(3)").click()

driver.get("https://the-internet.herokuapp.com/")
#9
driver.find_element(By.LINK_TEXT, "Inputs").click()
driver.find_element(By.CSS_SELECTOR, "div.row:nth-child(2) div.large-12.columns:nth-child(2) div.row div.large-6.small-12.columns.large-centered div.example:nth-child(2) > input:nth-child(2)").send_keys(Keys.NUMPAD9)

driver.get("https://the-internet.herokuapp.com/")
#10
driver.find_element(By.LINK_TEXT, "Multiple Windows").click()
driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.row:nth-child(2) div.large-12.columns:nth-child(2) div.example > a:nth-child(2)").click()

driver.quit()
