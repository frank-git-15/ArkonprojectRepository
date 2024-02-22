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

## APIs disponibles

```bash
    Atributos
    Cada ENDPOINT puede retornar estos atributos de un punto de acceso wifi
     - id
     - programa
     - fechaInstalacion
     - latitud
     - longitud
     - colonia
     - alcaldia   
```

1. puntosDeAccesoWifi
    ```bash
    ENDPOINT que devuelve una lista con todos los puntos de acceso wifi en la Ciudad de Mexico de manera paginada
    Parametros
        - page: numero de pagina que queremos obtener, es un tipo de dato entero
        - pageSize: cantidad de resultados que queremos por pagina, es un tipo de dato enter
    ```
3. puntoDeAcceso
   ```bash
    ENDPOINT que devuelve el punto de acceso wifi que tenga el mismo ID que se le manda como parametro
    Parametros
        - id: id del punto de acceso wifi que queremos obtener
    ```
5. puntosdeAccesoPorColonia
     ```bash
    ENDPOINT que devuelve una lista de puntos de acceso wifi en la Ciudad de Mexico pertenecientes a cierta colonia
    Parametros
        - colonia: nombre de la colonia de la cual queremos obtener todos los puntos de acceso wifi disponibles
        - page: numero de pagina que queremos obtener, es un tipo de dato entero
        - pageSize: cantidad de resultados que queremos por pagina, es un tipo de dato enter
    ```
7. puntosDeAccesoMasCercanos
     ```bash
    ENDPOINT que devuelve una lista con todos los puntos de acceso wifi en la Ciudad de Mexico ordenados desde el mas cercano a las coordenadas  dadas en los parametros
     hasta el punto mas lejano, esta lista tambien esta paginada
    Parametros
        - latitud: tipo de dato flotante
        - longitud: tipo de dato flotante
        - page: numero de pagina que queremos obtener, es un tipo de dato entero
        - pageSize: cantidad de resultados que queremos por pagina, es un tipo de dato enter
    ```
## Uso y ejemplos

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

