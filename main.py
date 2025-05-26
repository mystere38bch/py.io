
import pygame
from variables import *
# Initialisation de pygame et de la fenêtre
pygame.init()
clock = pygame.time.Clock()
etat_jeu = 0 



def affichage_accueil(screen, background_image,bouton_niveau1, bouton_niveau2,bouton_niveau3):
    # Afficher l'image de fond
    screen.blit(background_image, (0, 0))
    bouton_niveau_3.draw(screen)
    bouton_niveau_2.draw(screen)
    bouton_niveau_1.draw(screen)

def gestion_touche(perso,liste_mur,liste_spike,s,c,distance,ennemie):
    keys = pygame.key.get_pressed()
    s.arrivee = 3*hauteur//4
    # Gestion du saut
    if (keys[pygame.K_SPACE] or keys[pygame.K_UP])and s.saut_en_cours == 0 and c.chute_en_cours == 0:
        s.saut_en_cours = 1
        s.position_saut = 0
        s.phase_saut = 1
        s.arrivee = hauteur // 2
        s.vitesse = 1
        s.depart = perso.y

    if c.chute_en_cours != 0:
        s.saut_en_cours = 0
        s.sur_le_mur = False
        c.arrivee = 3*hauteur//4
        c.vitesse += 1
        perso.y += 0.05*c.vitesse*c.vitesse
        if perso.y + perso_hauteur >= c.arrivee:
            c.chute_en_cours = 0
            perso.y = c.arrivee - perso_hauteur
            c.vitesse = 1

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
        if perso.y + perso_hauteur < objet_mur.y:
            s.arrivee = objet_mur.y
            s.sur_le_mur = False
        elif (perso.x + perso_largeur > objet_mur.x and perso.x < objet_mur.x + objet_mur.largeur and
              perso.y + perso_hauteur >= objet_mur.y and perso.y < objet_mur.y + objet_mur.hauteur):
            # Collision avec le dessus du mur
            if perso.y + perso_hauteur - perso.vitesse <= objet_mur.y:
                s.sur_le_mur = True
                s.saut_en_cours = 0
                c.arrivee = objet_mur.y
                c.chute_en_cours = 0
                perso.y = objet_mur.y - perso_hauteur
            # Empêcher de traverser le mur par le bas
            elif perso.y < objet_mur.y + objet_mur.hauteur and perso.y > objet_mur.y and s.saut_en_cours:
                c.chute_en_cours = 1
                c.arrivee = 3*hauteur//4
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
            objet_mur.x = largeur-objet_mur.largeur+400
    for spikes in liste_spike:
        if spikes.x < -spikes.largeur:  # Si le mur sort de l'écran, le remettre à droite
                spikes.x = largeur-spikes.largeur+400

    if s.sur_le_mur==False and s.saut_en_cours == 0 :
        perso.y = min( 3*hauteur//4-perso_hauteur, perso.y + 3 )  # Si le joueur ne touche pas le mur et n'est pas en saut, il tombe

    # Empêcher le joueur de sortir de l'écran
    perso.x = max(0, min(largeur - perso_largeur, perso.x))
    perso.y = max(0, min(hauteur - perso_hauteur, perso.y))

    return perso, liste_mur,liste_spike, distance, ennemie


def init_niveau1():
    liste_mur = [
        Mur(0,  61,  50, 40, "image/mur_de10.png"),
        Mur(110, 62, 200, 20, "image/mur_de10.png"),
        Mur(400, 63, 200, 20, "image/mur_de10.png"),
        Mur(700, 100, 100, 20, "image/mur_de10.png"),
        Mur(900, 150, 100, 20, "image/mur_de10.png"),
        Mur(1000, 64, 100, 30, "image/mur_de10.png"),
        Mur(820, 2000, 0, 0, "image/fond.png")
    ]
    liste_spike = [
        spike(300, 0, 50, 30, "image/feu1.png"),
        spike(700, 0, 50, 30, "image/feu1.png")
    ]
    ennemie = [
        ennemi(600, 3*hauteur//4 - 40, 40, 40)
    ]
    return liste_mur, liste_spike, ennemie

def init_niveau2():
    liste_mur = [
        Mur(0,  61,  50, 40, "image/mur_de10.png"),
        Mur(200, 120, 200, 20, "image/mur_de10.png"),
        Mur(500, 200, 150, 20, "image/mur_de10.png"),
        Mur(800, 200, 100, 20, "image/mur_de10.png"),
        Mur(950, 340, 100, 20, "image/mur_de10.png"),
        Mur(1000, 64, 100, 30, "image/mur_de10.png"),
        Mur(820, 2000, 0, 0, "image/fond.png")
    ]
    liste_spike = [
        spike(350, 0, 50, 30, "image/feu1.png"),
        spike(600, 0, 50, 30, "image/feu1.png"),
        spike(850, 0, 50, 30, "image/feu1.png")
    ]
    ennemie = [
        ennemi(400, 3*hauteur//4 - 40, 40, 40),
        ennemi(900, 3*hauteur//4 - 40, 40, 40)
    ]
    return liste_mur, liste_spike, ennemie

def init_niveau3():
    liste_mur = [
        Mur(0,  61,  50, 40, "image/mur_de10.png"),
        Mur(150, 100, 150, 20, "image/mur_de10.png"),
        Mur(400, 180, 200, 20, "image/mur_de10.png"),
        Mur(700, 250, 150, 20, "image/mur_de10.png"),
        Mur(950, 350, 100, 20, "image/mur_de10.png"),
        Mur(1100, 450, 100, 20, "image/mur_de10.png"),
        Mur(1000, 64, 100, 30, "image/mur_de10.png"),
        Mur(820, 2000, 0, 0, "image/fond.png")
    ]
    liste_spike = [
        spike(350, 0, 50, 30, "image/feu1.png"),
        spike(500, 0, 50, 30, "image/feu1.png"),
        spike(750, 0, 50, 30, "image/feu1.png"),
        spike(1050, 0, 50, 30, "image/feu1.png")
    ]
    ennemie = [
        ennemi(350, 3*hauteur//4 - 40, 40, 40),
        ennemi(700, 3*hauteur//4 - 40, 40, 40),
        ennemi(1000, 3*hauteur//4 - 40, 40, 40)
    ]
    return liste_mur, liste_spike, ennemie
# Boucle principale
running = True
while running:
    #clock.tick(120)  # 120 FPS, plus fluide et suffisant

    #Gestion des événements (clics, fermeture, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Gestion des clics sur les boutons d'accueil
        if etat_jeu == 0 and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if bouton_niveau_1.rect.collidepoint(mouse_x, mouse_y):
                etat_jeu = 1
                # Réinitialiser les variables du jeu
                perso.x = largeur // 2
                perso.y = 3*hauteur // 4 - perso_hauteur
                liste_mur, liste_spike, ennemie = init_niveau1()
                play_again = True
                distance = 0
                fireballs.clear()
            elif bouton_niveau_2.rect.collidepoint(mouse_x, mouse_y):
                etat_jeu = 2
                # Réinitialiser les variables du jeu
                perso.x = largeur // 2
                perso.y = 3*hauteur // 4 - perso_hauteur
                liste_mur, liste_spike, ennemie = init_niveau2()
                play_again = True
                distance = 0
                fireballs.clear()
            elif bouton_niveau_3.rect.collidepoint(mouse_x, mouse_y):
                etat_jeu = 3
                # Réinitialiser les variables du jeu
                perso.x = largeur // 2
                perso.y = 3*hauteur // 4 - perso_hauteur
                liste_mur, liste_spike, ennemie = init_niveau3()
                play_again = True
                distance = 0
                fireballs.clear()

        # Gestion du bouton "Rejouer" en game over
        if not play_again and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if bouton_rejouer.rect.collidepoint(mouse_x, mouse_y):
                etat_jeu = 0

    #Logique et affichage selon l'état du jeu
    if etat_jeu == 0:
        affichage_accueil(screen, background_image, bouton_niveau_1, bouton_niveau_2, bouton_niveau_3)

    elif etat_jeu == 1 or etat_jeu == 2 or etat_jeu == 3:
        if play_again:
            # Afficher l'image de fond
            screen.blit(background_image, (0, 0))
            # Mettre à jour la position du joueur

            # Affichage du score, du perso, des ennemis, etc.
            screen.blit(background_image, (0, 0))

            # Mettre à jour la position du joueur
            perso,liste_mur,liste_spike,distance,ennemie = gestion_touche(perso,liste_mur,liste_spike,s,c,distance,ennemie)
            #mettre a jour position ennemi a modifier il fait pas des aller retour
            for mur in liste_mur:
                for ennemie1 in ennemie:
                    if ( ennemie1.y>mur.y) and( (ennemie1.x<mur.x+mur.largeur and ennemie1.x+ennemie1.largeur>mur.x+mur.largeur) or (ennemie1.x<mur.x and ennemie1.x+ennemie1.largeur>mur.x)):
                        game_speed=-game_speed
                    ennemie1.x += game_speed
            #mettre a jour position fireball
            for firebal in fireballs:
                if firebal.sens == 1:
                    firebal.x += abs(game_speed)*20
                else:
                    firebal.x -= abs(game_speed)*20
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
            # Vérifier la collision entre le perso et ennemis
            for ennemie1 in ennemie:
                    if (perso.x + perso_largeur > ennemie1.x and perso.x < ennemie1.x + ennemie1.largeur and perso.y + perso_hauteur > ennemie1.y and perso.y < ennemie1.y + ennemie1.hauteur):
                        play_again = False
                        mort_ennemi_son.play()
            # Dessiner le mur
            for objet_mur in liste_mur:
                screen.blit(objet_mur.image, (objet_mur.x, objet_mur.y))
            for spikes in liste_spike:
                spikes.animer()          
                screen.blit(spikes.image, (spikes.x, spikes.y))
                if (perso.x + perso_largeur > spikes.x and perso.x < spikes.x + spikes.largeur and perso.y + perso_hauteur > spikes.y and perso.y < spikes.y + spikes.hauteur):
                    play_again = False
                    mort_feu_son.play()     
                    print("collision avec le spike")
            #------------------------------------------------peut ralentir le jeu a partir de la
            #        animation courir / sauter
            keys = pygame.key.get_pressed()
            if s.saut_en_cours:                                   # saut
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
            screen.blit(texte, (920, 10))  # Position (x=20, y=10)
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
           
        else:
            # Afficher l'écran de Game Over
            screen.blit(gameover_image, (0, 0))
            font = pygame.font.Font(None, 36)
            texte = font.render(f"Score:{distance}", True, (255,255,255))
            screen.blit(texte, (largeur//2-25, 50))
            bouton_rejouer.draw(screen)

    pygame.display.flip()

pygame.quit()
