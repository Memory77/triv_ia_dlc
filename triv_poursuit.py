import pygame
import numpy as np
from gamers import *


# AFFICHAGE PYGAME


# Initialisation de Pygame
pygame.init()
width, height = 1500, 1000  # Ajustez selon vos besoins
screen = pygame.display.set_mode((width, height))


#liste contenant les id de toutes les categories 
cat_id = [1, 6, 4, 8, 9]

np.random.seed(5)
playing_board = np.random.choice(cat_id, size=(15, 25))

# une couleur pour chaque catégorie
#1 -> rouge
#2 -> bleu
#3 -> vert
#4 -> jaune
#5 -> purple
colors = {cat_id[0]: (110, 0, 0), cat_id[1]: (0, 110, 0), cat_id[2]: (0, 0, 110), cat_id[3]: (110, 110, 0), cat_id[4]: (160, 0, 69)}

# transposition du playing board en fonction des dimensions de l'écran 
cell_width = width // 25
cell_height = height // 15
for i in range(15):
    for j in range(25):
        rect = pygame.Rect(j * cell_width, i * cell_height, cell_width, cell_height)
        pygame.draw.rect(screen, colors[playing_board[i][j]], rect)

   


#creation/initialisation des joueurs et des éléments 
player_one = Gamer(0, 0, 1)
player_two = Gamer(0, 0, 2)

camembert_red = Element(0, 0, "camembert", "red")
camembert_blue = Element(0, 0, "camembert", "blue")
camembert_green = Element(0, 0, "camembert", "green")
camembert_yellow = Element(0, 0, "camembert", "yellow")
camembert_purple = Element(0, 0, "camembert", "purple")

fall_one = Element(0, 0, "fall")


# creation d'un groupe de sprite contenant tous les entités (joueurs et elements)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_one)
all_sprites.add(player_two)
all_sprites.add(camembert_red)
all_sprites.add(camembert_blue)
all_sprites.add(camembert_green)
all_sprites.add(camembert_yellow)
all_sprites.add(camembert_purple)
all_sprites.add(fall_one)


# requalibration de la position des personnage par rapport au tableau et à l'écran (cell_width = width de l'ecran // 25 colonne tb)

# definition de la position et de l'image par joueur
player_one.set_position(10, 2, cell_width, cell_height)
player_one.set_image()
player_two.set_position(10, 10, cell_width, cell_height)
player_two.set_image()

#definition de la position et de l'image du camembert (6 camemberts disposés dans le plateau)
camembert_red.set_position(5, 1, cell_width, cell_height)
camembert_red.set_image()

camembert_blue.set_position(12, 4, cell_width, cell_height)
camembert_blue.set_image()

camembert_green.set_position(6, 8, cell_width, cell_height)
camembert_green.set_image()

camembert_yellow.set_position(2, 9, cell_width, cell_height)
camembert_yellow.set_image()

camembert_purple.set_position(4, 20, cell_width, cell_height)
camembert_purple.set_image()

#idem pour le trou
fall_one.set_position(5, 12, cell_width, cell_height)
fall_one.set_image()




# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    all_sprites.draw(screen)
    all_sprites.update()

    # Mettre à jour l'écran
    pygame.display.flip()

pygame.quit()