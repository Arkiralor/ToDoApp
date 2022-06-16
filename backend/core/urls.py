from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('api/', include('api.urls')),
]

if settings.DEBUG or settings.ENV_TYPE=='dev':
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]

if settings.ENV_TYPE=='prod':
    urlpatterns += [
        path('hash-table-admin/', admin.site.urls),
    ]
