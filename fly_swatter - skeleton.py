import pygame
import tkinter as tk
import random
import os

def main():
    # Initialize pygame
    pygame.init()

    # Screen dimensions
    width, height = 800, 600

    # Colors
    white = (255, 255, 255)

    # Load images
    fly_image = pygame.image.load('fly.png')
    dead_fly_image = pygame.image.load('dead_fly.png')
    swatter_image = pygame.image.load('swatter.png')

    # Screen setup
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Fly Swatter')

    # Fly class
    class Fly:
        def __init__(self):
            self.x = random.randint(0, width - fly_image.get_width())
            self.y = random.randint(0, height - fly_image.get_height())
            self.alive = True
            self.dx = random.choice([-1, 1])
            self.dy = random.choice([-1, 1])

        def draw(self):
            if self.alive:
                screen.blit(fly_image, (self.x, self.y))
            else:
                screen.blit(dead_fly_image, (self.x, self.y))

        def move(self):
            if self.alive:
                self.x += self.dx
                self.y += self.dy

                if self.x < 0 or self.x + fly_image.get_width() > width:
                    self.dx = -self.dx
                if self.y < 0 or self.y + fly_image.get_height() > height:
                    self.dy = -self.dy

        def check_collision(self, swatter_x, swatter_y):
            swatter_rect = pygame.Rect(swatter_x, swatter_y, swatter_image.get_width(), swatter_image.get_height())
            fly_rect = pygame.Rect(self.x, self.y, fly_image.get_width(), fly_image.get_height())
            return swatter_rect.colliderect(fly_rect)

    # Generate flies
    flies = [Fly() for _ in range(20)]

    # Game loop
    running = True
    score = 0
    font = pygame.font.Font(None, 36)

    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw flies
        for fly in flies:
            fly.draw()
            fly.move()

        # Draw fly swatter
        swatter_x, swatter_y = pygame.mouse.get_pos()
        screen.blit(swatter_image, (swatter_x, swatter_y))

        # Check for swatting action
        if pygame.mouse.get_pressed()[0]:
            for fly in flies:
                if fly.alive and fly.check_collision(swatter_x, swatter_y):
                    fly.alive = False
                    score += 1

        # Draw score
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        pygame.time.delay(10)

    pygame.quit()

def launch_game():
    root.withdraw()
    main()
    root.deiconify()

# Create tkinter window
root = tk.Tk()
root.title("Fly Swatter Game Launcher")
root.geometry("300x200")

# Add a label to the GUI
label = tk.Label(root, text="Welcome to Fly Swatter Game!", font=("Arial", 16))
label.pack(pady=20)

# Add a button to launch the game
button = tk.Button(root, text="Start Game", font=("Arial", 14), command=launch_game)
button.pack(pady=20)

# Add a button to close the GUI
button_quit = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit)
button_quit.pack(pady=20)

# Start the tkinter event loop
root.mainloop()