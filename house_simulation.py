import pygame
import sys
import pandas as pd
import numpy as np   

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("House Simulation")

# Colors
WHITE = (255, 255, 255)
LIGHT_YELLOW = (255, 255, 204)
DARK_GRAY = (169, 169, 169)
DARKER_GRAY = (100, 100, 100)  # New darker gray color
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255, 182, 193)
BLUE = (173, 216, 230)
GREEN = (144, 238, 144)
RED = (255, 204, 204)

# Room dimensions
room_width = 200
room_height = 200

# import orders 
orders = pd.read_csv("orders.csv")
active = [col for col in orders.columns if orders[col].iloc[0] == 1]
print(active)

# Room states
room_colors = {
    'kitchen_12': YELLOW if 'Kitchen 12 [kW]' in active else DARK_GRAY,
    'kitchen_14': YELLOW if 'Kitchen 14 [kW]' in active else DARK_GRAY,
    'kitchen_38': YELLOW if 'Kitchen 38 [kW]' in active else DARK_GRAY,
    'living_room': YELLOW if 'Living room' in active else DARK_GRAY,
    'garage': YELLOW if 'Garage door [kW]' in active else DARK_GRAY,
    'wine_cellar': YELLOW if 'Wine cellar [kW]' in active else DARK_GRAY,
    'well': YELLOW if 'Well [kW]' in active else DARK_GRAY
}
room_text_colors = {
    'kitchen_12': BLACK,
    'kitchen_14': BLACK,
    'kitchen_38': BLACK,
    'living_room': BLACK,
    'garage': BLACK,
    'wine_cellar': BLACK,
    'well': BLACK
}

# Button dimensions
button_width = 80
button_height = 30

# Define font outside the functions
font = pygame.font.Font(None, 24)  # Smaller font size

