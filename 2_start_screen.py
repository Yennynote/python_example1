import pygame

def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)
    # 파이게임에서 제공하는 circle == 스크린 위에 흰 색으로 시작 버튼을 그려준다.

pygame.init()
screen_width = 1280  # 가로 크기
screen_height = 720  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")

start_button = pygame.Rect(0, 0, 120, 120) # Rect 값 == 네모 상자의 크기 값
start_button.center = (120, screen_height - 120) # 네모 상자가 위치할 x, y좌표 값

BLACK = (0, 0, 0)  # RGB
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False 


    screen.fill(BLACK)


    display_start_screen()


    pygame.display.update()


pygame.quit()
