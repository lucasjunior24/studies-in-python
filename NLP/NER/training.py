import zipfile
import pandas


dados = []
with zipfile.ZipFile("./texts.zip", "r") as zip:
  # print(*zip.namelist(), sep='\n')
  for nome_arquivo in zip.namelist():
    with zip.open(nome_arquivo) as arquivo:
      conteudo = arquivo.read().decode('utf-8')
      palavras = conteudo.split()
      for palavra in palavras:
        dados.append([nome_arquivo, palavra])
# print(texto)

tabela_palavras = pandas.DataFrame(dados, columns=["Arquivo", "Palavra"])

tabela_palavras.to_csv("./palavra.csv", index=False, sep="\t")
print(tabela_palavras)


