import random


print('H A N G M A N')
abc = 'qwertyuiopasdfghjklzxcvbnm'


def game():
    word = random.choice(['python', 'java', 'kotlin', 'javascript'])
    s = set()
    typed = set()
    lifes = 8
    while lifes > 0:
        print()
        for k in word:
            if k in s:
                print(k, end='')
            else:
                print('-', end='')
        print()
        print('Input a letter: ', end='')
        n = input()
        if n in typed:
            print('You already typed this letter')
        elif len(n) > 1:
            print('You should print a single letter')
        elif n not in abc:
            print('It is not an ASCII lowercase letter')
        elif n not in word:
            print('No such letter in the word')
            lifes -= 1
            typed.add(n)
        else:
            s.add(n)
            typed.add(n)
        if set(word) == s:
            print('You guessed the word!\nYou survived!\n')
            menu()
            break
    else:
        print('You are hanged!\n')
        menu()


def menu():
    x = ''
    while x not in ['play', 'exit']:
        print('Type "play" to play the game, "exit" to quit: ', end='')
        x = input()
        if x == 'exit':
            break
        elif x == 'play':
            game()


menu()
