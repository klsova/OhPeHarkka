import pygame, sys, random
from pygame.math import Vector2


pygame.init()
cell_size = 40
cell_number = 20
WINDOW = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
pygame.display.set_caption("Matopeli")

class SNAKE:
    pass

class FRUIT:
    def __init__(self):
        self.x  = random.randint(0, cell_number - 1)
        self.y  = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(WINDOW, (188,0,0), fruit_rect)


fruit = FRUIT()

def draw_window():
    WINDOW.fill((0, 153, 0))    

def main():

    
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        draw_window()
        fruit.draw_fruit()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()