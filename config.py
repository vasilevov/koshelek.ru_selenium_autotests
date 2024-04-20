from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

