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
* **Gameplay/Rule**: Pemain mengendalikan seekor burung yang bergerak maju secara otomatis dan jatuh karena gravitasi. Tujuannya adalah menjaga burung tetap di udara dengan mengetuk layar atau menekan tombol untuk membuatnya "mengepak" ke atas. Pemain harus menghindari tabrakan dengan rintangan (pipa) sambil mempertahankan posisi burung di dalam batas layar.
* **Objective**: Raih skor tertinggi dengan melewati pipa sebanyak-banyaknya tanpa menabraknya atau terjatuh.
* **Single/Multi Player**: Single Player

### 2.2 Fitur Utama
1. Pembuatan Rintangan: Pipa yang dibuat secara acak dengan celah yang harus dilewati pemain.
2. Sistem Penilaian: Skor meningkat dengan setiap pipa yang berhasil dilewati.
3. Simulasi Fisika: Gravitasi dan mekanika mengepak menciptakan gerakan burung yang realistis.
4. Layar Game Over: Menampilkan skor akhir dan menyediakan opsi untuk memulai kembali permainan.

## 3. Implementasi Fitur Wajib

### 3.1 Save/Load System
* **Implementasi**: Permainan ini memiliki sistem yang menyimpan skor tertinggi pemain dalam sebuah berkas. Setiap kali permainan berakhir, sistem akan membandingkan skor saat ini dengan skor tertinggi yang tersimpan dan memperbaruinya jika skor baru lebih tinggi.
* **Konsep OOP**: `Encapsulation & File I/O` digunakan di sini. Class `ScoreManager` menangani penyimpanan dan pemuatan skor tinggi, melindungi logika inti, dan memastikan desain modular.
* **Penerapan SOLID**: Single Responsibility Principle (SRP): `ScoreManager` didedikasikan hanya untuk mengelola fungsi penyimpanan/pemuatan skor tinggi.
* **Design Pattern yang Digunakan**:
* **Code Snippet**:
```
import json

class ScoreManager:
    def __init__(self, file_path='highscore.json'):
        self.file_path = file_path
        self.high_score = self.load_high_score()

    def load_high_score(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file).get('high_score', 0)
        except FileNotFoundError:
            return 0

    def save_high_score(self, score):
        if score > self.high_score:
            self.high_score = score
            with open(self.file_path, 'w') as file:
                json.dump({'high_score': self.high_score}, file)
```

### 3.2 Achievement System
* **Jenis Achievement**:
    Pencapaian berdasarkan tonggak pencapaian (misalnya, "Pipa Pertama Lulus," "10 Pipa Lulus," "Nilai Tertinggi Tercapai").
    1. Penerapan Pencapaian 1: "Pipa Pertama Berhasil" - Diaktifkan saat pemain berhasil melewati pipa pertama mereka.
    2. Penerapan Pencapaian 2: "Nilai Tertinggi Tercapai" - Diaktifkan saat pemain mengalahkan skor tertinggi.
* **Konsep OOP**: `Inheritance & Polymorphism`. Pencapaian yang berbeda-beda diperoleh dari class `Achievement`, yang memungkinkan masing-masing untuk menentukan kondisi yang unik untuk membuka kunci.
* **Penerapan SOLID**: Open/Closed Principle (OCP). Sistem dapat diperluas dengan pencapaian baru tanpa mengubah logika pencapaian yang ada.
* **Design Pattern yang Digunakan**:
* **Code Snippet**:
```
class Achievement:
    def __init__(self, name):
        self.name = name
        self.unlocked = False

    def check_condition(self, *args, **kwargs):
        raise NotImplementedError

class FirstPipeAchievement(Achievement):
    def check_condition(self, pipes_passed):
        if pipes_passed >= 1:
            self.unlocked = True

class HighScoreAchievement(Achievement):
    def __init__(self, high_score):
        super().__init__('High Score Reached')
        self.high_score = high_score

    def check_condition(self, current_score):
        if current_score > self.high_score:
            self.unlocked = True
```

## 4. Implementasi Fitur Lain

### 4.1 Fitur 1
* **Implementasi**:
* **Konsep OOP**:
* **Penerapan SOLID (Optional)**:
* **Design Pattern yang Digunakan (Optional)**:
* **Code Snippet**:
```
[Code snippet here]
```

### 4.2 Fitur 2
* **Implementasi**:
* **Konsep OOP**:
* **Penerapan SOLID (Optional)**:
* **Design Pattern yang Digunakan (Optional)**:
* **Code Snippet**:
```
[Code snippet here]
```

## 5. Screenshot dan Demo
* **Screenshot 1**: [Deskripsi]
* **Screenshot 2**: [Deskripsi]
* **Link Demo Video**: [URL]

## 6. Panduan Instalasi dan Menjalankan Game
1. [Langkah 1]
2. [Langkah 2]
3. [Langkah n]

## 7. Kendala dan Solusi
1. **Kendala 1**:
    * Solusi:
2. **Kendala 2**:
    * Solusi:

## 8. Kesimpulan dan Pembelajaran
* **Kesimpulan**:
* **Pembelajaran**:
