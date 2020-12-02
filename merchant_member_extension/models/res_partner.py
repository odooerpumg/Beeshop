# -*- coding: utf-8 -*-

import base64
import collections
import datetime
import hashlib
import pytz
import threading
import re

import requests
from lxml import etree
from werkzeug import urls

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.modules import get_module_resource
from odoo.osv.expression import get_unaccent_wrapper
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    commission_type = fields.Selection([('line', 'Line'), ('each', 'Each')], 'Commission Type')
    commission_value = fields.Integer('Commission Value')
    delivery_pickup_address = fields.Text('Delivery Pick Up Address')
    reg_fname = fields.Char(string='Filename')
    reg_file = fields.Binary(string='Company Registeration File')
    nrc_type_select = fields.Selection([('nrc', 'NRC'), ('nrc_foc', 'FOC')], 'NRC Type')
    id_name = fields.Char('ID Name')
    nrc_type = fields.Many2one('nrc.type','NRC Type and region')
    nrc_desc = fields.Many2one('nrc.description','NRC Description')
    nrc_number = fields.Char('NRC Number')
    nrc_fname = fields.Char(string='Filename')
    nrc_file = fields.Binary(string='NRC Front')
    nrc_bfname = fields.Char(string='Filename')
    nrc_bfile = fields.Binary(string='NRC Back')
    is_merchant = fields.Boolean('Is Merchant', default=False)


class NRCDescription(models.Model):
    _name = "nrc.description"

    name = fields.Char('Name')

class NRCType(models.Model):
    _name = "nrc.type"

    name = fields.Char('Type')

class ResBank(models.Model):
	_inherit = 'res.partner.bank'

	acc_type = fields.Char('Account Type')
