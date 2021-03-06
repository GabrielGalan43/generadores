from django.contrib import admin
from generadores.models import (StatusDispositivo, TipoDispositivo,
                                Dispositivo, LecturaDispositivo,
                                )


class StatusDispositivoAdmin(admin.ModelAdmin):
    list_display = ['status_dispositivo',]   
admin.site.register(StatusDispositivo, StatusDispositivoAdmin)


class TipoDispositivoAdmin(admin.ModelAdmin):
    list_display = ['tipo',]   
admin.site.register(TipoDispositivo, TipoDispositivoAdmin)


class DispositivoAdmin(admin.ModelAdmin):
    list_display = ['nombre_equipo', 'tipo_dispositivo', 'fecha_creacion',
                    'fecha_actualizacion', 'potencia_actual',
                    'status_dispositivo',
                    ]
admin.site.register(Dispositivo, DispositivoAdmin)


class LecturaDispositivoAdmin(admin.ModelAdmin):
    list_display = ['tipo_dispositivo', 'potencia_actual',
                    'timestamp_potencia',
                    ]
admin.site.register(LecturaDispositivo, LecturaDispositivoAdmin)


