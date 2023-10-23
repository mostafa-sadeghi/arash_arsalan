# secret number  "123"
# "456" -> "bagels"
# "167" ->  "Fermi"
# "671" ->  "Pico"
# "127" ->  "Fermi,Fermi"
# "231" ->  "Fermi,Fermi"
# "231" ->  "Pico,Pico,Pico"
import random


def create_secret_number(num_digits):
    all_digits = list('0123456789')
    random.shuffle(all_digits)
    return ''.join(all_digits[:num_digits])


def check_guess(user_g, sec_num):
    res = []
    if user_g == sec_num:
        return "you won"
    for i in range(len(user_g)):
        if user_g[i] == sec_num[i]:
            res.append("Fermi")
        elif user_g[i] in sec_num:
            res.append("Pico")
    if not len(res):
        return "Bagels"
    random.shuffle(res)
    return " ".join(res)


max_number = 10
while True:
    counter = 0
    secret_number = create_secret_number(3)
    print("secret number generated")
    while counter < max_number:
        print(f"guess number{counter + 1}")
        user_guess = input("enter your guess: ")
        print("user guess:", user_guess)

        res = check_guess(user_guess, secret_number)
        print(res)
        if user_guess == secret_number:
            break
        counter += 1
    
    user_choice = input("Do you want to continue?  (y or n): ")
    if user_choice == "n":
        break