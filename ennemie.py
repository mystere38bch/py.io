import pygame


class ennemi(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Chargement des images pour l'animation de marche
        taille=(100,50)
        self.images = [
            pygame.transform.scale(pygame.image.load("image/ennemi1.png"), taille),
            pygame.transform.scale(pygame.image.load("image/ennemi2.png"), taille),
            pygame.transform.scale(pygame.image.load("image/ennemi3.png"), taille),

        ]
        self.i = 0
        self.image = pygame.transform.scale(self.images[self.i], (50, 50))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.vitesse = 2
        self.direction = 1  # 1 = droite, -1 = gauche
        self.temps_anim=0


    def mettre_a_jour(self):
        self.rect.x += self.vitesse*self.direction
    
        self.temps_anim+=1
        if self.temps_anim>=20:
            self.i=(self.i+1)%len(self.images)
            self.image=self.images[self.i]
            self.temps_anim=0
        
        if self.rect.left<0 or self.rect.right>1000:
            self.direction*=-1



    def dessiner(self, screen):
        screen.blit(self.image, self.rect)