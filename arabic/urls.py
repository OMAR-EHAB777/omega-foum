from django.conf.urls import url
from .views import (
              home_page2,
              about_page2,
              wallpanell_page2,
              roofpanel_page2,
              chiller_page2,
              freezer_page2,
              deepfreezer_page2,
              cravans_page2,
              slidingdoor_page2,
              steelsheet_page2,
              hingeddoors_page2
)
urlpatterns = [
    url(r'', home_page2, name='home/ar'),
     url(r'about2/', about_page2, name='about2'),
    url('wallpanel2/', wallpanell_page2, name='wallpanel/ar'),
    url('roofpanel2/', roofpanel_page2, name='roofpanel/ar'),
    url('freezer2/', freezer_page2, name='freezer/ar'),
    url('chiller2/', chiller_page2, name='chiller/ar'),
    url('deepfreezer2/', deepfreezer_page2, name='deepfreezer/ar'),
    url('slidingdoors2/', slidingdoor_page2, name='slidingdoors/ar'),
    url('hingedoors2/', hingeddoors_page2, name='hingedoors/ar'),
    url('cravans2/', cravans_page2, name='cravans/ar'),
    url('steelsheet2/', steelsheet_page2, name='steelsheet/ar'),
]
