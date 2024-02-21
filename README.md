# API Django con GraphQL en Docker

Este proyecto es una API basada en Django que utiliza GraphQL. Puedes ejecutar la aplicación dentro de un contenedor Docker para simplificar la configuración del entorno.
Esta API consulta una base de datos de los puntos de acceso wifi en la Ciudad de Mexico, esta base de datos esta en AWS

## Ejecución con Docker

1. Clona el repositorio:

    ```bash
    https://github.com/frank-git-15/ArkonprojectRepository.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd ArkonprojectRepository
    ```

3. Construye la imagen Docker:

    ```bash
    docker build -t api-puntosdeacceso .
    ```

4. Ejecuta el contenedor:

    ```bash
    docker run -p 8000:8000 api-puntosdeacceso
    ```

   La API estará disponible en http://localhost:8000/graphql

## Uso

La API se ejecuta en `http://localhost:8000/graphql`. 
Puedes interactuar con GraphQL utilizando herramientas como GraphiQL o enviar consultas directamente. A continuación, un ejemplo de consulta GraphQL:

Ejemplo 1
{
  puntosDeAccesoWifi(page:1,pageSize:10){
    id,programa,fechaInstalacion,latitud,longitud,colonia,alcaldia
  }
}

Ejemplo 2
{
  puntoDeAcceso(id:"800786_S_02"){
    id,programa,colonia
  }
}

Ejemplo 3
{
  puntosdeAccesoPorColonia(colonia:"GUERRERO",page:1,pageSize:5) {
    id,colonia,alcaldia
  }
}

Ejemplo 4
{
  puntosDeAccesoMasCercanos(latitud:19.466,longitud:-99.105,page:1,pageSize:20){
    id
    colonia
    latitud
    longitud
  }
}

