import pygame
import numpy as np
from gamers import *
import random
import main
import sql_game

#quelques fonctions, a mettre surement dans un autre fichier plus tard
def roll_dice(dice: int):
    return random.randint(1, dice)

def verifier_reponse(response):
    if response == False:
        sound = pygame.mixer.Sound('sounds/hahaha.wav')
        sound.play()
    return response  # retourne true si la réponse est correcte, False sinon

def draw_button(screen, text, x, y, width, height, active_color, inactive_color, font_size):
    mouse = pygame.mouse.get_pos()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, width, height))
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    
    font = pygame.font.SysFont(None, font_size)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (width / 2)), (y + (height / 2)))
    screen.blit(text_surf, text_rect)
    

    
# AFFICHAGE PYGAME

# Initialisation de Pygame
pygame.init()

pygame.mixer.init() 

width, height = 1800, 1000  # Ajustez selon vos besoins
screen = pygame.display.set_mode((width, height))


## === INTERFACE (coté droit, pour tout ce qui est interaction questions etc.)
#dimensions de l'interface
interface_width = 500  
interface_height = height  # même hauteur que votre fenêtre de jeu
interface_x = width - interface_width  #  positionne l'interface à droite
interface_y = 0  #  positionne l'interface en haut de l'écran

interface_bg_color = (255, 255, 255)
interface_image = pygame.image.load('img/interface_img.png')  
interface_image = pygame.transform.scale(interface_image, (interface_width, interface_height))  # redimensionner l'image

# dimensions du bouton principal de l'interface pour l'interaction(dé, questions etc)
button_x = interface_x + 50
button_y = 100
button_width = 400
button_height = 50
active_color = (255, 105, 180)
inactive_color = (10, 210, 255)



## === PLATEAU DE JEU (coté gauche, cependant, il est réellement defini dans la boucle de jeu car doit se mettre à jour)

#liste contenant les id de toutes les categories 
cat_id = []
colors = {}
for categorie in sql_game.categories():
    cat_id.append(categorie[0])
    colors[categorie[0]] = (categorie[1], categorie[2], categorie[3])

np.random.seed(5)#graine pour figer le random choice mais c pas obligé en soit
game_board = np.random.choice(cat_id, size=(15, 25))


# import du nouveau jeu
game = main.new_game()

# definition de la largeur du plateau de jeu en soustrayant la largeur de l'interface
game_board_width = width - interface_width

# definition des cellules par rapport au playing board et des dimensions de l'écran afin de pouvoir positionner les entités apres
cell_width = game_board_width  // game.board_game_width
cell_height = height // game.board_game_height


#=== INITIALISATION DES JOUEURS ET DES ELEMENTS 
# creation des joueurs 
gamer_sprites = pygame.sprite.Group()
joueurs = []
game_gamers_sprite = game.gamers_sprite()
for gamer in game_gamers_sprite:
    joueurs.append(gamer)
    gamer_sprites.add(gamer)
    gamer.set_position(gamer.y, gamer.x, cell_width, cell_height)
    gamer.set_params(gamer.personnage)
print('Que le jeu TRIV POURSUITE IA COMMENCE !\n règles du jeu : à definir')

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
camembert_red.set_position(0, 24, cell_width, cell_height)
camembert_red.set_image()

camembert_green.set_position(14, 24, cell_width, cell_height)
camembert_green.set_image()

camembert_blue.set_position(5, 13, cell_width, cell_height)
camembert_blue.set_image()

camembert_yellow.set_position(0, 0, cell_width, cell_height)
camembert_yellow.set_image()

camembert_purple.set_position(14, 0, cell_width, cell_height)
camembert_purple.set_image()

#idem pour le trou
fall_one.set_position(10, 13, cell_width, cell_height)
fall_one.set_image()


# États de jeu
ETAT_LANCER_DE = 1
ETAT_QUESTION = 2
etat_jeu = ETAT_LANCER_DE
current_player_index = 0
dice_roll = 0
dice_rolled = False

