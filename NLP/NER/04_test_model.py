import spacy

modelo_ner = spacy.load('./modelo')

doc = modelo_ner("João nasceu dia 04/12/1998 em Brasilia")


for entidade in doc.ents:

  print(f'{entidade.text} -> {entidade.label_}')


# print(spacy.displacy.render(doc, style='ent', jupyter=True))
# print(spacy.displacy.render(doc, style='ent'))

with open('./texto.txt', encoding='utf-8') as arquivo:
    texto = arquivo.read()


print(texto)