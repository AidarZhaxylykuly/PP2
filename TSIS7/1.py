import pygame
pygame.init()
pygame.display.set_mode((800,800), pygame.RESIZABLE)
pygame.display.set_caption('Clocks')



pygame.display.update()
c=pygame.time.Clock()
while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    c.tick(30)