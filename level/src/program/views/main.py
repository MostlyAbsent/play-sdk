from django.http import HttpResponse, Http404
from django.template import loader
from ..utils import is_optimal

def index(request):
    return HttpResponse("Connected to server, post examples to http://localhost:8080/employee")
