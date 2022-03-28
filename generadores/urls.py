from django.urls import path
from . import views


from generadores.views import (ListaDispositivo, DetalleDispositivo,
                               ListaTipoDispositivo, ListaStatusDispositivo,
                               ListaLecturaDispositivo, DetalleLecturaDispositivo,)



urlpatterns = [        
    path('dispositivos/', views.ListaDispositivo.as_view()),
    path('dispositivo/<int:pk>', views.DetalleDispositivo.as_view()),
    
    path('tipo_dispositivo/', views.ListaTipoDispositivo.as_view()),
    path('status_dispositivo/', views.ListaStatusDispositivo.as_view()),
    
    path('lecturas/', views.ListaLecturaDispositivo.as_view()),
    path('lectura/<int:pk>', views.DetalleLecturaDispositivo.as_view()),     
]
