from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login_usuario(driver, username, password):
    """
    Navega a saucedemo.com e inicia sesión esperando que los campos sean visibles.
    """
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    
    username_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    username_field.clear()
    username_field.send_keys(username)
    
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password_field.clear()
    password_field.send_keys(password)
    
    login_button = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    login_button.click()
