import pygame

pygame.init()  # 파이게임을 생성한다.
screen_width = 1280  # 스크린의 가로 길이 설정값
screen_height = 720  # 스크린의 세로 길이 설정값
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # 오른쪽 값을 왼쪽 스크린에 집어넣겠다는 의미인가?
pygame.display.set_caption("Memory Game")  # 게임을 나타낼 캡션 이름 설정

running = True  # 게임이 실행되는가?
while running:  # 실행되고 있을 때
    for event in pygame.event.get():  # 파이게임 이벤트 안에 이벤트가 발생했는가?
        if event.type == pygame.QUIT:  # 이벤트 타입이 그만해를 실행한다면?
            running = False  # False 값을 통해 게임에서 나오도록 한다.
pygame.quit()  # 게임 종료 실행
