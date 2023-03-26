import pygame
pygame.init()
sc=pygame.display.set_mode((800,800))
pygame.display.set_caption('Circle')
c=pygame.time.Clock()
x=400
y=400


while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    sc.fill((255,255,255))
    pygame.draw.circle(sc, (255,0,0), (x,y), 25)
    events=pygame.key.get_pressed()
    if events[pygame.K_LEFT] and x>25:
        x-=20
    if events[pygame.K_RIGHT] and x<780:
        x+=20
    if events[pygame.K_UP] and y>25:
        y-=20
    if events[pygame.K_DOWN] and y<780:
        y+=20
    pygame.display.update()
    c.tick(60)