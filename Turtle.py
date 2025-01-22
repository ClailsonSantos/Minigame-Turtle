from turtle import Turtle

t = Turtle()
t.speed(1)
while True:
    direction_ft = str(input("PARA MOVIMENTAR INSIRA (F) PARA FRENTE E (T) PARA TRÁS: "))

    if direction_ft.upper() == "F":
        direction_ed = str(input("ESCOLHA A DIREÇÃO (D) PARA DIREITA (E) PARA ESQUERDA: "))

        if direction_ed.upper() == "D":
            distanc = int(input("informe a distancia: "))
            angulo = int(input("Angulo: "))
            t.right(angulo)

        elif direction_ed.upper() == "E":
            distanc = int(input("informe a distancia: "))
            angulo = int(input("Angulo: "))
            t.left(angulo)
        t.forward(distanc)

    elif direction_ft.upper() == "T":
        direction_ed = str(input("ESCOLHA A DIREÇÃO (D) PARA DIREITA (E) PARA ESQUERDA: "))

        if direction_ed.upper() == "D":
            distanc = int(input("informe a distancia: "))
            angulo = int(input("Angulo: "))
            t.right(angulo)

        elif direction_ed.upper() == "E":
            distanc = int(input("informe a distancia: "))
            angulo = int(input("Angulo: "))
            t.left(angulo)
        t.backward(distanc)
    resposta = input("Continuar andando? (S) PARA SIM (N) PARA NÃO:  ")
    if resposta.upper() not in ("S"):
        break