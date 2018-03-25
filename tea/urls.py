# All of the URLS for the project
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings



from . import views

urlpatterns = [
    url(r'^$', views.TeaListView.as_view(), name='index'),
] + static("media", document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
