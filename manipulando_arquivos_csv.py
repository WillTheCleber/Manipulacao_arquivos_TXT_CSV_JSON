#para manipular arquivos csv usa biblioteca csv

import csv #biblioteca nativa do python

with open('arquivos/nomes.csv','w+', encoding= 'UTF8',newline='') as fcsv:
    escrever = csv.writer(fcsv, delimiter=',') #para manipular a biblioteca voce digita o nome da biblioteca e coloca um ponto e apos isso CHAMA A FUNÇÃO
    escrever.writerow(("Nome", "Sobrenome", "Idade"))
    escrever.writerow(("William", "Cleber", 24))
    escrever.writerow(("Juca", "Roberto", 56))
    escrever.writerow(("Cleiton", "Robertin", 27))
    

#ler o arquivo
with open('arquivos/nomes.csv','r') as fcsv:
    ler = csv.reader(fcsv)
    lista1= list(ler)
    print(lista1)

    for i in lista1:
        print(i)

#Ler e transformar em dicionario

with open('arquivos/nomes.csv','r',encoding='UTF8') as fcsv:
    ler_dict = csv.DictReader(fcsv)

    for i in ler_dict:
        print(i)
        #dicionario é somente chaves e valor, nao tem indice

    for d in ler_dict:
        print(d["Nome"]) #se tiver outro for em cima, ele não vai rodar esse, afinal o for vai iterar a memoria do ler_dict e ZERAR a memoria
print('###########################################################')
with open('arquivos/nomes.csv','r',encoding='UTF8') as fcsv:
    ler_dict = csv.DictReader(fcsv)

    for d in ler_dict:
        print(d["Nome"])

## Ler e gravar csv

with open('arquivos/arquivo csv.csv','r') as arq1:
    arq1 = csv.reader(arq1)

    # for i in arq1:
    #     print(i)

    lista2 = list(arq1)

    print(lista2)

