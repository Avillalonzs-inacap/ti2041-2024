# Gestión de Productos S.A.

Esta es una aplicación web simple para gestionar productos utilizando Django. Permite registrar y consultar productos. 

## Instrucciones para ejecutar el proyecto

1. Clonar el repositorio.
2. Acceder a la ruta `\evaluaciones`
   Recomendaciones:
   1. Crea el entorno virtual `python -m venv env`
   1. Activa el entorno virtual `.\env\Scripts\activate`
3. Instalar las dependencias con `pip install -r requirements.txt`.
4. Accede a la ruta `\gestion_productos`
3. Ejecutar `python manage.py migrate` para configurar la base de datos.
4. Ejecutar el servidor con `python manage.py runserver`.
5. Acceder a las siguientes URL:
   - `http://localhost:8000/productos/registro/` para registrar productos.
   - `http://localhost:8000/productos/consulta/` para consultar los productos.
