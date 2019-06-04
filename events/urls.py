from django.conf.urls import url
from .views import (
                            eventlistView,
                            eventDetailSlugView,

                            )


urlpatterns = [


    url(r'^$', eventlistView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', eventDetailSlugView.as_view(), name='detail'),


    ]
