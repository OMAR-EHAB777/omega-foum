from django.conf.urls import url
from .views import (
              home_page2,
             
)
urlpatterns = [
    url(r'', home_page2, name='home/ar')  
]
