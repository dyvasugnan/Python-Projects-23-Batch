# Initialize pygame
import pygame
import sys
import numpy as np
import math
import random

pygame.init()
pygame.mixer.init()  # Initialize the mixer module

celebration_sound = pygame.mixer.Sound(r"C:\Users\Hp\Downloads\celebration_sound.mp3")
# Set the dimensions of the window
window_size = (1000, 600)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption('Front Page Image')

# Load the images
image_path = r"C:\Users\Hp\Downloads\front page new.jpeg"
play_button_path = "C:/Users/Hp/Downloads/play button.jpeg"
instructions_path = r"C:\Users\Hp\Downloads\instructions new.jpeg"
next_button_path = "C:/Users/Hp/Downloads/next button.jpeg"  # Path to the next button image
choose_player_path = r"C:\Users\Hp\Downloads\choose player new.jpeg"  # Path to the choose player page image
hare_button_path = r"C:\Users\Hp\Downloads\hare_button.jpeg" # Path to the hare button image
hound_button_path = r"C:\Users\Hp\Downloads\hound_button.jpeg"  # Path to the hound button image

try:
    front_page_image = pygame.image.load(image_path)
    play_button_image = pygame.image.load(play_button_path)
    instructions_image = pygame.image.load(instructions_path)
    next_button_image = pygame.image.load(next_button_path)
    choose_player_image = pygame.image.load(choose_player_path)
    hare_button_image = pygame.image.load(hare_button_path)
    hound_button_image = pygame.image.load(hound_button_path)
except pygame.error as e:
    print(f"Unable to load image: {e}")
    pygame.quit()
    sys.exit()

# Resize the play button
play_button_size = (100, 50)  # Adjust the size as needed
play_button_image = pygame.transform.scale(play_button_image, play_button_size)

# Resize the next button
next_button_size = (100, 50)  # Adjust the size as needed
next_button_image = pygame.transform.scale(next_button_image, next_button_size)

# Resize the hare and hound buttons
button_size = (150, 75)  # Adjust the size as needed
hare_button_image = pygame.transform.scale(hare_button_image, button_size)
hound_button_image = pygame.transform.scale(hound_button_image, button_size)

