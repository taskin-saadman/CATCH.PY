import pygame
#class for storing images used in the game
class Images:
    def __init__(self):
        #constructor to initialize the images used in the game
        self.basket_image = pygame.image.load('images/basket.png')
        self.apple_image = pygame.image.load('images/apple.png')
        self.bomb_image = pygame.image.load('images/bomb.jpg')
        self.heart_image = pygame.image.load('images/heart.png')
        self.bg_image = pygame.image.load('images/bg.png')
        self.gApple_image = pygame.image.load('images/golden apple.png')
        self.magnet_image = pygame.image.load('images/magnet.png')
        self.pause_image = pygame.image.load('images/pause.png')

        self.heart_image = pygame.transform.scale(self.heart_image, (30, 30))
        self.basket_image = pygame.transform.scale(self.basket_image, (100, 100))
        self.apple_image = pygame.transform.scale(self.apple_image, (50, 50))
        self.bomb_image = pygame.transform.scale(self.bomb_image, (50, 50))
        self.diagonal_bomb_image = pygame.transform.scale(self.bomb_image, (50, 50))
        self.bg_image = pygame.transform.scale(self.bg_image, (700, 800))
        self.gApple_image = pygame.transform.scale(self.gApple_image, (60, 60))
        self.magnet_image = pygame.transform.scale(self.magnet_image, (60, 60))
        self.pause_image = pygame.transform.scale(self.pause_image, (60, 60))