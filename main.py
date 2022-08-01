from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=760, height=600)
screen.bgcolor("#222325")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = ["red_tim", "orange_tim", "yellow_tim", "green_tim", "blue_tim", "purple_tim"]

for x in range(0, 6):
    turtles[x] = Turtle(shape="turtle")
    turtles[x].color(colours[x])
    turtles[x].penup()
    turtles[x].goto(x=-330.0, y=(x - 3) * 90 + 38)
user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win race? : ")
race_on = True
this_loop_to_continue = True
while race_on:
    x_cor = []
    for x in range(0, 6):
        x_cor.append(turtles[x].xcor() + 350)
    max_x = 0
    for xcor in x_cor:
        if xcor > max_x:
            max_x = xcor
    if max_x >= 700:
        race_on = False
    this_loop_to_continue = True
    while max_x < 700 and this_loop_to_continue == True:
        for x in range(0, 6):
            a = random.randint(1, 10)
            turtles[x].forward(a)
            this_loop_to_continue = False
for x in range(0, 6):
    if turtles[x].xcor() + 350 == max_x:
        for turtle in turtles:
            turtle.hideturtle()
        result = Turtle()
        result.penup()
        result.goto(0, 0)
        result.color("#F4A355")
        if turtles[x].color() == user_bet:
            result.hideturtle()
            result.write(f"You Won!",  move=False, align="center", font=("Didot", 40, "bold"))
            print(f"You w0n!🎉\n{user_bet} turtle is winner.")
        else:
            result.hideturtle()
            result.write(f"You lost!\n{colours[x]} turtle is winner", move=False, align="center", font=("Didot", 40, "bold"))
            print(f"You lost!🥲\n{colours[x][0].upper()} turtle is winner!")
for x in range(0, 6):
    print(f"{colours[x]} turtle final position : {turtles[x].xcor()}")
screen.exitonclick()
