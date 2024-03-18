# Aproksimasi Kurva Bezier

Demo langsung: Kurva Bezier dengan Metode Brute Force | Kurva Bezier dengan Metode Divide and Conquer

## Daftar Isi
* [Informasi Umum](#informasi-umum)
* [Tujuan](#tujuan)
* [Mengapa Melakukannya](#mengapa-melakukannya)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Fitur](#fitur)
* [Output](#output)
* [Setup](#setup)
* [Dependensi](#dependensi)
* [Penggunaan](#penggunaan)
* [Penjelasan Tambahan](#penjelasan-tambahan)
* [Status Proyek](#status-proyek)
* [Ruangan untuk Perbaikan](#ruangan-untuk-perbaikan)
* [Ucapan Terima Kasih](#ucapan-terima-kasih)
* [Kontak](#kontak)


## Informasi Umum
Proyek ini bertujuan untuk mengaproksimasi kurva Bezier kuadratik menggunakan algoritma brute-force dan divide-and-conquer. Kurva Bezier banyak digunakan dalam grafika komputer dan aplikasi desain untuk membuat kurva yang halus berdasarkan serangkaian titik kontrol.

## Tujuan
Tujuan dari proyek ini adalah untuk membandingkan kinerja dan akurasi dari algoritma brute-force dan divide-and-conquer dalam mengaproksimasi kurva Bezier. Dengan mengimplementasikan kedua algoritma ini, kita dapat mengevaluasi waktu eksekusi dan kualitas kurva yang dihasilkan.

## Mengapa Melakukannya ?
Memahami berbagai algoritma untuk aproksimasi kurva sangat penting dalam grafika komputer dan desain. Dengan mengimplementasikan dan membandingkan algoritma-algoritma ini, kita dapat memperoleh wawasan tentang kelebihan, kelemahan, dan aplikasi praktisnya.

## Teknologi yang Digunakan
- Python - versi 3.12.2
- Matplotlib - versi  3.8.3
- NumPy - versi 1.26.4
- Six - versi 1.16.0

## Fitur
Daftar fitur yang sudah siap :
- Algoritma brute-force untuk mengaproksimasi kurva Bezier kuadratik.
- Algoritma divide-and-conquer untuk mengaproksimasi kurva Bezier kuadratik.
  
## Output
![BruteForce_1](./test/BruteForce_1.png)
![DivideAndConquer_1](./test/DevideandConquer_1.png)

## Setup

Untuk menjalankan proyek ini, pastikan Anda sudah menginstal Python. Clone repositori dan navigasikan ke direktori proyek.

## Dependensi

Pastikan Python versi 3.12.2 atau lebih tinggi telah terinstal. Gunakan pip untuk menginstal NumPy dan Matplotlib:

- [Python](https://www.python.org/downloads/): Pastikan Python versi 3.12.2 atau lebih tinggi telah terinstal.
- [NumPy](https://numpy.org/) : Library untuk komputasi numerik dalam Python.
- [Matplotlib](https://matplotlib.org/) : Library untuk membuat visualisasi data dalam Python.
- [six](https://pypi.org/project/six/): Library untuk memastikan kompatibilitas antara Python 2 dan Python 3.
- [Time](https://docs.python.org/3/library/time.html) : Modul standar Python untuk manajemen waktu.

Anda dapat menginstal dependensi menggunakan pip:

```bash
pip install numpy
```
```bash
pip install matplotlib
```
```bash
pip install six
```
or
```bash
pip install --upgrade six
```


## Penggunaan

1. Clone repositori ke sistem lokal Anda**: Dapatkan salinan proyek ini di komputer Anda dengan menggunakan perintintah git clone dalam terminal :

    ```bash
    git clone https://github.com/Fiqri317/Tucil2_10023519.git
    ```

2. Buka terminal dan navigasi ke direktori proyek**: Setelah mengkloning repositori, buka terminal dan navigasikan ke direktori proyek :

    ```bash
    cd Tucil2_10023519
    ```

3. Menjalankan algoritma brute force**:

    Untuk menggunakan algoritma brute force, jalankan perintah berikut di terminal :

    ```bash
    python src/bezierCurveBruteForce.py
    ```

4. Menjalankan algoritma divide and conquer**:

    Untuk menggunakan algoritma divide and conquer, jalankan perintah berikut di terminal :

    ```bash
    python src/bezierCurveDivideAndConquer.py
    ```

5. Ikuti instruksi di terminal**: Setelah menjalankan salah satu dari kedua perintah di atas, terminal akan meminta Anda untuk memasukkan titik kontrol dan jumlah iterasi. Ikuti instruksi yang diberikan di terminal untuk memasukkan data yang diperlukan.

## Penjelasan Tambahan

Proyek ini bertujuan untuk mendemonstrasikan penggunaan algoritma brute force dan divide and conquer untuk mengaproksimasi kurva Bezier. Dengan menjalankan kedua algoritma ini, Anda dapat mengevaluasi waktu eksekusi dan kualitas kurva yang dihasilkan.

Dengan menggunakan algoritma brute force, Anda akan mendapatkan solusi yang diperoleh dengan cara mencoba semua kemungkinan titik kontrol dalam rentang tertentu, sementara algoritma divide and conquer membagi masalah menjadi sub-masalah yang lebih kecil dan menggabungkan solusi-solusi tersebut.

Pastikan untuk mengikuti instruksi yang diberikan di terminal dengan cermat untuk mendapatkan hasil yang akurat dan memahami bagaimana setiap algoritma bekerja. Semoga Anda menikmati penggunaan proyek ini!



## Status Proyek
Proyek ini sudah selesai.

## Ruangan untuk Perbaikan
Area yang dapat diperbaiki :
- Implementasikan algoritma lebih lanjut untuk aproksimasi kurva.
- Tingkatkan antarmuka pengguna untuk interaksi dan visualisasi yang lebih baik.

Yang akan dilakukan :
- Tambahkan dukungan untuk kurva Bezier dengan orde yang lebih tinggi.
- Implementasikan teknik optimasi untuk eksekusi yang lebih cepat.

## Ucapan Terima Kasih
Proyek ini terinspirasi oleh [Tugas Kecil 2 Algoritma dan Struktur Data. Rinaldi Munir (2024)](https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2023-2024/Tucil2-2024.pdf)].

## Kontak
Dibuat oleh __Muhammad Fiqri__ - Silakan Hubungi Saya! Email : [10023519@std.stei.itb.ac.id)](mailto:10023519@std.stei.itb.ac.id)
