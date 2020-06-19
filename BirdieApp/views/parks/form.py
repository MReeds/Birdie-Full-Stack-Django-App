import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BirdieApp.models import Park, model_factory
from ..connection import Connection
from .details import get_park

@login_required
def park_form(request):
    if request.method == 'GET':
        template = 'parks/form.html'

        return render(request, template)
    
@login_required
def park_edit_form(request, park_id):

    if request.method == 'GET':
        park = get_park(park_id)

        template = 'parks/form.html'
        context = {
            'park': park
        }

        return render(request, template, context)