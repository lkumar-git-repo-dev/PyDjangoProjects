
from django.http import HttpResponse

def display(request):
    return HttpResponse("<html><body bgcolor='red'><h1>Hello World</h1></body></html>")
