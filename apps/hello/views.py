from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from models import MyProfile, HttpRequests


def index(request):
    context = {}
    context['profile'] = get_object_or_404(MyProfile) 
    return render(request, 'profile.html', context)

def http_requests(request):
    context = {}
    context['http_requests'] = HttpRequests.objects.all().order_by('-id')[:10]
    context['len_http_requests'] = len(HttpRequests.objects.all())
    return render(request, 'http_requests.html', context)
    