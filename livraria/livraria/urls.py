from django.contrib import admin
from django.urls import path
from api.views import api

urlpatterns = [
    path('admin/', admin.site.urls),
    # Rota de api adicionada
    path("api/", api.urls),
]