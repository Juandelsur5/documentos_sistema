from odoo import models, fields, api


class DsConfig(models.Model):
    _name = "ds.config"
    _description = "Configuración de Documentos del Sistema"
    _rec_name = "name"

    name = fields.Char(
        string="Configuración",
        default="Configuración General",
        readonly=True
    )

    footer_html = fields.Html(
        string="Pie de Página del Documento",
        help="Texto legal, notas y dirección de la empresa. Visible en todos los documentos del sistema."
    )

    @api.model
    def get_footer_html(self):
        config = self.search([], limit=1)
        return config.footer_html if config else ""


