import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BirdieApp.models import Park, model_factory
from ..connection import Connection

@login_required
def park_form(request):
    if request.method == 'GET':
        template = 'parks/form.html'

        return render(request, template)
    
# @login_required
# def book_edit_form(request, book_id):

#     if request.method == 'GET':
#         book = get_book(book_id)
#         libraries = get_libraries()

#         template = 'books/form.html'
#         context = {
#             'book': book,
#             'all_libraries': libraries
#         }

#         return render(request, template, context)