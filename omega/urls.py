"""omega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .view import (home_page  ,
                   about_page ,
                   wallpanell_page ,
                   roofpanel_page ,
                   freezer_page ,
                   chiller_page ,
                   deepfreezer_page ,
                   slidingdoor_page ,
                   hingeddoors_page ,
                   cravans_page,
                   steelsheet_page ,
                   about_page2 ,
                   wallpanell_page2 ,
                   roofpanel_page2 ,
                   chiller_page2 ,
                   freezer_page2 ,
                   deepfreezer_page2 ,
                   cravans_page2 ,
                   slidingdoor_page2 ,
                   steelsheet_page2 ,
                   hingeddoors_page2 ,
                   thank
                )

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('events/', include(("events.urls","events"), namespace='events')),
    path('wallpanel/', wallpanell_page, name='wallpanel'),
    path('roofpanel/', roofpanel_page, name='roofpanel'),
    path('freezer/', freezer_page, name='freezer'),
    path('chiller/', chiller_page, name='chiller'),
    path('deepfreezer/', deepfreezer_page, name='deepfreezer'),
    path('slidingdoors/', slidingdoor_page, name='slidingdoors'),
    path('hingedoors/', hingeddoors_page, name='hingedoors'),
    path('cravans/', cravans_page, name='cravans'),
    path('steelsheet/', steelsheet_page, name='steelsheet'),
    path('about/ar', about_page2, name='about/ar'),
    path('wallpanel/ar', wallpanell_page2, name='wallpanel/ar'),
    path('roofpanel/ar', roofpanel_page2, name='roofpanel/ar'),
    path('freezer/ar', freezer_page2, name='freezer/ar'),
    path('chiller/ar', chiller_page2, name='chiller/ar'),
    path('deepfreezer/ar', deepfreezer_page2, name='deepfreezer/ar'),
    path('slidingdoors/ar', slidingdoor_page2, name='slidingdoors/ar'),
    path('hingedoors/ar', hingeddoors_page2, name='hingedoors/ar'),
    path('cravans/ar', cravans_page2, name='cravans/ar'),
    path('steelsheet/ar', steelsheet_page2, name='steelsheet/ar'),
    path('thanks/', thank, name='thank'),
    path('feedback/', include(("feedback.urls","feedback"), namespace='feedback')),
    path('arabic/', include(("arabic.urls","arabic"), namespace='arabic')),

]
if settings.DEBUG:
    # test mode
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

