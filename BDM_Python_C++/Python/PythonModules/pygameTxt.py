import pygame
import time
import subprocess

pygame.init()

screen = pygame.display.set_mode((800, 250))
clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)
pygame.time.set_timer(pygame.USEREVENT, 200)


def text_generator(text):
    tmp = ''
    for letter in text:
        tmp += letter
        if letter != '':
            yield tmp


class DynamicText(object):
    def __init__(self, font, text, pos, autoreset=False):
        self.done = False
        self.font = font
        self.text = text
        self.pos = pos
        self._gen = text_generator(self.text)
        self.autoreset = autoreset
        self.update()

    def reset(self):
        self._gen = text_generator(self.text)
        self.done = False
        self.update()

    def update(self):
        if not self.done:
            try:
                self.rendered = self.font. \
                    render(next(self._gen), True, (0, 128, 0))
            except StopIteration:
                self.done = True
                time.sleep(10)
                subprocess.Popen("python3 pygameModule.py 1", shell=True)

    def draw(self, screen):
        screen.blit(self.rendered, self.pos)


text = ('A little time ago, a drone hovered in from the far West. '
        'Camera on gimbal...')
message = DynamicText(font, text, (65, 120), autoreset=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.USEREVENT:
            message.update()
    else:
        screen.fill(pygame.color.Color('black'))
        message.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        continue
    break
pygame.quit()
exit()
