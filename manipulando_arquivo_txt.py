#vamos abri um arquivo para leitura

arqu1= open('arquivos/arquivo.txt','r')

print(arqu1.read())

arqu1.seek(0) #Aqui estou retornando o cursor para a linha 0 

print(arqu1.read)

arqu1.close()

arqu2 = open('arquivos/arquivo.txt','w+')

arqu2.write("Temos novos conteudos \n")
arqu2.write("Tem novo conteudo escrito de novo \n")

arqu2.close

arq3 = open('arquivos/arquivo.txt', 'a+')

arq3.write("Nova escrita sem excluir.")