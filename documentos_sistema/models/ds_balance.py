from odoo import models, api


class SaleOrderBalance(models.Model):
    _inherit = "sale.order"

    def ds_get_partner_balance_to_date(self):
        """
        Retorna el saldo total del cliente incluyendo:
        - Facturas abiertas
        - Notas débito/crédito abiertas
        - Esta orden actual
        """
        self.ensure_one()
        partner = self.partner_id
        if not partner:
            return 0.0

        # Facturas abiertas del cliente
        domain = [
            ("partner_id", "=", partner.id),
            ("move_type", "in", ("out_invoice", "out_refund")),
            ("state", "=", "posted"),
            ("payment_state", "!=", "paid"),
        ]

        invoices = self.env["account.move"].search(domain)
        balance = sum(invoices.mapped("amount_residual"))

        # Incluir esta orden actual
        balance += self.amount_total

        return balance


class AccountMoveBalance(models.Model):
    _inherit = "account.move"

    def ds_get_partner_balance_to_date(self):
        """
        Retorna el saldo del cliente incluyendo este movimiento.
        """
        self.ensure_one()
        partner = self.partner_id
        if not partner:
            return 0.0

        domain = [
            ("partner_id", "=", partner.id),
            ("move_type", "in", ("out_invoice", "out_refund")),
            ("state", "=", "posted"),
            ("payment_state", "!=", "paid"),
        ]

        invoices = self.env["account.move"].search(domain)
        return sum(invoices.mapped("amount_residual"))