# Boucle principale
running = True
while running:
    
    #definition visuel du plateau (qui est remis à jour a chaque tour dans la boucle)
    for i in range(game.board_game_height):
        for j in range(game.board_game_width):
            rect = pygame.Rect(j * cell_width, i * cell_height, cell_width, cell_height)
            pygame.draw.rect(screen, colors[game_board[i][j]], rect)

    # definition des lignes du playing_board
    line_color = (255, 255, 255)
    # Dessiner les lignes verticales
    for j in range(game.board_game_width):  
        pygame.draw.line(screen, line_color, (j * cell_width, 0), (j * cell_width, height))
    # Dessiner les lignes horizontales
    for i in range(game.board_game_height): 
        pygame.draw.line(screen, line_color, (0, i * cell_height), (game_board_width, i * cell_height))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if dice_rolled == False and button_x + button_width > event.pos[0] > button_x and button_y + button_height > event.pos[1] > button_y:
                dice_roll = roll_dice(game.dice)
                dice_rolled = True
                player_moves = dice_roll
                print(f"Joueur {current_player_index + 1} a lancé le dé: {dice_roll}")

        elif event.type == pygame.KEYDOWN:
            if dice_rolled and player_moves > 0:
                if event.key == pygame.K_LEFT:
                    joueurs[current_player_index].move("left", cell_height, cell_width, game)
                    player_moves -= 1
                elif event.key == pygame.K_RIGHT:
                    joueurs[current_player_index].move("right", cell_height, cell_width, game)
                    player_moves -= 1
                elif event.key == pygame.K_UP:
                    joueurs[current_player_index].move("up", cell_height, cell_width, game)
                    player_moves -= 1
                elif event.key == pygame.K_DOWN:
                    joueurs[current_player_index].move("down", cell_height, cell_width, game)
                    player_moves -= 1
                on_camembert = joueurs[current_player_index].check_camembert(camembert_sprites)
                if on_camembert:
                    etat_jeu = ETAT_QUESTION
                    player_moves = 0
            if player_moves == 0 and dice_rolled:
                etat_jeu = ETAT_QUESTION
                if event.key == pygame.K_SPACE:  # espace pour la confirmation de la fin du tour
                    dice_rolled = False
                    etat_jeu = ETAT_LANCER_DE 
                    current_player_index = (current_player_index + 1) % main.nb_gamers
                    joueurs[current_player_index].yell()
                    print(f"Passage au joueur {current_player_index + 1}")
                    dice_roll = 0

    
    # définition visuelle de l'interface
    interface_rect = pygame.Rect(interface_x, interface_y, interface_width, interface_height)
    pygame.draw.rect(screen, interface_bg_color, interface_rect)
    # pour afficher l'image de l'interface
    screen.blit(interface_image, (interface_x, interface_y))
    
    ### === mise à jour des scores
    button_start_x = 1300  
    button_start_y = 800   
    button_x_ = button_start_x
    button_y_ = button_start_y

    max_buttons_per_row = 4  #nombre maximal de boutons par ligne
    button_count = 0  # cpt de boutons pour contrôler la création de nouvelles lignes

    for gamer in gamer_sprites:
        draw_button(screen, gamer.player_name, button_x_, button_y_, 150, button_height, active_color, inactive_color,25)
        draw_button(screen, f"{gamer.score}", button_x_, button_y_ + 50, 150, button_height, active_color, inactive_color,25)

        # mise à jour des positions des boutons pour le prochain joueur
        button_x_ += 120
        button_count += 1

        # Passer à la ligne suivante si le nombre maximal de boutons est atteint
        if button_count >= max_buttons_per_row:
            button_x_ = button_start_x
            button_y_ += 100  # Augmenter de 100 pour la prochaine ligne
            button_count = 0
    
    # mise à jour le texte du bouton en fonction de l'état du jeu
    if etat_jeu == ETAT_LANCER_DE:
        texte_bouton = f"{joueurs[current_player_index].player_name} : Lancer le dé"
        draw_button(screen, texte_bouton, button_x, button_y, button_width, button_height, active_color, inactive_color, 40)
        if dice_roll > 0:
            draw_button(screen, f"{player_moves}", 1450, 200, 200, button_height, active_color, inactive_color, 40)
            
            
    elif etat_jeu == ETAT_QUESTION:
        
        draw_button(screen, f"{joueurs[current_player_index].player_name}", button_x, button_y, button_width, button_height, active_color, inactive_color, 40)
        
        ##id categorie de la position du gamer 
        case_categorie_id = game_board[joueurs[current_player_index].y][joueurs[current_player_index].x]
        
        questions_et_reponses = {
            "Qu'est ce que l'IA ? (test)": {
                "la bonne réponse": True,
                "suggestion_2": False,
                "suggestion_3": False,
                "suggestion_4": False
            }
        }

        # creation des rectangles pour les boutons de réponse
        reponse_1_rect = pygame.Rect(button_x, 250, button_width, button_height)
        reponse_2_rect = pygame.Rect(button_x, 300, button_width, button_height)
        reponse_3_rect = pygame.Rect(button_x, 350, button_width, button_height)
        reponse_4_rect = pygame.Rect(button_x, 400, button_width, button_height)
        
        
        la_question = "Qu'est ce que l'IA ? (test)"
        draw_button(screen, la_question, button_x, 200, button_width, button_height, active_color, inactive_color, 40)
        draw_button(screen, "la bonne réponse", button_x, 250, button_width, button_height, active_color, inactive_color, 35)
        draw_button(screen, "suggestion_2", button_x, 300, button_width, button_height, active_color, inactive_color, 35)
        draw_button(screen, "suggestion_3", button_x, 350, button_width, button_height, active_color, inactive_color, 35)
        draw_button(screen, "suggestion_4", button_x, 400, button_width, button_height, active_color, inactive_color, 35)
        
        reponse = None

        if event.type == pygame.MOUSEBUTTONDOWN:
            if reponse_1_rect.collidepoint(event.pos):
                reponse = "la bonne réponse"
            elif reponse_2_rect.collidepoint(event.pos):
                reponse = "suggestion_2"
            elif reponse_3_rect.collidepoint(event.pos):
                reponse = "suggestion_3"
            elif reponse_4_rect.collidepoint(event.pos):
                reponse = "suggestion_4"

            if reponse is not None and reponse in questions_et_reponses[la_question]:
                if verifier_reponse(questions_et_reponses[la_question][reponse]): 
                    joueurs[current_player_index].take_camembert(camembert_sprites, game)
                    joueurs[current_player_index].score += 500
                etat_jeu = ETAT_LANCER_DE
                dice_rolled = False
                dice_roll = 0
                current_player_index = (current_player_index + 1) % main.nb_gamers
                
        #######
        #
        #
        #
        #
        #definir reste code
        
        
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