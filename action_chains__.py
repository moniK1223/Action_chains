'''

ACTION CHAINS : To handle the low level operations(mouse and keyboard operations) we use Action chains
    eg : mouse hovering, drag drop, double click, right click,...
First we have to import action chains
--> from selenium.webdriver.common.action_chains import ActionChains
        action_chains --> module
        ActionChains --> class
'''
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts)
action_chain_object = ActionChains(driver)


#-----------------------------------------------------------------------------
# ## mouse hovering
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# element1 = driver.find_element('xpath', '//a[text()="Home & Living"]')
# action_chain_object.move_to_element(element1).perform()
# time.sleep(2)
#
# element2 = driver.find_element('xpath', '//a[text()="Men"]')
# action_chain_object.move_to_element(element2).perform()


#-------------------------------------------------------------------------------
## double click operation

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# element = driver.find_element('xpath', '//button[text()="Copy Text"]')
# action_chain_object.double_click(element).perform()
# time.sleep(2)
#
# ele2 = driver.find_element('xpath', '//label[text()="Name:"]')
# action_chain_object.double_click(ele2).perform()

#-------------------------------------------------------------------------------
# ## right click
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# element = driver.find_element('xpath', '//label[text()="Name:"]')
# action_chain_object.context_click(element).perform()

#-------------------------------------------------------------------------------
## scrolling operations

# ## scrolling to a specific element
# driver.get('https://www.myntra.com/')
# time.sleep(3)
#
# element = driver.find_element('xpath', '//a[text()=" ONLINE SHOPPING "]')
# action_chain_object.scroll_to_element(element).perform()

## scrolling using keys
# driver.get('https://www.myntra.com/')
# time.sleep(3)
#
# action_chain_object.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.PAGE_DOWN).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.PAGE_UP).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.ARROW_DOWN).perform()
# time.sleep(2)
# action_chain_object.send_keys(Keys.ARROW_UP).perform()

#----------------------------------------------------------------------------------------
## To scroll down till the end of the page
# driver.get('https://www.myntra.com/')
# time.sleep(3)
#
# ## will scroll till the end of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(3)
#
# ## scrolling back to the top
# driver.execute_script("window.scrollTo(0, -document.body.scrollHeight)")


#---------------------------------------------------------------------------------------
## To select everything on web application
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# action_chain_object.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()

#---------------------------------------------------------------------------------------
## drag and drop
##
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# element = driver.find_element('xpath', '//h2[text()="Frames"]')
# action_chain_object.scroll_to_element(element).perform()
# time.sleep(2)
#
# draggable_ele = driver.find_element('xpath', '//div[@id="draggable"]')
# droppable_ele = driver.find_element('xpath', '//div[@id="droppable"]')
#
# action_chain_object.drag_and_drop(draggable_ele, droppable_ele).perform()

#------------------------------------------------------------------------------------

## ASSIGNMENT
## 1. Go to http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html, drag and drop


#--------------------------------------------------------------------------------------
## slider

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(3)
#
# element = driver.find_element('xpath', '//h2[text()="Frames"]')
# action_chain_object.scroll_to_element(element).perform()
# time.sleep(2)
#
# slider = driver.find_element('xpath', '//div[@id="slider"]')
# action_chain_object.click_and_hold(slider).move_by_offset(20, 0).release().perform()

#---------------------------------------------------------------------------------------

# driver.get('https://www.flipkart.com/')
# driver.find_element('xpath', '//input[@name="q"]').send_keys('Phone')
#
# search_ele = driver.find_element('xpath', '//button[@type="submit"]')
# action_chain_object.send_keys_to_element(search_ele, Keys.ENTER).perform()
#
# start_slider_val = driver.find_element('xpath','//div[@class="_3FdLqY"]')
# action_chain_object.click_and_hold(start_slider_val).move_by_offset(30, 0).perform()
#
# end_slider_val = driver.find_element('xpath','(//div[@class="_3FdLqY"])[2]')
# action_chain_object.click_and_hold(end_slider_val).move_by_offset(0, 10).perform()

#----------------------------------------------------------------------------------------

# import time
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
# action_chain_object = ActionChains(driver)
# driver.get('https://www.flipkart.com/')
# time.sleep(3)
# driver.find_element('xpath', '//input[@title="Search for Products, Brands and More"]').send_keys('Dress')
# time.sleep(2)
# driver.find_element('xpath', '//button[@title="Search for Products, Brands and More"]').click()
# time.sleep(2)
# element = driver.find_element('xpath', '//div[text()="Customer Ratings"]')
# action_chain_object.scroll_to_element(element).perform()
# slider = driver.find_element('xpath', '//div[@class="_2IN3-t _1mRwrD"]')
# action_chain_object.click_and_hold(slider).move_by_offset(20, 0).release().perform()
# action_chain_object.scroll_to_element(element).perform()
# action_chain_object.click_and_hold(slider).move_by_offset(0, 10).release().perform()


#_----------------------------------------------------------------------------------

## drag and drop assignment

# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# time.sleep(3)
#
# capitals_list = []
# capitals = driver.find_elements('xpath', '//div[@id="dropContent"]//div')   ## ['', w1,'',  w2,'',  w3, w4,..]
# for ele in capitals:
#     capitals_list.append(ele.text)
#
# countries_list = []
# countries = driver.find_elements('xpath', '//div[@id="countries"]//div')    ## [w1, w2, w3, w4,..]
# for ele in countries:
#     countries_list.append(ele.text)
#
# print(capitals_list)    ## ['', 'Oslo', '', 'Stockholm', '', 'Washington', '', 'Copenhagen', '', 'Seoul', '', 'Rome', '', 'Madrid']
# print(countries_list)   ## ['Italy', 'Spain', 'Norway', 'Denmark', 'South Korea', 'Sweden', 'United States']
#
#
# for city, country in zip(capitals[1::2], countries):
#     action_chain_object.drag_and_drop(city, country).perform()
#     time.sleep(1)

## The above code doesnt work as per the requirement

#----------------------------------------------------------------------------
#
# driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
# time.sleep(3)
#
# for i in range(1, 8):
#     draggable_ele = driver.find_element('xpath', f'//div[@id="box{i}"]')
#     droppable_ele = driver.find_element('xpath', f'//div[@id="box10{i}"]')
#
#     action_chain_object.drag_and_drop(draggable_ele, droppable_ele).perform()
#     time.sleep(1)





































































































































