import pygame
import random
from variables import *

# Initialisation de pygame et de la fenêtre
pygame.init()
clock = pygame.time.Clock()

def gestion_touche(perso,liste_mur,liste_spike,s,c,distance,ennemie):
    keys = pygame.key.get_pressed()
    s.arrivee = hauteur//2
    # Gestion du saut
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP])and s.saut_en_cours == 0:
        s.saut_en_cours = 1
        s.position_saut = 0
        s.phase_saut = 1
        s.arrivee = hauteur // 2
        s.vitesse = 1
        s.depart = perso.y

    if s.saut_en_cours == 1:
        perso.y = 0.05*s.vitesse*s.vitesse - 5*s.vitesse + s.depart
        
        s.vitesse += 1
        if s.phase_saut == 1:
            s.position_saut += 1
            if s.position_saut > 50:
                s.phase_saut = 0
        else :
            s.position_saut -= 1
            if perso.y + perso_hauteur > s.arrivee:
                s.saut_en_cours = 0
                s.phase_saut = 1
                perso.y  = s.arrivee - perso_hauteur
        
    # Déplacement horizontal
    if keys[pygame.K_LEFT]:
        perso.x -= perso.vitesse
        perso.sens = 0  
    if keys[pygame.K_RIGHT]:
        if(perso.x >= largeur // 2):
            distance+= 1
        perso.sens = 1  
        if perso.x < largeur // 2:
            perso.x += perso.vitesse
        else:
            for objet_mur in liste_mur:
                objet_mur.x -= perso.vitesse  # Déplacer le mur vers la gauche
            for spikes in liste_spike:
                spikes.x -= perso.vitesse
            for ennemie1 in ennemie:
                ennemie1.x -= perso.vitesse
        perso.sens = 1

     

    if keys[pygame.K_c]:
        if len(fireballs) < 1:
            if perso.sens == 1:
                fireballs.append(fireball(perso.x+perso_largeur, perso.y-perso_hauteur/2, 50, 50, perso.sens))
            else:
                fireballs.append(fireball(perso.x, perso.y-perso_hauteur/2, 50, 50, perso.sens))




    # Collision avec le mur
    for objet_mur in liste_mur:
        # Si le joueur est au-dessus du mur
        if perso.y + perso_hauteur <= objet_mur.y:
            s.arrivee = objet_mur.y
            s.sur_le_mur = False
        elif (perso.x + perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and
              perso.y + perso_hauteur > objet_mur.y and perso.y < objet_mur.y + objet_mur.hauteur):
            # Collision avec le dessus du mur
            if perso.y + perso_hauteur - perso.vitesse <= objet_mur.y:
                s.sur_le_mur = True
                s.saut_en_cours = 0
                perso.y = objet_mur.y - perso_hauteur
            # Empêcher de traverser le mur par le bas
            elif perso.y < objet_mur.y + objet_mur.hauteur and perso.y > objet_mur.y and s.saut_en_cours:
                perso.y = objet_mur.y + objet_mur.hauteur
                s.saut_en_cours = 1
                s.vitesse = 90
                s.arrive = hauteur // 2
                s.sur_le_mur = False
            else:
                s.sur_le_mur = False
                # Collision latérale droite
                if perso.x + perso_largeur > objet_mur.x and perso.x < objet_mur.x and perso.sens == 1:
                    perso.x = objet_mur.x - perso_largeur
                # Collision latérale gauche
                elif perso.x < objet_mur.x + objet_mur.largeur and perso.x + perso_largeur > objet_mur.x + objet_mur.largeur and perso.sens == 0:
                    perso.x = objet_mur.x + objet_mur.largeur
        else:
            s.sur_le_mur = False
        
        if objet_mur.x < -objet_mur.largeur:  # Si le mur sort de l'écran, le remettre à droite
            objet_mur.largeur = random.randint(10,largeur//4)
            objet_mur.hauteur = random.randint(10,hauteur//4)
            objet_mur.x = largeur-objet_mur.largeur+400
            objet_mur.y = random.randint(hauteur//2,3*hauteur//4-objet_mur.hauteur)
    for spikes in liste_spike:
        if spikes.x < -spikes.largeur:  # Si le mur sort de l'écran, le remettre à droite
                spikes.x = largeur-spikes.largeur+400

    if s.sur_le_mur==False and s.saut_en_cours == 0:
        perso.y = min( hauteur//2-perso_hauteur, perso.y + 1 )  # Si le joueur ne touche pas le mur et n'est pas en saut, il tombe

    # Empêcher le joueur de sortir de l'écran
    perso.x = max(0, min(largeur - perso_largeur, perso.x))
    perso.y = max(0, min(hauteur - perso_hauteur, perso.y))

    return perso, liste_mur,liste_spike, distance, ennemie

def affichage_boutton(screen, text, x, y, width, height, color, text_color): #exemple trouver sur internet à peut être améliorer
    pygame.draw.rect(screen, color, (x, y, width, height))  # Dessiner le rectangle du bouton
    font = pygame.font.Font(None, 36)  # Police par défaut, taille 36
    text_surface = font.render(text, True, text_color)  # Rendre le texte
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))  # Centrer le texte
    screen.blit(text_surface, text_rect)  # Afficher le texte

# Boucle principale
running = True
while running:
    clock.tick(50)  # Limiter la boucle à 30 FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Fermer la fenêtre
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :  # Si un clic est détecté
            mouse_x, mouse_y = event.pos  # Position de la souris
            if bouton_x <= mouse_x <= bouton_x + bouton_width and bouton_y <= mouse_y <= bouton_y + bouton_height:
                # Réinitialiser les variables du jeu
                perso.x = largeur // 2
                perso.y = hauteur // 2- perso_hauteur
                ennemie1.x = largeur
                ennemie1.y = hauteur // 2 - ennemie1.hauteur
                liste_mur = [Mur(0,  60,  50, 40, "image/mur_de10.png"),
                            Mur(110, 60, 200, 20, "image/mur_de10.png"),
                            Mur(400, 60, 200, 20, "image/mur_de10.png"),
                            Mur(1000, 60,  100, 30, "image/mur_de10.png"),
                            Mur(820, 2000,  0, 0, "image/fond.png")]  # Liste des obstacles
                liste_spike= [spike(700, 0, 50, 30, "image/feu1.png"),
                            spike(300, 0, 50, 30, "image/feu1.png")]
                play_again = True
                distance = 0
                fireballs.clear()


    if play_again:  # Si le jeu est en cours
        # Afficher l'image de fond
        screen.blit(background_image, (0, 0))

        # Mettre à jour la position du joueur
        perso,liste_mur,liste_spike,distance,ennemie = gestion_touche(perso,liste_mur,liste_spike,s,distance,ennemie)
       


        #mettre a jour position ennemi a modifier il fait pas des aller retour
        for mur in liste_mur:
            for ennemie1 in ennemie:
                if ((ennemie1.x<mur.x+mur.largeur and ennemie1.x+ennemie1.largeur>mur.x+mur.largeur) or (ennemie1.x<mur.x and ennemie1.x+ennemie1.largeur>mur.x)):
                    game_speed=-game_speed
                ennemie1.x += game_speed


        #mettre a jour position fireball
        for firebal in fireballs:
            if firebal.sens == 1:
                firebal.x += abs(game_speed)*5
            else:
                firebal.x -= abs(game_speed)*5
            if firebal.x > largeur:
                fireballs.remove(firebal)
            if firebal.x < 0:
                fireballs.remove(firebal)
        # Afficher les fireballs
        for firebal in fireballs:
            if firebal.sens == 1:
                screen.blit(firebal.image_right, (firebal.x, firebal.y))
            else:
                screen.blit(firebal.image_left, (firebal.x, firebal.y))
            for ennemie1 in ennemie:
                if (firebal.x + firebal.largeur > ennemie1.x and firebal.x < ennemie1.x + ennemie1.largeur and firebal.y + firebal.hauteur > ennemie1.y and firebal.y < ennemie1.y + ennemie1.hauteur):
                    fireballs.remove(firebal)
                    ennemie.remove(ennemie1)
        for objet_mur in liste_mur:
            for firebal in fireballs:
                if (firebal.x + firebal.largeur > objet_mur.x and firebal.x < objet_mur.x + objet_mur.largeur and firebal.y + firebal.hauteur > objet_mur.y and firebal.y < objet_mur.y + objet_mur.hauteur):
                    fireballs.remove(firebal)
                
        

        # Vérifier la collision entre le perso et les spikes et ennemis
        for ennemie1 in ennemie:
                if (perso.x + perso_largeur > ennemie1.x and perso.x < ennemie1.x + ennemie1.largeur and perso.y + perso_hauteur > ennemie1.y and perso.y < ennemie1.y + ennemie1.hauteur):
                    play_again = False
        
        
        # Dessiner le mur
        for objet_mur in liste_mur:
            objet_mur.image = pygame.transform.scale(objet_mur.image, (objet_mur.largeur, objet_mur.hauteur))
            screen.blit(objet_mur.image, (objet_mur.x, objet_mur.y))
        for spikes in liste_spike:
            screen.blit(spikes.image, (spikes.x, spikes.y))  # Afficher le spike
            if (perso.x + perso_largeur > spikes.x and perso.x < spikes.x + spikes.largeur and perso.y + perso_hauteur > spikes.y and perso.y < spikes.y + spikes.hauteur):
                play_again = False
                print("collision avec le spike")
            


       #animation courir / sauter
        keys = pygame.key.get_pressed()
        if s.saut_en_cours:                                       # saut
             perso_image_actuelle = perso_image7
        elif keys[pygame.K_RIGHT]:                                # course au sol
            perso_image_actuelle = perso_run_right[(pygame.time.get_ticks() // 100) % 3] 
        elif keys[pygame.K_LEFT]:
            perso_image_actuelle = perso_run_left[(pygame.time.get_ticks() // 100) % 3] 
        elif perso.sens==1:                                                 # immobile
            perso_image_actuelle = perso_image1
        elif perso.sens==0:
            perso_image_actuelle = perso1_left

        # Afficher le perso
        if keys[pygame.K_LEFT]:
            perso_image_actuelle= perso_image11
        screen.blit(perso_image_actuelle, (perso.x, perso.y))
        font = pygame.font.Font(None, 20)  # Taille du texte
        texte = font.render(f"Score:{distance}", True, (0, 0, 0))  # Blanc
        screen.blit(texte, (940, 10))  # Position (x=20, y=10)
        for ennemie1 in ennemie:
            if (ennemie1.temps_anim==0):
                screen.blit(ennemie1.image1, (ennemie1.x, ennemie1.y))
                ennemie1.temps_anim=ennemie1.temps_anim+1
            elif (ennemie1.temps_anim==1):
                screen.blit(ennemie1.image2, (ennemie1.x, ennemie1.y))
                ennemie1.temps_anim=ennemie1.temps_anim+1
            elif (ennemie1.temps_anim==2):
                screen.blit(ennemie1.image3, (ennemie1.x, ennemie1.y))
                ennemie1.temps_anim=0

    else:  # Si le jeu est terminé
        # Afficher l'écran de Game Over

        screen.blit(gameover_image, (0, 0))
        texte = font.render(f"Score:{distance}", True, (255,255,255))  # Blanc
        screen.blit(texte, (largeur//2-25, 50))  # Position (x=20, y=10)

        # Afficher le bouton "Rejouer"
        affichage_boutton(screen, "Rejouer", bouton_x, bouton_y, bouton_width, bouton_height, (255, 0, 0), (255, 255, 255))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter pygame
pygame.quit()
