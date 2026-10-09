from utils.helpers import login_usuario
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_agregar_al_carrito(driver):
    # Autenticación usando el helper
    login_usuario(driver, 'standard_user', 'secret_sauce')
    wait = WebDriverWait(driver, 10)
    
    # Clic en agregar al carrito del primer producto
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_to_cart_btn.click()
    
    # Verificación del badge del carrito en '1'
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert badge.text == "1"
    
    # Navegación a '/cart.html'
    cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_link.click()
    wait.until(EC.url_contains("/cart.html"))
    
    # Validación de que el producto aparezca listado
    cart_item_name = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert cart_item_name.text == "Sauce Labs Backpack"
