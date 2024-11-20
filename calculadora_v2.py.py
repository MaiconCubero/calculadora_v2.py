# Fun��o para somar dois n�meros
def adicao(x, y):
    print("Soma: ", x + y)

# Fun��o para subtrair dois n�meros
def subtracao(x, y):
    print("Subtra��o: ", x - y)

# Fun��o para multiplicar dois n�meros
def multiplicacao(x, y):
    print("Multiplica��o: ", x * y)

# Fun��o para dividir dois n�meros
def divisao(x, y):
    if y == 0:
        print("N�o foi poss�vel realizar a divis�o por 0")
    else:
        print("Divis�o: ", x / y)

# Fun��o principal da calculadora
def calculadora():
    while True:
        # Solicita os n�meros
        x = float(input("Primeiro n�mero: "))
        y = float(input("Segundo n�mero: "))
        
        # Solicita a opera��o
        operacao = input("Digite a opera��o a realizar (+, -, *, /): ").strip()
        
        # Executa a opera��o correspondente
        if operacao == "+":
            adicao(x, y)
        elif operacao == "-":
            subtracao(x, y)
        elif operacao == "*":
            multiplicacao(x, y)
        elif operacao == "/":
            divisao(x, y)
        else:
            print("Opera��o inv�lida!")
        
        # Pergunta se o usu�rio quer continuar
        continuar = input("Deseja realizar outra opera��o? (s/n): ").strip().lower()
        if continuar != 's':
            print("Fim da calculadora.")
            break

# Chama a fun��o principal