from odoo import models, api


class SaleOrderDocumentHelpers(models.Model):
    _inherit = "sale.order"

    @api.model
    def _ds_safe_currency(self):
        return self.env.company.currency_id

    def ds_amount_total_to_text(self):
        """Devuelve el TOTAL del documento en letras (moneda del documento)."""
        self.ensure_one()
        currency = self.currency_id or self._ds_safe_currency()
        try:
            return currency.amount_to_text(self.amount_total)
        except Exception:
            # Fallback seguro: nunca romper impresión
            return ""

    def ds_footer_html(self):
        """HTML del pie de página (editable por admin)."""
        self.ensure_one()
        config = self.env["ds.config"].search([], limit=1)
        return config.footer_html if config and config.footer_html else ""


class AccountMoveDocumentHelpers(models.Model):
    _inherit = "account.move"

    @api.model
    def _ds_safe_currency(self):
        return self.env.company.currency_id

    def ds_amount_total_to_text(self):
        """Devuelve el TOTAL del documento en letras (moneda del documento)."""
        self.ensure_one()
        currency = self.currency_id or self._ds_safe_currency()
        try:
            return currency.amount_to_text(self.amount_total)
        except Exception:
            return ""

    def ds_footer_html(self):
        """HTML del pie de página (editable por admin)."""
        self.ensure_one()
        config = self.env["ds.config"].search([], limit=1)
        return config.footer_html if config and config.footer_html else ""


