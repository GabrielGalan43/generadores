#from django.shortcuts import render

from rest_framework import generics
# from rest_framework import viewsets
# from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from generadores.models import (StatusDispositivo, TipoDispositivo,
                                Dispositivo, LecturaDispositivo,
                                )
                                

from generadores.serializers import (StatusDispositivoSerializer, TipoDispositivoSerializer,
                                DispositivoSerializer, LecturaDispositivoSerializer,
                                )




"""
Generics CRUD Operations Status Dispositivos
"""
class ListaStatusDispositivo(generics.ListCreateAPIView):
    queryset = StatusDispositivo.objects.all()
    serializer_class = StatusDispositivoSerializer


class DetalleStatusDispositivo(generics.RetrieveUpdateDestroyAPIView):
    queryset = StatusDispositivo.objects.all()
    serializer_class = StatusDispositivoSerializer



"""
Generics CRUD Operations Tipo Dispositivos
"""
class ListaTipoDispositivo(generics.ListCreateAPIView):
    queryset = TipoDispositivo.objects.all()
    serializer_class = TipoDispositivoSerializer
    
    
class DetalleTipoDispositivo(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoDispositivo.objects.all()
    serializer_class = TipoDispositivoSerializer




"""
Generics CRUD Operations Dispositivos
"""
class ListaDispositivo(generics.ListCreateAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tipo_dispositivo']
    
    

class DetalleDispositivo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer



"""
Generics CRUD Operations Lecturas
"""
class ListaLecturaDispositivo(generics.ListCreateAPIView):
    queryset = LecturaDispositivo.objects.all()
    serializer_class = LecturaDispositivoSerializer


class DetalleLecturaDispositivo(generics.RetrieveUpdateDestroyAPIView):
    queryset = LecturaDispositivo.objects.all()
    serializer_class = LecturaDispositivoSerializer











"""
    queryset = Dispositivo.objects.all().filter(tipo_dispositivo__id=self.kwargs['pk'])
    

class BlogPostList(generics.ListCreateAPIView):
   serializer_class = BlogPostSerializer
   permission_classes = (AllowAny,)
   filter_class = BlogPostListFilter
   paginate_by = 100

   def get_queryset(self):
      queryset = BlogPost.objects.filter(pk=self.kwargs['post_id'])
      return queryset

"""