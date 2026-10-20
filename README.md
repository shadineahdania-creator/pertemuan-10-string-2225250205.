# Pertemuan 10 - String dan Pengolahan Teks

**Nama:** Shadine Ahdania Sofyan
**NIM:** 2225250205
**Kelas:** 3B

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python agar nama, inisial, dan kode kelas memiliki format yang konsisten.

**Algoritma dan Pemrograman | Pertemuan 10**

S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa | 2026/2027 Ganjil

## Struktur Program

File `tugas/normalisasi_data_mahasiswa.py` berisi program untuk menormalisasi nama mahasiswa, membuat inisial nama, dan menormalisasi kode kelas menggunakan fungsi string Python.

## Cara Menjalankan

Jalankan perintah berikut melalui terminal dari folder utama proyek:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

## Algoritma

1. Meminta pengguna memasukkan nama dan kode kelas.
2. Menghapus spasi berlebih pada nama dan merapikan huruf kapital di setiap kata.
3. Membuat inisial dari huruf pertama setiap kata pada nama.
4. Mengubah kode kelas menjadi huruf kapital dan mengganti spasi antarkata dengan tanda hubung.
5. Menampilkan nama, kode kelas, dan inisial yang telah dinormalisasi.

## Test Case

| Input Nama | Input Kode | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|
| `aan hendrayana` | `pmat a 2026` | Aan Hendrayana \| PMAT-A-2026 \| AH | Aan Hendrayana \| PMAT-A-2026 \| AH | Lulus |
| `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah \| KELAS-B \| FM | Fathiyyah Muthmainnah \| KELAS-B \| FM | Lulus |
| `BUDI` | `pmtk 01` | Budi \| PMTK-01 \| B | Budi \| PMTK-01 \| B | Lulus |
| `siti  nur aisyah` | `kelas  c` | Siti Nur Aisyah \| KELAS-C \| SNA | Siti Nur Aisyah \| KELAS-C \| SNA | Lulus |

## Refleksi

Masalah teks yang ditemukan adalah penggunaan huruf kapital yang tidak konsisten dan spasi berlebih pada nama serta kode kelas. Masalah tersebut diperbaiki menggunakan fungsi `split()`, `join()`, `title()`, dan `upper()` sehingga data menjadi lebih rapi dan seragam. Saya juga memahami cara membuat inisial secara otomatis menggunakan list dan perulangan.