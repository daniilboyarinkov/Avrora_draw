from turtle import *
from random import random, randint, choice

title('Drawing itself')

# (-330, 280)  # up-left angle
# (330, 280)  # up-right angle
# (330, -280)  # down-right angle
# (-330, -280)  # down-left angle

up_left_angle = (-330, 280)

size = 0


def choose_bgcolor():
	red = random()
	green = random()
	blue = random()
	bgcolor(red, green, blue)


def choose_color():
	red = random()
	green = random()
	blue = random()
	return red, green, blue


def go_line_to_line():
	global size
	x = -330 - size
	for line in range(660 // size + 1):
		pos_x = x + size
		x += size
		for mazok in range(7):
			speed(10)
			up()
			color(choose_color())
			pos_y = randint(-280, 280)
			length = randint(0, 100)
			goto(pos_x, pos_y)
			down()
			forward(length)
		up()
		goto(pos_x, 280)
		down()
		forward(length)
		up()


def randomize_line():
	for mazok in range(randint(21, 100)):
		speed(10)
		up()
		color(choose_color())
		length = randint(0, 100)
		x_pos = randint(-330, 330)
		y_pos = randint(-280, 280)
		goto(x_pos, y_pos)
		down()
		forward(length)


def draw_first_layer():
	global size
	size = 25
	pensize(size)
	up()
	goto(up_left_angle)
	right(90)
	down()
	length = randint(0, 280)
	forward(length)
	go_line_to_line()


def draw_second_layer():
	global size
	size = 15
	pensize(size)
	up()
	goto(up_left_angle)
	right(90)
	down()
	length = randint(0, 280)
	forward(length)
	go_line_to_line()


# def draw_other_layers():
# 	global size
# 	size = 15
# 	pensize(size)
# 	draw = True
# 	while draw:
# 		for i in range(randint(1, 2)):
# 			up()
# 			goto(up_left_angle)
# 			right(90)
# 			down()
# 			length = randint(0, 280)
# 			forward(length)
# 			randomize_line()
# 		size -= randint(1, 3)
# 		pensize(size)

# 		if size <= 0:
# 			draw = False


def draw_other_layers():
	global size
	size = randint(1, 12)
	pensize(size)
	draw = True
	while draw:
		for i in range(randint(5, 15)):
			up()
			goto(up_left_angle)
			right(randint(0, 361))
			down()
			length = randint(0, 280)
			forward(length)
			randomize_line()

			size = randint(1, 10)
			pensize(size)

		for i in range(randint(7, 12)):
			up()
			goto(up_left_angle)
			right(randint(0, 361))
			down()
			length = randint(0, 280)
			forward(length)
			randomize_line()

			size = randint(1, 5)
			pensize(size)

		draw = False

def main():
        choose_bgcolor()
        draw_first_layer()
        draw_second_layer()
        draw_other_layers()

        mainloop()

if __name__ == "__main__":
        # Информационный принт
        print("Start drawing....")
        main()
        print("Done!")
