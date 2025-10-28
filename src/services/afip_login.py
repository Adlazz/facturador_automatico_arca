from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

class AFIPLogin:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.logger = logging.getLogger(__name__)

    def login(self, cuit, password, empresa):
        try:
            self.logger.info("Iniciando login en AFIP...")
            self.driver.get("https://auth.afip.gob.ar/contribuyente_/login.xhtml")

            # CUIT
            cuit_field = self.wait.until(EC.presence_of_element_located((By.ID, "F1:username")))
            cuit_field.clear()
            cuit_field.send_keys(cuit)

            siguiente_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "F1:btnSiguiente")))
            siguiente_btn.click()

            # PASSWORD
            password_field = self.wait.until(EC.presence_of_element_located((By.ID, "F1:password")))
            password_field.send_keys(password)

            ingresar_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "F1:btnIngresar")))
            ingresar_btn.click()

            time.sleep(5)

            # "Ver Todos"
            ver_todos_btn = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Ver todos")))
            ver_todos_btn.click()

            # "Comprobantes en Línea"
            comprobantes_btn = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//h3[contains(text(),'COMPROBANTES EN LÍNEA')]"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", comprobantes_btn)
            time.sleep(1)
            try:
                comprobantes_btn.click()
            except:
                self.driver.execute_script("arguments[0].click();", comprobantes_btn)

            time.sleep(5)
            self.driver.switch_to.window(self.driver.window_handles[-1])

            # Botón empresa
            empresa_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f"input.btn_empresa[value='{empresa}']"))
            )
            self.driver.execute_script("arguments[0].scrollIntoView(true);", empresa_btn)
            time.sleep(1)
            try:
                empresa_btn.click()
            except:
                self.driver.execute_script("arguments[0].click();", empresa_btn)

            self.logger.info("Login exitoso y acceso a Comprobantes en Línea completado")
            return True

        except Exception as e:
            self.logger.error(f"Error durante el login en AFIP: {str(e)}")
            self.driver.save_screenshot("error_login_afip.png")
            return False
