import os
import json

from django.shortcuts import render

from .tools import remover_duplicados


def limpieza_data_artistas():

    headers_documents = os.listdir('./Deezer/static')
    counter = len(headers_documents)

   # for i in range(counter):

    with open(f'Deezer/static/{headers_documents[0]}', 'r') as file:
        document = json.load(file)

        num_obj_list_data = (len(document['data']))

        ids = {}
        nombres = {}
        pictures = {}
        types = {}

        for i in range(num_obj_list_data):

            name_artist = document['data'][i]['artist']['name']
            nombres[i] = name_artist

            picture_artist = document['data'][i]['artist']['picture']
            pictures[i] = picture_artist
            
            type_artist = document['data'][i]['artist']['type']
            types[i] = type_artist

        id = remover_duplicados(ids)
        names = remover_duplicados(nombres)
        pictures = remover_duplicados(pictures)
        type = remover_duplicados(types)
        
        artist_id_list = list(id.values())
        artist_names_list = list(names.values())
        artist_pictures_list = list(pictures.values())
        artist_types_list = list(type.values())

    return artist_id_list, artist_names_list, artist_pictures_list, artist_types_list



def limpieza_data_albums():
    
    headers_documents = os.listdir('./Deezer/static')
    counter = len(headers_documents)

   # for i in range(counter):

    with open(f'Deezer/static/{headers_documents[0]}', 'r') as file:
        document = json.load(file)

        num_obj_list_data = (len(document['data']))

        titles = {}
        tracklist = {}
        types = {}

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
            type = album_types_list[0]
            types.append(type)

        return print(albums_titles_list, album_tracklist_list, types)
        


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

        print(titles, artist, album, link, duration, types)



def load_data(data):
    pass








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