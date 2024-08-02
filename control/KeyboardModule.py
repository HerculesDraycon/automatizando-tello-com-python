import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(key):
    response = False

    for e in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    pressedKey = getattr(pygame, 'K_{}'.format(key))

    if keyInput[pressedKey]:
        response = True
    pygame.display.update()

    return response

def main():
    print(getKey("DOWN"))

if __name__ == '__main__':
    init()
    while True:
        main()