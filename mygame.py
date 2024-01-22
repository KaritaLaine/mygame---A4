import pygame
import sys     # Mahdollistaa pelin sulkemisen
from pygame.locals import * # Tuottaa mahdolliset muuttujat pygameen
pygame.init()  # Ottaa pygamen käyttöön

# Ikkunan koko
width = 960
height = 600
dispSurf = pygame.display.set_mode((width,height))
pygame.display.set_caption("My game") # Ikkunan nimen vaihto
pygame.display.set_icon(pygame.image.load("mario.png")) # Ikkunan kuvan vaihto

# Objektit
level = pygame.image.load("level.jpg").convert()
mario = pygame.image.load("mario.png").convert()
fireball = pygame.image.load("fireball.png").convert()
# Convert muuttaa kuvan oikeaan muotoon

# Suorakulmion arvot, musta (width, height)
rectangle = pygame.Surface((300,50))

# RGB värejä, 0-255
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
pink = (255,0,130)

# Asetetaan suorakulmiolle väri
rectangle.fill(pink)

# Asetetaan objektit tiettyihin koordinaatteihin
dispSurf.blit(level, (0,0))
dispSurf.blit(fireball, (0,0))
dispSurf.blit(mario, (400,450)) # 400p oikealle, 450p alas
dispSurf.blit(rectangle, (0,200)) # Random suorakulmio?

# Päivittää muutokset, myös pygame.display.update()
pygame.display.flip()

# Surface.get_rect() method returns the Rect object of "Surface"
# Rect objects are needed to move Surfaces and for collision detection
# Rect(left, top, width, height) contains left/top-coordinates and width/height
fireballArea = fireball.get_rect()
marioArea = mario.get_rect()
rectangleArea = rectangle.get_rect()

# get_rect() method by default sets the left-top corner to (0,0)
# mario and rectangle were not blitted into (0,0)
# the left and top coordinates have to be changed with dot notation
marioArea.left = 400
marioArea.top = 450
rectangleArea.left = 0
rectangleArea.top = 200

# Tulipallon [x, y] nopeus pikseleinä per iteraatio
speed = [1,1]



# Looppi pyörii, kunnes pelaaja sulkee pelin
while True:


    # Käy läpi kaikki tapahtumat (quit, exit)
    for event in pygame.event.get():  # Lista kaikista eventeistä (tapahtumista)
        if event.type == pygame.QUIT: # Jos pelaaja sulkee ikkunan
            pygame.quit() # Ikkuna sulkeutuu
            sys.exit()    # Python ohjelma sulkeutuu
        if event.type == KEYDOWN:     # Jos käyttäjä painaa mitä tahansa näppäintä
            if event.key == K_ESCAPE: # Jos näppäin on ESC,
                                      # Lista näppäimistä löytyy pygame.key
                pygame.quit() # Ikkuna sulkeutuu
                sys.exit()    # Python ohjelma sulkeutuu


    # fireball will be moved by speed=[1,1] in every iteration
    # move_ip([x,y]) changes the Rect-objects left-top coordinates by x and y
    fireballArea.move_ip(speed)


    # fireball bounces from the edges of the display surface
    if fireballArea.left < 0 or fireballArea.right > width: # fireball is vertically outside the game
        speed[0] = -speed[0] # the x-direction of the speed will be converted
    if fireballArea.top < 0 or fireballArea.bottom > height: # fireball is horizontally outside the game
        speed[1] = -speed[1] # the y-direction of the speed will be converted


    # Fireball törmää suorakulmioon
    if rectangleArea.colliderect(fireballArea):
    # a.colliderect(b) returns True if Rect-objects a and b overlap
        if rectangleArea.colliderect(fireballArea.move(-speed[0],0)):
        # if the fireball came from vertical direction
            speed[1] = -speed[1] # the y-direction of the speed will be converted
        else:
        # otherwise the fireball came from horizontal direction
            speed[0] = -speed[0] # the x-direction of the speed will be converted


    # Mario liikkuu nuolinäppäimien avulla
    # get.pressed() listaa kaikki painetut näppäimet, monitoroi näppäimistön toimintaa
    pressings = pygame.key.get_pressed()
    if pressings[K_LEFT]:          # Jos pelaaja painaa vasenta nuolinäppäintä
        marioArea.move_ip((-1,0))  # Mario liikkuu yhden pikselin vasemmalle
    if pressings[K_RIGHT]:
        marioArea.move_ip((1,0))
    if pressings[K_DOWN]:
        marioArea.move_ip((0,1))
    if pressings[K_UP]:
        marioArea.move_ip((0,-1))


    # Päivitä objektit paikoilleen
    dispSurf.blit(level, (0,0)) # Ilman tätä liikkuvat objektit jättäisivät "jäljen"
                                # eli mustan vanan peräänsä
    dispSurf.blit(fireball, fireballArea)
    dispSurf.blit(mario, marioArea)
    dispSurf.blit(rectangle, rectangleArea)


    # updating the display surface is always needed at the end of each iteration of game loop
    pygame.display.flip()