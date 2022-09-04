from gettext import find
from lib2to3.pgen2 import driver
from select import select
from tkinter.tix import Select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

class TestAdmin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_search_admin_user(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("ADMIN") # isi username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"input.oxd-input:nth-child(1)").send_keys("admin")
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"button.oxd-button:nth-child(2)").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.CSS_SELECTOR,"span.oxd-text:nth-child(1)").text


        self.assertIn('Found', response_data)
    

    def test_b_edit(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("ADMIN") # isi username
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"div.oxd-form-row:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".oxd-button").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[6]/div/button[2]").click()
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        time.sleep(1)
        
        # validasi

        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5").text
        

        self.assertIn('Users', response_data)
        
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()