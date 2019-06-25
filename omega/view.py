from django.shortcuts import render


def home_page(request):
    return render(request, "index.html", {})
def about_page(request):
    return render(request, "about.html", {})
def product_page(request):
    return render(request, "products.html", {})
def wallpanell_page(request):
    return render(request, "wallpanel.html", {})
def roofpanel_page(request):
    return render(request, "roofpanel.html", {})
def chiller_page(request):
    return render(request, "CHILLER.html", {})
def freezer_page(request):
    return render(request, "FREEZER.html", {})
def deepfreezer_page(request):
    return render(request, "DEEPFREEZER.html", {})
def hingeddoors_page(request):
    return render(request, "HINGEDDOORS.html", {})
def slidingdoor_page(request):
    return render(request, "SLIDINGDOORS.html", {})
def cravans_page(request):
    return render(request, "CARAVANS.html", {})
def steelsheet_page(request):
    return render(request, "STEEL-SHEETS.html", {})
def contact_page(request):
    return render(request, "contact.html", {})


