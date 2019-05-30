from django.shortcuts import render


def home_page(request):
    return render(request, "index.html", {})
def events_page(request):
    return render(request, "events2.html", {})
def product_page(request):
    return render(request, "products.html", {})