#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[2]:


import pathes


# In[3]:


def pony_driver_init():
    driver = webdriver.Firefox(executable_path=pathes.driver_path)
    driver.get(pathes.url_path)
    try:
        title = WebDriverWait(driver, 10).until(
            EC.title_is('Пегас'))
    except:
        print('не загрузилось')
        driver.close()
        raise
    return driver


# In[4]:


def pony_login(driver):
    element_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'login')))
    element_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password")))
    enter_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "css-1hnkt5t")))
    element_login.send_keys(pathes.login)
    element_password.send_keys(pathes.password)
    enter_button.click()


# In[5]:


if __name__ == '__main__':
    driver = pony_driver_init()
    pony_login(driver)


# In[ ]:




