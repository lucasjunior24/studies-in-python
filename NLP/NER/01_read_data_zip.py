import zipfile
import pandas
import spacy.displacy
with zipfile.ZipFile("./texts.zip", "r") as zip:
  # print(*zip.namelist(), sep='\n')
  with zip.open("ADI2TJDFT.txt") as arquivo:
    texto = arquivo.read().decode('utf-8')

# print(texto)

import spacy
import pt_core_news_sm


print("loading modelo")
modelo_ner = pt_core_news_sm.load()

doc = modelo_ner(texto)




entidades = []
labels = []

for entidade in doc.ents:
  entidades.append(entidade.text)
  labels.append(entidade.label_)

print(pandas.DataFrame({"Entidade": entidades, "Labels": labels}))
print()
print(modelo_ner.get_pipe("ner").labels)
print()
print(spacy.displacy.render(doc, style='ent'))