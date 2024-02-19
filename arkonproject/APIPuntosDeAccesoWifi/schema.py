import graphene
from graphene_django import DjangoObjectType
from .models import WifiAccesPoint
from django.core.paginator import Paginator


#Aqui se define que datos del modelo se pueden consultar
class WifiAccesPointType(DjangoObjectType):
    class Meta:
        model = WifiAccesPoint
        fields = ("id","programa","fecha_instalacion","latitud","longitud","colonia","alcaldia")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value = "Hello")
    puntosDeAccesoWifi = graphene.List(WifiAccesPointType,page=graphene.Int(),pageSize=graphene.Int())
    puntoDeAcceso = graphene.Field(WifiAccesPointType,id= graphene.String(required=True))

    def resolve_puntosDeAccesoWifi(self,info,page,pageSize):
            #Aqui se realiza la consulta a base de datos para eso usamos el modelo PuntoDeAccesoWifi 
            #que es el modelo de la base de datos, consultamos todos lo objetos
            try:
                queryset = WifiAccesPoint.objects.all()
                #Paginar los resultados
                #Se dividen los resultados de la consulta en el tamaño de pagina deseada
                paginator = Paginator(queryset,pageSize)

                #Se obtiene la pagina deseada
                paginated_query = paginator.get_page(page)


                return paginated_query
            except WifiAccesPoint.DoesNotExist:
                return []

    def resolve_puntoDeAcceso(self,info,id):
        try:
            return WifiAccesPoint.objects.get(id=id)
        except WifiAccesPoint.DoesNotExist:
             return None



schema = graphene.Schema(query=Query)