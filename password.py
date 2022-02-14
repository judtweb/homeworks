from ntpath import join
import random
import string
from unicodedata import digit

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits

# password generator
# random
user_input = int(input("Enter lenght of your password. Put number from range 8 to 20:\n"))
while True:
    if user_input < 8:
        print("Number is too small. Please, enter number from range 8 - 20\n")
        user_input = int(input("Please, enter number again:\n"))
    elif user_input > 20:
        print("Number is too big. Please, enter number from range 8 - 20\n")
        user_input = int(input("Please, enter number again:\n"))
    else:
        print("Your password will have the length:", user_input)
        break

ran_lowsigns = random.sample(lowercase, 2)
ran_uppsigns = random.sample(uppercase, 2)
ran_digits = random.sample(digits, 2)
ran_puncts = random.sample(punctuation, 2)
general_signs= lowercase + uppercase + digits + punctuation 
basic_signs = ran_lowsigns + ran_uppsigns + ran_digits + ran_puncts
if user_input > 8:
    all_signs = basic_signs + random.sample(general_signs, user_input - 8)
else:
    all_signs = basic_signs

random.shuffle(all_signs)
password = ''.join(all_signs)
print("Your password is: ", password)






