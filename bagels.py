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


print(create_secret_number(3))
