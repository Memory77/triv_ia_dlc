import pygame
import random


class Gamer(pygame.sprite.Sprite):
    def __init__(self, x, y, id, player_name, personnage):
        super().__init__()
        self.image = pygame.image.load('img/big_player_one.png')
        self.rect = self.image.get_rect(topleft=(x, y))
        self.id = id
        self.player_name = player_name
        self.x = x
        self.y = y
        self.camembert_colors = []
        self.camembert_part = [] #ou voir pour mettre 0 plutot
        self.score = 0
        self.sound = []
        self.personnage = personnage
        self.current_camembert = None

    def set_position(self, row, col, cell_width, cell_height):
        # définit la position du sprite basée sur la position de la cellule du tableau
        self.rect.x = col * cell_width
        self.rect.y = row * cell_height

    def move(self, direction, cell_height, cell_width, game):
        sound = pygame.mixer.Sound('sounds/step.wav')
        sound.play()
        
        
        if direction == "up":
            self.rect.y -= cell_height
            if self.rect.y < 0:
                self.rect.y = (game.board_game_height - 1) * cell_height
        elif direction == "down":
            self.rect.y += cell_height
            if self.rect.y > (game.board_game_height - 1) * cell_height:
                self.rect.y = 0
        elif direction == "left":
            self.rect.x -= cell_width
            if self.rect.x < 0:
                self.rect.x = (game.board_game_width - 1) * cell_width
        elif direction == "right":
            self.rect.x += cell_width
            if self.rect.x > (game.board_game_width - 1) * cell_width:
                self.rect.x = 0
            
            
    def set_params(self,personnage):
        if personnage == 1: 
            self.image = pygame.image.load('img/big_player_one.png')
            self.sound.append('deadpool.wav')
            self.sound.append('alright-already.wav')
            self.sound.append('are-you-crazy.wav')
        elif personnage == 2: 
            self.image = pygame.image.load('img/big_player_two.png')
            self.sound.append('captain_america.wav')
        elif personnage == 3:
            self.image = pygame.image.load('img/big_player_tree.png')
            self.sound.append('work-work.wav')
            self.sound.append('humain-travail.wav')
            self.sound.append('orc.wav')
        elif personnage == 4:
            self.image = pygame.image.load('img/big_player_four.png')
            self.sound.append('ninja.wav')
            self.sound.append('naruto-chakra.wav')
            self.sound.append('ha-ha.wav')
        elif personnage == 5:
            self.image = pygame.image.load('img/big_player_five.png')
            self.sound.append('ninja.wav')
            self.sound.append('naruto-chakra.wav')
            self.sound.append('ha-ha.wav')
        elif personnage == 6:
            self.image = pygame.image.load('img/big_player_six.png')
            self.sound.append('alright-we-turn-it-on-im-very-thirsty.wav')
            self.sound.append('alright-fine.wav')
            self.sound.append('just-want-you.wav')
        elif personnage == 7:
            self.image = pygame.image.load('img/big_player_seven.png')
            self.sound.append('dragon-spell.wav')
        elif personnage == 8:
            self.image = pygame.image.load('img/big_player_eight.png')
            self.sound.append('naruto-chakra.wav')
            self.sound.append('naruto.wav')
            self.sound.append('naruto-believe-it.wav')
        else:
            self.image = pygame.image.load('img/big_player_tree.png')
            self.sound.append('work-work.wav')
            self.sound.append('humain-travail.wav')
            self.sound.append('orc.wav')
            
    def yell(self):
        random_sound = random.choice(self.sound)
        sound = pygame.mixer.Sound(f"sounds/{random_sound}")
        sound.play()
        
        ###à definir methodes camembert
    
    def check_camembert(self, camembert_sprites):
        for camembert in camembert_sprites:
            if self.rect.colliderect(camembert.rect) and camembert.color not in self.camembert_part:
                return True
        return False
    
    def take_camembert(self, camembert_sprites, game, cell_width, cell_height):
        for camembert in camembert_sprites:
            if self.rect.colliderect(camembert.rect) and camembert.color not in self.camembert_part:
                camembert.kill()
                self.camembert_part.append(camembert.color)
                sound = pygame.mixer.Sound('sounds/take_camembert.wav')
                sound.play()

                #generation d'un nouveau camembert aléatoirement 
                number_min = 0
                number_rows = game.board_game_height - 1
                y = random.randint(number_min, number_rows)

                number_min = 0
                number_cols = game.board_game_height - 1
                x = random.randint(number_min, number_cols)
                
                new_camembert = Element(0, 0, "camembert", camembert.color)
                new_camembert.set_position(y, x, cell_width, cell_height)
                new_camembert.set_image()
                camembert_sprites.add(new_camembert)
                
                print(game.board_game_height)
                print(game.board_game_width)
                print(camembert_sprites)
                print(self.camembert_part)
    
    
    




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

    # def check_fall(self, fall_sprites):
    #     for fall in fall_sprites:
    #         if self.rect.colliderect(fall.rect):

   

