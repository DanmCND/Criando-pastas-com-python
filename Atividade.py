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
import os

#1. Perguntar o nome da pasta ao usuiário
while True:
    nome_pasta = input("Digite o nome da pasta que deseja criar: ").strip().lower()
#2. Verificar se o nome da pasta é válido (não vazio, sem espaços e sem caracteres inválidos)    
    if " " in nome_pasta:
        print("O nome da pasta não pode conter espaços. Por favor, tente novamente.")
    elif not nome_pasta:
        print("O nome da pasta não pode ser vazio. Por favor, tente novamente.")  
#3.Verificar se a pasta já existe        
    elif os.path.exists(nome_pasta):
        print(f"A pasta '{nome_pasta}' já existe! Por favor, escolha outro nome.")      
#4. Criar a pasta e mostrar mensagem de sucesso
    else:
        os.makedirs(nome_pasta, exist_ok=True)
        print(f"O nome da pasta será: {nome_pasta}.\n Pasta criada com sucesso!")     
#5.Bonus perguntar se deseja criar outra pasta
        criar_outra = input("Deseja criar outra pasta? (s/n): ").strip().lower()
        if criar_outra != 's':
            print("Encerrando o programa. Até mais!")
            break
 
