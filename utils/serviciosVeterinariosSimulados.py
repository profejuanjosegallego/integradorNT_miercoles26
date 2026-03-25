#Funcion para generar N servicios veterinarios
#En spring boot el modelo de un servicio es:

#id(Integer)
#codigo(String)
#descripcion(String)
#mascota(String)
#fecha(LocalDate)
#valor(Integer)

import random
from datetime import datetime, timedelta
def simular_servicios_vetereniarios(numeroServicios):

    #Defino atributos base
    codigos=["CA748","CA899","CA001","CA2025","CA788"]
    descripciones=["desparasitar intestinos","lavado de orejas","diagnostico digestivo","limpieza de pulgas","corte de uñas"]
    mascotas=["Pedro","Margarita","Faustino","Zuker","Salomon","Piolin"]

    #Para simular una rango de fechas debo introducir una fecha Inicial
    fechaInicial=datetime(2026,1,1)
    fechaBase=fechaInicial+timedelta(days=random.randint(0,180))

    #Ciclo para generar N registros de la tabla servicios
    servicios=[]
    for _ in range (numeroServicios):
        servicio={
            "id":random.randint(1,1000),
            "codigo":random.choice(codigos),
            "descripcion":random.choice(descripciones),
            "mascota":random.choice(mascotas),
            "fecha":fechaBase.strftime("%Y/%m/%d"),
            "valor":random.randint(200000,1200000)
        }
        servicios.append(servicio)
    return servicios






