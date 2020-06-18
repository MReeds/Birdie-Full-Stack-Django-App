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
        
        template = 'discs/list.html'
        context = {
            'all_discs': all_discs
        }
        
        return render(request, template, context)
