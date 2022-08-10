from selenium import webdriver
import urllib
# import urllib2
from time import sleep

driver = webdriver.Firefox(executable_path = '/Users/niel/Downloads/fire-gecko/geckodriver')
driver.get("https://in.usembassy.gov/visas/immigrant-visas/scheduling-appointments/")

timedelta = 15*60

# #now you can refresh the page!
# while True:
#     sleep(2)
#     driver.refresh()
