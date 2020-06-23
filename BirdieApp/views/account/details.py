import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from BirdieApp.models.model_factory import model_factory
from django.contrib.auth.models import User

@login_required
def account_details(request):
    if request.method == 'GET':

        template = ('accounts/details.html')
        
        return render(request, template)
    
    if request.method == 'POST':
        form_data = request.POST
        user_id = request.user.id
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE auth_user
                SET
                    first_name = ?,
                    last_name = ?,
                    email = ?
                WHERE id = ?
                """,
                (form_data['first_name'], form_data['last_name'], form_data['email'], user_id))

            return redirect(reverse('BirdieApp:account'))
