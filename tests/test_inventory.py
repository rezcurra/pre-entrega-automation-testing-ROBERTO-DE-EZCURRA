from utils.helpers import login_usuario
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_inventory(driver):
    # Autenticación usando el helper
    login_usuario(driver, 'standard_user', 'secret_sauce')
    wait = WebDriverWait(driver, 10)
    
    # Verificación de título de pestaña
    assert driver.title == "Swag Labs"
    
    # Comprobación de presencia de productos
    products = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))
    assert len(products) > 0
    
    # Validación del nombre y precio del primer producto (índice 0)
    first_product_name = products[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert first_product_name == "Sauce Labs Backpack"
    
    first_product_price = products[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    assert first_product_price == "$29.99"
    
    # Comprobación de visibilidad de menú y filtro de productos
    menu = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
    assert menu.is_displayed()
    
    filter_dropdown = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    assert filter_dropdown.is_displayed()
