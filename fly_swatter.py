import pygame
import tkinter as tk
import random
import os
import time

pygame.mixer.init()

buzz_sound = pygame.mixer.Sound("buzz.mp3")
swat_sound = pygame.mixer.Sound("swat.wav")

fly_image1 = pygame.image.load("fly1.png")
fly_image2 = pygame.image.load("fly2.png")
fly_images = [fly_image1, fly_image2]

MAX_LEVEL = 5
INITIAL_FLIES = 5
TIME_LIMIT = 30


class Fly:
    def __init__(self, width, height, dead_fly_image):
        self.x = random.randint(0, width - 50)
        self.y = random.randint(0, height - 50)
        self.vx = random.choice([-2, -1, 1, 2])
        self.vy = random.choice([-2, -1, 1, 2])
        self.width = width
        self.height = height
        self.dead_fly_image = dead_fly_image
        self.alive = True
        self.animation_index = 0

    def draw(self, screen):
        if self.alive:
            # Animate the fly by cycling through images
            image = fly_images[self.animation_index // 10]
            self.animation_index += 1
            if self.animation_index >= len(fly_images) * 10:
                self.animation_index = 0
        else:
            image = self.dead_fly_image
        screen.blit(image, (self.x, self.y))
        
    def move(self):
        if self.alive:
            self.x += self.vx
            self.y += self.vy

            if self.x <= 0 or self.x >= self.width - 50:
                self.vx = -self.vx

            if self.y <= 0 or self.y >= self.height - 50:
                self.vy = -self.vy    

    def check_collision(self, swatter_x, swatter_y):
        return (swatter_x < self.x < swatter_x + 50) and (
            swatter_y < self.y < swatter_y + 50
        )


def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Fly Swatter")

    clock = pygame.time.Clock()

    dead_fly_image = pygame.image.load("dead_fly.png")
    swatter_image = pygame.image.load("swatter.png")
    white = (255, 255, 255)

    level = 1
    flies = [Fly(width, height, dead_fly_image) for _ in range(INITIAL_FLIES)]

    score = 0
    font = pygame.font.Font(None, 36)

    time_limit = TIME_LIMIT
    start_time = time.time()

    running = True
    while running:
        screen.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for fly in flies:
            fly.move()
            fly.draw(screen)

        swatter_x, swatter_y = pygame.mouse.get_pos()
        screen.blit(swatter_image, (swatter_x, swatter_y))

        if pygame.mouse.get_pressed()[0]:
            for fly in flies:
                if fly.alive and fly.check_collision(swatter_x, swatter_y):
                    fly.alive = False
                    score += 1
                    swat_sound.play()

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        time_remaining = time_limit - (time.time() - start_time)
        time_text = font.render(
            f"Time remaining: {int(time_remaining)}", True, (0, 0, 0)
        )
        screen.blit(time_text, (width - 300, 10))

        if int(time_remaining) <= 0:
            running = False

        if score >= level * INITIAL_FLIES and level < MAX_LEVEL:
            level += 1
            flies.extend([Fly(width, height, dead_fly_image) for _ in range(INITIAL_FLIES)])

        buzz_sound.play(-1)

        pygame.display.flip()
        clock.tick(60)

    buzz_sound.stop()
    pygame.quit()


def launch_game():
    root.withdraw()
    main()
    root.deiconify()


root = tk.Tk()
root.title("Fly Swatter Game Launcher")
root.geometry("300x200")

label = tk.Label(root, text="Welcome to Fly Swatter Game!", font=("Arial", 16))
label.pack(pady=20)

button = tk.Button(root, text="Start Game", font=("Arial", 14), command=launch_game)
button.pack(pady=20)

button_quit = tk.Button(root, text="Exit", font=("Arial", 14), command=root.quit)
button_quit.pack(pady=20)

root.mainloop()

       
