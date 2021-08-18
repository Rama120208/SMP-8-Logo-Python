import turtle

pen = turtle.Turtle()
pen.pensize(5)

def move_pen(x, y):
	pen.up()
	pen.goto(x, y)
	pen.down()

def first_base():
	move_pen(0, 120)
	pen.color("black", "white")
	pen.begin_fill()
	pen.right(90)
	pen.forward(280)
	pen.right(125)
	pen.forward(140)
	pen.right(55)
	pen.forward(200)
	pen.right(90)
	pen.forward(115)
	pen.end_fill()
	
def second_base():
	move_pen(0, -160)
	pen.color("black", "blue")
	pen.begin_fill()
	pen.left(35)
	pen.forward(140)
	pen.left(55)
	pen.forward(200)
	pen.left(90)
	pen.forward(115)
	pen.end_fill()
	
def inner_base():
	move_pen(115, 70)
	pen.forward(180)
	pen.left(90)
	pen.forward(185)
	move_pen(0, 0)
	
def write_smp():
	pen.color("blue")
	move_pen(-100, 10)
	pen.write("S")
	move_pen(-105, -20)
	pen.write("M")
	move_pen(-100, -50)
	pen.write("P")
	
def write_negeri():
	pen.color("blue")
	move_pen(-45, 75)
	pen.write("NE")
	pen.color("white")
	move_pen(3, 75)
	pen.write("GERI")
	
def write_eight():
	pen.color("orange")
	move_pen(50, -20)
	pen.write("8", font=("Arial", 16, "normal"))
	
def write_malang():
	pen.color("blue")
	move_pen(-53, -110)
	pen.write("MAL", font=("Arial", 6, "normal"))
	pen.color("white")
	move_pen(3, -110)
	pen.write("ANG", font=("Arial", 6, "normal"))
	
def book_base():
	pen.color("black", "white")
	pen.pensize(4)
	move_pen(-50, -80)
	pen.begin_fill()
	pen.left(90)
	pen.forward(100)
	pen.left(90)
	pen.forward(60)
	pen.left(90)
	pen.forward(100)
	pen.left(90)
	pen.forward(60)
	pen.end_fill()

	move_pen(-45, -75)
	pen.left(90)
	pen.forward(90)
	pen.left(90)
	pen.forward(55)
	pen.left(90)
	pen.forward(90)
	pen.left(90)
	pen.forward(55)

def book_details():
	move_pen(-45, -75)
	pen.left(65)
	for i in range(2):
		pen.left(50)
		pen.forward(15)
		pen.right(25)
		pen.forward(18)
		pen.right(25)
		pen.forward(15)

	move_pen(-15, -20)
	pen.right(20)
	pen.forward(20)
	pen.left(90)
	pen.forward(20)
	
	move_pen(-1, -75)
	pen.left(45)
	pen.forward(40)
	
	move_pen(-15, -20)
	pen.color("black", "orange")
	pen.begin_fill()
	pen.right(12)
	pen.forward(68)
	pen.right(156)
	pen.forward(68)
	pen.right(102)
	pen.forward(30)
	pen.end_fill()

first_base()
second_base()
inner_base()
write_smp()
write_negeri()
write_eight()
write_malang()
book_base()
book_details()

pen.ht()
turtle.done()