import pandas


tabela_palavras = pandas.read_csv("./palavras_IOB.tsv", sep='\t')

# print(tabela_palavras)
print()
# print(tabela_palavras["label"].unique())

print()

grupo_arquivos = tabela_palavras.groupby(by="arquivo")

tabela_agrupada = grupo_arquivos.get_group("ADI2TJDFT.txt")[['palavra', 'label']].values

conteudo = ''
anotacoes = {"entities": []}
inicio_palavra = 0
final_palavra = 0


for texto, label in tabela_agrupada:
  texto = str(texto)
  tamanho_texto = len(texto)+1

  inicio_palavra = final_palavra
  final_palavra = inicio_palavra + tamanho_texto

  if label != "O":
    anotacao = (inicio_palavra, final_palavra-1, label)
    anotacoes["entities"].append(anotacao)

  conteudo = conteudo + texto + ' '



print(conteudo.find("Conselho Especial"))
print()
arquivos = grupo_arquivos.groups.keys()
print(arquivos)

documentos = []
for arquivo in arquivos:
  documento = []
  tabela_agrupada = grupo_arquivos.get_group(arquivo)[['palavra', 'label']].values

  conteudo = ''
  anotacoes = {"entities": []}
  inicio_palavra = 0
  final_palavra = 0

  for texto, label in tabela_agrupada:
    texto = str(texto)
    tamanho_texto = len(texto)+1

    inicio_palavra = final_palavra
    final_palavra = inicio_palavra + tamanho_texto

    if label != "O":
      anotacao = (inicio_palavra, final_palavra-1, label)
      anotacoes["entities"].append(anotacao)

    conteudo = conteudo + texto + ' '
  
  documento = (conteudo, anotacoes)
  documentos.append(documento)