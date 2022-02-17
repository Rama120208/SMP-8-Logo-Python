import turtle
from math import sqrt, atan, acos, degrees

pen = turtle.Turtle()
pen.pensize(5)
pen.speed("fast")

WIDTH = HEIGHT = 400
# base : height = 400 : 75 = 16 : 3
TRIANGLE = {"base": WIDTH, "height": 75, "hypotenuse": int(sqrt(pow(WIDTH/2, 2)+pow(75, 2)))}

font = [("Times New Roman", 18, "normal"), ("Times New Roman", 9, "normal"), ("Arial", 32, "normal")]

def move_pen(x, y):
	# basic moving pen to another position
	pen.up()
	pen.goto(x, y)
	pen.down()

def draw_base():
	# draw the outer line
	half_width = WIDTH/2
	half_height = HEIGHT/2
	
	move_pen(0, -(half_height+TRIANGLE["height"]))
	pen.left(90)
	pen.forward(HEIGHT+TRIANGLE["height"])
	pen.left(90)
	pen.forward(half_width)
	pen.left(90)
	pen.forward(HEIGHT)
	pen.left(69)
	pen.forward(TRIANGLE["hypotenuse"])
	pen.left(21)
	
	move_pen(0, -(half_height+TRIANGLE["height"]))
	pen.color("black", "blue")
	pen.begin_fill()
	pen.left(90)
	pen.forward(HEIGHT+TRIANGLE["height"])
	pen.right(90)
	pen.forward(half_width)
	pen.right(90)
	pen.forward(HEIGHT)
	pen.right(69)
	pen.forward(TRIANGLE["hypotenuse"])
	pen.right(21)
	pen.end_fill()
	
	move_pen(half_width, half_height/2)
	pen.color("black")
	pen.forward(WIDTH-half_width/2)
	pen.left(90)
	pen.forward(HEIGHT-half_height/2+TRIANGLE["height"]/2)
	pen.left(90)

def write_text():
	pen.color("blue")
	move_pen(-170, 10)
	pen.write("S", font=font[0])
	move_pen(-185, -70)
	pen.write("M", font=font[0])
	move_pen(-175, -150)
	pen.write("P", font=font[0])
	
	move_pen(-5, 100)
	pen.write("NE", align="right", font=font[0])
	pen.color("white")
	move_pen(5, 100)
	pen.write("GERI", font=font[0])
	
	move_pen(100, -50)
	pen.color("orange")
	pen.write("8", font=font[2])
	
	move_pen(-86, -210)
	pen.color("blue")
	pen.write("MAL", font=font[1])
	move_pen(6, -210)
	pen.color("white")
	pen.write("ANG", font=font[1])

def draw_book():
	book_height = 110
	book_width = 180
	
	move_pen(-book_width/2, -40)
	pen.color("black", "white")
	pen.begin_fill()
	for i in range(4):
		pen.forward(book_width if i%2 == 0 else book_height)
		pen.right(90)
	pen.end_fill()
	
	move_pen(-(book_width-20)/2, -40)
	for i in range(4):
		pen.forward(book_width-20 if i%2 == 0 else book_height-10)
		if i != 3:
			pen.right(90)
			
	# tz standing for trapezoid
	tz_size = ((book_width-20)/2, 15) # width, height
	tz_hypotenuse = tz_size[1]*sqrt(2)
	
	# trapezoid 1 (left)
	move_pen(-tz_size[0], -40-(book_height-10))
	pen.right(45)
	pen.forward(tz_hypotenuse)
	pen.right(45)
	pen.forward(tz_size[0]-tz_size[1]*2)
	pen.right(45)
	pen.forward(tz_hypotenuse)
	
	# trapezoid 2 (right)
	pen.left(90)
	pen.forward(tz_hypotenuse)
	pen.right(45)
	pen.forward(tz_size[0]-tz_size[1]*2)
	pen.right(45)
	pen.forward(tz_hypotenuse)
	
	# middle line
	move_pen(0, -40-(book_height-10))
	pen.left(135)
	pen.forward(book_height-10)
	
	# ot standing for orange triangle 
	ot_size = (30, 100) # width, height
	ot_hypotenuse = sqrt(pow(ot_size[0]/2, 2)+ pow(ot_size[1], 2))
	
	move_pen(-ot_size[0]/2, -40)
	pen.color("black", "orange")
	pen.begin_fill()
	pen.right(degrees(atan(ot_size[0]/2/ot_size[1])))
	pen.forward(ot_hypotenuse)
	pen.right(degrees(acos(ot_size[0]/2/ot_hypotenuse))*2)
	pen.forward(ot_hypotenuse)
	pen.right(degrees(atan(ot_size[0]/2/ot_size[1]))+90)
	pen.forward(ot_size[0])
	pen.end_fill()
	
	# below this i use tz variable 'cause it's drawed in the same size
	move_pen(0, -40-ot_size[0]/2)
	pen.color("black", "white")
	pen.begin_fill()
	pen.right(45)
	pen.forward(tz_hypotenuse)
	pen.right(135)
	pen.forward(tz_size[1]*2)
	pen.right(135)
	pen.forward(tz_hypotenuse)
	pen.left(45)
	pen.end_fill()
	
	# it's for another detail
	line_length = book_height-10-tz_size[1]/2
	move_pen(-(book_width-20)/2+tz_size[1]/2, -40)
	pen.forward(line_length)
	move_pen((book_width-20)/2-tz_size[1]/2, -40)
	pen.forward(line_length)
	
	pen.pensize(3)
	pen.left(90)
	# det standing for detail, it's draw straight line for each book side
	det_length = book_width/2-10-5-tz_size[1]-tz_size[1]/2
	detx = (-det_length-10, 10) # x position for left side and right side
	for x in detx:
		dety = -65 # start of y position
		for _ in range(3):
			move_pen(x, dety)
			pen.forward(det_length)
			dety -= 20

draw_base()
write_text()
draw_book()

pen.hideturtle()
turtle.mainloop()

"""
Creator: Rama El

Social Media:
-> Instagram: @rama120208
-> Github: rama-el
"""
