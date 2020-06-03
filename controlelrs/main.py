from odoo import http
from odoo.addons.library.controllers.controllers import Books

class BookExtended(Books):
    @http.route()
    def list(self, **kwargs):
        response = super().list(**kwargs)
        # If this is inplace, the controller only context for available=1
        if kwargs.get('available=1'):
            Book = http.request.env['library.book']
            books = Book.search([('is_available','=',True)])
            response.qcontext['books'] = books
        return response




