from django.shortcuts import render


def home_page(request):
    #print(request.session.get('first_name','UNKNOWN '))
    context = {
        "title": "mashy"
    }
    return render(request, "index.html", {})
def events_page(request):
    return render(request, "events.html", {})


def product_page(request):
    return render(request, "products.html", {})