import random

print('Thank you for using the generator, better safe than sorry right?')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!&%$=?*+-@0123456789'

number = input('How many passwords would you like me to create?: ')
number = int(number)

length = input('How long do you want your password to be?: ')
length = int(length)

print('\nBased on your options, I have came up with this:')

for pwd in range(number):
    passwords = ''
    for x in range(length):
        passwords += random.choice(chars)
    print(passwords)

if __name__ == '__main__':
    print()
