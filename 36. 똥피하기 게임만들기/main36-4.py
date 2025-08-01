import pygame, sys
from pygame.locals import *
import random
import tkinter as tk
from tkinter import messagebox

FPS = 60
MAX_WIDTH = 400
MAX_HEIGHT = 600

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((MAX_WIDTH,MAX_HEIGHT))


class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    def move(self):
        if pressed_keys[K_RIGHT]:
            if self.x < MAX_WIDTH-40:
                self.x += 5
        if pressed_keys[K_LEFT]:
            if self.x > 0:
                self.x -= 5

class Enemy():
    def __init__(self):
        self.x = random.randrange(0, MAX_WIDTH-40)
        self.y = 50
        self.speed = random.randrange(10, 20)
        self.enemy = pygame.image.load(r'C:\Users\stone\codes\파이썬과 40개의 작품들_코드_20220602\py40\36. 똥피하기 게임만들기\똥.png')
        self.enemy = pygame.transform.scale(self.enemy,(40,40))
        
    def draw(self):
        return screen.blit(self.enemy, (self.x, self.y))
    
    def move(self):
        self.y = self.y + self.speed
        if self.y >= MAX_HEIGHT:
            self.y = 50
            self.x = random.randrange(0, MAX_WIDTH-40)
            self.speed = random.randrange(7, 15)


player = Player(MAX_WIDTH/2, MAX_HEIGHT - 40)
enemy = Enemy()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

                    
        clock.tick(FPS) 
        screen.fill((255, 255, 255))
        global pressed_keys
        pressed_keys = pygame.key.get_pressed()
        player_rect = player.draw()
        player.move()
        
        enemy_rect = enemy.draw()
        enemy.move()
        
        if player_rect.colliderect(enemy_rect):
            # print("충돌")
            # pygame.quit()
            # sys.exit()
            # Tkinter 창 숨기기
            root = tk.Tk()
            root.withdraw()  # 실제 GUI 창을 안 띄움

            # 팝업창 띄우기
            messagebox.showinfo("Game Over", "Game Over")
        
        pygame.display.update()

if __name__ == '__main__':
    main()