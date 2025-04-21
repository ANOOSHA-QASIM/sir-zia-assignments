import random 
import string

name = input("Enter your name: ")
length = int(input("\nEnter your password length (minimum 6):"))

def password_generator(name , length):
    
    name = name.lower()
    characters = string.digits + string.punctuation
    rand_characters = "".join(random.choice(characters) for _ in range(length - len(name)))

    password = name[:3] + rand_characters

    return password


if length < 6:
    print("\nPassword length should be at least 6!")

else:
    password = password_generator(name , length)
    print("\nYour generated password is:", password)





