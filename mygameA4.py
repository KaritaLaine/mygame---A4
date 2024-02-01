import pygame
import sys 
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()

# Näyttö
korkeus = 700
leveys = 900
naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("A4 Peli")

# RGB värit
valkoinen = (255,255,255)
punainen = (255,0,0)
harmaa = (128,128,128)
musta = (0,0,0)

# Ladattavat objektit
hahmo = pygame.image.load("hahmo.jpg").convert()
matikka = pygame.image.load("matikka.jpg").convert()
taustakuva = pygame.image.load('matikkaa.jpeg').convert()
# Ladataan musiikki ja asetetaan sen volume
mixer.music.load("panic.mp3")
# Voitto ja häviöbiisit
voitto = mixer.Sound("wow.mp3")
havio = mixer.Sound("wahwah.mp3")

# Looppaa musiikkia, asetetaan musiikin volume
mixer.music.set_volume(0.2)
mixer.music.play(-1,0.0)

# Taso
taso = pygame.Surface((leveys, 80))  
taso.fill(harmaa)  # Täytetään taso harmaalla

# Asetetaan taso peliruudun alareunaan
taso_rect = taso.get_rect()
taso_rect.bottom = korkeus

# Asetetaan fontti
font = pygame.font.SysFont('Arial', 25) # Fontti

# Asetetaan kirja peliin
matikka_rect = matikka.get_rect()

# Matikan kirjan liikkumisnopeus (x,y)
m_nopeus = [15,15]

