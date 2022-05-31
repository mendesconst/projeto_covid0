from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from usuarios.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('home/', include('cursos.urls')),
    path('', login, name='home')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

