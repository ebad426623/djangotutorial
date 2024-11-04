from django.http import HttpResponse # type: ignore

def index(request):
    return HttpResponse("Hello, world. One piece is real")