# Ajastin
aikaaJaljella = 60
ajastinTeksti = font.render('Time: ' + str(aikaaJaljella), True, musta) 
ajastin_rect = ajastinTeksti.get_rect(center=(leveys//2, korkeus//4))
aloitusAika = pygame.time.get_ticks()

# Hahmon nopeus ja positio
nopeus = 10
x = leveys // 2  # Hahmon X-positio, keskellä näyttöä
y = korkeus - hahmo.get_height() - taso.get_height()  #  Hahmon Y-positio, asetettuna tason päälle

# Asetetaan taustakuva
naytto.blit(taustakuva, (-60, -75))


# Asetetaan funktio vaikeusastevalikolle
def vaikeusasteet():
    vaikeusasteet = True
    fontti = pygame.font.SysFont('Arial', 20)
    # Nappeja vaikeusasteille, insinööri ja calculus
    insinoori_button = pygame.Rect(leveys//2 - 50, korkeus//2, 100, 50)
    calculus_button = pygame.Rect(leveys//2 - 50, korkeus//2 + 60, 100, 50)
    # Tekstit vaikeusasteille, insinööri ja calculus
    insinoori_text = fontti.render('Insinööri', True, (255, 255, 255))
    calculus_text = fontti.render('Calculus ', True, (255, 255, 255))

    while vaikeusasteet:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Jos painetaan hiiren nappia
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Saadaan hiiren positio
                mouse_pos = event.pos
                # Katsotaan onko hiiri painettu insinööri-napin 
                    # tai calculus-napin päällä
                if insinoori_button.collidepoint(mouse_pos):
                    return 'insinoori'
                if calculus_button.collidepoint(mouse_pos):
                    return 'calculus'
    
        # Piirretään napit näytölle
        pygame.draw.rect(naytto, [0, 0, 0], insinoori_button)  
        pygame.draw.rect(naytto, [0, 0, 0], calculus_button)

        # Piirretään tekstit nappien päälle
        naytto.blit(insinoori_text, (insinoori_button.x + (insinoori_button.width - insinoori_text.get_width()) // 2, insinoori_button.y + (insinoori_button.height - insinoori_text.get_height()) // 2))
        naytto.blit(calculus_text, (calculus_button.x + (calculus_button.width - calculus_text.get_width()) // 2, calculus_button.y + (calculus_button.height - calculus_text.get_height()) // 2))
        
        # Päivitetään muutokset
        pygame.display.update()


# Funktio menu-screenille
def main_menu():
    menu = True
    fontti = pygame.font.SysFont('Arial', 20)

    # Aloitus ja lopetusnapit
    start_button = pygame.Rect(leveys//2 - 50, korkeus//2, 100, 50) 
    quit_button = pygame.Rect(leveys//2 - 50, korkeus//2 + 60, 100, 50)
    # Nappien tekstit
    start_text = fontti.render('Start', True, (255, 255,255))
    quit_text = fontti.render('Quit', True, (255, 255, 255))
    
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Jos painetaan hiiren nappia
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Saadaan hiiren positio
                mouse_pos = event.pos
                # Jos hiiri on painettaessa start-napin päällä
                if start_button.collidepoint(mouse_pos):
                    # Avataan vaikeusasteet-funktio
                    return vaikeusasteet()
                # Jos hiiri on painettaessa quit-napin päällä,
                    # peli suljetaan
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                
        # Piirretään napit näytölle
        pygame.draw.rect(naytto, [0, 0, 0], start_button)  
        pygame.draw.rect(naytto, [0, 0, 0], quit_button) 
        
        # Piirretään tekstit napeille
        naytto.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2, start_button.y + (start_button.height - start_text.get_height()) // 2))
        naytto.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + (quit_button.height - quit_text.get_height()) // 2))
        
        # Päivitetään muutokset
        pygame.display.update()

# Kutsutaan main-menu funktiota ja tallennetaan
        # paluuarvo muuttujaan difficulty (eli insinööri tai calculus)
difficulty = main_menu()

# Jos vaikeusaste on calculus
if difficulty == 'calculus':
    # Muutetaan ikoneita 
    matikka = pygame.image.load("calc.png").convert()
    hahmo = pygame.image.load("hahmo2.png").convert()
    taso.fill([255,127,80])
    # Tekstien väri
    color = punainen

    # Vaihdetaan pelin nopeutta
    m_nopeus = [25,20]

    # Vaihdetaan musiikkia
    mixer.music.load("running.mp3")
    mixer.music.play(-1,0.0)

# Jos vaikeusaste on insinööri
elif difficulty == 'insinoori':
    # Tekstien väri
    color = musta

# Pelin tehtäväteksti
teksti = font.render('Mission: Survive', True, color)  # Teksti ja väri
teksti_rect = teksti.get_rect(center=(leveys//2, korkeus//5.5))  # Positio

# Hahmon suunta
direction = 'right'

# Pelilogiikka, pyörii kunnes käyttäjä painaa ESC-näppäintä
# tai sulkee välilehden, tai kun häviää tai voittaa
while True:
    if difficulty == 'insinoori' or difficulty == 'calculus':
    
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
        voitto.play()
        mixer.music.set_volume(0.1)
        popup_font = pygame.font.SysFont('Arial', 35)
        popup_teksti = popup_font.render('You can skip your math homework for now...', True, musta)
        popup_rect = popup_teksti.get_rect(center=(leveys//2, korkeus//2.5))
        naytto.blit(popup_teksti, popup_rect)
        pygame.display.update()
        pygame.time.wait(3000)  # Viesti pysyy ruudulla 3 sekunnin ajan
        # Lopetetaan peli
        pygame.quit()
        sys.exit()
    
    # Hahmo liikkuu näppäimen mukaan
    if nappaimet[pygame.K_a]:  # Jos painetaan A
        if direction != 'left':  # Tarkistaa onko hahmo käännetty vasemmalle
            hahmo = pygame.transform.flip(hahmo, True, False)  # Käännetään hahmoa
            direction = 'left'  # Päivitetään suunta
        x -= nopeus  # Hahmo liikkuu vasemmalle
    if nappaimet[pygame.K_d]:  # Jos painetaan D
        if direction != 'right':
            hahmo = pygame.transform.flip(hahmo, True, False)  
            direction = 'right' 
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
            
    # Varmistetaan, että hahmo pysyy tason päällä
        # Jos hahmon x-koordinaatti on pienempi kuin tason vasemman reunan 
        # x-koordinaatti, asetetaan hahmo tason vasempaan reunaan
    if x < 0:
        x = 0
    # Jos hahmon x-koordinaatti on suurempi kuin tason oikean reunan, 
        # x-koordinaatti, asetetaan hahmo tason oikeaan reunaan
    elif x > (leveys - hahmo.get_width()):
        x = (leveys - hahmo.get_width())

    # Hahmon positio
    hahmo_rect = hahmo.get_rect(topleft=(x, y))

    # Tarkistetaan osuuko hahmo kirjaan
    if hahmo_rect.colliderect(matikka_rect):
        # Päivitetään näytölle häviämisruutu
        naytto.fill(valkoinen)
        havio.play()
        mixer.music.set_volume(0.1)
        popup_font = pygame.font.SysFont('Arial', 35)
        popup_teksti = popup_font.render('Do your math homework!', True, musta)
        popup_rect = popup_teksti.get_rect(center=(leveys//2, korkeus//2.5))
        naytto.blit(popup_teksti, popup_rect)
        pygame.display.update()
        pygame.time.wait(3000) # Viesti pysyy ruudulla 3 sekunnin ajan
        # Lopetetaan peli
        pygame.quit()
        sys.exit()

    # Päivitetään ajastimen tekstiä
    ajastinTeksti = font.render('Time: ' + str(aikaaJaljella), True, color)  # Päivitetään timerin tekstiä

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