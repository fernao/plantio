from django.urls import path
from django.conf.urls import include

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/especie/', include('especie.urls'))
   
]
