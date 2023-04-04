import requests
import json 
import pandas as pd

def coleta():
    link = 'https://agenciatatu.com.br/wp-json/wp/v2/posts'
    requisicao = requests.get(link)
    requisicao = requisicao.json()

    quantidade_materias = [0, 1, 2]
    lista_materias = []

    for index_materia in quantidade_materias:
        titulo_materia = requisicao[index_materia]['title']['rendered']
        link_materia = requisicao[index_materia]['link']

        infos_materia = {
            'titulo_materia': titulo_materia,
            'link_materia': link_materia,
        }
        lista_materias.append(infos_materia)

    lista_materias_json = json.dumps(lista_materias)

    df_dados = pd.DataFrame(eval(lista_materias_json))

    infos_materia

    df_dados

    df_dados = df_dados.assign(site='Agência Tatu')

    df_dados = df_dados.assign(data_extracao=date.today())

    # Converter o DataFrame para uma lista de listas
    dftatu = df_dados.values.tolist()

    # Função para coletar notícias do site Marco Zero Conteúdo
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    link_marco = 'https://marcozero.org/wp-json/wp/v2/posts'  # <--- url correta
    requisicao = requests.get(link_marco)
    requisicao = requisicao.json()

    quantidade_materias_marco = [0, 1, 2]
    lista_materias_marco = []

    for index_materia_marco in quantidade_materias_marco:
        requisicao_materia_marco = requisicao[index_materia_marco]
        if 'title' in requisicao_materia_marco:
            titulo_materia = requisicao_materia_marco['title']['rendered']
        else:
            titulo_materia = ''
        if 'link' in requisicao_materia_marco:
            link_materia = requisicao_materia_marco['link']
        else:
            link_materia = ''
        infos_materia_marco = {
            'titulo_materia': titulo_materia,
            'link_materia': link_materia,
        }
        lista_materias_marco.append(infos_materia_marco)

    lista_materias_marco_json = json.dumps(lista_materias_marco)

    lista_materias_marco.append(infos_materia_marco)

    df_dados_marco = pd.DataFrame(eval(lista_materias_marco_json))

    df_dados_marco = df_dados_marco.assign(site='Marco Zero Conteúdo')

    df_dados_marco = df_dados_marco.assign(data_extracao=date.today())

    dfmarco = df_dados_marco.values.tolist()

    # Função para coletar notícias do site Eco Nordeste
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    link_eco = 'https://agenciaeconordeste.com.br/wp-json/wp/v2/posts'
    requisicao_eco = requests.get(link_eco, headers=headers).json()

    quantidade_materias_eco = [0,1,2]
    lista_materias_eco = []

    for index_materia_eco in quantidade_materias_eco:
        titulo_materia_eco = requisicao_eco[index_materia_eco]['title']['rendered']
        link_materia_eco = requisicao_eco[index_materia_eco]['link']

        infos_materia_eco = {
            'titulo_materia': titulo_materia_eco,
            'link_materia': link_materia_eco,
            }
        lista_materias_eco.append(infos_materia_eco)

    lista_materias_eco_json = json.dumps(lista_materias_eco)


    df_dados_eco = pd.DataFrame(eval(lista_materias_eco_json))

    df_dados_eco=df_dados_eco.assign(site = 'Eco Nordeste')

    df_dados_eco=df_dados_eco.assign(data_extracao=date.today()) 

    df_eco = df_dados_eco.values.tolist()

    dftotal = pd.concat([df_dados, df_dados_marco, df_dados_eco],  
                   ignore_index = True,
                   sort = False)

coleta()