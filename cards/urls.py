from django.conf import settings
from django.conf.urls import url
from .import views
from django.conf.urls.static import static


app_name = 'cards'

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^flashcard/(?P<flashcard_id>\d+)$', views.flashcard, name = 'theflash')
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
