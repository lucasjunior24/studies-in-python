
import streamlit as st
import spacy

from spacy_streamlit import visualize_ner


st.title('Reconhecimento de entidades nomeadas (NER)')

caminho_medelo = './modelo_pt'
modelo = spacy.load(caminho_medelo)


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
rotulos = list(modelo.get_pipe('ner').labels)
opcoes = {
    "ents": rotulos,
    "colors": cores
}

escolha = st.radio(label = 'Escolha uma opção:', options = ['Texto', 'Arquivo'])

texto = ''

if escolha == 'Texto':
    texto = st.text_area('Insira o texto:')
elif escolha == 'Arquivo':
    arquivo = st.file_uploader('Faça o upload do arquivo (somente .txt):', type = 'txt')
    if arquivo is not None:
        texto = arquivo.read().decode('utf-8')

# if texto:
#     doc = modelo(texto)
#     st.subheader('Entidades reconhecidas:')
#     for entidade in doc.ents:
#         st.text(f'{entidade.text} -> {entidade.label_}')

doc = modelo(texto)

visualize_ner(doc, labels=rotulos, displacy_options=opcoes, title='Reconhecimento de entidades nomeadas (NER)')