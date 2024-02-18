import json
import pytest
from graphene.test import Client
from django.test import TestCase
from APIPuntosDeAccesoWifi.schema import schema 
from APIPuntosDeAccesoWifi.models import WifiAccesPoint

@pytest.mark.django_db
def test_puntosDeAccesoWifi_endpoint():
    # Creacion de un cliente GraphQL
    WifiAccesPoint.objects.create(id="mi id",programa="mi porgrama",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia",alcaldia="mi alcaldia")
    WifiAccesPoint.objects.create(id="mi id2",programa="mi porgrama2",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia2",alcaldia="mi alcaldia2")
    WifiAccesPoint.objects.create(id="mi id3",programa="mi porgrama3",fecha_instalacion="2016-02-25",latitud=129,longitud=129,colonia="Mi colonia3",alcaldia="mi alcaldia3")
    client = Client(schema)

    # Definicion de la consulta GraphQL
    query = '''
        query {
            puntosDeAccesoWifi(page:1,pageSize:2){
                id
                programa
                latitud
                longitud
                alcaldia
        }
        }
    '''

    # Ejecucion de la consulta
    response = client.execute(query)
    print("Response ....")
    print(response)

    # Verificar que la respuesta no contiene errores
    assert "errors" not in response

    #Obtener cantidad de resultados
    cantidad_de_resultados = len(response["data"]["puntosDeAccesoWifi"])
    print(cantidad_de_resultados)
    #Comprobar que solo se obtuvieron 2 resultados
    assert cantidad_de_resultados == 2
    
    #Comprobar que el id del primero resultado es "mi id"
    #obtener el id del primer resultado
    puntos = response["data"]["puntosDeAccesoWifi"]
    id_primer_resultado = puntos[0]["id"]
    assert "mi id" == id_primer_resultado

