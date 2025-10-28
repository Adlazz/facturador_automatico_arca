# Facturador Automático AFIP 

Sistema automatizado para la generación de comprobantes en línea en AFIP utilizando Selenium.

**Facturador especializado para:** Comisiones por cobranzas - Actividad de intermediación financiera.

## 📋 Estructura del Proyecto

```
/
├── src/
│   ├── handlers/          # Manejadores de interacciones web
│   │   ├── alert_handler.py
│   │   ├── browser_manager.py
│   │   └── element_handler.py
│   ├── services/          # Lógica de negocio
│   │   ├── afip_login.py
│   │   ├── excel_handler.py
│   │   └── invoice_processor.py
│   ├── config.py          # Configuración y variables de entorno
│   └── main.py            # Punto de entrada principal
├── logs/                  # Archivos de log (generados automáticamente)
├── run.py                 # Script de ejecución
├── .env.example           # Plantilla de variables de entorno
└── requirements.txt       # Dependencias del proyecto
```

## 🔧 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd "Comprobantes_En_Linea_Auto"
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **⚠️ IMPORTANTE: Configurar credenciales**
   ```bash
   # Copiar el archivo de ejemplo
   cp .env.example .env

   # Editar .env y agregar tus credenciales reales
   # AFIP_CUIT=tu_cuit_aqui
   # AFIP_PASSWORD=tu_password_aqui
   # AFIP_EMPRESA=Nombre de tu empresa tal como aparece en AFIP
   ```

## 🚀 Uso

```bash
python run.py
```

El sistema:
1. Iniciará un navegador Chrome automatizado
2. Se autenticará en AFIP con las credenciales del archivo `.env`
3. Leerá las facturas pendientes del archivo Excel
4. Procesará cada factura automáticamente
5. Generará y descargará los comprobantes en formato PDF

## 🔒 Seguridad

### ⚠️ NUNCA subir credenciales a GitHub

- El archivo `.env` contiene credenciales sensibles y está en `.gitignore`
- Solo se sube `.env.example` como plantilla
- Cada usuario debe crear su propio `.env` localmente

### Archivos excluidos del repositorio:
- `.env` - Credenciales
- `logs/` - Archivos de registro
- `*.xlsx` - Archivos Excel (excepto plantilla)
- `__pycache__/` - Cache de Python

## 📝 Configuración del Excel

Coloca tu archivo Excel con las facturas en la raíz del proyecto con el nombre `facturador_test.xlsx`.

El archivo debe seguir la estructura definida en `facturador_template.xlsx`.

## ⚙️ Configuración Específica del Facturador

Este facturador está configurado para un caso de uso específico. Si necesitas adaptarlo, modifica estos valores en `src/services/invoice_processor.py`:

### Punto de Venta
**Línea 97:** `"4"` - Punto de venta número 4
```python
self.handler.safe_select("puntodeventa", "4", description="Punto de Venta")
```

### Tipo de Comprobante
**Línea 103:** Se selecciona automáticamente según condición IVA:
- Factura A (`"10"`) para Responsable Inscripto o Monotributista
- Factura B (`"19"`) para Consumidor Final o Exento

### Concepto
**Línea 128:** `"2"` - Servicios
```python
self.handler.safe_select("idconcepto", "2", description="Concepto")
```

### Actividad AFIP
**Línea 136:** `"682091"` - Actividad de intermediación financiera
```python
self.handler.safe_select("actiAsociadaId", "682091", description="Actividad")
```

### Descripción del Comprobante
**Línea 249:** Genera automáticamente:
```
Comisiones por cobranzas Mes de {periodo} - Rendición N° {numero}
```
```python
descripcion = f"Comisiones por cobranzas Mes de {factura.periodo} - Rendición N° {str(factura.rendicion).strip()}"
```

### Forma de Pago
**Línea 213:** Contado (automático)

### Unidad de Medida
**Línea 258:** `"98"` - Unidad genérica
```python
self.handler.safe_select("detalle_medida1", "98", description="Unidad de Medida")
```

### IVA
**Línea 275:** Para Factura B, se aplica automáticamente IVA 21% (`"5"`)

## 📦 Dependencias principales

- `selenium` - Automatización del navegador
- `openpyxl` / `pandas` - Manejo de archivos Excel
- `python-dotenv` - Gestión de variables de entorno
- `webdriver-manager` - Gestión automática de ChromeDriver

## 🐛 Logs

Los archivos de log se generan automáticamente en la carpeta `logs/`:
- `main.log` - Log principal de la aplicación
- `invoice_processor.log` - Procesamiento de facturas
- `alert_handler.log` - Manejo de alertas
- `element_handler.log` - Interacciones con elementos
- `browser_manager.log` - Gestión del navegador

## 📄 Licencia

Este proyecto es de uso interno.
