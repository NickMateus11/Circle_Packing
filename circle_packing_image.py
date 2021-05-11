import pygame
import numpy as np
from random import randint
from PIL import Image
 
 
IMGFILE = "packing.png"
with Image.open(IMGFILE) as im:
    pixels = list(im.getdata())
    w,h = im.size
    valid_points = []
    for i in range(w):
        for j in range(h):
            if pixels[i+j*w] == (255,255,255):
                valid_points.append((i,j))
image = pygame.image.load(IMGFILE)

# w, h = 800, 600
pygame.init()
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
 
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
GREEN = pygame.Color("green")


class Circle():
    def __init__(self, c, r=2, w=2):
        self.center = np.array(c)
        self.radius = r
        self.width = w
        self.stop = False


def main():
    
    buff = 2
    circles = []
    count = 2
    FPS = 30

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        # screen.blit(image, (0,0))
        screen.fill(BLACK)

        current = 0
        attempts = 0
        while (current < count):
            pos = valid_points[randint(0,len(valid_points)-1)]
            collision = False
            for c in circles:
                if np.linalg.norm(pos-c.center) < c.radius+buff:
                    collision = True
                    attempts += 1
                    break
            if not collision:
                circles.append(Circle( pos ))
            current += 1
            if attempts > count**2:
                break

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
                    c.radius += buff/2
 
        pygame.display.flip()
        clock.tick(FPS)
 

if __name__ == "__main__":
    main()
