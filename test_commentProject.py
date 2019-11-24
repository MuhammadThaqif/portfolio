import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_comment_project():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")

    elemComment = driver.find_element_by_name("body")

    elem.clear()
    elemName.send_keys(Keys.RETURN)


def test_comment_blank():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("John")


    elemName.send_keys(Keys.RETURN)

def test_comment():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/blog/")
    driver.find_element_by_link_text("Projects done").click()

    elemName = driver.find_element_by_name("author")
    elemName.send_keys("John")

    elemComment = driver.find_element_by_name("body")
    elemComment.send_keys("Test")

 
    elemName.send_keys(Keys.RETURN)
