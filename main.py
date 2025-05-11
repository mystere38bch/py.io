import pygame


# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600


# Création de la fenêtre
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de OUUUUUF") # Titre de la fenêtre
# Charger l'image de fond
background_image = pygame.image.load("Capture d'écran 2024-10-03 202909.png") 
background_image = pygame.transform.scale(background_image, (largeur, hauteur))  

# Joueur

joueur_image = pygame.image.load("Capture d'écran 2024-09-27 201400.png") 
joueur_largeur, joueur_hauteur = 50, 50  # Taille du joueur
joueur_image = pygame.transform.scale(joueur_image, (joueur_largeur, joueur_hauteur))  # Redimensionner l'image du joueur
joueur_x = largeur // 2
joueur_y = hauteur // 2
joueur_speed = 5  # Vitesse de déplacement du joueur

#objet a éviter
image_des_murs = pygame.image.load("Capture d'écran 2024-09-27 201400.png")
largeur_mur, hauteur_mur = 30, 30  # Taille du mur
image_des_murs = pygame.transform.scale(image_des_murs, (largeur_mur, hauteur_mur))  #j'ai choisi la taille de manière aléatoire
mur_x = largeur  # Position initiale de l'objet (hors de l'écran à droite)
mur_y = hauteur // 2  # Position verticale du mur
mur_speed = 10  # Vitesse de déplacement du mur
flag_vitesse = 0 # Variable pour la vitesse du mur


# Boucle principale
running = True
while running:
    # Afficher l'image de fond
    screen.blit(background_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
    screen.blit(background_image, (0, 0)) # Affiche l'image de fond
    keys = pygame.key.get_pressed()
    if not(keys[pygame.K_SPACE]):
        joueur_y=hauteur/2
    if keys[pygame.K_SPACE]:
        joueur_y =joueur_hauteur//2
    if keys[pygame.K_DOWN]:
        joueur_y += joueur_speed
    if keys[pygame.K_LEFT]:
        joueur_x -= joueur_speed
    if keys[pygame.K_RIGHT]:
        joueur_x += joueur_speed 
    if (joueur_x + joueur_largeur > mur_x and joueur_x < mur_x + largeur_mur and joueur_y + joueur_hauteur > mur_y and joueur_y < mur_y + hauteur_mur):
        # Collision détectée, arret du programme
        print("Collision avec le mur !")
        pygame.quit()
    # Mettre à jour l'affichage
    # Empêcher le joueur de sortir de l'écran
    joueur_x = max(0, min(largeur - joueur_largeur, joueur_x))
    joueur_y = max(0, min(hauteur - joueur_hauteur, joueur_y))
    # Déplacer le mur vers la gauche

    mur_x -= mur_speed

    if mur_x <largeur_mur:  # Si le mur sort de l'écran, le remettre à droite
        mur_x = largeur
    print(f"Mur position: x={mur_x}, y={mur_y}")

    # Dessiner le mur
    screen.blit(image_des_murs, (mur_x, mur_y))
   
    # Afficher le joueur
    screen.blit(joueur_image, (joueur_x, joueur_y))

    pygame.display.flip()

# Quitter pygame
pygame.quit()
