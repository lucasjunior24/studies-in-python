ola = "Ola mundo";

texto = "Sou um texto"
# linguaem fracamente tipada

"""
Comentario mutiplas linhas
num = 1
num = 43323
num = 3
"""
num = "Oi"; num = 3.2

print(num);
print(ola + " - " + texto);



# aula 2
print("");
print("aula 2");

if 10 > 2:
  print("Maior");
  print("aula 2");
print("Fim");


# aula 3 - VARIÁVEIS
print("");
print("aula 3");
num0=num1=num2=0
print(num0);
print(num1);
print(num2);

canal = "CFB Cursos"
def cn():
    print(canal);
cn();

# Esccopo global
def cn2():
    global canalGlobal
    canalGlobal = "Texto canal variável global 2";
    
cn2();
# acessando variavel com escopo global
print(canalGlobal);


# aula 4 - Tipos de dados
print("");
print("aula 4");

x=1 #int
x="Texto" #string
x=3.6 # float
x=True #bool

print("");
print("Números Complexos");
n1=5;n2=2;n=complex(n1,n2);

print(n.real);
print(n.imag);
print("Valor: "+str(n));
print("Tipo: "+str(type(n)));

print("");
print("Valor: "+str(x));
print("Tipo: "+str(type(x)));

print("");
print("(listas / List) = array");
# aceita tipo de dados diferentes
lista = ["Carro", "Avião", "Moto", 2, False, 434.43] #List / Array"

# Acessandp atributo
print("Valor: "+lista[0]);
print("Valor: "+str(lista));

# possivel subistituir elementos
lista[0] = "Mudado nome"
print("Valor: "+lista[0]);
print("Valor: "+str(lista));
print("Tipo: "+str(type(lista)));
# Da erro
# listIndex = lista[3]

print("");
print("range em listas");
# cria um list de 0 a 100 com range
meuRange=range(0, 100, 1)
print(meuRange);
print("Valor: "+str(meuRange[0]));
print("Valor: "+str(meuRange[99]));
print("Valor: "+str(meuRange));
print("Tipo: "+str(type(meuRange)));

#tipo dictionary (Dict), elemento chave e valor 
print("");
print("dictionary / Dict");
testeDictionary = {
    "chave 1": "valor 1",
    1: "teste valor 2",
    "chave 3": "valor 3"
}

print("Valor: "+str(testeDictionary["chave 1"]));
print("Tipo: "+str(type(testeDictionary)));


print("");
print("Tipo Set");
print("Esse tipo não repete valores");
testeSet = {3, 3, 5, 65, 53, 3, 6, 7}
print("Valor: "+str(testeSet));
print("Tipo: "+str(type(testeSet)));

print("");
print("Tupla");
tupla = ("Carro", "Avião", "Moto", 2, False, 434.43) #Tupla

# Acessandp atributo
print("Valor: "+tupla[0]);
print("Valor: "+str(tupla));

# tupla[0] = "Não é possivel subistituir elementos"
# Da erro
# print("Valor: "+tupla[0]);
# print("Valor: "+str(tupla));
print("Tipo: "+str(type(tupla)));
