import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from BirdieApp.models.model_factory import model_factory
from BirdieApp.models import Park

def get_park(park_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Park)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            p.id AS park_id,
            p.title,
            p.city,
            p.state
        FROM BirdieApp_park p
        WHERE id = ?
        """, (park_id,))

        return db_cursor.fetchone()

@login_required
def park_details(request, park_id):
    if request.method == 'GET':
        park = get_park(park_id)
        
        template = 'parks/details.html'
        context = {
            'park': park
        }
        
        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM BirdieApp_park
                WHERE id = ?
                """, (park_id,))

            return redirect(reverse('BirdieApp:parks'))
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE BirdieApp_park
                SET title = ?,
                    city = ?,
                    state = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['city'], 
                    form_data['state'], park_id,
                ))

            return redirect(reverse('BirdieApp:parks'))
