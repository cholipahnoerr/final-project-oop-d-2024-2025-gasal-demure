[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4ZAJL3PP)
# Laporan Akhir Final Project OOP D

## 1. Informasi Umum
* **Nama Game**: Flappy Bird
* **Anggota Kelompok**:
    1. Nadya Zafira - 5025231310
    2. Izzudin Ali Akbari - 5025231313
    3. Alya Rahmatillah Machmud - 5025231315
    4. Cholipah Noer Amanah - 5025231317
* **Tech Stack**: Python, Visual Studio Code, Pygame library

## 2. Deskripsi Game

### 2.1 Konsep Game
* **Genre**: Arcade, Endless Runner
* **Gameplay/Rule**: Pemain mengendalikan burung yang terbang dengan menekan tombol spasi untuk menghindari pipa yang bergerak.
* **Objective**: Raih skor tertinggi dengan melewati pipa sebanyak-banyaknya tanpa menabraknya atau terjatuh.
* **Single/Multi Player**: Single Player

### 2.2 Fitur Utama
1. Sistem Penyimpanan dan Pemulihan Skor (Save/Load skor)
2. Sistem Pencapaian (Achievement System)
3. Pemilihan tingkat kesulitan


## 3. Implementasi Fitur Wajib

### 3.1 Save/Load System
* **Implementasi**: Skor disimpan dalam file "score_history.txt" dan dapat dimuat di menu history saat dibutuhkan.
* **Konsep OOP**: Menggunakan prinsip enkapsulasi dengan kelas `ScoreManager` dan methodnya untuk menangani semua aspek terkait skor, seperti membaca dan menulis skor.
* **Penerapan SOLID**: Single Responsibility Principle (SRP) - Setiap fungsi memiliki tanggung jawab tunggal untuk mengelola skor. Dalam konteks ini, kelas `ScoreManager` mengatur hanya tentang keterkaitan skor, dan `SoundManager` yang berfokus dalam mengelola sound.
* **Design Pattern yang Digunakan**: Tidak menggunakan desain pola khusus untuk fitur ini.
* **Code Snippet**:

SRP - SoundManager
```
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

```

SRP - ScoreManager
```
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

```

### 3.2 Achievement System
* **Jenis Achievement**: Pencapaian berdasarkan jumlah skor tertentu.
* **Implementasi Achievement**: Pemain mendapatkan pencapaian setelah mencapai skor tertentu.
    1. Penerapan Pencapaian 1: "Pipe Whisperer" pada skor 5.
    2. Penerapan Pencapaian 2: "uwuwuwuwuw" pada skor 25.
* **Konsep OOP**: `Inheritance & Polymorphism`. Pencapaian yang berbeda-beda diperoleh dari class `Achievement`, yang memungkinkan masing-masing untuk menentukan kondisi yang unik untuk membuka kunci.
* **Penerapan SOLID**: Open/Closed Principle (OCP). Sistem dapat diperluas dengan pencapaian baru tanpa mengubah logika pencapaian yang ada.
* **Design Pattern yang Digunakan**:
* **Code Snippet**:
```
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

```

## 4. Implementasi Fitur Lain

### 4.1 Fitur Tampilan Menu dan Tingkat Kesulitan
* **Implementasi**: Menu utama dengan pilihan "Start", "History", dan "Difficulty".
* **Konsep OOP**: Menggunakan kelas Game untuk mengelola tampilan dan interaksi menu.
* **Penerapan SOLID (Optional)**:
* **Design Pattern yang Digunakan (Optional)**:
* **Code Snippet**:

Menu
```
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
```
Tingkat Kesulitan
```
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
```

### 4.2 Fitur Skor dan Riwayat
* **Implementasi**: Menampilkan riwayat skor terakhir dan memungkinkan kembali ke menu utama.
* **Konsep OOP**: Kelas Game menangani tampilan riwayat skor.
* **Penerapan SOLID (Optional)**: Mengikuti prinsip SRP dan OCP untuk memperluas riwayat skor.
* **Design Pattern yang Digunakan (Optional)**: Tidak ada.
* **Code Snippet**: 
```
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
```

## 5. Screenshot dan Demo
* **Screenshot 1**: Main Menu

    ![WhatsApp Image 2024-12-11 at 13 55 56_343e0d48](https://github.com/user-attachments/assets/e8572613-d131-4fb3-9c12-4bb600b10dd4)

* **Screenshot 2**: Difficulty

    ![WhatsApp Image 2024-12-11 at 13 56 31_d5e78244](https://github.com/user-attachments/assets/40ac13cf-2f2a-4b42-af71-a43c48f124d5)

* **Screenshot 3**: History

    ![WhatsApp Image 2024-12-11 at 13 59 11_9bb0fbea](https://github.com/user-attachments/assets/03c6aa85-48cb-49d6-bbae-6d6838f2d494)

* **Screenshot 4**: Start
  
     ![WhatsApp Image 2024-12-11 at 11 53 52_6c910d6b](https://github.com/user-attachments/assets/d895d4df-ae3e-43b7-ab7d-01ce82905223)

* **Screenshot 5**: Game Over

    ![WhatsApp Image 2024-12-11 at 14 00 07_7aaff691](https://github.com/user-attachments/assets/27d6b613-2eba-4bfe-9f34-3094b0573bb0)

* **Screenshot 6**: Achievment
  
    ![WhatsApp Image 2024-12-11 at 15 05 09_0e8e1e78](https://github.com/user-attachments/assets/ec776239-6eef-4988-b95d-5caeec31bc19)

* **Screenshot 7**: Difficulty

    ![WhatsApp Image 2024-12-11 at 15 08 20_0cb7e57f](https://github.com/user-attachments/assets/190d6708-05ad-4e3e-af87-aa10a806ba05)



* **Link Demo Video**: [URL]

## 6. Panduan Instalasi dan Menjalankan Game
1. Download semua file dalam folder
2. Jalankan di terminal dengan perintah `python3 -m game.py`
3. Pilih level yang diinginkan
4. Start
5. Restart/Kembali ke main menu untuk melihat history

## 7. Kendala dan Solusi
1. **Kendala 1**: 
    * Solusi:
2. **Kendala 2**:
    * Solusi:

## 8. Kesimpulan dan Pembelajaran
* **Kesimpulan**: Proyek pengembangan game Flappy Bird menggunakan OOP berhasil menerapkan fitur Save/Load System dan Achievement System yang meningkatkan pengalaman bermain. Penerapan prinsip SOLID membuat kode lebih terstruktur dan mudah dipelihara. Fitur penyesuaian tingkat kesulitan dan sistem pencapaian memberikan tantangan dan motivasi lebih bagi pemain.
* **Pembelajaran**:
  1. Penerapan OOP memudahkan pengelolaan objek dan kode.
  2. Prinsip SOLID membuat kode lebih modular dan mudah dikembangkan.
  3. Save/Load System dan Achievement System meningkatkan pengalaman pengguna.
  4. Penyesuaian tingkat kesulitan memberikan tantangan sesuai kemampuan pemain.
Proyek ini memperkaya pemahaman tentang pengembangan game dan manajemen kode yang efisien.
