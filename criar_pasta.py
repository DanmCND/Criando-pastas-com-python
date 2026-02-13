#importa uma biblioteca para manipular/interagir arquivos e diretórios
import os

nome_pasta = 'minha_pasta'
 
#mkdir = make directory (criar diretório)
#rmdir = remove directory (remover diretório)

#Criar uma pasta com o nome definido na variável nome_pasta
#os.mkdir(nome_pasta)

#cria a pasta, se ela já existir, não gera erro
os.makedirs(nome_pasta, exist_ok=True) 

#Remover a pasta criada
#os.rmdir(nome_pasta)

#criar arquivo dentro da pasta criada
caminho_arquivo = os.path.join(nome_pasta, 'meu_arquivo.txt')
with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Hello, World!')

