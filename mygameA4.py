import pygame
import sys 
from pygame.locals import *
pygame.init()


# Näyttö
korkeus = 600
leveys = 800
naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("A4 Peli")

# RGB värit
valkoinen = (255,255,255)
vihrea = (0,80,0)
musta = (0,0,0)

# Taustaväri
naytto.fill(valkoinen)

# Objektit
hahmo = pygame.image.load("hahmo.jpg").convert()
matikka = pygame.image.load("matikkaI.jpg").convert()


# Taso
platform = pygame.Surface((leveys, 20))  
platform.fill(vihrea)  # Täytetään taso vihreällä

# Asetetaan taso peliruudun alareunaan
platform_rect = platform.get_rect()
platform_rect.bottom = korkeus

# Asetetaan teksti peliin
font = pygame.font.SysFont('Arial', 25) # Fontti
teksti = font.render('Mission: Survive', True, musta)  # Teksti ja väri
teksti_rect = teksti.get_rect(center=(leveys//2, korkeus//8))  # Positio


# Ajastin
aikaaJaljella = 60

timer_text = font.render('Time: ' + str(aikaaJaljella), True, musta)  # Update timer text
timer_rect = timer_text.get_rect(center=(leveys//2, korkeus//4))

start_time = pygame.time.get_ticks()

# Hahmon nopeus
speed = 5
x = leveys // 2  # Hahmon X-positio
y = korkeus - hahmo.get_height() - platform.get_height()  #  Hahmon Y-positio

# Pelilogiikka, pyörii kunnes käyttäjä painaa ESC-näppäintä
# tai sulkee välilehden
while True:
    for event in pygame.event.get():  # Etsii tapahtumia
        if event.type == pygame.QUIT:  # Jos pelaaja sulkee ikkunan
            pygame.quit()  # Ikkuna sulkeutuu
            sys.exit()  # Peli sulkeutuu
        if event.type == KEYDOWN:  # Jos pelaaja painaa jotakin näppäintä
            if event.key == K_ESCAPE:  # Jos näppäin on ESC
                pygame.quit()
                sys.exit()
    
    # Pelaaja painaa näppäintä
    keys = pygame.key.get_pressed()

    elapsed_time = pygame.time.get_ticks() - start_time
    aikaaJaljella = max(0, 60 - int(elapsed_time / 1000))
    if aikaaJaljella <= 0:
        print("Aika loppui! Peli päättyy...")
        # Add game over logic here
    
    # Hahmo liikkuu näppäimen mukaan
    if keys[pygame.K_a]:  # Jos painetaan A
        x -= speed  # hahmo liikkuu vasemmalle
    if keys[pygame.K_d]:  # Jos painetaan D
        x += speed  # Hahmo liikkuu oikealle

    # Varmistetaan, että hahmo pysyy platformin päällä
    x = max(0, min(leveys - hahmo.get_width(), x))  

    # Blitataan opjektit näytölle
    naytto.fill(valkoinen) 
    naytto.blit(platform, platform_rect)
    naytto.blit(hahmo, (x, y))
    naytto.blit(teksti, teksti_rect)
    
    naytto.fill(valkoinen, timer_rect)  # Fill the area where the old timer text was with the background color
    timer_text = font.render('Time: ' + str(aikaaJaljella), True, musta)  # Update timer text
    naytto.blit(timer_text, timer_rect)  # Blit the updated timer text to the screen
    


    # Päivitys
    pygame.display.update()
    
    # FPS
    pygame.time.Clock().tick(60)
