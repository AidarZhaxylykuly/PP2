import pygame, random, sys ,os
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)
FPS = 40
BADDIEMINSIZE = 10
BADDIEMAXSIZE = 40
BADDIEMINSPEED = 8
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 6
PLAYERMOVERATE = 5
count=3
coinscore = 0
s = 0

def terminate():
    pygame.quit()
    sys.exit()

def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect1']):
            return True
    return False

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# set up pygame, the window, and the mouse cursor
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Racer')
pygame.mouse.set_visible(False)

# fonts
font = pygame.font.SysFont(None, 30)

# sounds
gameOverSound = pygame.mixer.Sound('crash.wav')
pygame.mixer.music.load('car.wav')
laugh = pygame.mixer.Sound('laugh.wav')


# images
playerImage = pygame.image.load('car1.png')
playerRect = playerImage.get_rect()
coin = pygame.image.load('coin.png')
sample = [coin]
wallLeft = pygame.image.load('left.png')
wallRight = pygame.image.load('right.png')


# "Start" screen
drawText('Press any key to start the game.', font, windowSurface, (WINDOWWIDTH / 3) - 30, (WINDOWHEIGHT / 3))
drawText('And Enjoy', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)+30)
pygame.display.update()
waitForPlayerToPressKey()
zero=0
if not os.path.exists("data/save.dat"):
    f = open("data/save.dat", 'w')
    f.write(str(zero))
    f.close()
v=open("data/save.dat", 'r')
topScore = int(v.readline())
v.close()



while (count>0):
    # start of the game
    baddies = []
    score = 0
    playerRect.topleft = (WINDOWWIDTH / 2, WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # the game loop
        score += 1 # increase score

        for event in pygame.event.get():

            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == ord('z'):
                    reverseCheat = True
                if event.key == ord('x'):
                    slowCheat = True
                if event.key == K_LEFT or event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == ord('w'):
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == ord('z'):
                    reverseCheat = False
                if event.key == ord('x'):
                    slowCheat = False
                if event.key == K_ESCAPE:
                        terminate()


                if event.key == K_LEFT or event.key == ord('a'):
                    moveLeft = False
                if event.key == K_RIGHT or event.key == ord('d'):
                    moveRight = False
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveDown = False



        # Add new baddies at the top of the screen
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == ADDNEWBADDIERATE:
            baddieAddCounter = 0
            baddieSize =30
            newBaddie = {'rect': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 23, 47),
                         'rect1': pygame.Rect(random.randint(140, 485), 0 - baddieSize, 33, 40),
                         'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                         'surface': pygame.transform.scale(random.choice(sample), (23, 47)),
                        }
            baddies.append(newBaddie)
            sideLeft= {'rect': pygame.Rect(0,0,126,600),
                       'rect1': pygame.Rect(0, 0, 126, 600),
                       'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                       'surface':pygame.transform.scale(wallLeft, (126, 599)),
                       }
            baddies.append(sideLeft)
            sideRight= {'rect': pygame.Rect(497,0,303,600),
                        'rect1': pygame.Rect(497, 0, 303, 600),
                        'speed': random.randint(BADDIEMINSPEED, BADDIEMAXSPEED),
                        'surface':pygame.transform.scale(wallRight, (303, 599)),
                       }
            baddies.append(sideRight)



        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * PLAYERMOVERATE)
        if moveDown and playerRect.bottom < WINDOWHEIGHT:
            playerRect.move_ip(0, PLAYERMOVERATE)

        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect1'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect1'].move_ip(0, -5)
            elif slowCheat:
                b['rect1'].move_ip(0, 1)


        for b in baddies[:]:
            if b['rect'].top > WINDOWHEIGHT:
                baddies.remove(b)
            if b['rect1'].top > WINDOWHEIGHT:
                baddies.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (s), font, windowSurface, 128, 0)
        drawText('Rest Life: %s' % (count), font, windowSurface,128, 40)

        windowSurface.blit(playerImage, playerRect)


        for b in baddies:
            windowSurface.blit(b['surface'], b['rect1'])

        pygame.display.update()

        # Check if any of the car have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            coinscore+=1
            if coinscore%23==0 or coinscore%22==0 or coinscore%24==0:
                s+=1

        mainClock.tick(FPS)
