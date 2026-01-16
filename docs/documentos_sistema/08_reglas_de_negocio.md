# Reglas de Negocio — Documentos del Sistema

## Principio General
Los documentos del sistema son **documentos operativos internos de Odoo**.
No son documentos fiscales ni contables definitivos.

## Separación de Responsabilidades
- Odoo:
  - Genera documentos
  - Maneja flujo comercial
  - Provee UX a usuarios
- Sistemas externos (ej. GIITIC):
  - Consumen flujos de datos
  - Generan asientos contables
  - No dependen del PDF

## Regla — Documento Base Único
- Existe un solo Documento Base
- Todos los documentos lo reutilizan
- No se duplican formatos

## Regla — Pie de Página Editable
- Todo el bloque inferior del documento es editable
- Controlado únicamente por administrador
- Incluye:
  - Texto legal
  - Firmas
  - Cédulas
  - Dirección
  - Observaciones

## Regla — Orden Genera Cartera
- Toda orden de pedido genera cartera automática
- El saldo mostrado debe incluir:
  - Cartera previa del cliente
  - Documentos abiertos
  - La orden actual

## Regla — Saldo a la Fecha
- El saldo es informativo
- No es fiscal
- No genera asientos
- Visible en el documento para control comercial

## Regla — Formato
- A4 vertical
- Tabla de productos ocupa la hoja completa
- Columnas de detalle amplias
- Columnas numéricas compactas

## Regla — Extensibilidad
Agregar un nuevo documento:
- No modifica el Documento Base
- Solo requiere un nuevo wrapper
- Registrar un nuevo reporte

## Regla — Prohibiciones
Está prohibido:
- Hardcodear textos legales
- Meter lógica fiscal en QWeb
- Duplicar estructura
- Acoplar el documento a integraciones externas


