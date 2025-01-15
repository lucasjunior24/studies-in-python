import pandas


tabela_palavras = pandas.read_csv("./palavras_IOB.tsv", sep='\t')

print(tabela_palavras)
print()
print(tabela_palavras["label"].unique())