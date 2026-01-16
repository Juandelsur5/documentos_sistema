# Estructura del Módulo — Documentos del Sistema

## Nombre del módulo
documentos_sistema

## Dependencias
- sale
- account

No depende de:
- GIITIC
- módulos fiscales
- integraciones externas

## Estructura de carpetas

documentos_sistema/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── ds_config.py
│   ├── ds_doc_helpers.py
│   └── ds_balance.py
├── security/
│   ├── security.xml
│   └── ir.model.access.csv
├── views/
│   ├── ds_config_views.xml
│   └── ds_menus.xml
├── report/
│   ├── ds_document_base.xml
│   ├── sale_order_report.xml
│   ├── invoice_report.xml
│   └── report_actions.xml
└── data/
    └── ds_default_config.xml

## Archivos críticos

### __manifest__.py
- Declara dependencias
- Registra XML
- Controla instalación

### ds_document_base.xml
- Documento base QWeb
- Header + pie editable
- No contiene lógica

### sale_order_report.xml
- Wrapper para cotización / orden
- Tabla de productos
- Totales y saldo

### report_actions.xml
- Registra reportes
- Hace visible el documento en "Imprimir"

### ds_config.py
- Modelo de configuración
- Campo footer_html editable por admin

## Convenciones
- Un archivo = una responsabilidad
- Nada hardcodeado en QWeb
- Sin duplicar estructura
- Backend para lógica, QWeb para render

## Regla de recreación
Si falta cualquiera de estos archivos, el módulo:
- No instala
- No imprime
- O no cumple negocio

