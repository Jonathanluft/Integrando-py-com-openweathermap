#!/usr/bin/env python
# coding: utf-8

# In[12]:


# permite fazer chamadas na internet (HTTP)
import requests

#A função será usada para fins de organização
def obter_clima(cidade, api_key):
    #criacao de url base e parametros
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    parametros = {
        'q': cidade,
        'appid': api_key,
        'units': 'metric',
        'lang': 'pt_br'
    }
    
    try:
        #faz a requisição da API 
        resposta = requests.get(base_url, params=parametros)
        
                          
        #verifica se a requisição foi bem sucedida sendo 4xx ou 5xx um erro
        resposta.raise_for_status()  
        
        #retorna a resposta, em formato de dicinário
        return resposta.json()
        
        #RequestException trata varios tipos de erros de uma vez
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None

# Configurações
API_KEY = "13ba7b34c4c1d8c96ee4d6fbb3292b5a"
CIDADE = "Ivoti"

# Obter dados do clima
dados_clima = obter_clima(CIDADE, API_KEY
                         
#verifica se a função não retornou None
if dados_clima:
    #Buscando a condição do tempo
    try:
        condicao = (dados_clima['weather'][0]['main'])
    except KeyError as e:
        print(f"Erro ao processar os dados: campo {e} não encontrado na resposta")

#integração com sistema de controle
#variaveis do sistema
sensor_umidade = 29 #buscar no codigo principal
bomba_irrigação = False

#A bomba sera ligada se a umidade for menor que 50% e a condição do tempo não seja: chuvisco, chuva ou tempestade
bomba_irrigação = (True if sensor_umidade < 50 and condicao not in ['Rain','Drizzle','Thunderstorm'] else False)
print('Bomba de irrigação ligada') if bomba_irrigação == True else print('Bomba de irrigação desligada')

