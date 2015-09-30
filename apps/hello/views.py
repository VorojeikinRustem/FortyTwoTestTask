from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from models import MyProfile


def index(request):
    context = {}
    context['profile'] = get_object_or_404(MyProfile) 
    return render(request, 'profile.html', context)
