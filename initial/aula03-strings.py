print("Strings em python")

curso = "Curso de python"
print(curso[9])
print(curso[0])
print(curso[0:4])

print("tamanho da string = " + str(len(curso))) #método len retorna o tamanho da string
print("tamanho da string = ", len("c"))

print("")
print("# método strip remove espaços inicial e final de frases")
comEspaco = " Curso de python "
print("tamanho da string = ", len(comEspaco))
semEspaço = comEspaco.strip()
print(semEspaço)
print("tamanho da string = ", len(semEspaço))


print("")
print("# método replace substitue string ou caracter por outra string ou caracter")
usandoReplace = curso.replace("python", "C#")
print(usandoReplace)

deixatudoMaiusculo = curso.upper()
print(deixatudoMaiusculo)

deixaTudoMinusculo = curso.lower()
print(deixaTudoMinusculo)


print("")
print("# método split faz cortes nas strings, separando as palavras pelo parametro infomado, retornado um array de strings")
usandoSplit = curso.split("o")
print(usandoSplit)

usandoSplit = curso.split(" ")
print(usandoSplit)
print(usandoSplit[0])

print("")
print("# in - ele server pra verificar se palavra ou caracte esta contida na string")
print("#Eetorna true se contem e false se não contem")
curso = curso.lower()

usandoIn = "python" in curso;
print(usandoIn)

usandoVariavel = "python"
usandoIn = usandoVariavel.upper() in curso.upper();
print(usandoIn)

# verificando se contem palavra carro na variavel curso
usandoIn = "carro" in curso;
print(usandoIn)


print("")
print("# not in - ele server pra verificar se palavra ou caractte não esta contida na string")
usandoNotIn = "python" not in curso;
print(usandoNotIn)



print("")
print("# Concatenando strings")
fraseTeste = " para todo mundo"
palavraConcatenada = curso + fraseTeste;
print(palavraConcatenada)

print("# Formatando strings")
cidade= "Belo Horizonte"
dia= 24
mes = "Dezembro"
ano = 2022
textoFormatado = "{}, {} de {} de {} - \"{}\""
print(textoFormatado.format(cidade, dia, mes, ano,curso.upper()))
