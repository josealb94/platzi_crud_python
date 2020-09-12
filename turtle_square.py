import turtle

#Genera Ventana
window = turtle.Screen()
#Crea Tortuga
tortuga = turtle.Turtle()

distance = 100
while distance > 10:
    for i in range(4):
        tortuga.forward(distance)
        tortuga.right(90)
    distance -= 5

window.mainloop()