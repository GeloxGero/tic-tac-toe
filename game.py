import pygame
import numpy as np

def checkWinner():
    # Check rows
    for row in coordinate:
        if row.count(row[0]) == len(row) and row[0] is not None:
            return row[0]
    # Check columns
    for col in range(len(coordinate[0])):
        check = []
        for row in coordinate:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] is not None:
            return check[0]
    # Check diagonals
    if coordinate[0][0] == coordinate[1][1] == coordinate[2][2] and coordinate[0][0] is not None:
        return coordinate[0][0]
    if coordinate[0][2] == coordinate[1][1] == coordinate[2][0] and coordinate[0][2] is not None:
        return coordinate[0][2]
    return


# Create a 500x500 pixel array
width, height = 500, 500
pixels = np.zeros([width, height, 3], dtype=np.uint8)

# Modify pixels - let's fill the array with white as an example
pixels[:,:] = [255, 255, 255]  # Set all pixels to white

# Initialize Pygame
pygame.init()
font = pygame.font.Font(None, 150)

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


#asfasfasf
#testtesttest
#testtesttest
#testtesttest
#testtesttest


# Main loop
running = True
while running:
    if(checkWinner()):
        window.fill((255, 255, 255))  # Clear the window
        text = font.render("Winner!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(width//2, height//2))
        window.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(1900)  # Wait for 3 seconds
        coordinate = [[None]*columns for _ in range(rows)]
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Right mouse button
            
            mouse_pos = pygame.mouse.get_pos()
            for i in range(rows):
                for j in range(columns):
                    if squares[i][j].collidepoint(mouse_pos) and coordinate[i][j] == None:
                        print(f"Right clicked on square ({i}, {j})")
                        coordinate[i][j] = input
                        input = "o" if input == "x" else "x"
            print(coordinate)


    # Draw the surface to the window
    window.blit(surface, (0, 0))

    # Draw squares and implement hover effect
    for i in range(rows):
        for j in range(columns):
            if squares[i][j].collidepoint(pygame.mouse.get_pos()) and coordinate[i][j] == None:
                pygame.draw.rect(window, (200, 200, 200, 120), squares[i][j].inflate(5,5))  # Inflate square by 50 pixels on hover
            else:
                pygame.draw.rect(window, (100,100,100), squares[i][j], 1)  # Draw border with width of 1 pixel

            if coordinate[i][j] is not None:
                text = font.render(coordinate[i][j].upper(), True, (0, 0, 0))
                text_rect = text.get_rect(center=squares[i][j].center)
                window.blit(text, text_rect)




    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()