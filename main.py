import pygame
import random

pygame.init()

W = 800
H = 800
FPS = 30

win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Flying Bird")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pipes = []

class Pipe:

    def __init__(self):
        self.width = 30
        self.x = W
        self.topPipe = random.randint(0, H / 2)
        self.bottomPipe = random.randint(0, H / 2)

    def draw(self, touched):

        self.touched = touched

        if touched:
            pygame.draw.rect(win, (255, 0, 0), (self.x, 0, self.width, self.topPipe))
            pygame.draw.rect(win, (255, 0, 0), (self.x, H - self.bottomPipe, self.width, self.bottomPipe))
        
        else:
            pygame.draw.rect(win, BLACK, (self.x, 0, self.width, self.topPipe))
            pygame.draw.rect(win, BLACK, (self.x, H - self.bottomPipe, self.width, self.bottomPipe))


    def update(self):

        self.x -= 10

def drawScreen(py, pipes):

    win.fill(WHITE)

    touched = False

    for pipe in pipes:
        pipe.update()

        if ( 20 < pipe.x < 50):
            if (py < pipe.topPipe or py > H - pipe.bottomPipe):
                touched = True

        pipe.draw(touched)
        touched = False

    pygame.draw.circle(win, BLACK, (50, py), 20)

    pygame.display.update()

def game_loop():

    run = True

    py = H / 2
    pVel = 4
    pAcc = 2

    time = 0

    while run:

        global pipes

        clock.tick(FPS)

        time += 1

        if (time % 60 == 0):
            pipes.append(Pipe())

        for pipe in pipes:
            if pipe.x < -pipe.width:
                pipes.pop(pipes.index(pipe))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pVel = -20

        pVel += pAcc
        py += pVel

        if py >= H:
            py = H

        if py <= 0:
            py = 0

        drawScreen(round(py), pipes)


game_loop()

