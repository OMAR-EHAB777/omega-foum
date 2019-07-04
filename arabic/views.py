from django.shortcuts import render
#from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
# Create your views here.
def home_page2(request):
    return render(request, "arabic/index2.html", {})
