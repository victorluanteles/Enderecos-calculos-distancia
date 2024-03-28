import requests
import pandas as pd
import openpyxl
def obter_localizacao_viacep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    dados = resposta.json()

    return dados

cep = "30130300"  # CEP da Praça Sete de Setembro em Belo Horizonte

dados_endereco = obter_localizacao_viacep(cep)

if "erro" not in dados_endereco:
    df = pd.DataFrame({
        "CEP": [dados_endereco["cep"]],
        "Logradouro": [dados_endereco["logradouro"]],
        "Complemento": [dados_endereco["complemento"]],
        "Bairro": [dados_endereco["bairro"]],
        "Cidade": [dados_endereco["localidade"]],
        "Estado": [dados_endereco["uf"]],
    })

    # Criando a coluna com as informações de logradouro, bairro e localidade
    df["Endereço Completo"] = df["Logradouro"] + ", " + df["Bairro"] + ", " + df["Cidade"]

    nome_arquivo = "endereco_via_cep.xlsx"
    df.to_excel(nome_arquivo, index=False)
    print(f"DataFrame salvo como '{nome_arquivo}'")
    print(dados_endereco)
else:
    print("CEP não encontrado.")