def draw_house():
    # Draw rooms
    pygame.draw.rect(screen, room_colors['kitchen_12'], (50, 50, room_width, room_height))  # Kitchen 12
    pygame.draw.rect(screen, room_colors['kitchen_14'], (300, 50, room_width, room_height))  # Kitchen 14
    pygame.draw.rect(screen, room_colors['kitchen_38'], (550, 50, room_width, room_height))  # Kitchen 38
    pygame.draw.rect(screen, room_colors['living_room'], (50, 300, room_width, room_height))  # Living Room
    pygame.draw.rect(screen, room_colors['garage'], (300, 300, room_width, room_height))  # Garage
    pygame.draw.rect(screen, room_colors['wine_cellar'], (550, 300, room_width, room_height))  # Wine Cellar
    pygame.draw.rect(screen, room_colors['well'], (800, 300, room_width, room_height))  # Well

    # Add labels for rooms
    text_kitchen_12 = font.render("Kitchen 12", True, room_text_colors['kitchen_12'])
    text_kitchen_14 = font.render("Kitchen 14", True, room_text_colors['kitchen_14'])
    text_kitchen_38 = font.render("Kitchen 38", True, room_text_colors['kitchen_38'])
    text_living_room = font.render("Living Room", True, room_text_colors['living_room'])
    text_garage = font.render("Garage", True, room_text_colors['garage'])
    text_wine_cellar = font.render("Wine Cellar", True, room_text_colors['wine_cellar'])
    text_well = font.render("Well", True, room_text_colors['well'])
    screen.blit(text_kitchen_12, (70, 70))
    screen.blit(text_kitchen_14, (320, 70))
    screen.blit(text_kitchen_38, (570, 70))
    screen.blit(text_living_room, (70, 320))
    screen.blit(text_garage, (320, 320))
    screen.blit(text_wine_cellar, (570, 320))
    screen.blit(text_well, (820, 320))

    # Draw buttons
    pygame.draw.rect(screen, WHITE, (50 + (room_width - button_width) // 2, 250, button_width, button_height))  # Kitchen 12 button
    pygame.draw.rect(screen, WHITE, (300 + (room_width - button_width) // 2, 250, button_width, button_height))  # Kitchen 14 button
    pygame.draw.rect(screen, WHITE, (550 + (room_width - button_width) // 2, 250, button_width, button_height))  # Kitchen 38 button
    pygame.draw.rect(screen, WHITE, (50 + (room_width - button_width) // 2, 500, button_width, button_height))  # Living Room button
    pygame.draw.rect(screen, WHITE, (300 + (room_width - button_width) // 2, 500, button_width, button_height))  # Garage button
    pygame.draw.rect(screen, WHITE, (550 + (room_width - button_width) // 2, 500, button_width, button_height))  # Wine Cellar button

    # Add button labels
    button_text_kitchen_12 = font.render("On/Off", True, BLACK)
    button_text_kitchen_14 = font.render("On/Off", True, BLACK)
    button_text_kitchen_38 = font.render("On/Off", True, BLACK)
    button_text_living_room = font.render("On/Off", True, BLACK)
    button_text_garage = font.render("On/Off", True, BLACK)
    button_text_wine_cellar = font.render("On/Off", True, BLACK)
    screen.blit(button_text_kitchen_12, (50 + (room_width - button_width) // 2 + 5, 250 + 5))
    screen.blit(button_text_kitchen_14, (300 + (room_width - button_width) // 2 + 5, 250 + 5))
    screen.blit(button_text_kitchen_38, (550 + (room_width - button_width) // 2 + 5, 250 + 5))
    screen.blit(button_text_living_room, (50 + (room_width - button_width) // 2 + 5, 500 + 5))
    screen.blit(button_text_garage, (300 + (room_width - button_width) // 2 + 5, 500 + 5))
    screen.blit(button_text_wine_cellar, (550 + (room_width - button_width) // 2 + 5, 500 + 5))

def draw_objects():
    # Draw appliances
    if('Dishwasher [kW]' in active):
        pygame.draw.rect(screen, YELLOW, (70, 150, 100, 30))
    else:
        pygame.draw.rect(screen, DARK_GRAY, (70, 150, 100, 30))
    if('Furnace 1 [kW]' in active):
        pygame.draw.rect(screen, YELLOW, (70, 190, 100, 30))
    else:
        pygame.draw.rect(screen, DARK_GRAY, (70, 190, 100, 30))
    screen.blit(font.render("Dishwasher", True, BLACK), (70, 150))
    screen.blit(font.render("Furnace 1", True, BLACK), (70, 190))
    
    # Kitchen 14 appliances
    if('Furnace 2 [kW]' in active):
        pygame.draw.rect(screen, YELLOW, (320, 150, 100, 30))
    else:
        pygame.draw.rect(screen, DARK_GRAY, (320, 150, 100, 30))
    screen.blit(font.render("Furnace 2", True, BLACK), (320, 150))
    
    # Kitchen 38 appliances
    if('Microwave [kW]' in active):
        pygame.draw.rect(screen, YELLOW, (570, 150, 100, 30))
    else:
        pygame.draw.rect(screen, DARK_GRAY, (570, 150, 100, 30))
    if('Fridge [kW]' in active):
        pygame.draw.rect(screen, YELLOW, (570, 190, 100, 30))
    else:
        pygame.draw.rect(screen, DARK_GRAY, (570, 190, 100, 30))
    screen.blit(font.render("Microwave", True, BLACK), (570, 150))
    screen.blit(font.render("Fridge", True, BLACK), (570, 190))

    # Living Room appliances
    if('TV [kW]' in active):
        pygame.draw.rect(screen, YELLOW, (70, 350, 100, 30))
    else : 
        pygame.draw.rect(screen, DARK_GRAY, (70, 350, 100, 30))
    screen.blit(font.render("TV", True, BLACK), (70, 350))
def handle_button_click(pos):
    # Check if buttons are clicked
    if 50 + (room_width - button_width) // 2 < pos[0] < 50 + (room_width + button_width) // 2 and 250 < pos[1] < 250 + button_height:
        room_colors['kitchen_12'] = YELLOW if room_colors['kitchen_12'] != YELLOW else DARK_GRAY
    elif 300 + (room_width - button_width) // 2 < pos[0] < 300 + (room_width + button_width) // 2 and 250 < pos[1] < 250 + button_height:
        room_colors['kitchen_14'] = YELLOW if room_colors['kitchen_14'] != YELLOW else DARK_GRAY
    elif 550 + (room_width - button_width) // 2 < pos[0] < 550 + (room_width + button_width) // 2 and 250 < pos[1] < 250 + button_height:
        room_colors['kitchen_38'] = YELLOW if room_colors['kitchen_38'] != YELLOW else DARK_GRAY
    elif 50 + (room_width - button_width) // 2 < pos[0] < 50 + (room_width + button_width) // 2 and 500 < pos[1] < 500 + button_height:
        room_colors['living_room'] = YELLOW if room_colors['living_room'] != YELLOW else DARK_GRAY
    elif 300 + (room_width - button_width) // 2 < pos[0] < 300 + (room_width + button_width) // 2 and 500 < pos[1] < 500 + button_height:
        room_colors['garage'] = YELLOW if room_colors['garage'] != YELLOW else DARK_GRAY
    elif 550 + (room_width - button_width) // 2 < pos[0] < 550 + (room_width + button_width) // 2 and 500 < pos[1] < 500 + button_height:
        room_colors['wine_cellar'] = YELLOW if room_colors['wine_cellar'] != YELLOW else DARK_GRAY
    elif 300 + (room_width - button_width) // 2 < pos[0] < 300 + (room_width + button_width) // 2 and 600 < pos[1] < 600 + button_height:
        room_colors['well'] = YELLOW if room_colors['well'] != YELLOW else DARK_GRAY

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_button_click(event.pos)

    screen.fill(WHITE)
    draw_house()
    draw_objects()
    pygame.display.flip()
