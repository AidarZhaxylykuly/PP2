import pygame
import datetime
pygame.init()
sc=pygame.display.set_mode((420,420))
pygame.display.set_caption('Clock')



main_surf=pygame.image.load(('main-clock.png')).convert_alpha()
l_hand=pygame.image.load(('left-hand.png')).convert_alpha()#seconds
r_hand=pygame.image.load(('right-hand.png')).convert_alpha()#minutes
main_surf=pygame.transform.scale(main_surf, (main_surf.get_width()//2, main_surf.get_height()//2))
cent_coor_1=main_surf.get_rect(center=(210,210))
l_hand=pygame.transform.scale(l_hand, (l_hand.get_width()//2, l_hand.get_height()//2))
cent_coor_2=l_hand.get_rect(center=(210,210))
r_hand=pygame.transform.scale(r_hand, (r_hand.get_width()//2, r_hand.get_height()//2))
cent_coor_3=r_hand.get_rect(center=(210,210))
c=pygame.time.Clock()



while True:
    for i in pygame.event.get():
        if i.type==pygame.QUIT:
            exit()
    x=datetime.datetime.now()
    sc.blit(main_surf, cent_coor_1)
    l_handr=pygame.transform.rotate(l_hand, -(x.second*6-90))
    cent_coor_2=l_handr.get_rect(center=(210,210))
    sc.blit(l_handr, cent_coor_2)
    r_handr=pygame.transform.rotate(r_hand, -(x.minute*6-90))
    cent_coor_3=r_handr.get_rect(center=(210,210))
    sc.blit(r_handr, cent_coor_3)
    pygame.display.update()
    c.tick(3)