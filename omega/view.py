from django.shortcuts import render


def home_page(request):
    #print(request.session.get('first_name','UNKNOWN '))
    context = {
        "title": "mashy"
    }
    return render(request, "index.html", {})