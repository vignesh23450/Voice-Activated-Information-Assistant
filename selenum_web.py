from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Info:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_info(self, query):
        self.query = query
        self.driver.get(url="http://www.wikipedia.org")
        
        try:
            search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
            search.click()
            search.send_keys(query)
            enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
            enter.click()
            
            # Keep the browser open until manually closed
            while True:
                time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            try:
                self.driver.quit()
            except:
                pass

#assist = Info()
#assist.get_info("star")
