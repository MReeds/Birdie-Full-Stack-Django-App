import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BirdieApp.models import model_factory
from ..connection import Connection

@login_required
def account_edit_form(request):

    if request.method == 'GET':

        template = 'accounts/form.html'

        return render(request, template)

    elif request.method == 'POST':
            form_data = request.POST
            
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()
                
                db_cursor.execute("""
                INSERT INTO auth_user
                    (first_name, last_name, email)
                VALUES
                    (?, ?, ?)
                """,
                (form_data['first_name'], 
                form_data['last_name'], form_data['email']))
                
            return redirect(reverse('BirdieApp:account'))