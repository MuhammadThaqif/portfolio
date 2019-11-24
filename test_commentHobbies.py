import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_comment_hobbies():
     driver = webdriver.Chrome()
     driver.get("http://localhost:8000/blog/")
     driver.find_element_by_link_text("Hobbies").click()

     elemName = driver.find_element_by_name("author")

     elemComment = driver.find_element_by_name("body")

     elem.clear()
     elemName.send_keys(Keys.RETURN)
