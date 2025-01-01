import pygame
import random

pygame.init()


WIDTH = 800
HEIGHT = 800
COL1 = (62, 88, 121)
COL2 = (216, 196, 182)
COL3 = (245, 239, 231)
BG_COLOR_TOP = (33, 53, 85)
BG_COLOR_BOTTOM = (85, 105, 135)
FONT1 = pygame.font.SysFont("Arial", 40, bold=True)
FONT2 = pygame.font.SysFont("Arial", 30)
FONT3 = pygame.font.SysFont("Arial", 25)

player_choice = None
computer_choice = None
result = None
player_score = 0
computer_score = 0

paper_img = pygame.image.load("rock-paper-scissors/Icons_image/paper.png")
scissors_img = pygame.image.load("rock-paper-scissors/Icons_image/scissor (1).png")
rock_img = pygame.image.load("rock-paper-scissors/Icons_image/stone.png")
choices = {"Rock": rock_img, "Paper": paper_img, "Scissors": scissors_img}

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ROCK PAPER SCISSORS")

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def draw_image(image, x, y, highlight=False):
    original_width, original_height = image.get_size()
    ratio = original_height / original_width
    scaled_image = pygame.transform.scale(image, (150, int(150 * ratio)))
    if highlight:
        pygame.draw.rect(screen, (255, 215, 0), (x - 10, y - 10, 170, 170), 5)
    screen.blit(scaled_image, (x, y))

def draw_background():
    for y in range(HEIGHT):
        color = [
            BG_COLOR_TOP[i] + (BG_COLOR_BOTTOM[i] - BG_COLOR_TOP[i]) * y // HEIGHT
            for i in range(3)
        ]
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))

def draw():
    draw_background()
    draw_text("Rock Paper Scissors", FONT1, COL1, 0.5 * WIDTH, 0.1 * HEIGHT)

    draw_image(choices["Rock"], 0.1 * WIDTH, 0.3 * HEIGHT)
    draw_image(choices["Paper"], 0.4 * WIDTH, 0.3 * HEIGHT)
    draw_image(choices["Scissors"], 0.7 * WIDTH, 0.3 * HEIGHT)

    if player_choice:
        draw_text("Your Choice:", FONT2, COL2, 0.25 * WIDTH, 0.6 * HEIGHT)
        draw_image(choices[player_choice], 0.1 * WIDTH, 0.7 * HEIGHT, highlight=True)

    if computer_choice:
        draw_text("Computer:", FONT2, COL2, 0.75 * WIDTH, 0.6 * HEIGHT)
        draw_image(choices[computer_choice], 0.65 * WIDTH, 0.7 * HEIGHT, highlight=True)

    if result:
        draw_text(result, FONT3, (0, 255, 0) if "Win" in result else (255, 0, 0), 0.5 * WIDTH, 0.9 * HEIGHT)

    
    draw_text(f"Player: {player_score}", FONT2, COL3, 0.3 * WIDTH, 0.95 * HEIGHT)
    draw_text(f"Computer: {computer_score}", FONT2, COL3, 0.7 * WIDTH, 0.95 * HEIGHT)

    pygame.display.update()

def determine_winner(player_choice, computer_choice):
    global player_score, computer_score
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        player_score += 1
        return "You Win!"
    else:
        computer_score += 1
        return "You Lose!"

def get_choice_from_click(pos):
    x, y = pos
    if 0.1 * WIDTH <= x <= 0.1 * WIDTH + 150 and 0.3 * HEIGHT <= y <= 0.3 * HEIGHT + 150:
        return "Rock"
    elif 0.4 * WIDTH <= x <= 0.4 * WIDTH + 150 and 0.3 * HEIGHT <= y <= 0.3 * HEIGHT + 150:
        return "Paper"
    elif 0.7 * WIDTH <= x <= 0.7 * WIDTH + 150 and 0.3 * HEIGHT <= y <= 0.3 * HEIGHT + 150:
        return "Scissors"
    return None

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            player_choice = get_choice_from_click(event.pos)
            if player_choice:
                computer_choice = None
                result = None

                
                pygame.time.wait(500)
                computer_choice = random.choice(list(choices.keys()))
                result = determine_winner(player_choice, computer_choice)

    draw()

pygame.quit()
