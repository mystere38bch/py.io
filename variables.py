
import pygame

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True
game_speed = 1  # Vitesse de déplacement du mur
distance = 0

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
        self.run=0

perso = Joueur(largeur//2, hauteur//2, 5)  # Initialisation du perso 

perso_largeur, perso_hauteur = 50, 50  # Taille du perso

perso_run_right= [
    pygame.transform.scale(pygame.image.load("image/perso1.png"), (perso_largeur, perso_hauteur)) ,
    pygame.transform.scale(pygame.image.load("image/perso2.png"), (perso_largeur, perso_hauteur)) ,
    pygame.transform.scale(pygame.image.load("image/perso3.png"), (perso_largeur, perso_hauteur)) 

]
perso_run_left=[
    pygame.transform.scale(pygame.image.load("image/perso1_left.png"), (perso_largeur, perso_hauteur)) ,
    pygame.transform.scale(pygame.image.load("image/perso2_left.png"), (perso_largeur, perso_hauteur)) ,
    pygame.transform.scale(pygame.image.load("image/perso3_left.png"), (perso_largeur, perso_hauteur)) 
]

perso_image1 = pygame.transform.scale(pygame.image.load("image/perso1.png"), (perso_largeur, perso_hauteur))  # Redimensionner l'image1 du perso
perso1_left = pygame.transform.scale(pygame.image.load("image/perso1_left.png"), (perso_largeur, perso_hauteur))  # Redimensionner l'image1 du perso
perso_image2 = pygame.transform.scale(pygame.image.load("image/perso2.png") , (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image7 = pygame.transform.scale(pygame.image.load("image/perso7.png") , (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image8= pygame.transform.scale(pygame.image.load("image/perso8.png"), (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image_actuelle = perso_image1




class Mur:
    def __init__(self, x, y, murlargeur, murhauteur, image):
        self.image = pygame.image.load(image)
        self.x = murlargeur+x
        self.y = hauteur//2-y-murhauteur
        self.largeur = murlargeur
        self.hauteur = murhauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        
liste_mur = [Mur(0,  0,  50, 40, "image/mur_de10.png"),
             Mur(210, 0, 200, 20, "image/mur_de10.png"),
             Mur(220, 30,  10, 30, "image/mur_de10.png")]  # Liste des obstacles

#creation de spikes
class spike:
    def __init__(self, x, y, spikelargeur, spikehauteur, image):
        self.image = pygame.image.load(image)
        self.x = spikehauteur+x
        self.y = hauteur//2-y-spikehauteur
        self.largeur = spikelargeur
        self.hauteur = spikehauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
liste_spike= [spike(700, 0, 100, 30, "image/perso1.png"),
               spike(300, 0, 100, 30, "image/perso1.png")]

class fireball:
    def __init__(self, x, y, largeur, hauteur,sens):
        self.x = x
        self.y = y
        self.sens = sens
        self.largeur = largeur
        self.hauteur = hauteur
        self.image_right = pygame.transform.scale(pygame.image.load("image/fireball.png"), (self.largeur, self.hauteur))
        self.image_left= pygame.transform.scale(pygame.image.load("image/fireball_left.png"), (self.largeur, self.hauteur))

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
perso_image1 = pygame.image.load("image/perso1.png")
perso_image2 = pygame.image.load("image/perso2.png") 
perso_image7 = pygame.image.load("image/perso7.png") 
perso_image8 = pygame.image.load("image/perso8.png") 

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
        self.sens = 1
        self.image1 = pygame.transform.scale(self.image1, (self.largeur, self.hauteur))
        self.image2 = pygame.transform.scale(self.image2, (self.largeur, self.hauteur))
        self.image3 = pygame.transform.scale(self.image3, (self.largeur, self.hauteur))
        self.temps_anim=0
    
ennemie1 = ennemi(largeur, hauteur//2-50,27,50)

ennemie=[ennemie1]
