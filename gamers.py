import pygame
import numpy as np



class Gamer(pygame.sprite.Sprite):
    def __init__(self, x, y, player_number):
        super().__init__()
        self.image = pygame.image.load('img/big_player_one.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.player_number = player_number
        self.camembert_part = []
    

    def set_position(self, row, col, cell_width, cell_height):
        # définit la position du sprite basée sur la position de la cellule du tableau
        self.rect.x = col * cell_width
        self.rect.y = row * cell_height

    def move(self, direction, cell_height, cell_width):
            if direction == "up":
                self.rect.y -= cell_height
            elif direction == "down":
                self.rect.y += cell_height
            elif direction == "left":
                self.rect.x -= cell_width
            elif direction == "right":
                self.rect.x += cell_width
                
    def set_image(self):
        if self.player_number == 1:
            self.image = pygame.image.load('img/big_player_one.png')
        elif self.player_number == 2:
            self.image = pygame.image.load('img/big_player_two.png')
        elif self.player_number == 3:
            self.image = pygame.image.load('img/big_player_tree.png')
        elif self.player_number == 4:
            self.image = pygame.image.load('img/big_player_four.png')
        elif self.player_number == 5:
            self.image = pygame.image.load('img/big_player_five.png')
        elif self.player_number == 6:
            self.image = pygame.image.load('img/big_player_six.png')
            
            
    def collect_camembert(self, camembert_color):
        if camembert_color not in self.camembert_part:
            self.camembert_part.append(camembert_color)
        
        if len(self.camembert_part) == 5:
            print(f'le joueur : {self.player_number} a gagné !')
            self.kill
            
    def check_for_camembert(player, camembert_sprites):
        for camembert in camembert_sprites:
            if player.rect.colliderect(camembert.rect):
                player.collect_camembert()
                # camembert.kill()  # retirer le camembert du plateau
                break  



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

   
   

