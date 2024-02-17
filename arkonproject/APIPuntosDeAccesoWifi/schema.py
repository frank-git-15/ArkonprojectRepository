import graphene
from graphene_django import DjangoObjectType
from .models import WifiAccesPoint


#Aqui se define que datos del modelo se pueden consultar
class WifiAccesPointType(DjangoObjectType):
    class Meta:
        model = WifiAccesPoint
        fields = ("id","programa","fecha_instalacion","latitud","longitud","colonia","alcaldia","distancia")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value = "Hello")



schema = graphene.Schema(query=Query)