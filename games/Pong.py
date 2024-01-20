import random
import pygame
import time

pygame.init()

background_colour = 255,255,255
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Pong')
screen.fill(background_colour)
pygame.display.flip()

white = 255,255,255
black = 0,0,0

running = True

class Ball:
    _ChangeModifierX = -1
    _ChangeModifierY = -1
    circleX = random.randint(400, 600)
    circleY = 300

    def __init__(self, screen):
        self.screen = screen

    def draw_ball(self):
        black = 0, 0, 0
        white = 255, 255, 255

        pygame.draw.circle(screen, white, (self.circleX - self._ChangeModifierX, self.circleY - self._ChangeModifierY), 15)
        pygame.draw.circle(screen, black, (self.circleX, self.circleY), 15)
        time.sleep(0.005)


    def check_direction(self, padX1, padX2, padY1, padY2):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)

        if self.circleX > 1000:
            text = font.render('Player 1 won!', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (500, 200)
            screen.blit(text, textRect)

        if self.circleX < 0:
            text = font.render('Player 2 won!', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (500, 200)
            screen.blit(text, textRect)

        if self.circleY > 600:
            self._ChangeModifierY = -1
        if self.circleY < 0:
            self._ChangeModifierY = 1

        if padX1-10 < self.circleX-15 < padX1+10 and padY1 - 50 < self.circleY < padY1 + 50:
            #print("Touched")
            self._ChangeModifierX = 1
        if padX2-10 < self.circleX+15 < padX2+10 and padY2 - 50 < self.circleY < padY2 + 50:
            #print("Touched")
            self._ChangeModifierX = -1


        self.circleX += self._ChangeModifierX
        self.circleY += self._ChangeModifierY

class Pad:
    def __init__(self, screen):
        self.screen = screen


    def draw_pad(self, padX, padY, colour):
        pygame.draw.rect(screen, colour, pygame.Rect(padX, padY, 15, 100))



ball1 = Ball(screen)

pad1 = Pad(screen)
pad2 = Pad(screen)
padX1 = 60
padX2 = 930
padY1 = 300
padY2 = 300

while running:
    ball1.draw_ball()
    pad1.draw_pad(padX1, padY1, black)
    pad2.draw_pad(padX2, padY2, black)
    ball1.check_direction(padX1, padX2, padY1, padY2)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                pad1.draw_pad(padX1, padY1+10, white)
                pad1.draw_pad(padX1, padY1, black)
                padY1 -= 10
            if event.key == pygame.K_s:
                pad1.draw_pad(padX1, padY1-10, white)
                pad1.draw_pad(padX1, padY1, black)
                padY1 += 10
            if event.key == pygame.K_UP:
                pad2.draw_pad(padX2, padY2+10, white)
                pad2.draw_pad(padX2, padY2, black)
                padY2 -= 10
            if event.key == pygame.K_DOWN:
                pad2.draw_pad(padX2, padY2-10, white)
                pad2.draw_pad(padX2, padY2, black)
                padY2 += 10









