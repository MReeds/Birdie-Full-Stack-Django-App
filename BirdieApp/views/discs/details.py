import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from BirdieApp.models.model_factory import model_factory
from BirdieApp.models import Disc

def get_disc(disc_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Disc)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            d.id AS disc_id,
            d.brand,
            d.name,
            d.disc_type,
            d.color,
            d.speed,
            d.glide,
            d.turn,
            d.fade
        FROM BirdieApp_disc d
        WHERE d.id = ?
        """, (disc_id,))
        
        return db_cursor.fetchone()

@login_required
def disc_details(request, disc_id):
    if request.method == 'GET':
        disc = get_disc(disc_id)
        
        template = 'discs/details.html'
        context = {
            'disc': disc
        }
        
        return render(request, template, context)


# @login_required
# def book_details(request, book_id):
#     if request.method == 'GET':
#         book = get_book(book_id)

#         template = 'books/details.html'
#         context = {
#             'book': book
#         }

#         return render(request, template, context)
      
#     if request.method == 'POST':
#         form_data = request.POST

#         # Check if this POST is for deleting a book
#         #
#         # Note: You can use parenthesis to break up complex
#         #       `if` statements for higher readability
#         if (
#             "actual_method" in form_data
#             and form_data["actual_method"] == "DELETE"
#         ):
#             with sqlite3.connect(Connection.db_path) as conn:
#                 db_cursor = conn.cursor()

#                 db_cursor.execute("""
#                 DELETE FROM libraryapp_book
#                 WHERE id = ?
#                 """, (book_id,))

#             return redirect(reverse('libraryapp:books'))

#         # Check if this POST is for editing a book
#         if (
#             "actual_method" in form_data
#             and form_data["actual_method"] == "PUT"
#         ):
#             with sqlite3.connect(Connection.db_path) as conn:
#                 db_cursor = conn.cursor()

#                 db_cursor.execute("""
#                 UPDATE libraryapp_book
#                 SET title = ?,
#                     author = ?,
#                     isbn = ?,
#                     year_published = ?,
#                     location_id = ?,
#                     publisher = ?
#                 WHERE id = ?
#                 """,
#                 (
#                     form_data['title'], form_data['author'],
#                     form_data['isbn'], form_data['year_published'],
#                     form_data["location"], form_data["publisher"], 
#                     book_id,
#                 ))

#             return redirect(reverse('libraryapp:books'))
