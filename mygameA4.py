import pygame
import sys 
from pygame.locals import *
pygame.init()


# Näyttö
korkeus = 700
leveys = 900
naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("A4 Peli")

# RGB värit
valkoinen = (255,255,255)
harmaa = (128,128,128)
punainen = (255,0,0)
musta = (0,0,0)
# Taustaväri
naytto.fill(valkoinen)

# Ladattavat objektit
hahmo = pygame.image.load("hahmo.jpg").convert()
matikka = pygame.image.load("matikka.jpg").convert()

# Taso
taso = pygame.Surface((leveys, 80))  
taso.fill(harmaa)  # Täytetään taso vihreällä

# Asetetaan taso peliruudun alareunaan
taso_rect = taso.get_rect()
taso_rect.bottom = korkeus

# Asetetaan teksti peliin
font = pygame.font.SysFont('Arial', 25) # Fontti
teksti = font.render('Mission: Survive', True, musta)  # Teksti ja väria
teksti_rect = teksti.get_rect(center=(leveys//2, korkeus//5.5))  # Positiod

# Asetetaan kirja peliin
matikka_rect = matikka.get_rect()

# Matikan nopeus
m_nopeus = [15,25]

# Ajastin
aikaaJaljella = 60
ajastinTeksti = font.render('Time: ' + str(aikaaJaljella), True, musta)  # Update timer texta
ajastin_rect = ajastinTeksti.get_rect(center=(leveys//2, korkeus//4))
aloitusAika = pygame.time.get_ticks()

# Hahmon nopeus ja positio
nopeus = 10
x = leveys // 2  # Hahmon X-positio
y = korkeus - hahmo.get_height() - taso.get_height()  #  Hahmon Y-positio




# Pelilogiikka, pyörii kunnes käyttäjä painaa ESC-näppäintä
# tai sulkee välilehden, tai kun häviää tai voittaa
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
    nappaimet = pygame.key.get_pressed()

    aikaaJaljella = pygame.time.get_ticks() - aloitusAika
    aikaaJaljella = max(0, 60 - int(aikaaJaljella / 1000))
    if aikaaJaljella <= 0:
        # Päivitetään näytölle voittoruutu
        naytto.fill(valkoinen)
        popup_font = pygame.font.SysFont('Arial', 35)
        popup_text = popup_font.render('You can skip your math homework for now...', True, (0,0,0))
        popup_rect = popup_text.get_rect(center=(leveys//2, korkeus//2.5))
        naytto.blit(popup_text, popup_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # Viesti pysyy ruudulla 3 sekunnin ajan
        # Lopetetaan peli
        pygame.quit()
        sys.exit()
    
    # Hahmo liikkuu näppäimen mukaan
    if nappaimet[pygame.K_a]:  # Jos painetaan A
        x -= nopeus  # hahmo liikkuu vasemmalle
    if nappaimet[pygame.K_d]:  # Jos painetaan D
        x += nopeus  # Hahmo liikkuu oikealle
        
        
    # Matikan kirja liikkuu joka iteraatiolla
    matikka_rect.move_ip(m_nopeus)
    
    # Matikan kirja kimpoaa seinistä kun se yrittää mennä ikkunan ulkopuolelle
    if matikka_rect.left < 0 or matikka_rect.right > leveys: 
        m_nopeus[0] = -m_nopeus[0] 
    if matikka_rect.top < 0 or matikka_rect.bottom > korkeus: 
        m_nopeus[1] = -m_nopeus[1] 


    # Matikan kirja kimpoaa lattiasta
    if taso_rect.colliderect(matikka_rect):
    # Kun matikan kirja osuu taso-alueeseen, se kimpoaa vastakkaiseen suuntaan
        if taso_rect.colliderect(matikka_rect.move(-m_nopeus[0],0)):
            m_nopeus[1] = -m_nopeus[1]
        else:
            m_nopeus[0] = -m_nopeus[0]
            
    # Varmistetaan, että hahmo pysyy tasoin päällä
    x = max(0, min(leveys - hahmo.get_width(), x))  

    # Hahmon positio
    hahmo_rect = hahmo.get_rect(topleft=(x, y))

    # Tarkistetaan osuuko hahmo kirjaan
    if hahmo_rect.colliderect(matikka_rect):
        # Päivitetään näytölle häviämisruutu
        naytto.fill(valkoinen)
        popup_font = pygame.font.SysFont('Arial', 35)
        popup_text = popup_font.render('Do your math homework!', True, (0,0,0))
        popup_rect = popup_text.get_rect(center=(leveys//2, korkeus//2.5))
        naytto.blit(popup_text, popup_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # Viesti pysyy ruudulla 3 sekunnin ajan
        # Lopetetaan peli
        pygame.quit()
        sys.exit()

    # Päivitetään ajastimen tekstiä
    ajastinTeksti = font.render('Time: ' + str(aikaaJaljella), True, musta)  # Päivitetään timerin tekstiä

    # Blitataan opjektit näytölle
    naytto.fill(valkoinen) 
    naytto.blit(hahmo, (x, y))
    naytto.blit(taso, taso_rect)
    naytto.blit(teksti, teksti_rect)
    naytto.fill(valkoinen, ajastin_rect)  # Täytetään timerin alue valkoisella
    naytto.blit(ajastinTeksti, ajastin_rect)  # Laitetaan päivitetty teksti näytölle
    naytto.blit(matikka, matikka_rect)

    # Päivitys
    pygame.display.update()
    
    # FPS
    pygame.time.Clock().tick(60)