import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def bag_form(request):
    if request.method == 'GET':
        template = 'bags/form.html'

        return render(request, template)
