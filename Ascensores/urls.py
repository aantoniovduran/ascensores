from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from Pagina import views as viewsPag
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('Pagina.urls')),    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)