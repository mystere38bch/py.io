import pygame


# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True

#Bouton rejouer
bouton_width, bouton_height = 200, 50
bouton_x = (largeur - bouton_width) // 2  # Centré horizontalement
bouton_y = ((hauteur - bouton_height) // 10)*9  # Centré verticalement

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


#Game over
gameover_image = pygame.image.load("game_over.png")
gameover_image = pygame.transform.scale(gameover_image, (largeur, hauteur))  

def position_joueur(joueur_x, joueur_y):
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
    # Empêcher le joueur de sortir de l'écran
        joueur_x = max(0, min(largeur - joueur_largeur, joueur_x))
        joueur_y = max(0, min(hauteur - joueur_hauteur, joueur_y))
    return joueur_x, joueur_y

def affichage_boutton(screen, text, x, y, width, height, color, text_color): #exemple trouver sur internet à peut être améliorer
    pygame.draw.rect(screen, color, (x, y, width, height))  # Dessiner le rectangle du bouton
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36
    text_surface = font.render(text, True, text_color)  # Rendre le texte
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Centrer le texte
    screen.blit(text_surface, text_rect)  # Afficher le texte
# Boucle principale
# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic est détecté
            mouse_x, mouse_y = event.pos  # Position de la souris
            if bouton_x <= mouse_x <= bouton_x + bouton_width and bouton_y <= mouse_y <= bouton_y + bouton_height:
                # Réinitialiser les variables du jeu
                joueur_x = largeur // 2
                joueur_y = hauteur // 2
                mur_x = largeur
                play_again = True

    if play_again:  # Si le jeu est en cours
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))

        # Mettre à jour la position du joueur
        joueur_x, joueur_y = position_joueur(joueur_x, joueur_y)

        # Déplacer le mur vers la gauche
        mur_x -= mur_speed
        if mur_x < -largeur_mur:  # Si le mur sort de l'écran, le remettre à droite
            mur_x = largeur

        # Vérifier la collision entre le joueur et le mur
        if (joueur_x + joueur_largeur > mur_x and joueur_x < mur_x + largeur_mur and
            joueur_y + joueur_hauteur > mur_y and joueur_y < mur_y + hauteur_mur):
            play_again = False

        # Dessiner le mur
        screen.blit(image_des_murs, (mur_x, mur_y))

        # Afficher le joueur
        screen.blit(joueur_image, (joueur_x, joueur_y))

    else:  # Si le jeu est terminé
        # Afficher l'écran de Game Over
        screen.blit(gameover_image, (0, 0))

        # Afficher le bouton "Rejouer"
        affichage_boutton(screen, "Rejouer", bouton_x, bouton_y, bouton_width, bouton_height, (255, 0, 0), (255, 255, 255))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()