[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/4ZAJL3PP)
# Laporan Akhir Final Project OOP D

## 1. Informasi Umum
* **Nama Game**: [Nama Game]
* **Anggota Kelompok**:
    1. [Nadya Zafira - 5025231310]
    2. [Izzudin Ali Akbari - 5025231313]
    3. [Alya Rahmatillah Machmud - 5025231315]
    4. [Cholipah Noer Amanah - 5025231317]
* **Tech Stack**: [Python, StudioCode, Pygame library]

## 2. Deskripsi Game

### 2.1 Konsep Game
* **Genre**: Arcade, Endless Runner
* **Gameplay/Rule**: Pemain mengendalikan burung yang terbang dengan menekan tombol spasi untuk menghindari pipa yang bergerak.
* **Objective**: Raih skor tertinggi dengan melewati pipa sebanyak-banyaknya tanpa menabraknya atau terjatuh.
* **Single/Multi Player**: Single Player

### 2.2 Fitur Utama
1. Sistem Save/Load skor
2. Sistem Pencapaian (Achievement System)
3. Pemilihan tingkat kesulitan


## 3. Implementasi Fitur Wajib

### 3.1 Save/Load System
* **Implementasi**: Skor disimpan dalam file "score_history.txt" dan dapat dimuat saat dibutuhkan.
* **Konsep OOP**: Menggunakan kelas dan metode untuk membaca, menulis, dan menghapus data skor.
* **Penerapan SOLID**: Single Responsibility Principle (SRP) - Setiap fungsi memiliki tanggung jawab tunggal untuk mengelola skor.
* **Design Pattern yang Digunakan**: Tidak menggunakan desain pola khusus untuk fitur ini.
* **Code Snippet**:
```
def save_score_to_file(score):
    with open("score_history.txt", "a") as file:
        file.write(f"{score}\n")
```

### 3.2 Achievement System
* **Jenis Achievement**: Pencapaian berdasarkan jumlah skor tertentu.
* **Implementasi Achievement**: Pemain mendapatkan pencapaian setelah mencapai skor tertentu (contoh: "Pipe Whisperer" pada skor 5).


    1. Penerapan Pencapaian 1: "Pipa Pertama Berhasil" - Diaktifkan saat pemain berhasil melewati pipa pertama mereka.
    2. Penerapan Pencapaian 2: "Nilai Tertinggi Tercapai" - Diaktifkan saat pemain mengalahkan skor tertinggi.
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
2. Jalankan di terminal dengan perintah `python game.py`
3. Pilih level yang diinginkan
4. Start
5. Restart/Kembali ke main menu untuk melihat history

## 7. Kendala dan Solusi
1. **Kendala 1**: 
    * Solusi:
2. **Kendala 2**:
    * Solusi:

## 8. Kesimpulan dan Pembelajaran
* **Kesimpulan**:
* **Pembelajaran**:
