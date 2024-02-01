import pygame
import sys 
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()

# Ladataan musiikki ja asetetaan sen volume
mixer.music.load("panic.mp3")
mixer.music.set_volume(0.2)

# Näyttö
korkeus = 700
leveys = 900
naytto = pygame.display.set_mode((leveys, korkeus))
pygame.display.set_caption("A4 Peli")

# RGB värit
valkoinen = (255,255,255)
harmaa = (128,128,128)
musta = (0,0,0)

# Ladattavat objektit
hahmo = pygame.image.load("hahmo.jpg").convert()
matikka = pygame.image.load("matikka.jpg").convert()
# Looppaa musiikkia
mixer.music.play(-1,0.0)

# Taso
taso = pygame.Surface((leveys, 80))  
taso.fill(harmaa)  # Täytetään taso harmaalla

# Asetetaan taso peliruudun alareunaan
taso_rect = taso.get_rect()
taso_rect.bottom = korkeus

# Asetetaan teksti peliin
font = pygame.font.SysFont('Arial', 25) # Fontti
teksti = font.render('Mission: Survive', True, musta)  # Teksti ja väria
teksti_rect = teksti.get_rect(center=(leveys//2, korkeus//5.5))  # Positio

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

start_screen_image = pygame.image.load('matikkaa.jpeg')
naytto.blit(start_screen_image, (-60, -75))
pygame.display.update()

def difficulty_menu():
    difficulty_menu = True
    button_font = pygame.font.SysFont('Arial', 20)
    easy_button = pygame.Rect(leveys//2 - 50, korkeus//2, 100, 50)  # Easy button
    hard_button = pygame.Rect(leveys//2 - 50, korkeus//2 + 60, 100, 50)  # Hard button

    easy_text = button_font.render('Insinööri', True, (255, 255, 255))  # valkoinen
    hard_text = button_font.render('Calculus ', True, (255, 255, 255))  # valkoinen

    while difficulty_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                if easy_button.collidepoint(mouse_pos):
                    print('Easy button was pressed at {0}'.format(mouse_pos))
                    return 'easy'
                    
                if hard_button.collidepoint(mouse_pos):
                    print('Hard button was pressed at {0}'.format(mouse_pos))
                    return 'hard'
                    # Add code here to set difficulty to hard

        # draw button
        pygame.draw.rect(naytto, [0, 0, 0], easy_button)  # draw button
        pygame.draw.rect(naytto, [0, 0, 0], hard_button)  # draw button

        # draw text on buttons
        naytto.blit(easy_text, (easy_button.x + (easy_button.width - easy_text.get_width()) // 2, easy_button.y + (easy_button.height - easy_text.get_height()) // 2))
        naytto.blit(hard_text, (hard_button.x + (hard_button.width - hard_text.get_width()) // 2, hard_button.y + (hard_button.height - hard_text.get_height()) // 2))

        pygame.display.update()
def main_menu():
    menu = True
    button_font = pygame.font.SysFont('Arial', 20)
    start_button = pygame.Rect(leveys//2 - 50, korkeus//2, 100, 50)  # Start button
    quit_button = pygame.Rect(leveys//2 - 50, korkeus//2 + 60, 100, 50)  # Quit button
    

    start_text = button_font.render('Start', True, (255, 255,255))  # valkoinen
    quit_text = button_font.render('Quit', True, (255, 255, 255))  # valkoinen
    

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                # checks if mouse position is over the button
                if start_button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    return difficulty_menu()
                if quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                
    
        # Napit
        pygame.draw.rect(naytto, [0, 0, 0], start_button)  # draw button
        pygame.draw.rect(naytto, [0, 0, 0], quit_button)  # draw button
        
        #Teksti napeille
        naytto.blit(start_text, (start_button.x + (start_button.width - start_text.get_width()) // 2, start_button.y + (start_button.height - start_text.get_height()) // 2))
        naytto.blit(quit_text, (quit_button.x + (quit_button.width - quit_text.get_width()) // 2, quit_button.y + (quit_button.height - quit_text.get_height()) // 2))
        
        
        pygame.display.update()

# Call the main menu function before your game loop
difficulty = main_menu()
# Pelilogiikka, pyörii kunnes käyttäjä painaa ESC-näppäintä
# tai sulkee välilehden, tai kun häviää tai voittaa
while True:
    if difficulty == 'easy':
    
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