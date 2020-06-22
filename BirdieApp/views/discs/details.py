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
            d.bag_id,
            d.brand,
            d.name, 
            d.color,
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
    
    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM BirdieApp_disc
                WHERE id = ?
                """, (disc_id,))

            return redirect(reverse('BirdieApp:discs'))
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE BirdieApp_disc
                SET bag_id = ?,
                    brand = ?,
                    name = ?,
                    disc_type = ?,
                    color = ?,
                    speed = ?,
                    glide = ?,
                    turn = ?,
                    fade = ?
                WHERE id = ?
                """,
                (
                    form_data['bag_id'], form_data['brand'],
                    form_data['name'], form_data['disc_type'],
                    form_data['color'], form_data['speed'],
                    form_data['glide'], form_data['turn'], 
                    form_data['fade'],  disc_id,
                ))

            return redirect(reverse('BirdieApp:discs'))
