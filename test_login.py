import unittest
import time
import os
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import HtmlTestRunner

# Configuración de directorios para los reportes y capturas de pantalla
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(CURRENT_DIR, "screenshots")
REPORT_DIR = os.path.join(CURRENT_DIR, "reports")

# Crear directorios si no existen
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)
if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

class LoginTests(unittest.TestCase):
    """
    Pruebas de automatización para la página de login de The Internet Herokuapp
    """
    
    def setUp(self):
        """Configuración inicial antes de cada prueba"""
        # Configuración del WebDriver usando webdriver_manager para gestionar el driver automáticamente
        options = Options()
        options.add_argument("--start-maximized")  # Maximizar ventana
        
        # Usar webdriver_manager para gestionar el chromedriver automáticamente
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        
        # URL base para las pruebas
        self.base_url = "https://the-internet.herokuapp.com/login"
        
        # Credenciales válidas según la documentación del sitio
        self.valid_username = "tomsmith"
        self.valid_password = "SuperSecretPassword!"
        
    def tearDown(self):
        """Limpieza después de cada prueba"""
        if self.driver:
            self.driver.quit()
    
    def take_screenshot(self, test_name):
        """Toma una captura de pantalla y la guarda con el nombre del test y timestamp"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join(SCREENSHOT_DIR, filename)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")  # Añadir log para verificar
        return screenshot_path
    
    def test_001_successful_login(self):
        """
        Historia de Usuario 1: Como usuario registrado, quiero poder iniciar sesión con credenciales válidas
        para acceder a mi área segura.
        
        Criterio de aceptación: El sistema debe permitir el acceso y mostrar un mensaje de éxito.
        Criterio de rechazo: El sistema no permite el acceso o no muestra el mensaje de éxito.
        """
        self.driver.get(self.base_url)
        self.take_screenshot("test_001_inicio")
        
        # Ingresar credenciales válidas
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username_field.send_keys(self.valid_username)
        password_field.send_keys(self.valid_password)
        self.take_screenshot("test_001_credenciales_ingresadas")
        
        login_button.click()
        
        # Verificar login exitoso
        try:
            success_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
            )
            self.assertIn("You logged into a secure area!", success_message.text)
            self.take_screenshot("test_001_login_exitoso")
        except (TimeoutException, NoSuchElementException) as e:
            self.take_screenshot("test_001_error")
            self.fail(f"No se pudo completar el login exitoso: {str(e)}")
    
    def test_002_invalid_username(self):
        """
        Historia de Usuario 2: Como sistema de seguridad, quiero validar las credenciales de los usuarios
        para evitar accesos no autorizados.
        
        Criterio de aceptación: El sistema debe rechazar el acceso con un nombre de usuario incorrecto y mostrar un mensaje de error.
        Criterio de rechazo: El sistema permite el acceso con un nombre de usuario incorrecto o no muestra un mensaje de error claro.
        """
        self.driver.get(self.base_url)
        self.take_screenshot("test_002_inicio")
        
        # Ingresar usuario inválido
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username_field.send_keys("usuario_incorrecto")
        password_field.send_keys(self.valid_password)
        self.take_screenshot("test_002_credenciales_ingresadas")
        
        login_button.click()
        
        # Verificar mensaje de error
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
            )
            self.assertIn("Your username is invalid!", error_message.text)
            self.take_screenshot("test_002_error_validacion")
        except (TimeoutException, NoSuchElementException) as e:
            self.take_screenshot("test_002_error")
            self.fail(f"No se mostró el mensaje de error esperado para usuario inválido: {str(e)}")
    
    def test_003_invalid_password(self):
        """
        Historia de Usuario 3: Como usuario registrado, quiero recibir retroalimentación clara
        cuando ingrese una contraseña incorrecta.
        
        Criterio de aceptación: El sistema debe mostrar un mensaje específico cuando la contraseña es incorrecta.
        Criterio de rechazo: El sistema no diferencia entre problemas de usuario y contraseña o muestra mensajes genéricos.
        """
        self.driver.get(self.base_url)
        self.take_screenshot("test_003_inicio")
        
        # Ingresar contraseña inválida
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username_field.send_keys(self.valid_username)
        password_field.send_keys("contraseña_incorrecta")
        self.take_screenshot("test_003_credenciales_ingresadas")
        
        login_button.click()
        
        # Verificar mensaje de error específico para contraseña
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
            )
            self.assertIn("Your password is invalid!", error_message.text)
            self.take_screenshot("test_003_error_validacion")
        except (TimeoutException, NoSuchElementException) as e:
            self.take_screenshot("test_003_error")
            self.fail(f"No se mostró el mensaje de error esperado para contraseña inválida: {str(e)}")
    
    def test_004_empty_fields(self):
        """
        Historia de Usuario 4: Como sistema de validación, quiero verificar que todos los campos obligatorios
        estén completos antes de procesar un inicio de sesión.
        
        Criterio de aceptación: El sistema debe mostrar un mensaje de error cuando no se completan los campos.
        Criterio de rechazo: El sistema procesa el formulario incompleto sin avisar al usuario.
        """
        self.driver.get(self.base_url)
        self.take_screenshot("test_004_inicio")
        
        # Enviar formulario vacío
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()
        self.take_screenshot("test_004_campos_vacios")
        
        # Verificar mensaje de error
        try:
            error_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
            )
            self.assertIn("Your username is invalid!", error_message.text)
            self.take_screenshot("test_004_error_validacion")
        except (TimeoutException, NoSuchElementException) as e:
            self.take_screenshot("test_004_error")
            self.fail(f"No se mostró el mensaje de error esperado para campos vacíos: {str(e)}")
    
    def test_005_logout_functionality(self):
        """
        Historia de Usuario 5: Como usuario autenticado, quiero poder cerrar mi sesión
        para proteger mi cuenta cuando termine de usar el sistema.
        
        Criterio de aceptación: El sistema debe permitir cerrar sesión y mostrar un mensaje de confirmación.
        Criterio de rechazo: El sistema no proporciona una forma de cerrar sesión o no muestra confirmación.
        """
        # Primero debemos iniciar sesión
        self.driver.get(self.base_url)
        self.take_screenshot("test_005_inicio")
        
        # Ingresar credenciales válidas
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username_field.send_keys(self.valid_username)
        password_field.send_keys(self.valid_password)
        login_button.click()
        
        # Verificar que estamos en el área segura
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        self.take_screenshot("test_005_login_exitoso")
        
        # Buscar y hacer clic en el botón de logout
        try:
            logout_button = self.driver.find_element(By.CSS_SELECTOR, "a.button[href='/logout']")
            logout_button.click()
            
            # Verificar mensaje de logout exitoso
            logout_message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
            )
            self.assertIn("You logged out", logout_message.text)
            self.take_screenshot("test_005_logout_exitoso")
            
            # Verificar que estamos de vuelta en la página de login
            login_form = self.driver.find_element(By.ID, "login")
            self.assertTrue(login_form.is_displayed())
        except (TimeoutException, NoSuchElementException) as e:
            self.take_screenshot("test_005_error")
            self.fail(f"No se pudo completar el proceso de logout correctamente: {str(e)}")


if __name__ == "__main__":
    # Configurar el runner de pruebas HTML
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output=REPORT_DIR,
        report_name="LoginTestReport",
        report_title="Pruebas de Login Automatizadas",
        combine_reports=True,
        add_timestamp=True
    ))