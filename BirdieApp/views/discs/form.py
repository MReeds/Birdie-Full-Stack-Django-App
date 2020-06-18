import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

types = [
    'Putter',
    'Mid-range',
    'Driver'
]

@login_required
def disc_form(request):
    if request.method == 'GET':
        template = 'discs/form.html'
        context = {
            'types': types
        }

        return render(request, template, context)


