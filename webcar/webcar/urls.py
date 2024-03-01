from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('main.urls')),
                  path('news/', include('news.urls')),
                  path('pages/', include('django.contrib.flatpages.urls')),
                  path('products/', include('simpleapp.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', include("accounts.urls")),
                  path("accounts/", include("allauth.urls")),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
