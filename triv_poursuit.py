import pygame
import numpy as np
from gamers import *
import random

#quelques fonctions, a mettre surement dans un autre fichier plus tard
def roll_dice():
    return random.randint(1, 6)

def draw_button(screen, text, x, y, width, height, active_color, inactive_color):
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    
    font = pygame.font.SysFont(None, 40)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)
    
    
    
    
# AFFICHAGE PYGAME

# Initialisation de Pygame
pygame.init()
width, height = 1800, 1000  # Ajustez selon vos besoins
screen = pygame.display.set_mode((width, height))


#liste contenant les id de toutes les categories 
cat_id = [1, 6, 4, 8, 9]

np.random.seed(5)
game_board = np.random.choice(cat_id, size=(15, 25))
print(game_board)

## === INTERFACE
#dimensions de l'interface
interface_width = 500  
interface_height = height  # même hauteur que votre fenêtre de jeu
interface_x = width - interface_width  #  positionne l'interface à droite
interface_y = 0  #  positionne l'interface en haut de l'écran

interface_bg_color = (255, 255, 255)
interface_image = pygame.image.load('img/interface_img.png')  
interface_image = pygame.transform.scale(interface_image, (interface_width, interface_height))  # redimensionner l'image

# dimensions de l'écran de l'interface (questions etc)
button_x = interface_x + 50
button_y = 100
button_width = 400
button_height = 50
active_color = (255, 105, 180)
inactive_color = (10, 210, 255)
current_player_index = 0  # Index du joueur actuel


## === PLATEAU DE JEU 
# une couleur pour chaque catégorie
#1 -> rose
#2 -> vert
#3 -> bleu
#4 -> jaune(10, 210, 255)
#5 -> purple
colors = {cat_id[0]: (255, 105, 180), cat_id[1]: (119, 221, 119), cat_id[2]: (10, 210, 255), cat_id[3]: (255, 255, 102), cat_id[4]: (190, 35, 253)}

# largeur du plateau de jeu en soustrayant la largeur de l'interface
game_board_width = width - interface_width

# definition des cellules par rapport au playing board et des dimensions de l'écran 
cell_width = game_board_width  // 25
cell_height = height // 15



#=== INITIALISATION DES JOUEURS ET DES ELEMENTS 
# creation des joueurs 
gamer_sprites = pygame.sprite.Group()
nombre_de_joueurs = 2 #requete bdd pour récup le nombre de player
joueurs = []
for num_joueur in range(1, nombre_de_joueurs + 1):
    nouveau_joueur = Gamer(0, 0, num_joueur)
    joueurs.append(nouveau_joueur)
    gamer_sprites.add(nouveau_joueur)
    nouveau_joueur.set_position(0, 0, cell_width, cell_height)
    nouveau_joueur.set_image()

#creation des camemberts
camembert_red = Element(0, 0, "camembert", "red")
camembert_green = Element(0, 0, "camembert", "green")
camembert_blue = Element(0, 0, "camembert", "blue")
camembert_yellow = Element(0, 0, "camembert", "yellow")
camembert_purple = Element(0, 0, "camembert", "purple")

camembert_sprites = pygame.sprite.Group()
camembert_sprites.add(camembert_red)
camembert_sprites.add(camembert_green)
camembert_sprites.add(camembert_blue)
camembert_sprites.add(camembert_yellow)
camembert_sprites.add(camembert_purple)

#création des trous
fall_one = Element(0, 0, "fall")

fall_sprites = pygame.sprite.Group()
fall_sprites.add(fall_one)



#requalibration de la position et de l'image du camembert (6 camemberts disposés dans le plateau)
camembert_red.set_position(5, 1, cell_width, cell_height)
camembert_red.set_image()

camembert_green.set_position(6, 8, cell_width, cell_height)
camembert_green.set_image()

camembert_blue.set_position(12, 4, cell_width, cell_height)
camembert_blue.set_image()

camembert_yellow.set_position(2, 9, cell_width, cell_height)
camembert_yellow.set_image()

camembert_purple.set_position(4, 20, cell_width, cell_height)
camembert_purple.set_image()

#idem pour le trou
fall_one.set_position(5, 12, cell_width, cell_height)
fall_one.set_image()


# États de jeu
ETAT_LANCER_DE = 1
ETAT_QUESTION = 2
etat_jeu = ETAT_LANCER_DE


# Boucle principale
running = True
while running:
    
    
    #definition visuel du plateau (qui est remis à jour a chaque tour dans la boucle)
    for i in range(15):
        for j in range(25):
            rect = pygame.Rect(j * cell_width, i * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, colors[game_board[i][j]], rect)

    # definition des lignes du playing_board
    line_color = (255, 255, 255)
    # Dessiner les lignes verticales
    for j in range(25):  
        pygame.draw.line(screen, line_color, (j * cell_width, 0), (j * cell_width, height))
    # Dessiner les lignes horizontales
    for i in range(15): 
        pygame.draw.line(screen, line_color, (0, i * cell_height), (game_board_width, i * cell_height))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_x + button_width > event.pos[0] > button_x and button_y + button_height > event.pos[1] > button_y:
                dice_roll = roll_dice()
                player_moves = dice_roll
                print(f"Joueur {current_player_index + 1} a lancé le dé: {dice_roll}")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                joueurs[current_player_index].move("left", cell_height, cell_width)
                player_moves -= 1
            elif event.key == pygame.K_RIGHT:
                joueurs[current_player_index].move("right", cell_height, cell_width)
                player_moves -= 1
            elif event.key == pygame.K_UP:
                joueurs[current_player_index].move("up", cell_height, cell_width)
                player_moves -= 1
            elif event.key == pygame.K_DOWN:
                joueurs[current_player_index].move("down", cell_height, cell_width)
                player_moves -= 1
                
            # Après le mouvement, vérifiez si le joueur a utilisé tous ses mouvements
            if player_moves == 0:
                # Passer au joueur suivant
                current_player_index = (current_player_index + 1) % nombre_de_joueurs
                etat_jeu = ETAT_LANCER_DE  # Réinitialiser l'état du jeu pour le prochain joueur
        
    # màjour du texte du bouton en fonction de l'état du jeu
    if etat_jeu == ETAT_LANCER_DE:
        texte_bouton = f"Joueur {current_player_index + 1} : Lancer le dé"
    elif etat_jeu == ETAT_QUESTION:
        texte_bouton = "Répondre à la question"

  
    
    
    
    
    
    #definition de l'interface
    interface_rect = pygame.Rect(interface_x, interface_y, interface_width, interface_height)
    pygame.draw.rect(screen, interface_bg_color, interface_rect)
    # Afficher l'image de l'interface
    screen.blit(interface_image, (interface_x, interface_y))
    
    draw_button(screen, texte_bouton, button_x, button_y, button_width, button_height, active_color, inactive_color)
    
    #on dessine les différents groupe de sprites
    gamer_sprites.draw(screen)
    gamer_sprites.update()
    
    camembert_sprites.draw(screen)
    camembert_sprites.update()
    
    fall_sprites.draw(screen)
    fall_sprites.update()

    # Mettre à jour l'écran
    pygame.display.flip()

pygame.quit()