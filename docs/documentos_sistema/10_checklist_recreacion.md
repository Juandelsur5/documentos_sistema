# Checklist de Recreación — Documentos del Sistema

Este checklist permite **recrear el sistema de documentos desde cero**
sin necesidad de rediseñar ni tomar decisiones adicionales.

---

## 1. Crear módulo
- [ ] Crear carpeta `documentos_sistema`
- [ ] Crear `__manifest__.py`
- [ ] Definir dependencias (`sale`, `account`)

## 2. Crear modelos
- [ ] Crear `ds_config.py`
- [ ] Crear `ds_doc_helpers.py`
- [ ] Crear `ds_balance.py`
- [ ] Importar modelos en `models/__init__.py`

## 3. Seguridad
- [ ] Crear grupo `Documentos del Sistema / Administrador`
- [ ] Definir permisos en `ir.model.access.csv`
- [ ] Restringir edición de configuración a admin

## 4. Documento Base QWeb
- [ ] Crear `ds_document_base.xml`
- [ ] Header con logo dinámico
- [ ] Contenedor neutro
- [ ] Pie editable desde `ds.config.footer_html`

## 5. Wrappers
- [ ] Crear `sale_order_report.xml`
- [ ] Definir título dinámico
- [ ] Renderizar tabla de productos
- [ ] Renderizar totales y saldo

## 6. Registro de reportes
- [ ] Crear `report_actions.xml`
- [ ] Registrar `ir.actions.report`
- [ ] Binding a `sale.order`
- [ ] Verificar aparición en "Imprimir"

## 7. Configuración Admin
- [ ] Crear vista de configuración
- [ ] Crear menú solo para admin
- [ ] Probar edición del pie de página

## 8. Pruebas
- [ ] Instalar módulo
- [ ] Actualizar módulo
- [ ] Imprimir cotización
- [ ] Imprimir orden
- [ ] Validar PDF A4 vertical

## 9. CloudPepper
- [ ] Verificar compatibilidad
- [ ] Confirmar que no hay rutas locales
- [ ] Confirmar que no hay dependencias externas

---

## Resultado esperado
Si todos los ítems están completos:
- El módulo instala
- El documento imprime
- El formato es consistente
- El sistema es recreable y mantenible

