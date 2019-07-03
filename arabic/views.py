from django.shortcuts import render
#from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
# Create your views here.
def home_page2(request):
    return render(request, "arabic/index2.html", {})
def about_page2(request):
    return render(request, "about3.html", {})
def product_page2(request):
    return render(request, "products2.html", {})
def wallpanell_page2(request):
    return render(request, "wallpanel2.html", {})
def roofpanel_page2(request):
    return render(request, "roofpanel3.html", {})
def chiller_page2(request):
    return render(request, "chiller2.html", {})
def freezer_page2(request):
    return render(request, "freezer2.html", {})
def deepfreezer_page2(request):
    return render(request, "DEEPFREEZER2.html", {})
def hingeddoors_page2(request):
    return render(request, "HINGEDDOORS2.html", {})
def slidingdoor_page2(request):
    return render(request, "SLIDINGDOORS2.html", {})
def cravans_page2(request):
    return render(request, "CARAVANS2.html", {})
def steelsheet_page2(request):
    return render(request, "STEEL-SHEETS2.html", {})