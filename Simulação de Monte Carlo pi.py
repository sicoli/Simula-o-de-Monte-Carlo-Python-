#Simulação de Monte Carlo sem Turtle, calculando pela distância:
import math
import random
incircle = 0
outcircle = 0
dados=1000000
for i in range(dados):
    x = random.random()*random.choice([-1,1])
    y = random.random()*random.choice([-1,1])
    
    
    d= ((x**2)+(y**2))**0.5
    if d<=1:
        incircle=incircle+1
    else:
        outcircle=outcircle+1

   
total=(incircle+outcircle)
pi=(4*(incircle/total))
print(total)
print(outcircle)
print(incircle)
print("o número pi é ", pi)
#########################################################################
#Simulação de Monte Carlo para Pi pelo Turtle

import turtle
import math
import random

fred = turtle.Turtle()
fred.shape("circle")
fred.speed(3)
pinumber = (3.14159265358979323846264338327)
raio = 1
diametro = (2*pinumber*raio)
desloc = (diametro/360)
wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

fred.penup()
fred.goto(1,0)
fred.left(90)
fred.pendown()

#Desenhar um circulo de coordenadas (-1,-1,1,1)
for i in range (360):
    fred.forward(desloc)
    fred.left(1)
#Desenha as coordenadas x e y    
fred.left(90)
fred.forward(2)
fred.penup()
fred.goto(0,1)
fred.pendown()
fred.left(90)
fred.forward(2)
    
#joga os dados aleatoriamente dentro da tábua
dados = 50
incircle = 0
outcircle = 0
for i in range(dados):
    x = random.random()*random.choice([-1,1])
    y = random.random()*random.choice([-1,1])
    
    fred.penup()
    fred.goto(x,y)
    fred.stamp()
    d=fred.distance(0,0)
    if d<=1:
        incircle=incircle+1
    else:
        outcircle=outcircle+1
    fred.penup()
    
total=(incircle+outcircle)
pi=(4*(incircle/total))
print(total)
print(outcircle)
print(incircle)
print("o número pi é ", pi)


wn.exitonclick()