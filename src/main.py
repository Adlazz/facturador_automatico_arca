from services.excel_handler import ExcelHandler
from services.invoice_processor import InvoiceProcessor
from handlers.element_handler import ElementHandler
from handlers.alert_handler import AlertHandler
from handlers.browser_manager import BrowserManager
from services.afip_login import AFIPLogin
import config
import keyboard
import logging
import os

# Configuración de logging
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'main.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Iniciar navegador
        browser = BrowserManager()
        driver, wait = browser.setup_driver()

        # Login automático en AFIP
        login_handler = AFIPLogin(driver, wait)
        if not login_handler.login(config.AFIP_CUIT, config.AFIP_PASSWORD, config.AFIP_EMPRESA):
            return

        # Inicializar handlers
        element_handler = ElementHandler(driver, wait)
        alert_handler = AlertHandler()
        processor = InvoiceProcessor(driver, element_handler, alert_handler)
        excel_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "facturador_test.xlsx")
        excel_handler = ExcelHandler(excel_file)

        # Cargar Excel y obtener facturas
        if not excel_handler.load_excel():
            logger.error("No se pudo cargar el archivo Excel.")
            return

        facturas = excel_handler.get_facturas_pendientes()
        if not facturas:
            logger.info("No hay facturas pendientes para procesar.")
            return

        # Procesar cada factura
        for factura in facturas:
            if processor.process_invoice(factura):
                excel_handler.marcar_como_realizada(factura)
            else:
                logger.warning(f"Factura fallida para {factura.cliente}")

        logger.info("Proceso finalizado. Presione 'Esc' para cerrar el navegador.")
        while True:
            if keyboard.is_pressed('esc'):
                logger.info("Tecla 'Esc' presionada. Cerrando navegador.")
                break

    except Exception as e:
        logger.error(f"Error general en el proceso: {str(e)}")

    finally:
        browser.close_browser()

if __name__ == "__main__":
    main()
