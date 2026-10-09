# Pre-entrega Automation Testing

## Propósito del proyecto
Este proyecto corresponde a la pre-entrega del curso de Automation Testing. Su principal objetivo es aplicar los conocimientos adquiridos para automatizar flujos básicos de navegación web utilizando **Selenium WebDriver y Python** sobre el sitio de e-commerce de prueba [SauceDemo](https://www.saucedemo.com/).

## Tecnologías usadas
- **Python:** Lenguaje principal de desarrollo.
- **Selenium WebDriver:** Herramienta para automatizar la interacción con el navegador.
- **Pytest:** Framework de pruebas estructurado.
- **pytest-html:** Plugin para la generación de reportes HTML.
- **Git y GitHub:** Control de versiones y alojamiento del repositorio.

## Estructura del proyecto

A continuación se detalla la organización de los archivos y directorios del proyecto:

```text
pre-entrega-automation-testing-ROBERTO-DE-EZCURRA/
├── .gitignore               # Archivos ignorados por git (ej. venv/)
├── README.md                # Documentación del proyecto
├── pytest.ini               # Archivo de configuración central de pytest
├── requirements.txt         # Archivo con las dependencias necesarias
├── reports/                 # Directorio de reportes
│   └── reporte.html         # Reporte HTML generado tras la ejecución (auto-generado)
├── tests/                   # Directorio que contiene los casos de prueba
│   ├── __init__.py
│   ├── conftest.py          # Fixture de Pytest (inicialización y cierre del WebDriver)
│   ├── test_cart.py         # Pruebas de interacción con el carrito de compras
│   ├── test_inventory.py    # Pruebas de validación del catálogo de productos
│   └── test_login.py        # Pruebas relacionadas al inicio de sesión
└── utils/                   # Directorio para funciones auxiliares (helpers)
    ├── __init__.py
    └── helpers.py           # Funciones reutilizables como el proceso de login
```

## Pasos de instalación

Para ejecutar este proyecto de forma local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/TU-USUARIO/pre-entrega-automation-testing-ROBERTO-DE-EZCURRA.git
   cd pre-entrega-automation-testing-ROBERTO-DE-EZCURRA
   ```

2. **Crear un entorno virtual:**
   ```bash
   python3 -m venv venv
   ```

3. **Activar el entorno virtual:**
   - En macOS y Linux:
     ```bash
     source venv/bin/activate
     ```
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```

4. **Instalar las dependencias requeridas:**
   ```bash
   pip install -r requirements.txt
   ```

## Comandos para ejecutar los tests
Una vez activado el entorno virtual y con las dependencias instaladas, puedes ejecutar los tests mediante el siguiente comando en la terminal:
```bash
pytest
```
Este comando correrá todos los casos de prueba y, gracias a la configuración en `pytest.ini`, generará automáticamente un reporte HTML detallado en `reports/reporte.html`.
