from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
# als toegevoegd is aan "PATH":
#chrome_browser = webdriver.Chrome()

chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name('btn-default')
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_input = chrome_browser.find_element_by_id('user-message')
user_input.clear()
user_input.send_keys('Hallo allemaal, wat fijn dat je er bent')
show_message_button.click()
output_message = chrome_browser.find_element_by_id('display')

assert 'Hallo allemaal' in output_message.text

chrome_browser.close()
#chrome_browser.close()
#chrome_browser.quit()

