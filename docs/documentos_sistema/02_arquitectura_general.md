# Arquitectura General — Documentos del Sistema

## Visión General
El módulo `documentos_sistema` implementa una arquitectura documental desacoplada,
basada en un **Documento Base QWeb reutilizable**, sobre el cual se construyen
formatos específicos mediante wrappers.

La arquitectura está diseñada para:
- Minimizar duplicación
- Facilitar recreación del formato
- Asegurar mantenibilidad
- Cumplir requisitos CloudPepper + Odoo 17

## Componentes Principales

### 1. Documento Base QWeb
Archivo:
- report/ds_document_base.xml

Responsabilidad:
- Definir estructura A4 vertical
- Header con datos de empresa y logo dinámico
- Contenedor neutro del documento
- Pie de página 100% editable por administrador

No contiene:
- Lógica fiscal
- Cálculos
- Tablas de productos
- Condicionales por tipo de documento

### 2. Wrappers por Documento
Archivos:
- report/sale_order_report.xml
- report/invoice_report.xml (futuro)

Responsabilidad:
- Inyectar contenido específico:
  - Tabla de productos
  - Totales
  - Saldo
- Definir título dinámico
- Reutilizar el Documento Base sin duplicar estructura

### 3. Configuración Administrativa
Modelo:
- ds.config

Responsabilidad:
- Almacenar el pie de página completo
- Permitir edición solo por administrador
- Proveer HTML libre para firma, textos legales, dirección, etc.

### 4. Registro de Reportes
Archivo:
- report/report_actions.xml

Responsabilidad:
- Registrar los documentos como reportes oficiales
- Hacerlos visibles en el menú "Imprimir"
- No reemplazar reportes estándar de Odoo

## Flujo de Impresión
1. Usuario abre Cotización / Orden
2. Selecciona "Imprimir"
3. Odoo ejecuta ir.actions.report
4. Wrapper llama al Documento Base
5. Documento Base renderiza header + pie
6. Wrapper inyecta contenido central
7. Odoo genera PDF vía QWeb

## Principios Arquitectónicos
- Un solo documento base
- Separación estricta de responsabilidades
- Sin dependencias externas
- Sin lógica compleja en QWeb
- Backend solo para cálculos

