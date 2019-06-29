from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template
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
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('thank')

    return render(request, 'contact.html', {
        'form': form_class,
})


def thank(request):
    return render(request, "contactt-successs.html", {})