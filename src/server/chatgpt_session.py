from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import os
import subprocess
import sys

# from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium import webdriver


def start(emailTxt, passwordTxt):
    subprocess.Popen(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome','--headless','--remote-debugging-port=9222','--user-data-dir=chromedata'],stdout = subprocess.PIPE, stderr = subprocess.PIPE)

    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = uc.Chrome(options=options)
    driver.get("https://chat.openai.com/chat")

    WebDriverWait(driver, 20).until( \
            EC.visibility_of_element_located( \
                    (By.XPATH, "//*[text()='Log in']"))).click()

    WebDriverWait(driver, 20).until( \
            EC.visibility_of_element_located( \
                    (By.XPATH, "//*[text()='Continue with Google']"))).click()

    email=WebDriverWait(driver, 20).until( \
            EC.visibility_of_element_located( \
                    (By.CSS_SELECTOR, "input[type='email']")))
    email.click()
    email.send_keys(emailTxt)

    driver.find_element(By.XPATH, "//*[text()='Next']").click()

    WebDriverWait(driver, 20).until( \
            EC.visibility_of_element_located( \
                    (By.CSS_SELECTOR, "input[type='password']"))) \
                        .send_keys(passwordTxt)

    driver.find_element(By.XPATH, "//*[text()='Next']").click()
    driver.set_window_size(10,10)

    return driver

