import pygame
import numpy as np
font = pygame.font.Font(None, 36)

# Create a 500x500 pixel array
width, height = 500, 500
pixels = np.zeros([width, height, 3], dtype=np.uint8)

# Modify pixels - let's fill the array with white as an example
pixels[:,:] = [255, 255, 255]  # Set all pixels to white

# Initialize Pygame
pygame.init()

# Create a Pygame surface from the NumPy array
surface = pygame.surfarray.make_surface(pixels)

# Create a window
window = pygame.display.set_mode((width, height))


columns = 3;
rows = 3;
# Define squares for tic-tac-toe board
squares = [[pygame.Rect(x*width//rows, y*height//columns, width//rows, height//columns) for x in range(columns)] for y in range(rows)]


coordinate = [[None]*columns for _ in range(rows)]


input = "x"




# Main loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Right mouse button
            
            mouse_pos = pygame.mouse.get_pos()
            for i in range(rows):
                for j in range(columns):
                    if squares[i][j].collidepoint(mouse_pos):
                        print(f"Right clicked on square ({i}, {j})")
                        coordinate[i][j] = input
                        input = "o" if input == "x" else "x"
            print(coordinate)


    # Draw the surface to the window
    window.blit(surface, (0, 0))

    # Draw squares and implement hover effect
    for i in range(rows):
        for j in range(columns):
            if squares[i][j].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(window, (0, 0, 0), squares[i][j].inflate(5,5))  # Inflate square by 50 pixels on hover
            else:
                pygame.draw.rect(window, (100,100,100), squares[i][j], 1)  # Draw border with width of 1 pixel

            if coordinate[i][j] is not None:
                text = font.render(coordinate[i][j].upper(), True, (0, 0, 0))
                window.blit(text, squares[i][j].center)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()