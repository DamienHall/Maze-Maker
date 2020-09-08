import pygame, sys

"""
Script by https://github.com/LilZcrazyG
"""

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()


# Window class
class Window:
    def __init__(self, width=800, height=800, title="Pygame Window", icon=False):
        self.width = width
        self.height = height
        self.title = title

        if icon != False:
            self.icon = pygame.image.load(icon)
            pygame.display.set_icon(self.icon)

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def game_loop(self, function=None):
        while True:
            if function != None:
                function()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            fps = pygame.font.Font(None, 100).render(str(int(clock.get_fps())), True, pygame.Color('lightblue'))
            #self.window.blit(fps, ((self.width/2)-50,(self.height/2)-50))
            pygame.display.flip()

    def return_self(self):
        return self.window

    def return_size(self):
        return pygame.display.get_surface().get_size()


# Graphics class
class Graphics:
    def __init__(self, window):
        self.window = window
        self.color = (255, 255, 255)
        self.line_width = 1

    def set_background(self, color):
        self.window.fill(color)

    def load_image(self, img):
        return pygame.image.load(img)

    def set_color(self, color):
        self.color = color

    def line(self, point_a, point_b):
        pygame.draw.line(self.window, self.color, point_a, point_b, self.line_width)

    def rectangle(self, pos, size):
        x, y = pos
        width, height = size
        pygame.draw.rect(self.window, self.color, (x, y, width, height))

    def square(self, pos, size):
        self.rectangle(pos, (size, size))

    def circle(self, pos, size):
        pygame.draw.circle(self.window, self.color, pos, size)
