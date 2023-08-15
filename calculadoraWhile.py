#Calculadora com while

#Solicitar os números e operadores enquanto a condição for verdadeira
while True:
    numero_1 = input('Digite um número: ')
    operador = input("""Digite um operador: 
[+Soma+] [-Subtração-] [/Divisão/] [*Multiplicação*]: """)
    numero_2 = input('Digite outro número: ')
    operadores_permitidos = '+-/*'
    
    #Flag
    numeros_validos = None
    
#Tentativa de transformar o número que o usuário digitou em número flutuante, se funcionar, a nossa Flag se torna verdadeira e o código prossegue
#se não funcionar, a flag continua sendo None, indo assim para a parte de [Tratativa de Erros]
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
#[Tratativa de Erros]
#Se não conseguir converter para float (por ser um valor inválido), a variável vai ser None, sendo assim:
    if numeros_validos is None:
        print("Um, ou ambos números não são válidos. ")
        continue
    
#Se o operador não estiver dentro de um dos operadores permitidos (linha 11), ou a quantidade de operadores digitados for maior que 1
    if (operador not in operadores_permitidos) or (len(operador) > 1):
        print('Operador inválido, tente novamente. ')
        continue
print('Estamos realizando a sua operação, observe o resultado: ')

#Estrutura condicional para mostrar na tela o resultado das operações
    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'O resultado da sua soma é: {num_1_float} + {num_2_float} = {soma}')
    elif operador == '-':
        subtração = num_1_float - num_2_float
        print(f'O resultado da sua subtração é: {num_1_float} - {num_2_float} = {subtração}')
    elif operador == '/':
        divisão = num_1_float / num_2_float
        print(f'O resultado da sua divisão é: {num_1_float} / {num_2_float} = {divisão}')
    elif operador == '*':
        multiplicação = num_1_float * num_2_float
        print(f'O resultado da sua multiplicação é: {num_1_float} * {num_2_float} = {multiplicação}')
#Se o usuário conseguir executar alguma calamidade para vir parar aqui, ele é muito incrível.
    else:
        print('O que você está fazendo aqui? ')
        
#Quando terminar a operação, o usuário pode decidir de sai ou não
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    if sair is True:
        print("""Obrigado por utilizar nossos serviços!
github.com/gustavogbsdev
instagram.com/gustaxou""")
        break
