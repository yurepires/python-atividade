# -*- coding: utf-8 -*-
"""questao1.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19tKCtTdMc4OBwDgLbJv6_42dqOGKRMMP
"""

import os
import matplotlib.pyplot as plt
import numpy as np

tabela = [[[300, 400], 14],
           [[400, 500], 46],
           [[500, 600], 58],
           [[600, 700], 76],
           [[700, 800], 68],
           [[800, 900], 62],
           [[900, 1000], 48],
           [[1000, 1100], 22],
           [[1100, 1200], 6]]

def ordenaTabela(tabela):
    numerosOrdenados = []
    for classe in tabela:
        i = 0
        while i < classe[1]:
            numerosOrdenados.append((classe[0][0] + classe[0][1]) / 2)
            i += 1
    return numerosOrdenados

def pontoMedio(tabela):
    pontoMedioClasses = []
    i = 0
    while i < len(tabela):
        pontoMedioClasses.append((tabela[i][0][0] + tabela[i][0][1]) / 2)
        i += 1
    return pontoMedioClasses

def media(tabela):
    pontoMedioClasses = pontoMedio(tabela)
    media = 0
    i = 0
    while i < len(tabela):
        media += pontoMedioClasses[i] * tabela[i][1]
        i += 1
    media = media / somaFrequencias(tabela)
    return media

def moda(tabela):
    maior = 0
    pegaModa = []
    i = 0
    while i < len(tabela):
        if(tabela[i][1] > maior):
            maior = tabela[i][1]
            pegaModa = tabela[i]
        i += 1
    return pegaModa

def maiorFrequencia(tabela):
    maior = 0
    for i in tabela:
        if(i[1] > maior):
            maior = i[1]
    return maior

def mediana(tabela):
    elementosOrdenados = ordenaTabela(tabela)
    meio = somaFrequencias(tabela) / 2
    if(meio % 1 == 0):
        pegaMediana = (elementosOrdenados[int(meio)] + elementosOrdenados[int(meio) + 1]) / 2
        return pegaMediana
    else:
        meio += 0.5
        pegaMediana = elementosOrdenados[int(meio)]
        return pegaMediana

def desvioPadrao(tabela):
    mediaTabela = media(tabela)
    elementosOrdenados = pontoMedio(tabela)
    calculoDesvioPadrao = 0
    i = 0
    while i < len(elementosOrdenados):
        calculoDesvioPadrao += (elementosOrdenados[i] - mediaTabela) ** 2
        i += 1
    calculoDesvioPadrao = calculoDesvioPadrao / (len(tabela) - 1)
    return calculoDesvioPadrao

def somaFrequencias(tabela, iteraAte=len(tabela)):
    soma = 0
    i = 0
    while i < iteraAte:
        soma += tabela[i][1]
        i += 1
    return soma

def descobreClasse(x, tabela):
    elementoProcurado = x * somaFrequencias(tabela)
    buscaClasse = 0
    i = 0
    while(i < len(tabela)):
        buscaClasse += tabela[i][1]
        if(buscaClasse >= elementoProcurado):
            return i
        i += 1

def calculoPercentil(x, tabela):
    indiceClasse = descobreClasse(x, tabela)
    classePercentil = tabela[indiceClasse]
    limiteInferior =  classePercentil[0][0]
    amplitudeClasse = classePercentil[0][1] - classePercentil[0][0]
    somaFrequenciasAnteriores = somaFrequencias(tabela, indiceClasse)
    calculo = limiteInferior + ((x * somaFrequencias(tabela) - somaFrequenciasAnteriores) * amplitudeClasse) / classePercentil[1]
    return calculo


def imprimeOperacaoEscolhida(menu):
    if menu == '1' or menu == 100:
        return "percentil"
    elif menu == '2' or menu == 10:
        return "decil"
    elif menu == '3' or menu == 3:
        return "quartil"

def retornaX(til):
    while True:
        x = int(input("Digite o %s: " % (imprimeOperacaoEscolhida(til))))
        if(x > 0 and x <= til):
            return x
        else:
            print("%s inválido! Digite um percentil válido." % (imprimeOperacaoEscolhida(til)))
            continue

def separaClasses(tabela):
    classesSeparadas = []
    for i in tabela:
        classesSeparadas.append(str(i[0][0]) + " a " + str(i[0][1]))
    return classesSeparadas

def separaFrequencias(tabela):
    frequenciasSeparadas = []
    for i in tabela:
        frequenciasSeparadas.append(i[1])
    return frequenciasSeparadas





print("--- DADOS ---")
print("média:  %s" % media(tabela))
print("moda: %s" % moda(tabela)[0])
print("mediana: %.3f" % mediana(tabela))
print("desvio padrão: %.3f" % desvioPadrao(tabela))
print("Quartil 1: %f" % calculoPercentil(0.25, tabela))
print("Décil 3: %f" % calculoPercentil(0.3, tabela))
print("Décil 7: %f" % calculoPercentil(0.7, tabela))
print("Percentil 15: %f" % calculoPercentil(0.15, tabela))
print("Percentil 90: %f" % calculoPercentil(0.9, tabela))

classes = separaClasses(tabela)
frequencias = separaFrequencias(tabela)

plt.ylabel("Frequência")
plt.xlabel("Classes")
plt.bar(classes, frequencias, width = 0.3)
plt.yticks(np.arange(6, maiorFrequencia(tabela) + 4, 6))
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle=':')-
plt.show()

# menu = input(">>> ")
# if menu == '1':
#     x = retornaX(100)
#     x /= 100
#     calculo = calculoPercentil(x, tabela)
# elif menu == '2':
#     x = retornaX(10)
#     x = (x * 10)/100
#     calculo = calculoPercentil(x, tabela)
# elif(menu == '3'):
#     x = retornaX(3)
#     x = (25 * x) / 100
#     calculo = calculoPercentil(x, tabela)
# else:
#     print("Opção inválida!")
#     os.system('pause')
#     continue

# print("O cálculo do %s é: %f" % (imprimeOperacaoEscolhida(menu), calculo))
# break