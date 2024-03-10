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
                  path('accounts_1/', include('django.contrib.auth.urls')),
                  path('accounts_2/', include("accounts.urls")),
                  path("accounts/", include("allauth.urls")),
                  path('projects/', include('projects.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
