import pygame, random
pygame.init()

WHITE = (255,255,255)
xy = 600
mousePos = ()
win = pygame.display.set_mode((xy, xy))
win.fill(WHITE)
colors = {'red': (255,0,0), 'green': (0,255,0), 'blue': (0,0,255), 'purple': (160, 32, 240), 'yellow': (255, 255, 0), 'lime': (191, 255, 0),
          'pink': (255, 192, 203), 'brown': (165, 42, 42)}


def redrawGameWin():
    if mouse.pressMouse()[0]:
        drawPoint(mouse.findMouse())
    pygame.display.update()


def drawPoint(coords):
    pygame.draw.circle(win, mouse.mousecolor, coords, radius)


class Mouse():
    def __init__(self):
        self.mousecolor = (0,0,0)
        pass

    def findMouse(self):
        global mousePos
        mousePos = pygame.mouse.get_pos()
        return pygame.mouse.get_pos()

    def pressMouse(self):
        b = pygame.mouse.get_pressed()
        return b

    def makeThicc(self):
        return int(input('Choose the size: '))

    def makeColor(self):
        return input('Choose the color (red, green, blue, brown, pink, yellow, lime, purple): ').lower()


mouse = Mouse()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        redrawGameWin()


try:
    mouse.mousecolor = colors[mouse.makeColor()]
except:
    pass
radius = mouse.makeThicc()
main()
