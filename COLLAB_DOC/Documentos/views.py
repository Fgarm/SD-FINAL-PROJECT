from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Documentos/index.html")

def redirect(request):
    return render(request, "Documentos/redirect.html")

def room(request, documento_id):
    return render(request, "Documentos/documento_edit.html", {"documento_id": documento_id})