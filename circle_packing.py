import pygame
import numpy as np
from random import randint
 
 
w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
 
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
 

class Circle():
    def __init__(self, c, r=2, w=2):
        self.center = np.array(c)
        self.radius = r
        self.width = w
        self.stop = False


def main():
    
    buff = 2
    circles = []
    count = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
         
        screen.fill(BLACK)

        if count:
            pos = np.array((randint(buff,w-buff), randint(buff,h-buff)))
            collision = False
            for c in circles:
                if np.linalg.norm(pos-c.center) < c.radius+buff:
                    collision = True
                    break
            if not collision:
                circles.append(Circle( pos ))
        count = (count+1)%30

        for c in circles:
            pygame.draw.circle(screen, WHITE, c.center, c.radius, c.width)
            if not c.stop:
                for other in circles:
                    if not np.array_equal(other.center, c.center) and np.linalg.norm(c.center-other.center) < c.radius+other.radius+buff:
                        c.stop = True
                        other.stop = True
                        break
                if not (min(c.center - c.radius) > buff and (c.center[0] + c.radius) < w-buff and (c.center[1] + c.radius) < h-buff):
                    c.stop = True
                else:
                    c.radius += buff
 
        pygame.display.flip()
        clock.tick(30)
 

if __name__ == "__main__":
    main()
