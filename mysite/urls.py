from django.contrib import admin
from django.urls import path, include
# from f_manager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('f_manager/', include('f_manager.urls')),  # Включіть шляхи з вашого додатку f_manager
]
