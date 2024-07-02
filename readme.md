# Interfaz Web para Scrapear Datos
___
### 1. Resumen
Interfaz enfocada en scrapear datos de webs y almacenarlos en una base de datos (BD).

Creé este proyecto ya que tengo pensado afinar un modelo de lenguaje (LLM) en distintas especialidades y para ello necesito datos actualizados de las documentaciones en las que quiera afinar su conocimiento. Para ello, he creado esta interfaz a la que, añadiéndole en el formulario distintos parámetros, se pueden scrapear los datos y almacenarlos en una base de datos relacional. 

En otro proyecto tengo pensado usar esos datos para vectorizar los datos y pasarlos a una base de datos vectorial o RAG y así poder afinar la respuesta del LLM.

<div style="display:flex; justify-content:center; align-items:center;">
   <img src="./webs_scrapings/static/images/interfaz.png" alt="imagen" style="width: 50%;">
</div>

### 2. Requerimientos

```bash
pip install Django
pip install django-environ
pip install psycopg
pip install beautifulsoup4
pip install selenium
pip install undetected-chromedriver
```
### 3. Scrapeando 
Al enviar 