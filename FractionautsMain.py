#!/usr/bin/python
#Fractionauts Main Class
import pygame
from gi.repository import Gtk
import random
from fractions import Fraction

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

class Button:

    def __init__(self, x, y, width, height, text, color=BLUE):
        self.fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.textObj = self.fontObj.render(text, True, GREEN)
        self.textRectObj = self.textObj.get_rect()
        self.textRectObj.center = (x + (width / 2), y + (height / 2))
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        screen.blit(self.textObj, self.textRectObj);

    def is_under(self, pos):
        x, y = pos
        if (self.x < x and 
            self.x + self.width > x and 
            self.y < y and 
            self.y + self.height > y
            ):
            return pos
        else:
            return None


class Question:
    def __init__(self,questionType):
        self.questionType = questionType
        numerator = random.randint(1,9)
        denominator = random.randint(numerator,9)
        self.goal = Fraction(numerator,denominator)
        print(self.goal)


class FractionautsMain:
    def __init__(self):
        self.needsUpdate = False
        self.initialized = False
        self.screen = pygame.display.get_surface()
        self.height = pygame.display.Info().current_h
        self.width = pygame.display.Info().current_w
        self.hcenter = self.width / 2
        self.vcenter = self.height / 2
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()
        self.buttons = []

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0
        self.mode = 'menu'
        self.paused = False
        self.direction = 1
        self.playBtn = Button(self.hcenter - (75*1.5), self.vcenter - 100, 200, 75, 'Play')
        self.howBtn = Button(self.hcenter - (75*1.5), self.vcenter, 200, 75, 'How to Play')
        self.quitBtn = Button(self.hcenter - (75*1.5), self.vcenter + 100, 200, 75, 'Quit')
        self.buttons.append(self.playBtn)
        self.buttons.append(self.howBtn)
        self.buttons.append(self.quitBtn)

    def on_click_me_clicked(self, button):
        print "\"Click me\" button was clicked"

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    # The main game loop.
    def run(self):
        self.running = True
        fontObj = pygame.font.Font('freesansbold.ttf', 32)
        self.textSurfaceObj = fontObj.render('Fractionauts', True, GREEN, BLUE)
        self.textRectObj = self.textSurfaceObj.get_rect()
        self.textRectObj.center = (self.hcenter, 150)

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            # Pump PyGame messages.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.listenForEvents()
            self.renderScreen()
            pygame.display.flip()

    def listenForEvents(self):
        if 1 in pygame.mouse.get_pressed():
            for button in self.buttons:
                if button.is_under(pygame.mouse.get_pos()):
                    print 'You clicked the ' + button.text + ' button'
                    if button == self.quitBtn:
                        self.running = False
                        pygame.quit()
                        exit()
                    elif button == self.playBtn:
                        self.mode = 'play'
                    elif button == self.howBtn:
                        self.mode = 'help'

    def renderScreen(self):
        if self.mode == 'menu':
            self.screen.fill((255, 255, 255))  # 255 for white
            self.screen.blit(self.textSurfaceObj, self.textRectObj);
            for button in self.buttons:
                button.draw(self.screen)
        elif self.mode == 'play':
            self.screen.fill((206, 156, 60))  # 255 for white
        elif self.mode == 'help':
            self.screen.fill((34, 215, 217))  # 255 for white




# This function is called when the game is run directly from the command line:
# ./FractionautsMain.py
def main():
    question = Question("multiplication")
    pygame.init()
    pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    game = FractionautsMain()
    game.run()

if __name__ == '__main__':
    main()
