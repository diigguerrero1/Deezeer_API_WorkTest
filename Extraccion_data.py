

import requests


def json_de_albums():
    for i in range(302027,302128):
        response = requests.get(f'https://api.deezer.com/album/{i}')

        contenido = response.content

        contenido = contenido.decode()

        file = open(f'Archivo_{i}.json', "w")   
        file.write(contenido)
        file.close()



def json_de_canciones():
    for i in range(0,50):
        response = requests.get(f'https://api.deezer.com/artist/{i}')

        contenido = response.content

        contenido = contenido.decode()

        file = open(f'DATA canciones/Archivo_{i}.json', "w")   
        file.write(contenido)
        file.close()

        file_filter = open(f'DATA canciones/Archivo_{i}.json', "r")
        if file_filter["error"]:

            
            




if __name__ == "__main__":
   json_de_canciones()