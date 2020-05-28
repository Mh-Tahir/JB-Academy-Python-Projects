import re
import random

d = {
  '1 1': 6,
  '1 2': 3,
  '1 3': 0,
  '2 1': 7,
  '2 2': 4,
  '2 3': 1,
  '3 1': 8,
  '3 2': 5,
  '3 3': 2
}
blank = list(range(9))
turn = 1
cells = list('_________')

def out():
  print('---------')
  for i in range(len(cells)):
    if i == 0:
        print('| ', end='')
    if i in (3, 6):
        print('|')
        print('| ', end='')
    print(cells[i] + ' ', end='')
  print('|')
  print('---------')

def check():
  x, o = False, False
  for i in (0, 3, 6):
    if cells[i] == cells[i + 1] == cells[i + 2] == 'X' or cells[0] == cells[4] == cells[8] == 'X' or cells[2] == cells[4] == cells[6] == 'X':
      x = True
    if cells[i] == cells[i + 1] == cells[i + 2] == 'O' or cells[0] == cells[4] == cells[8] == 'O' or cells[2] == cells[4] == cells[6] == 'O':
      o = True
  for i in (0, 1, 2):
    if cells[i] == cells[i + 3] == cells[i + 6] == 'X':
      x = True
    if cells[i] == cells[i + 3] == cells[i + 6] == 'O':
      o = True
  if x == o == True or abs(cells.count("X") - cells.count("O")) > 1:
    out()
    print('Impossible')
    return 0
  elif x == True:
    out()
    print('X wins')
    return 1
  elif o == True:
    out()
    print('O wins')
    return 1
  elif x == o == False and "_" not in cells:
    out()
    print('Draw')
    return 1
  else:
    out()
    return 0

def coordinate():
  global turn
  while True:
    try:
      c = input('Enter the coordinates: ')
      if re.match('[1-3] [1-3]', c) is not None:
        if cells[d[c]] == '_':
          cells[d[c]] = "O" if cells.count("X") > cells.count("O") else "X"
          turn += 1
          blank.remove(d[c])
          break
        else:
          print('This cell is occupied! Choose another one!')
      elif re.match('[0-9] [0-9]', c) is not None:
        print('Coordinates should be from 1 to 3!')
      else:
        print('You should enter numbers!')
    except:
      print('Wrong coordinates!')

def move():
  print('Making move level "easy"')
  r = random.choice(blank)
  cells[r] = 'O'
  blank.remove(r)

def play():
  out()
  while True:
    coordinate()
    if check() == 1:
      break
    move()
    if check() == 1:
      break

play()
