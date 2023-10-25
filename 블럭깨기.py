
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
BRICK_COLOR = (0, 128, 0)

# 블록과 아이템 생성 함수
def create_bricks():
    bricks = []
    for i in range(5):
        for j in range(8):
            brick = pygame.Rect(j * (BRICK_WIDTH + 5) + 50, i * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
            brick.depth = BRICK_DEPTH
            brick.color = random.choice(BRICK_COLORS)
            bricks.append(brick)
    return bricks

def create_item(x, y):
    item = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
    item.depth = BRICK_DEPTH
    item.color = random.choice(ITEM_COLORS)
    return item

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT - 50, 30, 30)
ball_speed_x = BALL_SPEED
ball_speed_y = -BALL_SPEED

# Game loop에서 아이템 관련 코드 추가
if ball.colliderect(paddle) and ball_speed_y > 0:
    ball_speed_y = -ball_speed_y
    if random.random() < 0.2:  # 20% 확률로 아이템 생성
        item = create_item(ball.x, ball.y)
        items.append(item)

# Draw everything
for brick in bricks:
    pygame.draw.rect(screen, brick.color, brick)

for item in items:
    pygame.draw.rect(screen, item.color, item)

# 아이템 처리
items_to_remove = []
for item in items:
    item.y += 1  # 아이템이 아래로 이동
    if item.colliderect(paddle):
        items_to_remove.append(item)

for item in items_to_remove:
    items.remove(item)

# Paddle properties
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 10, 120, 10)

# Bricks
bricks = []
for i in range(5):
    for j in range(8):
        brick = pygame.Rect(j * (BRICK_WIDTH + 5) + 50, i * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Game over 조건에 아이템 처리 추가
if len(bricks) == 0:
    game_over = True

# Game over 화면에서 아이템과 관련된 내용 추가
text = font.render("Game Over! Score: " + str(score), True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)

if len(items) > 0:
    item_text = font.render("Items Collected: " + str(len(items)), True, WHITE)
    item_text_rect = item_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(item_text, item_text_rect)


# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # Update the ball's position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x

    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_speed_y = -ball_speed_y

    # Game over condition
    if ball.top >= HEIGHT:
        game_over = True

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw everything
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    # Update the display
    pygame.display.flip()

    # Control the game speed
    pygame.time.delay(30)

# Game over screen
font = pygame.font.Font(None, 36)
text = font.render("Game Over!", True, WHITE)
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
screen.blit(text, text_rect)
pygame.display.flip()

# Wait for a while before quitting
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
sys.exit()
