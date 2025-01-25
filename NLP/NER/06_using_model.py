import spacy

modelo_ner = spacy.load('./modelo')



# print(spacy.displacy.render(doc, style='ent', jupyter=True))
# print(spacy.displacy.render(doc, style='ent'))

with open('./texto.txt', encoding='utf-8') as arquivo:
    texto = arquivo.read()

cores = {
'B-JURISPRUDENCIA': '#F0F8FF',
 'B-LEGISLACAO': '#FA8072',
 'B-LOCAL': '#98FB98',
 'B-ORGANIZACAO': '#DDA0DD',
 'B-PESSOA': '#F0E68C',
 'B-TEMPO': '#FFB6C1',
 'I-JURISPRUDENCIA': '#F0F8FF',
 'I-LEGISLACAO': '#FA8072',
 'I-LOCAL': '#98FB98',
 'I-ORGANIZACAO': '#DDA0DD',
 'I-PESSOA': '#F0E68C',
 'I-TEMPO': '#FFB6C1',
 'LOC': '#D3D3D3',
 'MISC': '#D3D3D3',
 'ORG': '#D3D3D3',
 'PER': '#D3D3D3'
}
rotulos = list(modelo_ner.get_pipe('ner').labels)
rotulos
opcoes = {
    "ents": rotulos,
    "colors": cores
}
doc = modelo_ner(texto)
# print(spacy.displacy.render(doc, style = 'ent', jupyter = True, options = opcoes))
print(spacy.displacy.render(doc, style='ent', options = opcoes))

# modelo_ner.to_disk("./modelo")