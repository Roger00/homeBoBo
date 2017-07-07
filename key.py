from readchar import readkey

UP = '\x1b[A'
DOWN = '\x1b[B'
RIGHT = '\x1b[C'
LEFT = '\x1b[D'

DIRECT_KEYS = [UP, DOWN, LEFT, RIGHT]

def doKey(key):
    if key == UP:
        print('UP')
    elif key == DOWN:
        print('DOWN')
    elif key == LEFT:
        print('LEFT')
    elif key == RIGHT:
        print('RIGHT')

print('Start reading keys...')

while 1:
    key = readkey()
    print key
    if key not in DIRECT_KEYS:
        print('This must be return signal' + key)
        break
    else:
        doKey(key)
