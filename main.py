from turtle import Turtle,Screen
import random

game_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color:")
print(f"You bet is on {user_bet}")
colors = ["red","black","blue","green","yellow","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []
for turtle_index in range(0,6):
    new_turtle= Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_on =False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! ,The {winning_color} turtle is the winner")
            else:
                print(f"Oops,You lose ,The {winning_color} turtle is the winner")

        
        
        
        rand_distance=random.randint(0,15)
        turtle.forward(rand_distance)
       

screen.exitonclick()
