import pygame

# Perso

perso_image = pygame.image.load("./image/Capture d'écran 2024-09-27 201400.png") 
perso_largeur, perso_hauteur = 50, 50  # Taille du perso
perso_image = pygame.transform.scale(perso_image, (perso_largeur, perso_hauteur))  # Redimensionner l'image du perso
class Joueur:
    def __init__(self, x, y, vitesse):
        self.x = x 
        self.y = y
        self.vitesse = vitesse #vitesse de déplacement du perso

perso = Joueur(largeur//2, hauteur//2-perso_hauteur, 5)  # Initialisation du perso
