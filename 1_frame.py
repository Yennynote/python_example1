import pygame

pygame.init() # 선언
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height)) # 변수 = 함수(크기 설정)
pygame.display.set_caption("Memory Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
