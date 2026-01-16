{
    "name": "Documentos del Sistema",
    "version": "17.0.1.0.0",
    "category": "Sales",
    "summary": "Formato documental unificado para cotizaciones, órdenes y facturas",
    "license": "LGPL-3",
    "author": "Sistema",
    "depends": [
        "sale",
        "account"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/ds_default_config.xml",
        "views/ds_config_views.xml",
        "views/ds_menus.xml",
        "report/ds_document_base.xml",
        "report/sale_order_report.xml",
        "report/report_actions.xml"
    ],
    "installable": True,
    "application": False
}


