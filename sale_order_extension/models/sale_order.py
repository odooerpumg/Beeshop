import calendar
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from requests.auth import HTTPBasicAuth
import hashlib
import json
import requests
import locale

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_compare, float_is_zero
from odoo.osv import expression

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    exchange_rate = fields.Float(string='Exchange Rate', store=True, copy=True)
    commission_ids = fields.One2many('sale.commission.line','sale_order_id','Sale Commission Line') 
            

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    uom_id = fields.Many2one('uom.uom', string='UOM')

class ProductCategory(models.Model):
    _inherit = 'product.category'

    category_code = fields.Char('Category Code')
    sub_categ = fields.Boolean('Sub Categtory?',default=False)
    # use_commission = fields.Boolean('Use Commission ?',default=False)

    @api.onchange('parent_id')
    def onchange_parent_id(self):
        if self.parent_id:
            self.sub_categ = True

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sub_cat_id = fields.Many2one('product.category',string='Sub Category')
    brand_id = fields.Many2one('product.brand',string='Brand')
    rating = fields.Integer('Rating')
    status = fields.Boolean('Status')
    is_feature = fields.Boolean('Feature')
    is_new = fields.Boolean('New Product')
    desc = fields.Text('Description')
    specification = fields.Text('Specification')

    @api.onchange('sub_cat_id')
    def onchange_sub_cat_id(self):
        if self.sub_cat_id:
            self.categ_id = self.sub_cat_id.parent_id

class ProductBrand(models.Model):
    _name = 'product.brand'

    name = fields.Char('Brand Name')

