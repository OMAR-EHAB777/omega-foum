
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView,View
from django.http import Http404, HttpResponse
from .models import event
import os
# Create your views here.



def get_queryset(self, *args, **kwargs):
    request = self.request
    views = request.user.objectviewed_set.by_model(event, model_queryset=False)
    return views
class eventlistView(ListView):
    queryset = event.objects.all()
    template_name = "events/event.html"


    def get_queryset(self, *args, **kwargs):
        request = self.request
        return event.objects.all()



class eventDetailSlugView( DetailView):
    queryset = event.objects.all().filter()
    template_name = "events/events-detail.html"

def get_object(self,*args,**kwargs):
   request = self.request
   slug = self.kwargs.get('slug')
   #instance = get_object_or_404(product,slug=slug,active=True)
   try:
       instance =event.objects.get(slug=slug,active=True)
   except event.DoesNotExist:
       raise Http404("NOT FOUND..")
   except event.MultipleObjectsReturned:
       qs = event.objects.filter(slug=slug, active=True)
       instance= qs.first()
   except:
       raise Http404("hmmm !")
   # object_viewed_signal.send(instance.__class__, instance=instance, request=request)
   return instance



