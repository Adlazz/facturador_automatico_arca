"""
Configuración del proyecto.
Carga variables de entorno desde archivo .env
"""
import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno desde .env
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Credenciales AFIP
AFIP_CUIT = os.getenv('AFIP_CUIT')
AFIP_PASSWORD = os.getenv('AFIP_PASSWORD')
AFIP_EMPRESA = os.getenv('AFIP_EMPRESA')

# Validar que las credenciales estén configuradas
if not AFIP_CUIT or not AFIP_PASSWORD or not AFIP_EMPRESA:
    raise ValueError(
        "Las credenciales AFIP no están configuradas. "
        "Por favor, copia el archivo .env.example como .env y completa las credenciales."
    )
