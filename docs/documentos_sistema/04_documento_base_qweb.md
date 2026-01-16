# Documento Base QWeb — Documentos del Sistema

## Propósito
El Documento Base QWeb es el **molde maestro** para todos los documentos del sistema.
Define la estructura común y reutilizable sobre la cual se construyen los formatos
específicos (cotización, orden, prefactura, factura visual).

## Archivo
report/ds_document_base.xml

## Responsabilidades
El documento base es responsable de:
- Definir el formato A4 vertical
- Renderizar el header de la empresa
- Mostrar el logo dinámico de la compañía
- Proveer un contenedor neutro para el contenido central
- Renderizar el pie de página editable por administrador

## Contenido del Header
El header incluye exclusivamente:
- Logo de la empresa (res.company.logo)
- Nombre de la empresa
- Dirección
- Ciudad
- Teléfono

El logo y los datos se obtienen dinámicamente desde la empresa activa.
No existe ningún valor hardcodeado.

## Contenedor Central
El documento base **NO contiene**:
- Tablas de productos
- Totales
- Cálculos
- Lógica por tipo de documento

El contenido central es inyectado por los wrappers mediante `t-call`.

## Pie de Página Editable
El pie de página:
- Se obtiene desde el modelo `ds.config`
- Usa el campo `footer_html`
- Es HTML libre
- Editable solo por administradores

En este bloque se incluye:
- Texto legal
- Dirección completa
- Firmas
- Cédula de quien recibe
- Notas comerciales

El documento base no interpreta ni valida este contenido.

## Restricciones
Está prohibido en el documento base:
- Cálculos
- Lógica fiscal
- Condicionales de negocio
- Acceso a modelos externos

## Regla Clave
Si el documento base cambia, **todos los documentos del sistema cambian**.
Por esta razón debe mantenerse simple, estable y sin lógica.

