# for i in range(5):
#     print("ok")
#     print("yes")

# for i in range(5):
#     print(i, end=" ")

# for i in range(1, 5):
#     print(i, end=" ")
# print()
# for i in range(1, 20, 2):
#     print(i, end=" ")

# TODO  اعداد زوج کمتر از 20

# for i in range(2,20,2):
#     print(i)


# for s in "python":
#     print(s.upper(), end=" ")

# numbers = [1, 2, 3, 4, 5, 6]

# for n in numbers:
#     print(n)


# for i in range(len(numbers)):
#     print(numbers[i])


# TODO  " برنامه ای بنویسید که با کمک حلیه فور، چهار عدد از ورودی دریافت نماید
# و هر یک از اعداد را در لیستی اضافه کند
# سپس مجموع اعداد زوج موجود در لیست را نمایش دهید"


# numbers = list()
# total = 0
# even_numbers = []
# for i in range(4):
#     n = float(input("number:> "))
#     numbers.append(n)
#     if n % 2 == 0:
#         total += n
#         even_numbers.append(n)

# print(f"total is {total}")
# print(f"total is {sum(even_numbers)}")



# TODO برنامه ای بنویسید که با کمک حلقه مجموع اعداد لیست زیر را محاسبه و نمایش دهد
# numbers = [2, 88, 444, 765, 1234]
# total = 0
# for n in numbers:
#     total += n
# print(f"total is {total}")
# print(f'total {sum(numbers)}')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(numbers)-1, -1, -1):
#     print(numbers[i], end=" ")

# import turtle

# main_screen = turtle.Screen()
# my_turtle = turtle.Turtle()

# sides = int(main_screen.textinput("sides", "How many sides?"))
# pen_size = int(main_screen.textinput("penSize", "Which size(enter a number)?"))
# pen_color = main_screen.textinput("penColor", "Which Color(example: red)?")

# my_turtle.pensize(pen_size)
# my_turtle.color(pen_color)
# my_turtle.shape("turtle")
# my_turtle.shapesize(2)
# my_turtle.begin_fill()

# for i in range(sides):
#     my_turtle.forward(150)
#     my_turtle.left(360/sides)

# my_turtle.end_fill()
# my_turtle.ht()

# turtle.done()
