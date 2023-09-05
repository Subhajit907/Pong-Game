import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
BALL_SPEED = [2,2]
PADDLE_SPEED = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Initialize paddles and ball
paddle_width, paddle_height = 10, 80
ball_width, ball_height = 10, 10

player_paddle = pygame.Rect(10, (HEIGHT // 2) - (paddle_height // 2), paddle_width, paddle_height)
opponent_paddle = pygame.Rect(WIDTH - 20, (HEIGHT // 2) - (paddle_height // 2), paddle_width, paddle_height)
ball = pygame.Rect((WIDTH // 2) - (ball_width // 2), (HEIGHT // 2) - (ball_height // 2), ball_width, ball_height)

# Initialize ball direction
ball_direction = random.choice([1, -1])

# Initialize scores
player_score = 0
opponent_score = 0

# Fonts
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        player_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        opponent_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        opponent_paddle.y += PADDLE_SPEED

    # Ball movement
    ball.x += BALL_SPEED[0] * ball_direction
    ball.y += BALL_SPEED[1]

    # Ball collisions with paddles and top/bottom walls
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        BALL_SPEED[0] *= -1

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED[1] *= -1

    # Ball out of bounds
    if ball.left <= 0:
        opponent_score += 1
        ball = pygame.Rect((WIDTH // 2) - (ball_width // 2), (HEIGHT // 2) - (ball_height // 2), ball_width, ball_height)
        ball_direction = 1

    if ball.right >= WIDTH:
        player_score += 1
        ball = pygame.Rect((WIDTH // 2) - (ball_width // 2), (HEIGHT // 2) - (ball_height // 2), ball_width, ball_height)
        ball_direction = -1

    # Drawing everything on the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Display scores
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (10, 10))
    screen.blit(opponent_text, (WIDTH - opponent_text.get_width() - 10, 10))

    pygame.display.flip()

pygame.quit()
