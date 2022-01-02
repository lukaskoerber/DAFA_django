from django.shortcuts import render

# Create your views here.

def main_page(request):
    # Ein request bekommen und ein HTML Dokument zurückgeben
    # Dabei zurückgreifen auf eine Message die in der Datenbank steht 
    return render(request, "main_page.html")