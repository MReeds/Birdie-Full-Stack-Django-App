import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from BirdieApp.models.model_factory import model_factory
from BirdieApp.models import Bag, Disc

def disc_list():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Disc)
        db_cursor = conn.cursor()
            
        db_cursor.execute("""
            SELECT
                d.id,
                d.name,
                d.brand,
                d.disc_type,
                d.bag_id
            FROM BirdieApp_disc d
            """)

        return db_cursor.fetchall()

def get_bag(bag_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bag)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            b.id AS bag_id,
            b.user_id,
            b.brand
        FROM BirdieApp_bag b
        WHERE b.id = ?
        """, (bag_id,))
        
        return db_cursor.fetchone()


@login_required
def bag_details(request, bag_id):
    if request.method == 'GET':
        current_user = request.user.id
        all_discs = disc_list()
        bag = get_bag(bag_id)
        
        template = 'bags/details.html'
        context = {
            'current_user': current_user,
            'bag': bag,
            'discs': all_discs
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
                DELETE FROM BirdieApp_bag
                WHERE id = ?
                """, (bag_id,))

            return redirect(reverse('BirdieApp:bags'))
