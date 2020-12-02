# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
# from datetime imsort datetime, time, timedelta
# from pytz imsort timezone, UTC


class SaleCommission(models.Model):
    _name = 'sale.commission'
    _description = 'Sale Commission'

    name = fields.Char('Description')
    branch_id = fields.Many2one('res.branch', 'Branch')
    product_tmpl_id = fields.Many2one('product.template',string='Product Template')
    merchant_id = fields.Many2one('res.partner', string='Merchant', required=True)
    is_line = fields.Boolean('Commission Is Line', compute='_is_line_true',default=False)
    commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percent')], 'Commission Type',
                                       default='fixed', required=True)
    line_ids = fields.One2many('sale.commission.line', 'commission_id', 'Commission Lines')
    commission_amount = fields.Integer('Commission Amount')

    @api.onchange('merchant_id')
    def _is_line_true(self):
        if self.merchant_id.commission_type == 'line':
            print('..................line.................')
            self.is_line = True
        else:
            print('......................else function..........')
            self.is_line = False

class SaleCommissionLine(models.Model):
    _name = 'sale.commission.line'
    _description = 'Sale Commission Line'

    product_ids = fields.Many2one('product.template', string='Product')
    commission_id = fields.Many2one('sale.commission', 'Sale Commission')
    commission_type = fields.Char('Commission Type')
    is_line = fields.Boolean('Is Line')
    merchant = fields.Many2one('res.partner',string='Merchant')
    commission_amt = fields.Integer('Commission Amount')
    list_price = fields.Float(related='product_ids.list_price',string='Price')
    commission_value = fields.Integer('Commission Values')
    sale_order_id = fields.Many2one('sale.order',string='Sale Order')

    @api.onchange('product_ids')
    def change_product(self):
        self.commission_type = self.commission_id.commission_type
        self.is_line = self.commission_id.is_line
        self.merchant = self.commission_id.merchant_id
        self.commission_amt = self.commission_id.commission_amount
        if self.commission_type == 'percent':
            self.commission_value = (self.list_price * self.commission_amt) / 100
            print('..........Percent.........')
        else:
            self.commission_value = self.list_price - self.commission_amt
            print('...........Fixed..............')

    @api.onchange('merchant')
    def change_merchant(self):
        line_ids = self.env['sale.order.line']
        product = 0
        for line in line_ids.search([('product_id','=',self.product_ids.id)]):
            product = line.product_id.id
            print('.............. product '+str(product)+' and '+str(self.product_ids.id))
        if product == self.product_ids.id:
            self.commission_type = self.commission_id.commission_type
            self.commission_amt = self.commission_id.commission_amount
            if self.commission_type == 'percent':
                self.commission_value = (self.list_price * self.commission_amt) / 100
                print('..........Percent.........')
            else:
                self.commission_value = self.list_price - self.commission_amt
                print('...........Fixed..............')
            print('.......... merchant onchnage ..........')
        