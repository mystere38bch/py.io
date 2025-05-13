import pygame

# Initialisation de pygame et de la fenêtre
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True
game_speed = 1

#Bouton rejouer
bouton_width, bouton_height = 200, 50
bouton_x = (largeur - bouton_width) // 2  # Centré horizontalement
bouton_y = ((hauteur - bouton_height) // 10)*9  # Centré verticalement


#Game over
gameover_image = pygame.image.load("game_over.png")
gameover_image = pygame.transform.scale(gameover_image, (largeur, hauteur))

# Création de la fenêtre
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de OUUUUUF") # Titre de la fenêtre
# Charger l'image de fond
background_image = pygame.image.load("Capture d'écran 2024-10-03 202909.png") 
background_image = pygame.transform.scale(background_image, (largeur, hauteur))  

# Perso
perso_image = pygame.image.load("Capture d'écran 2024-09-27 201400.png") 
perso_largeur, perso_hauteur = 50, 50  # Taille du perso
perso_image = pygame.transform.scale(perso_image, (perso_largeur, perso_hauteur))  # Redimensionner l'image du perso
class Joueur:
    def __init__(self, x, y, vitesse):
        self.x = x 
        self.y = y
        self.vitesse = vitesse #vitesse de déplacement du perso

perso = Joueur(largeur//2, hauteur//2-perso_hauteur, 5)  # Initialisation du perso

# Objet a éviter
class Mur:
    def __init__(self, x, y, vitesse, largeur, hauteur, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.largeur = largeur
        self.hauteur = hauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        
objet_mur = Mur(largeur, hauteur//2-30, 0, 100, 30, "Capture d'écran 2024-09-27 201400.png")

mur_speed = 0  # Vitesse de déplacement du mur/ tous les obstacles



class Saut:
    def __init__(self,saut_en_cours,position_saut,phase_saut):
        self.saut_en_cours=saut_en_cours
        self.position_saut=position_saut
        self.phase_saut=phase_saut
        self.sur_le_mur=0
        self.arrivee=0
s=Saut(0,0,1)

def position_joueur(perso, mur_speed, objet_mur, s):
    keys = pygame.key.get_pressed()

    # Gestion du saut
    if keys[pygame.K_SPACE]:
        if s.saut_en_cours == 0:
            s.saut_en_cours = 1
            s.position_saut = 0
    if s.saut_en_cours == 1 and s.phase_saut == 1:
        s.position_saut += 1
        perso.y -= 1
        if s.position_saut > 50:
            s.phase_saut = 0
    if s.saut_en_cours == 1 and s.phase_saut == 0:
        s.position_saut -= 1
        perso.y += 1
    if s.saut_en_cours == 1 and s.phase_saut == 0 and perso.y+perso_hauteur >= s.arrivee:
        s.saut_en_cours = 0
        s.phase_saut = 1

    # Déplacement horizontal
    if keys[pygame.K_LEFT]:
        if (perso.x+ perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and perso.y + perso_hauteur < objet_mur.y) and s.sur_le_mur == False:  # Si le joueur touche le mur
            perso.x = objet_mur.x + objet_mur.largeur
            mur_speed=0
        elif (s.sur_le_mur==True):
            mur_speed=-perso.vitesse
            perso.x-=1
        else:
            perso.x -= perso.vitesse
            mur_speed = game_speed
    if keys[pygame.K_RIGHT]:
        if (perso.x+ perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and perso.y + perso_hauteur < objet_mur.y) and s.sur_le_mur == False:  # Si le joueur touche le mur
            perso.x = objet_mur.x - perso_largeur
            mur_speed=0
        elif (s.sur_le_mur==True):
            mur_speed=perso.vitesse
            perso.x+=1
        else:
            perso.x += perso.vitesse
            mur_speed = game_speed

    # Collision avec le mur
    if (perso.x + perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and perso.y + perso_hauteur > objet_mur.y):  # Si le joueur touche le mur
        s.sur_le_mur = True
        s.arrivee = objet_mur.y
    else:
        s.sur_le_mur = False

    if s.sur_le_mur==False and s.saut_en_cours == 0:
       perso.y = min( hauteur//2-perso_hauteur, perso.y + 1 )  # Si le joueur ne touche pas le mur et n'est pas en saut, il tombe

    # Empêcher le joueur de sortir de l'écran
    perso.x = max(0, min(largeur - perso_largeur, perso.x))
    perso.y = max(0, min(hauteur - perso_hauteur, perso.y))

    return perso.x, perso.y, mur_speed

def affichage_boutton(screen, text, x, y, width, height, color, text_color): #exemple trouver sur internet à peut être améliorer
    pygame.draw.rect(screen, color, (x, y, width, height))  # Dessiner le rectangle du bouton
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36
    text_surface = font.render(text, True, text_color)  # Rendre le texte
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Centrer le texte
    screen.blit(text_surface, text_rect)  # Afficher le texte

# Boucle principale
running = True
while running:
    mur_speed = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Si un clic est détecté
            mouse_x, mouse_y = event.pos  # Position de la souris
            if bouton_x <= mouse_x <= bouton_x + bouton_width and bouton_y <= mouse_y <= bouton_y + bouton_height:
                # Réinitialiser les variables du jeu
                perso.x = largeur // 2
                perso.y = hauteur // 2- perso_hauteur
                objet_mur.x = largeur
                objet_mur.x = hauteur // 2 - objet_mur.largeur
                play_again = True

    if play_again:  # Si le jeu est en cours
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))

        # Mettre à jour la position du joueur
        perso.x, perso.y,mur_speed = position_joueur(perso, mur_speed, objet_mur,s)

        # Déplacer le mur vers la gauche
        objet_mur.x -= mur_speed
        if objet_mur.x < -objet_mur.largeur:  # Si le mur sort de l'écran, le remettre à droite
            objet_mur.x = largeur
    


        # Vérifier la collision entre le perso et le mur
        #if (perso.x + perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and perso.y + perso_hauteur > objet_mur.y and perso.y < objet_mur.y + objet_mur.largeur):
        #   play_again = False

        # Dessiner le mur
        screen.blit(objet_mur.image, (objet_mur.x, objet_mur.y))

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