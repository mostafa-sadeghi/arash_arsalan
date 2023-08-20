# for i in range(10):
#     print("print1")
#     print("print2")


# i = 0
# while i < 10:
#     print("print1")
#     print("print2")
#     i += 1

# user_input = ""
# while user_input != "n":
#     user_input = input("Do you want to continue? (y / n) ")
# print("bye ...")

# numbers = [1,2,3,4,5,6,7]
# print("my list", numbers)
# numbers[2] = 33333
# numbers.append(88888)
# numbers.remove(1)
# print("my list", numbers)



# numbers = (1,2,3,4,5,6,7,8,9)
# for n in numbers:
#     print(n * 2)

# print(numbers[:3])
# print(numbers[0])


# def myfunction(numbers, name):
#     print(name)
#     for num in numbers:
#         print(num ** 2)

# myfunction([1,2,3,4,5,6,7,8,9], "mylist")


def sum_of_numbers(mylist):
    total = 0
    for n in mylist:
        total += n
    return total


print(sum_of_numbers([11,33,54,34,90]))