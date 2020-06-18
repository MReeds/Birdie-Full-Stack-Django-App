import sqlite3
from django.shortcuts import render, redirect, reverse
from BirdieApp.models import model_factory, Bag
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def bag_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Bag)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
                SELECT
                    b.id,
                    b.brand
                FROM BirdieApp_bag b
                """)
            
            all_bags = db_cursor.fetchall()
        
        template = 'bags/list.html'
        context = {
            'all_bags': all_bags
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            INSERT INTO BirdieApp_bag
                (brand)
            VALUES
                (?)
            """,
            (form_data['brand'],))
            
        return redirect(reverse('BirdieApp:bags'))