import pygame


# Initialisation de pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True
game_speed = 2
saute=0
momentum_du_saut=0

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

# perso
class Joeur:
    def __init__(self, x, y, vitesse):
        self.x = x 
        self.y = y
        self.vitesse = vitesse #vitesse de déplacement du perso
perso = Joeur(largeur//2, hauteur//2, 5)  # Initialisation du perso
perso_image = pygame.image.load("Capture d'écran 2024-09-27 201400.png") 
perso_largeur, perso_hauteur = 50, 50  # Taille du perso
perso_image = pygame.transform.scale(perso_image, (perso_largeur, perso_hauteur))  # Redimensionner l'image du perso


#objet a éviter
image_des_murs = pygame.image.load("Capture d'écran 2024-09-27 201400.png")
largeur_mur, hauteur_mur = 30, 30  # Taille du mur
image_des_murs = pygame.transform.scale(image_des_murs, (largeur_mur, hauteur_mur))  #j'ai choisi la taille de manière aléatoire
mur_x = largeur  # Position initiale de l'objet (hors de l'écran à droite)
mur_y = hauteur // 2  # Position verticale du mur
mur_speed = 0  # Vitesse de déplacement du mur
flag_vitesse = 0 # Variable pour la vitesse du mur


#Game over
gameover_image = pygame.image.load("game_over.png")
gameover_image = pygame.transform.scale(gameover_image, (largeur, hauteur))  

def position_perso(perso, mur_speed, mur_x, mur_y, momentum_du_saut, saute):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or momentum_du_saut==1:
        
        if (saute<10):
            perso.y -= perso.vitesse
            saute+=1
        else:
            perso.y += perso.vitesse
            saute-=1
        if saute==0:
            momentum_du_saut=0
        
    if keys[pygame.K_DOWN]:
        perso.y += perso.vitesse
    if keys[pygame.K_LEFT]:
        perso.x -= perso.vitesse
        mur_speed= -game_speed
    if keys[pygame.K_RIGHT]:
        perso.x += perso.vitesse 
        mur_speed= game_speed
    if (perso.y==mur_y):
        perso.y=hauteur//2 - hauteur_mur
    mur_speed = game_speed #dépalcement automatoique du mur
    # Empêcher le perso de sortir de l'écran
    perso.x = max(0, min(largeur - perso_largeur, perso.x))
    perso.y = max(0, min(hauteur - perso_hauteur, perso.y))
    return perso.x, perso.y , mur_speed

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
    mur_speed = 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic est détecté
            mouse_x, mouse_y = event.pos  # Position de la souris
            if bouton_x <= mouse_x <= bouton_x + bouton_width and bouton_y <= mouse_y <= bouton_y + bouton_height:
                # Réinitialiser les variables du jeu
                perso.x = largeur // 2
                perso.y = hauteur // 2
                mur_x = largeur
                play_again = True

    if play_again:  # Si le jeu est en cours
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))

        # Mettre à jour la position du perso
        perso.x, perso.y,mur_speed = position_perso(perso, mur_speed, mur_x, mur_y,momentum_du_saut, saute)

        # Déplacer le mur vers la gauche
        mur_x -= mur_speed
        if mur_x < -largeur_mur:  # Si le mur sort de l'écran, le remettre à droite
            mur_x = largeur

        # Vérifier la collision entre le perso et le mur
        #if (perso.x + perso_largeur > mur_x and perso.x < mur_x + largeur_mur and perso.y + perso_hauteur > mur_y and perso.y < mur_y + hauteur_mur):
        #   play_again = False

        # Dessiner le mur
        screen.blit(image_des_murs, (mur_x, mur_y))

        # Afficher le perso
        screen.blit(perso_image, (perso.x, perso.y))

    else:  # Si le jeu est terminé
        # Afficher l'écran de Game Over
        screen.blit(gameover_image, (0, 0))

        # Afficher le bouton "Rejouer"
        affichage_boutton(screen, "Rejouer", bouton_x, bouton_y, bouton_width, bouton_height, (255, 0, 0), (255, 255, 255))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()