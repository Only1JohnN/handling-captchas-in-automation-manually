import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
    
def test_solve_captcha_manually(driver):
    
    #Get the webpage URL
    driver.get("https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php")
    
    
    # Clear and fill the input fields
    input_a = driver.find_element(By.NAME, "ex-a")
    input_b = driver.find_element(By.NAME, "ex-b")
    
    input_a.clear()
    input_b.clear()
    
    input_a.send_keys("Adeniyi")
    input_b.send_keys("John")
    
    
    # Pause for manual CAPTCHA solving 
    input("Please solve the CAPTCHA manually and press Enter to continue...")
    
    #Click the submit button
    submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
    
    #Wait for the page to load after the form submission
    driver.implicitly_wait(5)
    
    # Assert the success message is displayed
    success_message = driver.find_element(By.XPATH, "//body//main")
    assert success_message.is_displayed(), "Form submission failed, success message not found."