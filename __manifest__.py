{
    'name': 'Library Members',
    'description': 'Manage people who will be able to borrow books from the library',
    'author': 'Daniel Reis',
    'depends': ['library', 'mail'],
    'application': False,
    'data': [
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/member_view.xml',
        'security/library_security.xml',
        'security/ir.model.access.csv',
    ]

}