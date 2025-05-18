"""
Imagina que esta API es una biblioteca de peliculas.. la funcion load_movies() es como un bibliotecario que carga el catalogo de libros (pelicula) cuando se abre la biblioteca. la funcion get_movies() muestra todo el catalogo cuando alguien lo pide. La funcion get_movie(id) es como si alguien preguntara por una pelicula especifica por su codigo de identificacion. la funcion chatbot (query) es un asistente que busca peliculas segun palabras claves y sinonimo. la funcion get_movies_by_category(category) ayuda a encontrar peliculas segun su genero (acción, comedia, etc)  
"""

# Importamos las herramientas para construir nuesta API 
from fastapi import FastAPI, HTTPException # FastAPI nos ayuda a crear la API, HTTPException maneja errores
from fastapi.responses import HTMLResponse, JSONResponse # HTMLResponse para paginas web, JSONResponse para respuestas en formato JSON
import pandas as pd #p pandas nos ayuda a manejar datos en tablas como si fuera un excel.
import nltk #nltk es un libreria para procesar texto y analizar palabras
from nltk.tokenize import word_tokenize # Se usa para dividir un texto en palabras individuales
from nltk. corpus import wordnet # Nos ayuda a encontrar sinonomos de palabras


