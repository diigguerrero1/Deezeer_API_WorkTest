import os
import json

from django.shortcuts import render

from .tools import remover_duplicados

from .models import Artist, Album, Song


# ETL DATA ARTISTAS

def limpieza_data_artistas():

    headers_documents = list(os.listdir('./Deezer/static'))
    counter = len(headers_documents)

    # Usaaremos estos diccionarios para darle estructura a la información

    nombres = {}
    pictures = {}
    types = {}

    # Usaremos estas listas para entregar la información final.

    names_list = []
    pictures_list = []
    types_list = []

    for num in range(0, counter):

        # Aqui se abren los archivos JSON con la info:

        with open(f'Deezer/static/{headers_documents[num]}', 'r') as file:
            document = json.load(file)

            num_obj_list_data = (len(document['data']))

            # Generaremos un bucle para ingresar datos al diccionario
        
            for i in range(num_obj_list_data):

                name_artist = document['data'][i]['artist']['name']
                nombres[i] = name_artist

                picture_artist = document['data'][i]['artist']['picture']
                pictures[i] = picture_artist
                
                type_artist = document['data'][i]['artist']['type']
                types[i] = type_artist

            # Acá limpiamos los datos repetidos con una función exportada
        
            names = remover_duplicados(nombres)
            pictures = remover_duplicados(pictures)
            type = remover_duplicados(types)
            
            # Acá se agregan los nombres a una lista
        
            artist_names_list = list(names.values())
            artist_pictures_list = list(pictures.values())
            artist_types_list = list(type.values())

            # Acá se agrega cadaa lista x archivo a una lista superior que entrega la info.
        
            names_list.append(artist_names_list)
            pictures_list.append(artist_pictures_list)
            types_list.append(artist_types_list)
            

    return names_list, pictures_list, types_list



def load_data_artists():
    
    names, pics, types = limpieza_data_artistas()

    tamaño_list_principal = len(names)

    for i in range(tamaño_list_principal):
        list_names = names[i]
        list_pics = pics[i]
        list_types = types[i]

        print(list_types)
        
        for j in range(len(list_pics)):

            artist = Artist()

            artist.name = list_names[j]
            artist.picture = list_pics[j]
            artist.type = str(list_types[0])

            artist.save()
           
        print('Se han cargado los datos')
    
            
            

# ETL DATA ALBUMS


def limpieza_data_albums():
    
    headers_documents = os.listdir('./Deezer/static')
    counter = len(headers_documents)

    titles = {}
    tracklist = {}
    types = {}


   # for i in range(counter):

    with open(f'Deezer/static/{headers_documents[0]}', 'r') as file:
        document = json.load(file)

        num_obj_list_data = (len(document['data']))

        for i in range(num_obj_list_data):

            title_albums = document['data'][i]['album']['title']
            titles[i] = title_albums

            tracklist_album = document['data'][i]['album']['tracklist']
            tracklist[i] = tracklist_album
            
            type_albums = document['data'][i]['album']['type']
            types[i] = type_albums
        
        
        titles = remover_duplicados(titles)
        tracklist = remover_duplicados(tracklist)
        type = remover_duplicados(types)

        albums_titles_list = list(titles.values())
        album_tracklist_list = list(tracklist.values())
        album_types_list = list(type.values())

        types = []

        for i in range(len(albums_titles_list)):
            type = album_types_list[i]
            types.append(type)

        return albums_titles_list, album_tracklist_list, types
        


def limpieza_data_songs():

    headers_documents = os.listdir('./Deezer/static')
    counter = len(headers_documents)

    with open(f'Deezer/static/{headers_documents[0]}', 'r') as file:
        document = json.load(file)

        num_obj_list_data = (len(document['data']))

        titles = {}
        artist = {}
        album = {}
        link = {}
        duration = {}
        types = {}

        for i in range(num_obj_list_data):
    
            title_song = document['data'][i]['title']
            titles[i] = title_song

            artist_song = document['data'][i]['artist']['name']
            artist[i] = artist_song

            album_song = document['data'][i]['album']['title']
            album[i] = album_song

            link_song = document['data'][i]['link']
            link[i] = link_song
            
            duration_song = document['data'][i]['duration']
            duration[i] = duration_song
            
            type_song = document['data'][i]['type']
            types[i] = type_song

        return titles, artist, album, link, duration, types









            # picture_artist = document['data'][i]['title']
            # type_artist = document['data'][i]['title']
            # status_artist = document['data'][i]['title']
            
            # title_album = document['data'][i]['title']
            # picture_album = document['data'][i]['title']
            # artist_album = document['data'][i]['title']
            # duration_album = document['data'][i]['title']
            # tracklist_album = document['data'][i]['title']
            # type_album = document['data'][i]['title']

            # title_song = document['data'][i]['title']
            # picture_song = document['data'][i]['title']
            # artist_song = document['data'][i]['title']
            # album_song = document['data'][i]['title']
            # status_song = document['data'][i]['title']
            # link_song = document['data'][i]['title']
            # duration_song = document['data'][i]['title']
            # type_song = document['data'][i]['title']