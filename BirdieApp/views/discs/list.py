import sqlite3
from django.shortcuts import render, redirect, reverse
from BirdieApp.models import model_factory, Disc
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def disc_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Disc)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
                SELECT
                    d.id,
                    d.user_id,
                    d.name,
                    d.disc_type,
                    d.bag_id,
                    d.color,
                    d.speed,
                    d.glide,
                    d.turn,
                    d.fade,
                    d.brand
                FROM BirdieApp_disc d
                """)
            
            all_discs = db_cursor.fetchall()
        
        template = ('discs/list.html', 'bags/details.html')
        context = {
            'all_discs': all_discs
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user_id = request.user.id
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            INSERT INTO BirdieApp_disc
                (user_id, brand, name, disc_type, color, speed, glide, turn, fade)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (user_id, form_data['brand'], form_data['name'], form_data['disc_type'],
             form_data['color'], form_data['speed'], form_data['glide'],
             form_data['turn'], form_data['fade']))
            
        return redirect(reverse('BirdieApp:discs'))
