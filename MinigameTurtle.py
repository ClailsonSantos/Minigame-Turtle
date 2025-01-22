from turtle import Turtle

t = Turtle()

def obter_distancia():
    resposta = int(input("informe a distancia: "))
    return resposta

def rotacionar_turtle(turtle):
    movimentar_turtle = str(input("ESCOLHA A DIREÇÃO (D) PARA DIREITA (E) PARA ESQUERDA: "))
    if movimentar_turtle.upper() == "D":
        rotacionar_para_direita(turtle)
    elif movimentar_turtle.upper() == "E":
        rotacionar_para_esquerda(turtle)

def rotacionar_para_direita(turtle):
    angulo = int(input("Angulo: "))
    t.right(angulo)

def rotacionar_para_esquerda(turtle):
    angulo = int(input("Angulo: "))
    t.left(angulo)


while True:
    direction_ft = str(input("PARA MOVIMENTAR INSIRA (F) PARA FRENTE E (T) PARA TRÁS: "))

    if direction_ft.upper() == "F":
        distanc = obter_distancia()
        rotacionar_turtle(t)
        t.forward(distanc)

    elif direction_ft.upper() == "T":
        distanc = obter_distancia()
        rotacionar_turtle(t)
        t.backward(distanc)
    resposta = input("Continuar andando? (S) PARA SIM (N) PARA NÃO:  ")

    if resposta.upper() not in ("S"):
        break