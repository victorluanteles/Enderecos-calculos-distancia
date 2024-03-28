from geopy.geocoders import Nominatim
import requests
import pandas as pd

def obter_localizacao(endereco):
    geolocator = Nominatim(user_agent="MeuProjetoCep")
    location = geolocator.geocode(endereco)
    return location

def obter_localizacao_viacep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        resposta.raise_for_status()  # Lança uma exceção se a solicitação falhar
        dados = resposta.json()
        return dados
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter dados do ViaCEP: {e}")
        return None
    except ValueError as e:
        print(f"Erro ao decodificar JSON: {e}")
        return None

ceps = ["30620182"]  # Exemplo de lista de CEPs



for cep in ceps:
    dados_endereco = obter_localizacao_viacep(cep)
    print(dados_endereco)

    if dados_endereco:
        endereco = "SANTA LUZIA MG"
        localizacao = obter_localizacao(endereco)

        if localizacao:
            print("CEP:", cep)
            print("Latitude:", localizacao.latitude)
            print("Longitude:", localizacao.longitude)
            print("Endereço completo:", localizacao.address)

        else:
            print(f"Localização para o CEP {cep} não encontrada.")
    else:
        print(f"Dados do CEP {cep} não encontrados.")
