import sqlite3
from django.shortcuts import render, redirect, reverse
from BirdieApp.models import model_factory, Bag
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def bag_list(request):
    if request.method == 'GET':
        all_bags = Bag.objects.all()
        
        template = 'bags/list.html'
        context = {
            'all_bags': all_bags
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        new_bag = Bag.objects.create(
            brand = form_data['brand'],
            user_id = request.user.id
        )
            
        return redirect(reverse('BirdieApp:bags'))