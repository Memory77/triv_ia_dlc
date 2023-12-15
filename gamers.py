import pygame
import numpy as np



class Gamer(pygame.sprite.Sprite):
    def __init__(self, x, y, player_number):
        super().__init__()
        self.image = pygame.image.load('img/big_player_one.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.player_number = player_number
        
    

    def set_position(self, row, col, cell_width, cell_height):
        # définit la position du sprite basée sur la position de la cellule du tableau
        self.rect.x = col * cell_width
        self.rect.y = row * cell_height


    def set_image(self):
        if self.player_number == 1:
            self.image = pygame.image.load('img/big_player_one.png')
        elif self.player_number == 2:
            self.image = pygame.image.load('img/big_player_two.png')




class Element(pygame.sprite.Sprite):
    def __init__(self, x, y, name_element, color = 'yellow'):
        super().__init__()
        self.image = pygame.image.load('img/big_player_one.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name_element = name_element
        self.color = color

    def set_position(self, row, col, cell_width, cell_height):
        # définit la position du sprite basée sur la position de la cellule du tableau
        self.rect.x = col * cell_width
        self.rect.y = row * cell_height

    def set_image(self):
        if self.name_element == "fall":
            self.image = pygame.image.load('img/trou-noir.png')

        elif self.name_element == "camembert":
            if self.color == "red":
                self.image = pygame.image.load('img/camembert_red.png')
            elif self.color == "blue":
                self.image = pygame.image.load('img/camembert_blue.png')
            elif self.color == "green":
                self.image = pygame.image.load('img/camembert_green.png')
            elif self.color == "yellow":
                self.image = pygame.image.load('img/camembert_yellow.png')
            elif self.color == "purple":
                self.image = pygame.image.load('img/camembert_purple.png')

   
   

