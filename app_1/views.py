from django.shortcuts import render
from .models import Message

# Create your views here.

def main_page(request):
    
    # get first data-object from sqlite3 database
    message = Message.objects.first()

    # return the html template and the message instance
    return render(request, "main_page.html", {'Message': message})