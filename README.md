# 🤖 Visualisasi Karakter Robot 3D dengan Plotly

Proyek ini merupakan visualisasi interaktif dari sebuah **robot 3D lucu** yang dibangun menggunakan **Plotly** di Python. Robot ini dirakit dari beberapa bentuk geometri dasar seperti **bola (sphere)**, **silinder (cylinder)**, dan **kerucut (cone)** yang disusun menjadi bagian kepala, badan, lengan, kaki, sepatu, dan topi.

---

## 🎯 Tujuan

Memberikan contoh implementasi pembuatan karakter 3D modular menggunakan `Plotly`, serta menunjukkan bagaimana menyusun objek-objek geometri sederhana menjadi satu struktur visual yang kompleks (robot) dengan pendekatan scene graph.

---

## 🧩 Komponen Robot & Cara Pembangunannya

### 1. 🧠 Kepala (`create_sphere`)

- **Radius:** `0.7`
- **Pusat:** `(0, 0, 2.6)`
- **Warna:** `YlOrBr` (gradasi oranye ke coklat)

---

### 4. 🧍‍♂️ Badan (`create_cylinder`)

- **Radius:** `0.5`
- **Tinggi:** `1.2`
- **Pusat:** `(0, 0, 1.3)`
- **Warna:** `Reds`

---

### 5. 💪 Lengan (`create_cylinder`)

- **Radius:** `0.1`
- **Tinggi:** `0.9`
- **Pusat:** `(-0.8, 0, 1.5)` dan `(0.8, 0, 1.5)`
- **Warna:** `Reds`

---

### 6. 🦵 Kaki (`create_cylinder`)

- **Radius:** `0.15`
- **Tinggi:** `0.8`
- **Pusat:** `(-0.2, 0, 0.3)` dan `(0.2, 0, 0.3)`
- **Warna:** `Blues`

---

### 7. 👟 Sepatu (`create_sphere`)

- **Radius:** `0.2`
- **Pusat:** Sama dengan bawah kaki
- **Warna:** `Blues`

---

### 8. 🎩 Topi (`create_cone`)

- **Radius:** `0.6`
- **Tinggi:** `0.9`
- **Pusat:** `(0, 0, 3.3)`
- **Warna:** `Purples`

---

## 🖼 Contoh Visualisasi

> Berikut adalah hasil visualisasi robot yang ditampilkan secara interaktif di browser:

![Robot Preview](image/README/robot3d_example.png)

---

## 💻 Teknologi yang Digunakan

- Python 3.13+
- Plotly
- NumPy

---

## 🚀 Cara Menjalankan

1. Pastikan kamu sudah menginstall dependensi berikut:

```bash
pip install numpy plotly
```
