from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hom$', views.landing_page, name='home'),
    url(r'^secure$', views.secure, name='secure'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)