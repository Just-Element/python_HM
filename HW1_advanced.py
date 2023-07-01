import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

print('Welcome to the Linux User Password Generator!\n')

try:
    length = int(input('Please enter the desired password length: '))
    all = lower + upper + number + symbol
    rand = random.sample(all, length)
    password = ''.join(rand)
    if length < 4:
        print ('The minimum password length is 4 characters')  
    elif not upper and not lower and not number and not symbol in password:
        print('no no no ')
    else:
        print(f'Generated password: {password}')
except ValueError:
    print('Not number')


