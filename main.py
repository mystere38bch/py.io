import pygame


# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1000, 600


# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu de OUUUUUF") # Titre de la fenêtre
# Charger l'image de fond
background_image = pygame.image.load("Capture d'écran 2024-10-03 202909.png")  # Remplacez par le chemin de votre image
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  # Adapter à la taille de la fenêtre

# Joueur
player_image = pygame.image.load("Capture d'écran 2024-09-27 201400.png")  # Remplacez par le chemin de votre image de joueur
player_width, player_height = 50, 50  # Taille du joueur
player_image = pygame.transform.scale(player_image, (player_width, player_height))  # Redimensionner l'image du joueur
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5  # Vitesse de déplacement du joueur


# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
    screen.blit(background_image, (0, 0)) # Affiche l'image de fond
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed 
    # Mettre à jour l'affichage
    # Empêcher le joueur de sortir de l'écran
    player_x = max(0, min(WIDTH - player_width, player_x))
    player_y = max(0, min(HEIGHT - player_height, player_y))

    # Afficher l'image de fond
    screen.blit(background_image, (0, 0))

    # Afficher le joueur
    screen.blit(player_image, (player_x, player_y))

    pygame.display.flip()

# Quitter pygame
pygame.quit()
