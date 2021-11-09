from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('occupation/', include('apps.occupation.urls'))
]
