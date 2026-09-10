import pygame

# Initialisiert alle PyGame Pakete, ab hier stehen sie zur Verfügung
pygame.init()

# Fenster erstellen, im angegeben Format
window = pygame.display.set_mode((1400, 800))
# Einstellungen
# FPS Limit Variable
clock = pygame.time.Clock()

# Variablen
kreis_x_bewegung = 0
kreis_y_bewegung = 0

# Gameloop Bedingung
running = True

# ---------- Begin Gameloop ----------
# Gameloop erstellen für Ereigniss bearbeitung
while running:
    # --Ereignisse Prüfen--
    # Prüft ob das Fenster und damit auch PyGame geschlossen wird
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- Spielzustand Berechnen ----------
    kreis_x_bewegung += 1

    # ---------- Rendern ----------
    # Hintergrund einfährben
    window.fill("#dacbcb")

    # Erstellt einen Kreis
    kreis = pygame.draw.circle(
        window, "#ff00d4", (kreis_x_bewegung, kreis_y_bewegung), 100
    )
    viereck = pygame.draw.rect(window, "Blue", ((400, 300), (100, 150)))

    # Aktualisiert das Display
    pygame.display.flip()

    # FPS Limit erstellen
    clock.tick(60)

pygame.quit()
