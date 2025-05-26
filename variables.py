
import pygame

# Dimensions de la fenêtre
largeur, hauteur = 1000, 600
play_again = True
game_speed = 2  # Vitesse de déplacement du mur
distance = 0

#Bouton rejouer
class Bouton:
    def __init__(self, x, y, width, height, text, color=(0, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.x = x
        self.y = y
        self.largeur = width
        self.hauteur = height
        self.color = color

    def draw(self, screen):
        # Dessine le rectagnle du bouton
        pygame.draw.rect(screen, self.color, self.rect)
        # Affichage du texte
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

#ajout Effets sonores
pygame.mixer.init()                
mort_feu_son = pygame.mixer.Sound("Son/mort_feu.mp3") 
mort_ennemi_son = pygame.mixer.Sound("Son/mort_ennemi.mp3") 

bouton_rejouer = Bouton(largeur // 2 - 100, hauteur // 2 + 200, 200, 50, "Rejouer", (255, 0, 0))
bouton_niveau_1 = Bouton(largeur // 2 - 400, hauteur // 2 + 150, 200, 50, "Niveau 1", (0, 255, 0))
bouton_niveau_2 = Bouton(largeur // 2 -100, hauteur // 2 + 150, 200, 50, "Niveau 2", (0, 0, 255))
bouton_niveau_3 = Bouton(largeur // 2  +200, hauteur // 2 + 150, 200, 50, "Niveau 3", (255, 255, 0))

# Perso
perso_image = pygame.image.load("image/perso1.png") 
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

perso = Joueur(largeur//2, 3*hauteur//4, 1)  # Initialisation du perso 

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
perso_image11= pygame.transform.scale(pygame.image.load("image/perso11.png"), (perso_largeur, perso_hauteur))  # Redimensionner l'image2 du perso
perso_image_actuelle = perso_image1




class Mur:
    def __init__(self, x, y, murlargeur, murhauteur, image):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = 3*hauteur//4-y-murhauteur
        self.largeur = murlargeur
        self.hauteur = murhauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
        
liste_mur = [Mur(0,  60,  50, 40, "image/mur_de10.png"),
             Mur(110, 60, 200, 20, "image/mur_de10.png"),
             Mur(400, 60, 200, 20, "image/mur_de10.png"),
             Mur(1000, 60,  100, 30, "image/mur_de10.png"),
             Mur(200, 2000,  0, 0, "image/fond.png")]  # Liste des obstacles

#creation de spikes
class spike:
    def __init__(self, x, y, spikelargeur, spikehauteur, image):
        self.image = pygame.image.load(image)
        self.x = spikehauteur+x
        self.y = 3*hauteur//4-y-spikehauteur
        self.largeur = spikelargeur
        self.hauteur = spikehauteur
        self.image = pygame.transform.scale(self.image, (self.largeur, self.hauteur))
    def animer(self):
        self.image = images_feu[(pygame.time.get_ticks() // 100) % 3]

images_feu = [pygame.transform.scale(pygame.image.load(f"image/feu{i}.png"), (50, 30))
          for i in (1, 2, 3)]

liste_spike= [spike(700, 0, 50, 30, "image/feu1.png"),
               spike(300, 0, 50, 30, "image/feu1.png")]

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
        self.arrivee=3*hauteur//4
        self.vitesse=1
        self.depart=3*hauteur//4
s=Saut(0,0,1)

class Chute:
    def __init__(self,chute_en_cours):
        self.chute_en_cours=chute_en_cours
        self.arrivee=3*hauteur//4
        self.vitesse=1
        self.depart=3*hauteur//4
c=Chute(0)

#Game over
gameover_image = pygame.image.load("game_over.png")
gameover_image = pygame.transform.scale(gameover_image, (largeur, hauteur))

# Création de la fenêtre
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Jeu de OUUUUUF") # Titre de la fenêtre
# Charger l'image de fond
background_image = pygame.image.load("image/fond.png") 
background_image = pygame.transform.scale(background_image, (largeur, hauteur))  


perso = Joueur(largeur//2, 3*hauteur//4, 5)  # Initialisation du perso


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
    
ennemie1 = ennemi(largeur, 3*hauteur//4-50,27,50)

ennemie=[ennemie1]
