from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas principales
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    # Apps
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    path('messages/', include(('messaging.urls', 'messaging'), namespace='messaging')),
]

# Archivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
