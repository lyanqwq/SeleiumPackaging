#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TestElement.py
# @Author: lyan
# @Time  : 2022/7/31 16:56

from selenium import webdriver
from selenium.webdriver.common.by import By

def Element(driver, *loc):
    element = driver.find_element(*loc)
    return element


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    Element(driver, By.ID, 'kw').send_keys("hahah")
    Element(driver, By.ID, 'su').click()