FROM python:3.9

WORKDIR /app


COPY requirements.txt .

#Se instalan las dependencias requeridas
RUN pip install -r requirements.txt

#Se copian todos los archivos a docker
COPY . .

#Se realizan las migraciones parrevisar sí hay cambios en el codigo respecto a la base de datos que se deban hacer
RUN python arkonproject/manage.py makemigrations
#Aplicar los cambios correspondientes a la base de datos
RUN python arkonproject/manage.py migrate

#Correr servidor de djago en el puerto 8000
CMD ["python","arkonproject/manage.py","runserver","0.0.0.0:8000"]