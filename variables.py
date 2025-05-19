import pygame

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True
game_speed = 1  # Vitesse de déplacement du mur

#Bouton rejouer
bouton_width, bouton_height = 200, 50
bouton_x = (largeur - bouton_width) // 2  # Centré horizontalement
bouton_y = ((hauteur - bouton_height) // 10)*9  # Centré verticalement

# Perso
perso_image = pygame.image.load("Capture d'écran 2024-09-27 201400.png") 
perso_largeur, perso_hauteur = 50, 50  # Taille du perso
perso_image = pygame.transform.scale(perso_image, (perso_largeur, perso_hauteur))  # Redimensionner l'image du perso
class Joueur:
    def __init__(self, x, y, vitesse):
        self.x = x 
        self.y = y
        self.vitesse = vitesse #vitesse de déplacement du perso
        self.image = pygame.transform.scale(perso_image, (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sens = 1

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


class Mur:
    def __init__(self, x, y, vitesse, largeur, hauteur, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        
#objet_mur = Mur(largeur, hauteur//2-30, 0, 100, 30, "Capture d'écran 2024-09-27 201400.png")
liste_mur = [Mur(largeur+10, hauteur//2-200, 0, 50, 40, "image/mur_de10.png"),
             Mur(largeur+210, hauteur//2-20, 0, 200, 20, "image/mur_de10.png"),
             Mur(largeur+220, hauteur//2-30, 0, 10, 30, "image/mur_de10.png")]  # Liste des obstacles


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

class fireball:
    def __init__(self, x, y, largeur, hauteur):
        self.image = pygame.image.load("image/fireball.png")
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))

fireballs=[]

class Saut:
    def __init__(self,saut_en_cours,position_saut,phase_saut):
        self.saut_en_cours=saut_en_cours
        self.position_saut=position_saut
        self.phase_saut=phase_saut
        self.sur_le_mur=0
        self.arrivee=hauteur//2
        self.vitesse=1
        self.depart=hauteur//2
s=Saut(0,0,1)


#Game over
gameover_image = pygame.image.load("game_over.png")
gameover_image = pygame.transform.scale(gameover_image, (largeur, hauteur))

# Création de la fenêtre
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de OUUUUUF") # Titre de la fenêtre
# Charger l'image de fond
background_image = pygame.image.load("Fond.png") 
background_image = pygame.transform.scale(background_image, (largeur, hauteur))  


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

class ennemi:
    def __init__(self, x, y, largeur, hauteur):
        self.image1 = pygame.image.load("image/ennemi1.png")
        self.image2 = pygame.image.load("image/ennemi2.png")
        self.image3 = pygame.image.load("image/ennemi3.png")
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.image1 = pygame.transform.scale(self.image1, (self.largeur, self.hauteur))
        self.image2 = pygame.transform.scale(self.image2, (self.largeur, self.hauteur))
        self.image3 = pygame.transform.scale(self.image3, (self.largeur, self.hauteur))
        self.temps_anim=0
    
ennemie1 = ennemi(largeur, hauteur//2-50,27,50)


