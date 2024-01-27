from tkinter import *
import time 
import random

winner = False
red_horse_x = -5
red_horse_y = 110

blue_horse_x = -28
blue_horse_y = 20

def start_game():
    global red_horse_x
    global blue_horse_x
    global winner

    while winner == False:
        time.sleep(0.05)
        random_move_blue_horse = random.randint(0,20)
        random_move_red_horse = random.randint(0,20)

        #UPDATE horse x positions
        blue_horse_x += random_move_blue_horse
        red_horse_x += random_move_red_horse

        move_horses(random_move_red_horse, random_move_blue_horse)
        main_screen.update()
        winner = winner_of_race()

    if winner == "TIE":
        Label(main_screen,text=winner, font=("calibri", 20), fg="green").place(x=200, y=450)
    else:
        Label(main_screen,text=winner+" WINS!!", font=("calibri", 20), fg="green").place(x=200, y=450)

def move_horses(red_horse_random_move, blue_horse_random_move):
    canvas.move(red_horse, red_horse_random_move, 0)
    canvas.move(blue_horse, blue_horse_random_move, 0)

def winner_of_race():
    if blue_horse_x >= 550 and red_horse_x >=550:
        return "TIE"
    if red_horse_x >=550:
        return "RED Horse"
    if blue_horse_x >=550:
        return "BLUE Horse"
    return False

#Creating screen
main_screen =  Tk()
main_screen.title("Horse Racing")
main_screen.geometry("600x500")
main_screen.config(background="black")

#Creation of canvas
canvas = Canvas(main_screen, width=600, height=200, bg="black")
canvas.pack(pady= 20)

#import horse images
red_horse_img = PhotoImage(file="./Images/red-horse.png")
blue_horse_img = PhotoImage(file="./Images/blue-horse.png")

#changing image size
blue_horse_img = blue_horse_img.zoom(13)
blue_horse_img = blue_horse_img.subsample(90)

red_horse_img = red_horse_img.zoom(13)
red_horse_img = red_horse_img.subsample(50)

#add image to canvas
red_horse = canvas.create_image(red_horse_x,red_horse_y,anchor=NW, image=red_horse_img)
blue_horse = canvas.create_image(blue_horse_x, blue_horse_y, anchor=NW, image=blue_horse_img)


#text
t1 = Label(main_screen, text="Select your horse", font=("calibri", 20), bg="green")
t1.place(x=230, y=280)
t2 = Label(main_screen, text="Press play when ready!", font=("calibri", 20), bg="green" )
t2.place(x=200, y=335)

b1 = Button(main_screen, text="Play!", height= 2, width=15, bg="orange", font=("calibri", 10), command=start_game)
b1.place(x=270, y=390)


main_screen.mainloop()