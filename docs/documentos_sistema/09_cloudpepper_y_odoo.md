# CloudPepper y Odoo — Documentos del Sistema

## Objetivo
Asegurar que el módulo `documentos_sistema` cumple con los requisitos técnicos
de **Odoo 17 Community** y es **apto para despliegue en CloudPepper**.

## Compatibilidad Odoo 17
El módulo:
- Usa QWeb estándar
- Usa `ir.actions.report` con `qweb-pdf`
- No reemplaza reportes core
- No utiliza APIs obsoletas
- Respeta estructura de módulos Odoo

## Requisitos CloudPepper
El módulo cumple porque:
- No usa rutas locales del sistema
- No escribe archivos en disco
- No ejecuta comandos shell
- No depende de librerías externas
- Genera PDFs solo vía QWeb
- Usa `image_data_uri` para logos

## Rendimiento
- QWeb sin lógica pesada
- Sin queries por línea de producto
- Backend para cálculos
- Templates solo renderizan

## Seguridad
- Accesos definidos en `ir.model.access.csv`
- Configuración editable solo por admin
- No expone vistas sensibles a usuarios normales

## Multiempresa y Moneda
- Usa `company_id` dinámico
- Usa `currency_id` del documento
- No hardcodea empresa ni moneda

## Despliegue
- El módulo puede instalarse y actualizarse
- No rompe datos existentes
- Convive con módulos estándar
- Apto para producción en CloudPepper

## Conclusión
Con las correcciones de prioridad alta y media,
el módulo es **apto para producción** en Odoo 17 y CloudPepper.


