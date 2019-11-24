import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_login_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")
    
    elemName = driver.find_element_by_name("username")
    elemName.send_keys("")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys("")

    elemPassword.send_keys(Keys.RETURN)

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/admin/login/?next=/admin/")

    elemName = driver.find_element_by_name("username")
    elemName.send_keys("John")

    elemPassword = driver.find_element_by_name("password")
    elemPassword.send_keys(" ")

    elemPassword.send_keys(Keys.RETURN)

