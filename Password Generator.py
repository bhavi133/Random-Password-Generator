import string
import random

if __name__ == "__main__":
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    length = int(input("Input the length of the password : "))
    password = []
    password.extend(list(uppercase_letters))
    password.extend(list(lowercase_letters))
    password.extend(list(digits))
    password.extend(list(special_characters))
    print("Your password is :", "".join(random.sample(password, length)))
