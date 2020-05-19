import random
Turns = 10
lst = ['google', 'facebook', 'rainbow', 'unicorn', 'water', 'fire']
word = random.choice(lst)
whole_word = ''
while Turns > 0:
    failed = 0
    for char in word:
        if char in whole_word:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print('You won')
        break
    guess = input('enter a character:')
    whole_word += guess
    Turns -= 1
else:
    print('You lost')
