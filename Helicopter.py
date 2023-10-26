import pygame
import random

# Inicializácia pygame
pygame.init()

# Rozlíšenie obrazovky
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))

# Nastavenie helikoptéry a jej pohybu
helicopter = pygame.image.load('helicopter.png')  # Nahrajte obrázok helikoptéry bez čierneho pozadia
helicopter = pygame.transform.scale(helicopter, (100, 100))  # Prispôsobte veľkosť obrázka
x, y = width // 2, height // 2
speed_x, speed_y = random.choice([1, -1]) * 5, random.choice([1, -1]) * 5

# Načítanie zvuku
pygame.mixer.init()
pygame.mixer.music.load('Helicopter.mp3')
pygame.mixer.music.play(-1)  # -1 pre nekonečné opakovanie

# Hlavný cyklus
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += speed_x
    y += speed_y

    # Detekcia kolízie s hranicami obrazovky
    if x < 0 or x + 100 > width:
        speed_x *= -1
    if y < 0 or y + 100 > height:
        speed_y *= -1

    # Vyčistenie obrazovky
    screen.fill((0, 0, 0))

    # Zobrazenie helikoptéry na aktuálnej pozícii
    screen.blit(helicopter, (x, y))

    # Aktualizácia obrazovky
    pygame.display.flip()

# Ukončenie pygame
pygame.quit()
