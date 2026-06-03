from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def page_not_found(request, exception):
    return render (request, '404.html', status=404)

def server_error(request):
    return render (request, '500.html', status=500)

