import pygame


def dispay_start_screen():  # 시작 버튼은 다음과 같이 실행한다.
    pygame.draw.circle(screen, GREEN, start_button.center, 60, 5)  # 시작 버튼 설정 값


pygame.init()  # 파이게임을 생성한다.
screen_width = 1280  # 스크린의 가로 길이 설정값
screen_height = 720  # 스크린의 세로 길이 설정값
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # 오른쪽 값을 왼쪽 스크린에 집어넣겠다는 의미인가?
pygame.display.set_caption("Memory Game")  # 게임을 나타낼 캡션 이름 설정

start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)  # x, y 좌표 값

BLACK = (0, 0, 0)  # 바탕화면 색
GREEN = (89, 184, 149)  # 시작 버튼 색


running = True  # 게임이 실행되는가?
while running:  # 실행되고 있을 때
    for event in pygame.event.get():  # 파이게임 이벤트 안에 이벤트가 발생했는가?
        if event.type == pygame.QUIT:  # 이벤트 타입이 그만해를 실행한다면?
            running = False  # False 값을 통해 게임에서 나오도록 한다.

    screen.fill(BLACK)  # 스크린은 이 색으로 채운다.
    dispay_start_screen()
    pygame.display.update()


pygame.quit()  # 게임 종료 실행
