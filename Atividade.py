#====Atividade====

import os

#1. Perguntar o nome da pasta ao usuiário
while True:
    nome_pasta = input("Digite o nome da pasta que deseja criar: ").lower()
#2. Verificar se o nome da pasta é válido (não vazio, sem espaços e sem caracteres inválidos)    
    if " " in nome_pasta or not nome_pasta:
        print("O nome da pasta não pode conter espaços ou estar vazio. Por favor, tente novamente.") 
#3.Verificar se a pasta já existe        
    elif os.path.exists(nome_pasta):
        print(f"A pasta '{nome_pasta}' já existe! Por favor, escolha outro nome.")      
#4. Criar a pasta e mostrar mensagem de sucesso
    else:
        os.makedirs(nome_pasta, exist_ok=True)
        print(f"O nome da pasta será: {nome_pasta}.\n Pasta criada com sucesso!")     
#5.Bonus perguntar se deseja criar outra pasta
        escolha_usuario = input("Deseja criar outra pasta? (s/n): ").lower()
        if escolha_usuario != 's':
            print("Encerrando o programa. Até mais!")
            break
 
