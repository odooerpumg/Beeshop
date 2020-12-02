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

    is_member = fields.Boolean('Is Member ?',default=False)
    birthday = fields.Char('Birthday')
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string='Gender')
    
    def _compute_is_member(self):
    	if self.is_member == True:
    		self.company_type = 'person'
    	else:
    		self.company_type = 'company'

