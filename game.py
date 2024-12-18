import pygame as pg
import sys, time, os
from bird import Bird
from pipe import Pipe

pg.init()
pg.mixer.init()  # Initialize mixer for sound playback

# Load sounds
class SoundManager:
    def __init__(self):
        self.flap_sound = pg.mixer.Sound("assets/sfx/flap.wav")
        self.score_sound = pg.mixer.Sound("assets/sfx/score.wav")
        self.dead_sound = pg.mixer.Sound("assets/sfx/dead.wav")
        self.achievement_sound = pg.mixer.Sound("assets/sfx/success.mp3")
        self.bonus_sound = pg.mixer.Sound("assets/sfx/bonus.mp3")

    def play_flap(self):
        self.flap_sound.play()

    def play_score(self):
        self.score_sound.play()

    def play_dead(self):
        self.dead_sound.play()

    def play_achievement(self):
        self.achievement_sound.play()

    def play_bonus(self):
        self.bonus_sound.play()

class ScoreManager:
    def __init__(self):
        self.score = 0
        self.high_score = 0

    def save_score_to_file(self):
        with open("score_history.txt", "a") as file:
            file.write(f"{self.score}\n")

    def read_score_history(self):
        try:
            with open("score_history.txt", "r") as file:
                scores = file.readlines()
            return [int(score.strip()) for score in scores]
        except FileNotFoundError:
            return []

    def delete_score_history(self):
        if os.path.exists("score_history.txt"):
            os.remove("score_history.txt")

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.save_score_to_file()

