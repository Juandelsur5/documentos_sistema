# Configuración Administrativa — Documentos del Sistema

## Objetivo
Permitir que un **administrador** configure los textos que aparecen en el
pie de todos los documentos del sistema, sin modificar código.

## Modelo
ds.config

## Responsabilidad
El modelo de configuración es responsable de:
- Almacenar el contenido completo del pie de página
- Permitir HTML libre
- Centralizar la configuración para todos los documentos

## Campo Principal
footer_html

Características:
- Tipo: HTML
- Contenido libre
- Editable solo por administradores
- Renderizado tal cual en el PDF

## Uso del Pie de Página
En este campo el administrador puede incluir:
- Texto legal completo
- Dirección de la empresa
- Firmas
- Nombre y cédula de quien recibe
- Notas comerciales
- Cualquier información requerida por negocio o ley

El sistema no valida ni interpreta este contenido.

## Seguridad
- Solo usuarios del grupo:
  Documentos del Sistema / Administrador
  pueden modificar esta configuración.
- Usuarios normales no tienen acceso de edición.

## Regla Clave
Todo el contenido inferior del documento depende de esta configuración.
Si el administrador cambia el texto, **todos los documentos se actualizan**.


