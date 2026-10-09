from utils.helpers import login_usuario
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_login_exitoso(driver):
    # Inicio de sesión con credenciales válidas
    login_usuario(driver, 'standard_user', 'secret_sauce')
    
    wait = WebDriverWait(driver, 10)
    
    # Validación de redirección a /inventory.html
    wait.until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url
    
    # Aserción de presencia del logo 'Swag Labs'
    logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo")))
    assert logo.text == "Swag Labs"
    
    # Aserción de presencia del título 'Products'
    title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
    assert title.text == "Products"
