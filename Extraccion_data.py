import requests



def json_bajar_data():

    nombres = ['eminem', 'daftpunk', 'queen', 'vicentefernandez', 'jbalvin', 'adam_beyer', 'snoopdogg', 'gorillaz', 'phoenix', 'therollingstones', 'jenniferlopez', 'Eric Prydz', 'crazyfrog', 'barrywhite', 'christinemilton', 'thebeatles', 'manuchao', 'carlcox', 'benklock', 'trym', 'ihatemodels', 'miranda', 'kobosil', 'rivastarr','radioslave','nointellectualproperty','theprodigy','hooligans','marcanghony','seanpaul','christinavidal','50cent','fatboyslim','thechemicalbrothers', 'ladygaga']

    conteo = len(nombres)

    for i in range(conteo):
        response = requests.get(f'https://api.deezer.com/search?q={nombres[i]}')

        contenido = response.content

        contenido = contenido.decode()

        with open(f'Archivo_{nombres[i]}.json', "w") as file:  
            file.write(contenido)
            print(file)



if __name__ == "__main__":

    json_bajar_data()

