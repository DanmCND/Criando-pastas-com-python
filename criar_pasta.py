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

'''
🎯 Caso de Uso Real
Você foi contratado por uma empresa que organiza documentos por cliente.
Todos os dias, novos clientes chegam e precisam ter uma pasta criada com o nome deles.
Para evitar erros e retrabalho, a empresa pediu que você desenvolvesse um pequeno programa em Python que:
Pergunte o nome da pasta
Crie a pasta automaticamente
Informe se a pasta já existe
 
📋 O que o programa deve fazer
[x]Perguntar ao usuário:
[x]Verificar se a pasta já existe:
[x]Se não existir, criar a pasta
[x]Se já existir, mostrar a mensagem:
[x]Mostrar uma mensagem de sucesso caso a pasta seja criada:
 
🧠 Conceitos que deverão ser utilizados
input()
if / else
Biblioteca os
os.path.exists()
os.mkdir() ou os.makedirs()
 
💡 Comportamento esperado
 
[x]Caso 1 – Pasta nova
Digite o nome da pasta que deseja criar: cliente123 Pasta criada com sucesso! 
 
[x]Caso 2 – Pasta já existente
Digite o nome da pasta que deseja criar: cliente123 Essa pasta já existe! 

⭐ Desafio Extra (Opcional)
[x]Não permitir nome vazio
[x]Perguntar se deseja tentar novamente
[x]Converter o nome da pasta para minúsculo automaticamente
'''