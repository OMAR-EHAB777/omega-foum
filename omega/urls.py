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
from .view import home_page  ,about_page , wallpanell_page , roofpanel_page ,freezer_page,chiller_page,deepfreezer_page,slidingdoor_page,hingeddoors_page,cravans_page,steelsheet_page

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

]
if settings.DEBUG:
    # test mode
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

