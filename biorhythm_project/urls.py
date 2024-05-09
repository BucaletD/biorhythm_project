from django.contrib import admin
from django.urls import path
from biorhythm_project import views

urlpatterns = [
    path('admin/', admin.site.urls),

     path('', views.index, name='index'),
    path('calculate_biorhythm/', views.calculate_biorhythm, name='calculate_biorhythm'),
]
