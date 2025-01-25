import pandas

import spacy
import en_core_web_sm

tabela_palavras = pandas.read_csv("./palavras_IOB.tsv", sep='\t')

# print(tabela_palavras)
print()
# print(tabela_palavras["label"].unique())

print()

grupo_arquivos = tabela_palavras.groupby(by="arquivo")
def format_test():

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

# format_test()
print()

def format_data():
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

  print(documentos)
  print()
  return documentos

documentos = format_data()

import random
from tqdm import tqdm
from spacy.training import Example 

random.shuffle(documentos)

dados_treino = documentos[:40]
dados_validação = documentos[40:]



def treinar_modelo_ner(dados_treino: list, dados_validacao: list, epocas):
  modelo = spacy.load("en_core_web_sm")

  if 'ner' not in modelo.pipe_names:
    ner = modelo.create_pipe('ner')
    modelo.add_pipe(ner, last=True)

  else:
    ner = modelo.get_pipe('ner')
  for _, anotacoes in dados_treino:
    for entite in anotacoes.get('entities'):
      ner.add_label(entite[2])

  outros_pipelines = [pipeline for pipeline in modelo.pipe_names if pipeline != "ner"]
  with modelo.disable_pipes(*outros_pipelines):
    spacy.util.fix_random_seed()
    otimizador = modelo.create_optimizer()

    for epoca in tqdm(range(epocas), desc='Treinando modelo'):
      random.seed(10)
      random.shuffle(dados_treino)

      losses = {'ner': 0.0}

      for textos, anotacoes in dados_treino:
        exemplo = Example.from_dict(modelo.make_doc(textos), anotacoes)
        modelo.update([exemplo], drop=0.2, sgd=otimizador, losses=losses)

      print(f'\nÉpoca: {epoca} - loss médio de treino: {losses["ner"]/len(dados_treino)}')

      val_losses = {'ner': 0.0}
      exemplos = []
      for textos, anotacoes in dados_validacao:
        exemplo = Example.from_dict(modelo.make_doc(textos), anotacoes)
        exemplos.append(exemplo)

      for exemplo in exemplos:
        modelo.update([exemplo], sgd=None, drop=0, losses= val_losses)
      
      print(f'\nÉpoca: {epoca} - val_losses médio de treino: {val_losses["ner"]/len(dados_validacao)}')
  return modelo

modelo_ner = treinar_modelo_ner(dados_treino, dados_validação, 30)
import pickle

'Jeito mais pesado de pegar o modelo'
# pickle.dump(modelo_ner, open('modelo_ner.sav', 'wb'))


'Jeito mais performatico'
# modelo_ner.to_disk("./modelo")