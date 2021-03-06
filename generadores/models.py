from django.db import models



class StatusDispositivo(models.Model):
    status_dispositivo = models.CharField(max_length=50, primary_key=True)
    
    class Meta:
        db_table = 'Status Dispositivo' # Nombre de la tabla.
        verbose_name_plural = 'Status de Dispositivos' # Nombre de la tabla en plural.
        
    def __str__(self):
        return self.status_dispositivo
    
        
    
class TipoDispositivo(models.Model):
    tipo = models.CharField(max_length=50, primary_key=True)
    
    class Meta:
        db_table = 'Tipo Dispositivo' # Nombre de la tabla.
        verbose_name_plural = 'Tipos de Dispositivo' # Nombre de la tabla en plural.

    def __str__(self):
        return self.tipo   



class Dispositivo(models.Model):
    nombre_equipo = models.CharField(max_length=50, unique=True, primary_key=True)
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    potencia_actual = models.IntegerField()
    status_dispositivo = models.ForeignKey(StatusDispositivo, on_delete=models.CASCADE)
        
    class Meta:
        db_table = 'Dispositivo' # Nombre de la tabla.
        verbose_name_plural = 'Dispositivos' # Nombre de la tabla en plural.
        

    def __str__(self):
        return self.nombre_equipo



class LecturaDispositivo(models.Model):
    #dispositivo = models.ForeignKey(Dispositivo, on_delete= models.CASCADE)    
    tipo_dispositivo = models.ForeignKey(TipoDispositivo, on_delete= models.CASCADE)
    potencia_actual = models.IntegerField()
    timestamp_potencia = models.DateTimeField(auto_now_add=True)
    dispositivo = models.ManyToManyField(Dispositivo)
    
    class Meta:
        db_table = 'Lectura Dispositivo' # Nombre de la tabla.
        verbose_name_plural = 'Lectura Dispositivos' # Nombre de la tabla en plural.
    
    def __str__(self):
        return str(self.tipo_dispositivo)