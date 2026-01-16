# Wrappers por Documento — Documentos del Sistema

## Concepto
Un wrapper es una plantilla QWeb que **especializa** el Documento Base para un
tipo concreto de documento, sin duplicar estructura.

Cada wrapper:
- Llama al Documento Base
- Inyecta contenido central
- Define el comportamiento visual específico

## Wrapper de Cotización / Orden

Archivo:
- report/sale_order_report.xml

Modelo:
- sale.order

Responsabilidades:
- Definir el título dinámico:
  - Cotización (draft / sent)
  - Orden de Pedido (sale)
- Renderizar datos del cliente y vendedor
- Renderizar tabla de productos
- Mostrar totales
- Mostrar saldo a la fecha

No hace:
- Cálculos fiscales
- Lógica de pie de página
- Gestión de permisos

## Flujo Técnico
1. Odoo ejecuta ir.actions.report
2. Se llama al wrapper
3. El wrapper llama al Documento Base
4. El Documento Base renderiza header y pie
5. El wrapper inyecta contenido central

## Extensibilidad
Para agregar un nuevo documento:
1. Crear un nuevo wrapper
2. Llamar al Documento Base
3. Registrar un nuevo ir.actions.report

Ejemplos futuros:
- invoice_report.xml (account.move)
- delivery_report.xml
- proforma_report.xml

## Regla Clave
Nunca duplicar:
- Header
- Pie
- Estructura base

Todo wrapper debe ser delgado y específico.

