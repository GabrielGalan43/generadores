def run():
    datatest = open('dispositivos.csv')
    reader = csv.reader(datatest)

    Dispositivo.objects.all().delete()
    

    for row in reader:
        print(row)

        Dispositivo.objects.get_or_create(nombre_equipo=row[0],
                                          tipo_dispositivo=row[1],
                                          potencia_actual=row[2],
                                          status_dispositivo=row[3])          



if __name__=='__main__':
    import django
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'planta_energia.settings')
    import csv
    django.setup()
    from generadores.models import Dispositivo

    run()