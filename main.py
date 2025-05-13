import pygame

# Initialisation de pygame et de la fenêtre
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True
game_speed = 1  # Vitesse de déplacement du mur

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


perso = Joueur(largeur//2, hauteur//2-perso_hauteur, 5)  # Initialisation du persos
perso = Joueur(largeur//2, hauteur//2, 5)  # Initialisation du perso
perso_image1 = pygame.image.load("perso1.png")
perso_image2 = pygame.image.load("perso2.png") 
perso_image7 = pygame.image.load("perso7.png") 
perso_image8 = pygame.image.load("perso8.png") 

perso_largeur, perso_hauteur = 50, 50  # Taille du perso
perso_image1 = pygame.transform.scale(perso_image1, (perso_largeur, perso_hauteur))  # Redimensionner l'image1 du perso
perso_image2 = pygame.transform.scale(perso_image2, (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image7 = pygame.transform.scale(perso_image7, (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image8= pygame.transform.scale(perso_image8, (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image_actuelle = perso_image1


# Objet a sauter dessus
class Mur:
    def __init__(self, x, y, vitesse, largeur, hauteur, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        
objet_mur = Mur(largeur, hauteur//2-30, 0, 100, 30, "Capture d'écran 2024-09-27 201400.png")
liste_mur = [objet_mur]  # Liste des obstacles


#creation de spikes
class spike:
    def __init__(self, x, y, vitesse, largeur, hauteur, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
spikes= spike(largeur/4, hauteur//2-30, 0, 100, 30, "perso1.png")



class Saut:
    def __init__(self,saut_en_cours,position_saut,phase_saut):
        self.saut_en_cours=saut_en_cours
        self.position_saut=position_saut
        self.phase_saut=phase_saut
        self.sur_le_mur=0
        self.arrivee=0
s=Saut(0,0,1)

def position_joueur(perso, objet_mur, s):
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
            perso.x -= perso.vitesse
    if keys[pygame.K_RIGHT]:
            perso.x += perso.vitesse
 
    # Collision avec le mur
    if (perso.x + perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and perso.y + perso_hauteur >= objet_mur.y+1):  # Si le joueur touche le mur
        s.sur_le_mur = True
        s.arrivee = objet_mur.y
    else:
        s.sur_le_mur = False

    if s.sur_le_mur==False and s.saut_en_cours == 0:
       perso.y = min( hauteur//2-perso_hauteur, perso.y + 1 )  # Si le joueur ne touche pas le mur et n'est pas en saut, il tombe

    # Empêcher le joueur de sortir de l'écran
    perso.x = max(0, min(largeur - perso_largeur, perso.x))
    perso.y = max(0, min(hauteur - perso_hauteur, perso.y))
    #remettre phase saut a 0 
    if s.saut_en_cours and s.phase_saut == 0 and perso.y >= hauteur//2 - perso_hauteur:
        s.saut_en_cours = 0
        s.phase_saut = 1

    objet_mur.x -= game_speed  # Déplacer le mur vers la gauche
    if objet_mur.x < -objet_mur.largeur:  # Si le mur sort de l'écran, le remettre à droite
        objet_mur.x = largeur
    return perso, objet_mur

def affichage_boutton(screen, text, x, y, width, height, color, text_color): #exemple trouver sur internet à peut être améliorer
    pygame.draw.rect(screen, color, (x, y, width, height))  # Dessiner le rectangle du bouton
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36
    text_surface = font.render(text, True, text_color)  # Rendre le texte
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Centrer le texte
    screen.blit(text_surface, text_rect)  # Afficher le texte

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
                perso.x = largeur // 2
                perso.y = hauteur // 2- perso_hauteur
                objet_mur.x = largeur
                objet_mur.x = hauteur // 2 - objet_mur.largeur
                spikes.x = largeur / 10
                spikes.y = hauteur // 2 - spikes.largeur
                play_again = True
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
        

    if play_again:  # Si le jeu est en cours
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))

        # Mettre à jour la position du joueur
        perso,objet_mur = position_joueur(perso, objet_mur,s)
        if (perso.x + perso_largeur > objet_mur.x  and perso.y + perso_hauteur >= objet_mur.y+game_speed+1 and perso.x <objet_mur.x+ objet_mur.largeur):  # Si le joueur touche le mur

            if perso.x + perso_largeur - perso.vitesse< objet_mur.x +3 :  # Si le joueur est à droite du mur
                perso.x = objet_mur.x - perso_largeur
            elif perso.x > objet_mur.x : 
                perso.x = objet_mur.x + objet_mur.largeur



        # Vérifier la collision entre le perso et le mur
        #
        if (perso.x + perso_largeur > spikes.x and perso.x < spikes.x + spikes.largeur and perso.y + perso_hauteur > spikes.y and perso.y < spikes.y + spikes.hauteur):
            play_again = False 
        # Dessiner le mur
        for objet_mur in liste_mur:
            screen.blit(objet_mur.image, (objet_mur.x, objet_mur.y))


        


       #animation courir / sauter
        keys = pygame.key.get_pressed()
        if s.saut_en_cours:                                   # e
             perso_image_actuelle = perso_image7
        elif keys[pygame.K_m]:                                # course au sol
            perso_image_actuelle = (
                perso_image1 if (pygame.time.get_ticks() // 100) % 2 == 0 else perso_image2
            )
        else:                                                 # immobile
            perso_image_actuelle = perso_image1

        # Afficher le perso
        screen.blit(perso_image_actuelle, (perso.x, perso.y))
        screen.blit(spikes.image, (spikes.x, spikes.y))  # Afficher le spike

    else:  # Si le jeu est terminé
        # Afficher l'écran de Game Over

        screen.blit(gameover_image, (0, 0))

        # Afficher le bouton "Rejouer"
        affichage_boutton(screen, "Rejouer", bouton_x, bouton_y, bouton_width, bouton_height, (255, 0, 0), (255, 255, 255))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()