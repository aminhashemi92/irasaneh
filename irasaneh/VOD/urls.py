from django.urls import path
from .views import *


app_name = "VOD"

urlpatterns = [
    path('', ResanehList.as_view(), name='list'),
    path('<int:pk>', ResanehDetail.as_view(), name='detail'),

    path('advideo/', AdVideoList.as_view(), name='list-video'),
    path('advideo/<int:pk>', AdVideoDetail.as_view(), name='detail-video'),
    path('adbox/', AdBoxList.as_view(), name='list-box'),
    path('adbox/<int:pk>', AdBoxDetail.as_view(), name='detail-box'),
    path('adevent/', AdEventList.as_view(), name='list-event'),
    path('adevent/<int:pk>', AdEventDetail.as_view(), name='detail-event'),

    path('AdConnectionLog/', AdConnectionLogPost.as_view(), name='AdConnectionLog'),
    path('AdApplicationLog/', AdApplicationLogPost.as_view(), name='AdApplicationLog'),
    path('AdVideoLog/', AdVideoLogPost.as_view(), name='AdVideoLog'),
    path('AdVideoCounterLog/', AdVideoCounterLogPost.as_view(), name='AdVideoCounterLog'),

    path('AdMyBox/<int:pk>', AdMyBox.as_view(), name='AdMyBox'),
    path('AdMyResanehs/<str:phone>', AdMyResanehs.as_view(), name='AdMyResanehs'),
    # path('AdMyResanehs/<int:pk>', AdMyResanehs.as_view(), name='AdMyResanehs'),
    path('test/', testapi, name='test'),



]
