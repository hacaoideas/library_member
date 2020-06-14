from odoo import fields, models, api
import datetime

class Book(models.Model):
    _inherit = 'library.book'
    is_available = fields.Boolean('Is Available?')
    isbn = fields.Char(help="Use valid ISBN-13 or ISBN-10")
    publisher_id = fields.Many2one(index=True)
    review_date = fields.Date(store=True, compute='_compute_review_date', inverse='_inverse_review_date', search='_search_review_date')

    def _check_isbin(self):
        sef.ensure_one()
        digits = [int(x) for x in self.isbn if x.isdigit()]
        if len(digits) == 10:
            ponderators = [1,2,3,4,5,6,7,8,9]
            total = sum(a * b for a,b in zip(digits[:9], ponderators))
            check = total % 11
            return digits[-1] == check
        else:
            return super()._check_isbn()

    @api.depends('date_published')
    def _compute_review_date(self):
        for book in self:
            book.review_date = book.date_published + datetime.timedelta(days=15)

    def _inverse_review_date(self):
        for book in self:
            book.date_published = book.review_date - datetime.timedelta(days=15)

    def _search_review_date(self, operator, value):
        return [('review_date',operator,value)]

