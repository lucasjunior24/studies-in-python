
import pickle


modelo_ner = pickle.load(open('modelo_ner.sav', 'rb'))

doc = modelo_ner("João nasceu dia 04/12/1998 em Brasilia")


for entidade in doc.ents:

  print(f'{entidade.text} -> {entidade.label_}')


