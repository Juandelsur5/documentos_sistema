# Documentos del Sistema — Contexto y Objetivo

## Contexto
Este módulo existe para definir un **sistema de formatos documentales internos en Odoo 17**, desacoplado de cualquier lógica fiscal o contable externa.

Odoo actúa como:
- Sistema operativo comercial
- UX para ventas
- Generador de documentos visuales (PDF)

GIITIC u otros sistemas externos:
- NO dependen del PDF
- Solo consumen flujos de datos estructurados (ORM / eventos)

## Objetivo
Proveer un **Documento Base reutilizable** que sirva como fundamento para:
- Cotizaciones
- Órdenes / Pedidos
- Prefacturas
- Facturas visuales del sistema Odoo

## Principios clave
- Un solo documento base QWeb
- Wrappers por tipo de documento
- Pie de página 100% editable por administrador
- Logo dinámico desde la empresa
- Formato A4 vertical
- Tabla de productos ocupa la hoja completa
- Sin lógica fiscal en QWeb
- Compatible con CloudPepper y Odoo 17

## Fuera de alcance
- Lógica fiscal
- Asientos contables
- Validaciones legales
- Integraciones externas (GIITIC)

