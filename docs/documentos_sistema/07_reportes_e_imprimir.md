# Reportes e Impresión — Documentos del Sistema

## Objetivo
Definir cómo los documentos del sistema se registran en Odoo para que
aparezcan en el menú **Imprimir** y se generen como PDF.

## Registro de Reportes
Los documentos se registran mediante `ir.actions.report`.

Archivo:
- report/report_actions.xml

Cada reporte:
- Se asocia a un modelo (ej. sale.order)
- Usa QWeb PDF
- Aparece en el menú "Imprimir"
- No reemplaza reportes estándar de Odoo

## Ejemplo — Cotización / Orden
Modelo:
- sale.order

Reporte:
- Documento del Sistema (Cotización / Orden)

Al imprimir:
- Odoo llama al wrapper correspondiente
- El wrapper llama al Documento Base
- Se genera el PDF final

## Convivencia con Odoo
- Los reportes estándar permanecen intactos
- El usuario puede elegir qué formato imprimir
- No se sobreescribe ningún comportamiento core

## Reglas Técnicas
- Siempre usar `binding_type = report`
- Siempre usar `qweb-pdf`
- Nunca usar rutas locales
- Nunca generar PDFs manualmente
- Siempre usar QWeb

## Resultado Esperado
En una cotización u orden debe aparecer:

Imprimir
- Documento del Sistema (Cotización / Orden)
- Cotización en PDF (Odoo)
- Otros reportes estándar


