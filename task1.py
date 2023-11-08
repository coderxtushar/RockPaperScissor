import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 600

WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Red, Green, Blue

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

# Load images and resize them
rock_img = pygame.image.load("rock.png")
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.image.load("paper.png")
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissors_img = pygame.image.load("scissors.png")
scissors_img = pygame.transform.scale(scissors_img, (150, 150))

# Game options
options = ["Rock", "Paper", "Scissors"]

# Functions
def draw_text(text, x, y, font_size=36, colors=None):
    font = pygame.font.Font(None, font_size)
    x_pos = x
    for letter in text:
        if colors:
            color = random.choice(colors)
        else:
            color = WHITE
        text_surface = font.render(letter, True, color)
        screen.blit(text_surface, (x_pos, y))
        x_pos += font_size-10 # Adjust the spacing
    pygame.display.update()

def reset_game():
    screen.fill((0, 0, 0))
    draw_text("Rock, Paper, Scissors", 250, 50, 48, COLORS)
    draw_text("Choose your move:", 400, 180, 36, COLORS)
    draw_text("Rock", 200, 400, colors=COLORS)
    draw_text("Paper", 500, 400, colors=COLORS)
    draw_text("Scissors", 800, 400, colors=COLORS)
    pygame.display.update()

def draw_options():
    screen.blit(rock_img, (150, 250))
    screen.blit(paper_img, (450, 250))
    screen.blit(scissors_img, (750, 250))
    pygame.display.update()

def get_computer_choice():
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

reset_game()
draw_options()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 90 <= event.pos[0] <= 290 and 250 <= event.pos[1] <= 450:
                user_choice = "Rock"
            elif 380 <= event.pos[0] <= 580 and 250 <= event.pos[1] <= 450:
                user_choice = "Paper"
            elif 670 <= event.pos[0] <= 870 and 250 <= event.pos[1] <= 450:
                user_choice = "Scissors"
            else:
                continue

            computer_choice = get_computer_choice()
            winner = determine_winner(user_choice, computer_choice)

            reset_game()
            draw_options()
            draw_text(f"You chose: {user_choice}", 100, 100)
            draw_text(f"Computer chose: {computer_choice}", 100, 150)
            draw_text(winner, 350, 300, 48)
            pygame.display.update()

pygame.quit()