class Game:
    def __init__(self):
        self.width = 600
        self.height = 768
        self.scale_factor = 1.5
        self.win = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Flappy Bird")
        self.clock = pg.time.Clock()
        self.move_speed = 250
        self.bird = Bird(self.scale_factor)
        self.sound_manager = SoundManager()
        self.score_manager = ScoreManager()

        self.is_enter_pressed = False
        self.pipes = []
        self.pipe_generate_counter = 71
        self.game_over = False
        self.font = pg.font.Font("assets/font.ttf", 36)
        self.difficulty = "easy"

        self.setUpBgAndGround()
        self.mainMenu()

    def gameLoop(self):
        last_time = time.time()
        while True:
            new_time = time.time()
            dt = new_time - last_time
            last_time = new_time

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.score_manager.delete_score_history()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    self.handle_keydown(event, dt)

            if not self.game_over:
                self.updateEverything(dt)
                self.checkCollisions()
            self.drawEverything()
            pg.display.update()
            self.clock.tick(60)

    def handle_keydown(self, event, dt):
        if (event.key == pg.K_RETURN or event.key == pg.K_SPACE) and not self.game_over:
            self.is_enter_pressed = True
            self.bird.update_on = True
        if event.key == pg.K_SPACE and self.is_enter_pressed:
            self.sound_manager.play_flap()
            self.bird.flap(dt)
        if event.key == pg.K_r and self.game_over:
            self.resetGame()
        if event.key == pg.K_m and self.game_over:
            self.mainMenu()

    def checkCollisions(self):
        if len(self.pipes):
            if self.bird.rect.bottom > 568:
                self.end_game()
            if (self.bird.rect.colliderect(self.pipes[0].rect_down) or
                self.bird.rect.colliderect(self.pipes[0].rect_up)):
                self.end_game()

    def end_game(self):
        self.bird.update_on = False
        self.is_enter_pressed = False
        self.game_over = True
        self.sound_manager.play_dead()
        self.score_manager.update_high_score()

    def updateEverything(self, dt):
        if self.is_enter_pressed:
            self.move_ground(dt)
            self.generate_pipes()
            self.move_pipes(dt)
            self.bird.update(dt)

    def move_ground(self, dt):
        self.ground1_rect.x -= int(self.move_speed * dt)
        self.ground2_rect.x -= int(self.move_speed * dt)

        if self.ground1_rect.right < 0:
            self.ground1_rect.x = self.ground2_rect.right
        if self.ground2_rect.right < 0:
            self.ground2_rect.x = self.ground1_rect.right

    def generate_pipes(self):
        if self.pipe_generate_counter > 70:
            self.pipes.append(Pipe(self.scale_factor, self.move_speed, difficulty=self.difficulty))
            self.pipe_generate_counter = 0
        self.pipe_generate_counter += 1

    def move_pipes(self, dt):
        for pipe in self.pipes:
            pipe.update(dt)
            if pipe.rect_up.right < self.bird.rect.left and not pipe.passed:
                pipe.passed = True
                self.score_manager.score += 1
                self.sound_manager.play_score()
                if self.score_manager.score % 10 == 0:
                    self.sound_manager.play_bonus()
                if self.score_manager.score in [5, 25]:
                    self.sound_manager.play_achievement()
                    print("Achievement unlocked: Pipe Whisperer!")

        if len(self.pipes) != 0 and self.pipes[0].rect_up.right < 0:
            self.pipes.pop(0)

    def drawEverything(self):
        # Draw background, pipes, ground, bird, and score
        self.win.blit(self.bg_img, (0, -300))
        for pipe in self.pipes:
            pipe.drawPipe(self.win)
        self.win.blit(self.ground1_img, self.ground1_rect)
        self.win.blit(self.ground2_img, self.ground2_rect)
        self.win.blit(self.bird.image, self.bird.rect)

        # Draw current score
        score_text = self.font.render("Coins: " + str(self.score_manager.score), True, (255, 255, 255))
        self.win.blit(score_text, (10, 10))

        # Draw high score
        high_score_text = self.font.render("High Score: " + str(self.score_manager.high_score), True, (255, 215, 0))
        self.win.blit(high_score_text, (10, 50))

        # Draw copyright at the bottom
        copyright_text = self.font.render("OOP ASELOLE", True, (20, 110, 200))
        copyright_rect = copyright_text.get_rect(center=(self.width // 2, self.height - 20))
        self.win.blit(copyright_text, copyright_rect)

        # If score reaches x, display "Pipe Whisperer" notification
        if self.score_manager.score == 5:
            achievement_text = self.font.render("Pipe Whisperer!", True, (255, 215, 0))
            achievement_rect = achievement_text.get_rect(center=(self.width // 2, 100))
            self.win.blit(achievement_text, achievement_rect)
            
        if self.score_manager.score == 25:
            achievement_text = self.font.render("UuOWowwWWwWwwy!", True, (255, 215, 0))
            achievement_rect = achievement_text.get_rect(center=(self.width // 2, 100))
            self.win.blit(achievement_text, achievement_rect)
        
        # If game over, display restart and return to menu options
        if self.game_over:
            restart_text = self.font.render("Restart", True, (255, 0, 0))
            menu_text = self.font.render("Main Menu", True, (0, 255, 0))
        
            # Position buttons
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 - 50))
            menu_rect = menu_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
        
            self.win.blit(restart_text, restart_rect)
            self.win.blit(menu_text, menu_rect)

            # Check for mouse clicks to handle restart or menu navigation
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.score_manager.delete_score_history()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if restart_rect.collidepoint(event.pos):
                        self.resetGame()
                    elif menu_rect.collidepoint(event.pos):
                        self.mainMenu()
    
    def mainMenu(self):
        while True:
            self.win.fill((0, 0, 0))

            # Draw menu buttons
            title_text = self.font.render("Flappy Bird", True, (255, 255, 255))
            start_text = self.font.render("Start", True, (255, 255, 255))
            history_text = self.font.render("History", True, (255, 255, 255))
            difficulty_text = self.font.render("Difficulty", True, (255, 255, 255))

            title_rect = title_text.get_rect(center=(self.width // 2, 100))
            start_rect = start_text.get_rect(center=(self.width // 2, 250))
            history_rect = history_text.get_rect(center=(self.width // 2, 350))
            difficulty_rect = difficulty_text.get_rect(center=(self.width // 2, 450))

            self.win.blit(title_text, title_rect)
            self.win.blit(start_text, start_rect)
            self.win.blit(history_text, history_rect)
            self.win.blit(difficulty_text, difficulty_rect)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.score_manager.delete_score_history()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if start_rect.collidepoint(event.pos):
                        self.gameLoop()
                    elif history_rect.collidepoint(event.pos):
                        self.showHistory()
                    elif difficulty_rect.collidepoint(event.pos):
                        self.selectDifficulty()

    def showHistory(self):
        while True:
            self.win.fill((0, 0, 0))
            history_text = self.font.render("Score History:", True, (255, 255, 255))
            self.win.blit(history_text, (10, 10))

            scores = self.score_manager.read_score_history()
            for i, score in enumerate(scores[-10:]):  # Display the last 10 scores
                history_line = self.font.render(f"{i + 1}. {score}", True, (255, 255, 255))
                self.win.blit(history_line, (10, 50 + i * 30))

            back_text = self.font.render("Back", True, (255, 0, 0))
            back_rect = back_text.get_rect(center=(self.width // 2, self.height - 50))
            self.win.blit(back_text, back_rect)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.score_manager.delete_score_history()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        return

    def selectDifficulty(self):
        while True:
            self.win.fill((0, 0, 0))

            easy_text = self.font.render("Easy", True, (255, 255, 255))
            medium_text = self.font.render("Medium", True, (255, 255, 255))
            hard_text = self.font.render("Hard", True, (255, 255, 255))

            easy_rect = easy_text.get_rect(center=(self.width // 2, 250))
            medium_rect = medium_text.get_rect(center=(self.width // 2, 350))
            hard_rect = hard_text.get_rect(center=(self.width // 2, 450))

            self.win.blit(easy_text, easy_rect)
            self.win.blit(medium_text, medium_rect)
            self.win.blit(hard_text, hard_rect)

            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    self.score_manager.delete_score_history()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if easy_rect.collidepoint(event.pos):
                        self.difficulty = "easy"
                        return
                    elif medium_rect.collidepoint(event.pos):
                        self.difficulty = "medium"
                        return
                    elif hard_rect.collidepoint(event.pos):
                        self.difficulty = "hard"
                        return

    def setUpBgAndGround(self):
        # Loading images for background and ground
        self.bg_img = pg.transform.scale_by(pg.image.load("assets/bg.png").convert(), self.scale_factor)
        self.ground1_img = pg.transform.scale_by(pg.image.load("assets/ground.png").convert(), self.scale_factor)
        self.ground2_img = pg.transform.scale_by(pg.image.load("assets/ground.png").convert(), self.scale_factor)

        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()

        self.ground1_rect.x = 0
        self.ground2_rect.x = self.ground1_rect.right
        self.ground1_rect.y = 568
        self.ground2_rect.y = 568

    def resetGame(self):
        # Reset game state
        time.sleep(0.1)
        self.bird.reset()  # Call reset method on Bird object to reset its position
        self.pipes = []
        self.pipe_generate_counter = 71
        self.score_manager.score = 0
        self.is_enter_pressed = False
        self.game_over = False

game = Game()
game.mainMenu()
