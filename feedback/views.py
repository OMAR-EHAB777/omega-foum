from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import FeedbackForm
# Create your views here.
def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO,'thanks')
            return redirect('thank')
    else:
        f = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': f})