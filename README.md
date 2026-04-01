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
   cd "facturador_automatico_arca"
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

Coloca tu archivo Excel con las facturas en la raíz del proyecto con el nombre **`facturador.xlsx`**.

### Estructura del Excel

El archivo debe contener las siguientes columnas (A-L):

| Columna | Nombre | Descripción | Ejemplo |
|---------|--------|-------------|---------|
| A | Cliente | Nombre del cliente | Juan Pérez |
| B | CUIT | CUIT sin guiones | 20123456789 |
| C | Cond_IVA | Condición IVA (RI/CF/M/E) | RI |
| D | Importe | Monto sin IVA | 10000 |
| E | IVA | Monto de IVA | 2100 |
| F | TOTAL | Total de la factura | 12100 |
| G | Rendicion | Número de rendición | 123 |
| H | Fecha | Fecha del comprobante | 15/01/2024 |
| I | Periodo | Periodo a facturar | Enero 2024 |
| J | Realizado | Marca de procesamiento (✓) | |
| K | Pto Venta | Punto de venta AFIP | 4 |
| L | Cod. Actividad | Código de actividad AFIP | 682091 |

**Notas importantes:**
- Las columnas **Pto Venta** y **Cod. Actividad** permiten configurar valores específicos por cada factura
- Si no se especifican, el punto de venta por defecto es `4`
- El sistema marca automáticamente las facturas procesadas con ✓ en la columna "Realizado"

## ⚙️ Configuración del Facturador

### Valores Configurables desde el Excel

El sistema ahora permite configurar por factura (desde el Excel `facturador.xlsx`):

- **Punto de Venta** (Columna K): Configurable por cada factura
- **Código de Actividad** (Columna L): Configurable por cada factura

### Valores Automáticos

El sistema configura automáticamente los siguientes valores:

### Tipo de Comprobante
Se selecciona automáticamente según condición IVA:
- Factura A (`"10"`) para Responsable Inscripto (RI) o Monotributista (M)
- Factura B (`"19"`) para Consumidor Final (CF) o Exento (E)

### Concepto
`"2"` - Servicios (fijo)

### Descripción del Comprobante
Genera automáticamente:
```
Comisiones por cobranzas Mes de {periodo} - Rendición N° {numero}
```

### Forma de Pago
Contado (automático)

### Unidad de Medida
`"98"` - Unidad genérica

### IVA
Para Factura B, se aplica automáticamente IVA 21% (`"5"`)

### 📁 Ubicación de los PDFs

Los comprobantes generados se guardan automáticamente en el **Escritorio** con el formato:
```
{Cliente} x Honorarios {Periodo} - Rendición N° {Numero}.pdf
```
Ejemplo: `Juan Pérez x Honorarios Enero 2024 - Rendición N° 123.pdf`

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
