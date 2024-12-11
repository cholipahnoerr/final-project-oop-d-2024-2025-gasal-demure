import pygame as pg
from random import randint

class PipeImageLoader:
    def __init__(self, scale_factor):
        self.scale_factor = scale_factor

    def load_images(self):
        img_up = pg.transform.scale_by(pg.image.load("assets/pipeup.png").convert_alpha(), self.scale_factor)
        img_down = pg.transform.scale_by(pg.image.load("assets/pipedown.png").convert_alpha(), self.scale_factor)
        return img_up, img_down

class PipePositioner:
    def __init__(self, pipe_distance):
        self.pipe_distance = pipe_distance

    def set_initial_positions(self, rect_up, rect_down):
        rect_up.y = randint(250, 520)
        rect_up.x = 600
        rect_down.y = rect_up.y - self.pipe_distance - rect_up.height
        rect_down.x = 600

class Pipe:
    def __init__(self, scale_factor, move_speed, difficulty="easy"):
        # Load images for the pipes
        image_loader = PipeImageLoader(scale_factor)
        self.img_up, self.img_down = image_loader.load_images()
        
        # Set up pipe rectangles for collision and positioning
        self.rect_up = self.img_up.get_rect()
        self.rect_down = self.img_down.get_rect()
        
        # Set initial positions for the pipes
        positioner = PipePositioner(200)
        positioner.set_initial_positions(self.rect_up, self.rect_down)
        
        # Movement speed of the pipes
        self.move_speed = move_speed
        
        # New attribute to check if the pipe has been passed by the bird
        self.passed = False
        
        # Set difficulty level
        self.difficulty = difficulty
        self.randomize_gap()
    
    def drawPipe(self, win):
        # Draw the pipes on the screen
        win.blit(self.img_up, self.rect_up)
        win.blit(self.img_down, self.rect_down)
    
    def update(self, dt):
        # Update the position of the pipes based on the movement speed and delta time
        self.rect_up.x -= int(self.move_speed * dt)
        self.rect_down.x -= int(self.move_speed * dt)

    def randomize_gap(self):
        # Adjust gap size based on difficulty
        if self.difficulty == "easy":
            self.gap_size = randint(200, 230)  # Larger gap
        elif self.difficulty == "medium":
            self.gap_size = randint(150, 170)  # Medium gap
        elif self.difficulty == "hard":
            self.gap_size = randint(110, 140)  # Smaller gap
        else:
            raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")
        
        # Update pipe positions based on the new gap size
        self.rect_down.y = self.rect_up.y - self.gap_size - self.rect_up.height

    def set_difficulty(self, difficulty):
        # Set the difficulty level and randomize the gap
        self.difficulty = difficulty
        self.randomize_gap()