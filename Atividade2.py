#EXERCÍCIO 1
def numeros_impares(lista):
    
    lista_impar = [n for n in lista if n % 2 !=0]
    return lista_impar

lista1 = [1,2,3,4,5,6,7,8,9,10]

lista_impar = numeros_impares(lista1)

print(f" A lista original é: {lista1}")
print(f" A lista de números ímpares é: {lista_impar}")


#EXERCÍCIO 2
def numeros_primos(lista):
    lista_primos = []

    for n in lista:
        if n > 1:
            for j in range(2, n):
                if (n % j) == 0:
                    break
            else:
                lista_primos.append(n)

    return lista_primos

lista_normal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

primos = numeros_primos(lista_normal)
print(f" A lista de números primos é: {primos}")


#EXERCÍCIO 3

def elementos_unicos_lista(lista1, lista2):

    lista_unicos = []

    for i in lista1:
        for j in lista2:
            if (i in lista2) and (j in lista1):
                break
        else:
            lista_unicos.append(i)
            lista_unicos.append(j)
            lista_unicos_final = set(lista_unicos)

    return lista_unicos_final

lista1 = ['balas', 'abacaxis', 'pêra', 'rum', 'tênis']

lista2 = ['tênis', 'rum', 'orla', 'mar', 'balas', 3]

lista_final = elementos_unicos_lista(lista1, lista2)

print(lista_final)


#EXERCÍCIO 4

def segundo_maior_valor(lista):
    
    lista_ordenada = sorted(lista, reverse=True)

    return lista_ordenada[1]

lista1 = [13,15,8,4,52,31,7,96,12,5,48,78,1,64]

segundo__maior_da_lista = segundo_maior_valor(lista1)

print(f" O segundo maior valor da lista é: {segundo__maior_da_lista}")


#EXERCÍCIO 5

def ordenar_por_nome(lista_tuplas):
   
    lista_ordenada = sorted(lista_tuplas, key=lambda pessoa: pessoa[0])
    return lista_ordenada

lista_tuplas = [('Samuel', 37),('Natália', 29),('Sávio', 59),('Lourdinha', 63)]

lista_ordenada = ordenar_por_nome(lista_tuplas)

print(lista_ordenada)

#EXERCÍCIO 6

import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5),
 layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
        transform=axs[row, col].transAxes,
        ha='center', va='center', fontsize=18,
        color='darkgrey')

#EXERCÍCIO 7

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt
#Criando um array de pontos no intervalo [-2pi, 2pi] com 100 pontos
x = np.arange(-2 * np.pi, 2 * np.pi, 100)

#Calculando o valor da função seno para cada ponto em x e armazenando na variável y.
y = np.sin(x)

#Criando uma figura e um subconjunto de eixos
fig,ax = plt.subplots()

#Plotando a função seno
ax.plot(x,y)

#EXERCÍCIO 8

import pandas as pd

#Leitura do arquivo csv
df = pd.read_csv("caminho_para_arquivo.csv")

#Exibir primeiras cinco linhas do dataset
df.head(5)


#EXERCÍCIO 9

import pandas as pd
#Criação da base de dados
data = {
    'nome':['Pedro', 'Kátia', 'Alessandra'],
    'altura(m)':[1.80, 1.68, 1.72]
}
#Determinando o DataFrame
df = pd.DataFrame(data)

#Filtragem
altura_maior = df[df['altura(m)']> 1.75]

print(altura_maior)


#EXERCÍCIO 10

import pandas as pd

data = {
    'nome':['Pedro', 'Kátia', 'Alessandra'],
    'altura(m)':[1.80, 1.68, 1.72,]
}

df = pd.DataFrame(data)

#Determinando os valores ausentes
coluna_valores_ausentes = df['altura(m)'].isna()

coluna_valores_ausentes

#Opções para preencher os valores ausentes no dataset trabalhado
df['altura(m)'].fillna(df['altura(m)'].mean()) # substituindo pela média dos valores
df['altura(m)'].fillna(df['altura(m)'].median())
