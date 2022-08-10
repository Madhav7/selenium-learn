from selenium import webdriver
import urllib
# import urllib2
from time import sleep
from selenium.webdriver.common.by import By


url = "https://www.amazon.in/Ringke-Ergonomic-Transparent-Resistant-Protection/dp/B093Q3SHFB/ref=sr_1_3?crid=22RZ0SV1UTB5P&keywords=mi+11x+ringke&qid=1648981511&sprefix=mi+11x+ringk%2Caps%2C311&sr=8-3"

# url = "https://www.amazon.in/11X-Cosmic-Black-128GB-Storage/dp/B085J1QWFV/ref=sr_1_1?crid=271VEMIZWQZL0&keywords=mi%2B11x&qid=1648981330&sprefix=mi%2B11%2Caps%2C324&sr=8-1&th=1"


driver = webdriver.Firefox(executable_path = '/Users/niel/Downloads/fire-gecko/geckodriver')
driver.get(url)

timedelta = 15*60

# #now you can refresh the page!
# while True:
#     sleep(2)
#     driver.refresh()

price_block = driver.find_element(By.ID, "apex_desktop")

try:
    # table_cont_block = price_block.find_elements(By.XPATH, "//table[0]")
    # tbody_block = table_cont_block.find_element(By.XPATH, "//tbody")
    # tr_block = table_cont_block.find_element(By.XPATH, "//tr[1]")

    tr_block = price_block.find_element(By.XPATH, "//table/tbody/tr[2]")
    # print(tr_block.text)

except Exception as e:
    print(e)
    driver.quit()

item_price = tr_block.text.split('\n')[-1]

item_name = driver.find_element(By.ID, "title_feature_div").text

print(f"Item name is {item_name}" + "\n" +
f"Item cost is {item_price}")


driver.quit()
