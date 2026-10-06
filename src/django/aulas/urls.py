from django.urls import path
from .views import nuevoHello, bye, edad, cumpleanios

urlpatterns = [
    path('hello', nuevoHello, name='hello'),
    path('bye', bye, name='bye'),
    path('edad/<int:anios>', edad, name='edad'),
    path('cumpleanios/<int:anios>/<int:futuro>', cumpleanios, name='cumpleanios'),
]
