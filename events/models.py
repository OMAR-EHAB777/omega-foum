import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse
from django.conf import settings


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 215445658)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class event(models.Model):
    title = models.CharField(max_length=140)
    slug = models.SlugField(blank=True, unique=True, default=id(0))
    author = models.CharField(max_length=60)
    description = models.TextField()
    publication_date = models.DateField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)


    def get_absolute_url(self):
        return "/events/{slug}/".format(slug=self.slug)
        #return reverse("events:detail", kwargs={"slug": self.slug})
    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=event)
