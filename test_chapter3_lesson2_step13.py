from selenium import webdriver
import unittest
import time

class TestCh3L2S13(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstNameInput = browser.find_element_by_css_selector("div.first_block div.first_class input.first")
        firstNameInput.send_keys("Ivan")
        lastNameInput = browser.find_element_by_css_selector("div.first_block div.second_class input.second")
        lastNameInput.send_keys("Petrov")
        emailInput = browser.find_element_by_css_selector("div.first_block div.third_class input.third")
        emailInput.send_keys("ivan@petrov.ya")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_css_selector("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual (welcome_text, "Congratulations! You have successfully registered!", "Welcome text is correct")
        time.sleep(5)
        browser.quit()
    
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        firstNameInput = browser.find_element_by_css_selector("div.first_block div.first_class input.first")
        firstNameInput.send_keys("Ivan")
        lastNameInput = browser.find_element_by_css_selector("div.first_block div.second_class input.second")
        lastNameInput.send_keys("Petrov")
        emailInput = browser.find_element_by_css_selector("div.first_block div.third_class input.third")
        emailInput.send_keys("ivan@petrov.ya")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element_by_css_selector("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual (welcome_text, "Congratulations! You have successfully registered!", "Welcome text is correct")
        time.sleep(5)
        browser.quit()

if __name__ == "__main__":
    unittest.main()