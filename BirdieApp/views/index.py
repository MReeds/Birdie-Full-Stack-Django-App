from django.shortcuts import render, redirect

def index(request):
    """ The home page for Birdie """
    return render(request, 'birdie_templates/index.html')