from rest_framework import serializers

from generadores.models import (StatusDispositivo, TipoDispositivo,
                                Dispositivo, LecturaDispositivo,
                                )


class StatusDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusDispositivo
        fields = '__all__'


class TipoDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDispositivo
        fields = '__all__'
        

class DispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispositivo
        fields = '__all__'
        #depth = 1
        

class LecturaDispositivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturaDispositivo
        fields = '__all__'
