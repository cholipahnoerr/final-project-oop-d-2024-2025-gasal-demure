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
```
def save_score_to_file(score):
    with open("score_history.txt", "a") as file:
        file.write(f"{score}\n")
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
if self.score == 5:
    achievement_sound.play()  # Play achievement sound
    print("Achievement unlocked: Pipe Whisperer!")

```

## 4. Implementasi Fitur Lain

### 4.1 Fitur Tampilan Menu
* **Implementasi**: Menu utama dengan pilihan "Start", "History", dan "Difficulty".
* **Konsep OOP**: Menggunakan kelas Game untuk mengelola tampilan dan interaksi menu.
* **Penerapan SOLID (Optional)**:
* **Design Pattern yang Digunakan (Optional)**:
* **Code Snippet**:
```
def mainMenu(self):
    while True:
        # Draw menu
        if event.type == pg.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                self.gameLoop()
```

### 4.2 Fitur Skor dan Riwayat
* **Implementasi**: Menampilkan riwayat skor terakhir dan memungkinkan kembali ke menu utama.
* **Konsep OOP**: Kelas Game menangani tampilan riwayat skor.
* **Penerapan SOLID (Optional)**: Mengikuti prinsip SRP dan OCP untuk memperluas riwayat skor.
* **Design Pattern yang Digunakan (Optional)**: Tidak ada.
* **Code Snippet**: 
```
def showHistory(self):
    scores = read_score_history()
    for i, score in enumerate(scores[-10:]):
        history_line = self.font.render(f"{i + 1}. {score}", True, (255, 255, 255))
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
