import sqlite3
from django.shortcuts import render, redirect, reverse
from BirdieApp.models import model_factory, Park
from ..connection import Connection
from django.contrib.auth.decorators import login_required

def park_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Park)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
                SELECT
                    p.id,
                    p.title,
                    p.city,
                    p.state
                FROM BirdieApp_park p
                """)
            
            all_parks = db_cursor.fetchall()
        
        template = 'parks/list.html'
        context = {
            'all_parks': all_parks
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            INSERT INTO BirdieApp_park
                (title, city, state)
            VALUES
                (?, ?, ?)
            """,
            (form_data['title'], form_data['city'], form_data['state'],))
            
        return redirect(reverse('BirdieApp:parks'))
