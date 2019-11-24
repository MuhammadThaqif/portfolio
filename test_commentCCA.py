import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_comment_cca():
     driver = webdriver.Chrome()
     driver.get("http://localhost:8000/blog/")
     driver.find_element_by_link_text("CCA activites").click()

     elemName = driver.find_element_by_name("author")

     elemComment = driver.find_element_by_name("body")

     elem.clear()
     elemName.send_keys(Keys.RETURN)

def test_comment_blank():
     driver = webdriver.Chrome()
     driver.get("http://localhost:8000/blog/")
     driver.find_element_by_link_text("CCA activites").click()

     elemName = driver.find_element_by_name("author")
     elemName.send_keys("Stacy")


     elemName.send_keys(Keys.RETURN)

def test_comment_filled():
     driver = webdriver.Chrome()
     driver.get("http://localhost:8000/blog/")
     driver.find_element_by_link_text("CCA activites").click()

     elemName = driver.find_element_by_name("author")
     elemName.send_keys("Stacy")

     elemName = driver.find_element_by_name("body")
     elemName.send_keys("Testing123")
     elemName.send_keys(Keys.RETURN)
