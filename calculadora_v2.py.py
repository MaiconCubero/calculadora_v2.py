# Função para somar dois números
def adicao(x, y):
    print("Soma: ", x + y)

# Função para subtrair dois números
def subtracao(x, y):
    print("Subtração: ", x - y)

# Função para multiplicar dois números
def multiplicacao(x, y):
    print("Multiplicação: ", x * y)

# Função para dividir dois números
def divisao(x, y):
    if y == 0:
        print("Não foi possível realizar a divisão por 0")
    else:
        print("Divisão: ", x / y)

# Função principal da calculadora
def calculadora():
    while True:
        # Solicita os números
        x = float(input("Primeiro número: "))
        y = float(input("Segundo número: "))
        
        # Solicita a operação
        operacao = input("Digite a operação a realizar (+, -, *, /): ").strip()
        
        # Executa a operação correspondente
        if operacao == "+":
            adicao(x, y)
        elif operacao == "-":
            subtracao(x, y)
        elif operacao == "*":
            multiplicacao(x, y)
        elif operacao == "/":
            divisao(x, y)
        else:
            print("Operação inválida!")
        
        # Pergunta se o usuário quer continuar
        continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
        if continuar != 's':
            print("Fim da calculadora.")
            break

# Chama a função principal