# Get the image dimensions
front_page_image = pygame.transform.scale(front_page_image, (1000, 600))
front_page_rect = front_page_image.get_rect()
front_page_rect.center = (window_size[0] // 2, window_size[1] // 2)

play_button_image = pygame.transform.scale(play_button_image, (100, 50))
play_button_rect = play_button_image.get_rect()
play_button_rect.center = (window_size[0] // 2, window_size[1] - 100)

instructions_image = pygame.transform.scale(instructions_image, (1000, 600))
instructions_rect = instructions_image.get_rect()
instructions_rect.center = (window_size[0] // 2, window_size[1] // 2)

next_button_image = pygame.transform.scale(next_button_image, (100, 50))
next_button_rect = next_button_image.get_rect()
next_button_rect.bottomright = (window_size[0] - 20, window_size[1] - 20)  # Position the next button at the bottom-right

# Create a rectangle for the choose player image
choose_player_image = pygame.transform.scale(choose_player_image, (1000, 600))
choose_player_rect = choose_player_image.get_rect()
choose_player_rect.center = (window_size[0] // 2, window_size[1] // 2)  # Center the choose player image

# Create rectangles for the hare and hound buttons
hare_button_image = pygame.transform.scale(hare_button_image, (150, 75))
hound_button_image = pygame.transform.scale(hound_button_image, (150, 75))

hare_button_rect = hare_button_image.get_rect()
hound_button_rect = hound_button_image.get_rect()
hare_button_rect.center = (window_size[0] // 2 + 200, window_size[1] // 2 - 100)  # Move up by decreasing y-coordinate
hound_button_rect.center = (window_size[0] // 2 - 200, window_size[1] // 2 - 100)  # Move up by decreasing y-coordinate

# Load the sound
sound_path = "C:/Users/Hp/Downloads/click sound.mpeg"
try:
    click_sound = pygame.mixer.Sound(sound_path)
except pygame.error as e:
    print(f"Unable to load sound: {e}")
    pygame.quit()
    sys.exit()

# Hardcoded paths to images and sound for the game
hare_image_path = "C:/Users/Hp/Downloads/hare__new_new-removebg-preview.png"
hound_image_path = "C:/Users/Hp/Downloads/hound_circle.png"
selection_sound_path = r"C:\Users\Hp\Downloads\click sound.mpeg"
placement_sound_path = r"C:\Users\Hp\Downloads\click sound.mpeg"

pygame.mixer.init()

celebratory_sound = pygame.mixer.Sound(r"C:\Users\Hp\Downloads\tadaa-47995.mp3")
# Load images for the game
hare_image = pygame.image.load(hare_image_path)
hound_image = pygame.image.load(hound_image_path)

# Increase the image size by 20%
NODE_DIAMETER = 60  # New node diameter for increased image size
new_diameter = int(NODE_DIAMETER * 1.2)
hare_image = pygame.transform.scale(hare_image, (new_diameter, new_diameter))
hound_image = pygame.transform.scale(hound_image, (new_diameter, new_diameter))

# Load sounds for the game
selection_sound = pygame.mixer.Sound(selection_sound_path)
placement_sound = pygame.mixer.Sound(placement_sound_path)

# Define constants for the game
WIDTH, HEIGHT = 1000, 600  # Increased the width to 1000
NODE_RADIUS = 30
BG_COLOR = (210, 180, 140)  # Light brown color
FONT_COLOR = (255, 255, 255)  # White color for text
TURN_TEXT_COLOR = (102, 51, 0)  # Dark brown color for turn text
CONFETTI_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

# Create screen for the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hares and Hounds')

# Define the board using numpy for the game
board = np.zeros((3, 5))

# Set hound positions with value 1
board[0][1] = 1
board[1][0] = 1
board[2][1] = 1

# Set hare position with value 2
board[1][4] = 2

# Position of the nodes for the game
positions = [
    (200, 50), (400, 50), (600, 50),  # Top row (excluding corners)
    (50, 300), (200, 300), (400, 300), (600, 300), (750, 300),  # Middle row (excluding left and right corners)
    (200, 550), (400, 550), (600, 550)  # Bottom row (excluding corners)
]

# Calculate the offset to center the board
x_offset = (WIDTH - 800) // 2  # Assuming the board width is 800
y_offset = (HEIGHT - 600) // 2  # Assuming the board height is 600

# Apply the offset to the positions
centered_positions = [(x + x_offset, y + y_offset) for x, y in positions]

# Define edges (connections between nodes) for the game
edges = [
    (0, 1), (1, 2),  # Top row
    (0, 4), (1, 5), (2, 6),  # Top to middle row
    (3, 4), (4, 5), (5, 6), (6, 7),  # Middle row
    (4, 8), (5, 9), (6, 10),  # Middle to bottom row
    (8, 9), (9, 10),  # Bottom row
    (5, 0), (5, 2), (5, 8), (5, 10),  # New connections from 5
    (3, 0), (3, 8),  # New connections from 3
    (7, 2), (7, 10)  # New connections from 7
]

# Initial positions of the counters for the game
hare_position = 7  # Corresponds to board[1][4]
hound_positions = [3, 0, 8]  # Hound positions: left, middle, and bottom of the left side

# Game state
current_player = "Hare"
selected_hound = None
winner = None
game_over = False
confetti_start_time = None  # Track the start time of the confetti display

# Confetti class
class Confetti:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = random.choice(CONFETTI_COLORS)
        self.size = random.randint(5, 10)
        self.speed_x = random.uniform(-2, 2)
        self.speed_y = random.uniform(2, 5)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

confetti_particles = []


# Game loop
clock = pygame.time.Clock()


# Function to draw the board
def draw_board():
    screen.fill(BG_COLOR)

    # Draw the edges
    for edge in edges:
        start_pos = centered_positions[edge[0]]
        end_pos = centered_positions[edge[1]]
        pygame.draw.line(screen, (0, 0, 0), start_pos, end_pos, 5)

    # Draw the nodes
    for pos in centered_positions:
        pygame.draw.circle(screen, (255, 255, 255), pos, NODE_RADIUS)  # Change the color to white

    # Draw the counters
    screen.blit(hare_image, hare_image.get_rect(center=centered_positions[hare_position]))
    for hound_pos in hound_positions:
        screen.blit(hound_image, hound_image.get_rect(center=centered_positions[hound_pos]))

    # Display the current player's turn
    font = pygame.font.Font(None, 36)
    turn_text = "Hare's Turn" if current_player == "Hare" else "Hound's Turn"
    turn_surface = font.render(turn_text, True, TURN_TEXT_COLOR)
    if current_player == "Hare":
        screen.blit(turn_surface, (WIDTH - turn_surface.get_width() - 10, 10))  # Top-right corner
    else:
        screen.blit(turn_surface, (10, 10))  # Top-left corner

    # Draw confetti particles
    for confetti in confetti_particles:
        confetti.update()
        confetti.draw(screen)

# Function to draw the winner
def draw_winner():
    screen.fill(BG_COLOR)
    font = pygame.font.Font(None, 72)
    winner_text = f"{winner} Wins!"
    winner_surface = font.render(winner_text, True, TURN_TEXT_COLOR)
    screen.blit(winner_surface, (WIDTH // 2 - winner_surface.get_width() // 2, HEIGHT // 2 - winner_surface.get_height() // 2))

    # Draw confetti particles
    global confetti_start_time
    if confetti_start_time is None:
        confetti_start_time = pygame.time.get_ticks()
    elif pygame.time.get_ticks() - confetti_start_time < 5000:  # Show confetti for 5 seconds
        for _ in range(10):  # Number of confetti particles to add each frame
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT // 2)
            confetti_particles.append(Confetti(x, y))
    for confetti in confetti_particles:
        confetti.update()
        confetti.draw(screen)

    # Close the window after 3 seconds
    if pygame.time.get_ticks() - confetti_start_time >= 4000:
        pygame.quit()
        sys.exit()
# Function to handle movement
def handle_movement(player_pos, target_pos):
    placement_sound.play()
    return target_pos

# Function to check for valid hound move
def is_valid_hound_move(start, end):
    return end not in hound_positions and end!= hare_position and any(
        {start, end} == {edge[0], edge[1]} for edge in edges)

# Function to check for valid hare move
def is_valid_hare_move(start, end):
    return end not in hound_positions and end!= hare_position and any(
        {start, end} == {edge[0], edge[1]} for edge in edges)

# Function to check for game over conditions
def check_game_over():
    global winner
    # Condition 1: Hare wins by reaching the third position
    if hare_position == 3:
        winner = "Hare"
        celebratory_sound.play()
        return True

    # Condition 2: Hounds win by surrounding the hare
    adjacent_positions = [edge[1] for edge in edges if edge[0] == hare_position] + \
                         [edge[0] for edge in edges if edge[1] == hare_position]
    if all(pos in hound_positions for pos in adjacent_positions):
        winner = "Hounds"
        celebratory_sound.play()
        return True

    return False

# Main game loop
running = True
state = 'front_page'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if state == 'front_page':
                if play_button_rect.collidepoint(event.pos):
                    click_sound.play()  # Play the click sound
                    state = 'instructions'
            elif state == 'instructions':
                if next_button_rect.collidepoint(event.pos):
                    click_sound.play()  # Play the click sound
                    state = 'choose_player'
            elif state == 'choose_player':
                if hare_button_rect.collidepoint(event.pos):
                    click_sound.play()  # Play the click sound
                    # Start the game with the hare player
                    current_player = "Hare"
                    state = 'game'
                elif hound_button_rect.collidepoint(event.pos):
                    click_sound.play()  # Play the click sound
                    # Start the game with the hound player
                    current_player = "Hounds"
                    state = 'game'
            elif state == 'game' and not game_over:
                mouse_pos = pygame.mouse.get_pos()
                for i, pos in enumerate(centered_positions):
                    if pygame.Rect(pos[0] - NODE_RADIUS, pos[1] - NODE_RADIUS, 2 * NODE_RADIUS, 2 * NODE_RADIUS).collidepoint(mouse_pos):
                        if current_player == "Hounds" and selected_hound is not None:  # If a hound is selected
                            if is_valid_hound_move(selected_hound, i):
                                hound_positions[hound_positions.index(selected_hound)] = i
                                placement_sound.play()
                                selected_hound = None
                                current_player = "Hare"  # Switch to hare's turn
                                game_over = check_game_over()
                        elif current_player == "Hounds" and i in hound_positions:  # Select a hound
                            selected_hound = i
                            selection_sound.play()
                        elif current_player == "Hare" and i!= hare_position and is_valid_hare_move(hare_position, i):  # Move the hare
                            hare_position = handle_movement(hare_position, i)
                            current_player = "Hounds"  # Switch to hounds' turn
                            game_over = check_game_over()
                            if game_over:
                                state = 'winner'  # Switch to winner state

    # Update the screen based on the current state
    if state == 'front_page':
        screen.fill((255, 255, 255))
        screen.blit(front_page_image, front_page_rect)
        screen.blit(play_button_image, play_button_rect)
    elif state == 'instructions':
        screen.fill((255, 255, 255))
        screen.blit(instructions_image, instructions_rect)
        screen.blit(next_button_image, next_button_rect)
    elif state == 'choose_player':
        screen.fill((255, 255, 255))
        screen.blit(choose_player_image, choose_player_rect)
        screen.blit(hare_button_image, hare_button_rect)
        screen.blit(hound_button_image, hound_button_rect)
    elif state == 'game':
        draw_board()
        if game_over:
            if confetti_start_time is None:
                confetti_start_time = pygame.time.get_ticks()
            elif pygame.time.get_ticks() - confetti_start_time < 5000:  # Show confetti for 5 seconds
                for _ in range(10):  # Number of confetti particles to add each frame
                    x = random.randint(0, WIDTH)
                    y = random.randint(0, HEIGHT // 2)
                    confetti_particles.append(Confetti(x, y))
    elif state == 'winner':
        draw_winner()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
