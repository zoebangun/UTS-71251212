```bash
pip install --upgrade "streamlit>=1.52.0"
python -m install --upgrade "streamlit>=1.52.0"
python3.14 -m install --upgrade "streamlit>=1.52"

ATAU CEK DULU VERSI PYTHON KALIAN
```

> Streamlit minimal **1.52.0**. Kalau versi Anda lebih lama, perintah di atas akan meng-upgrade-nya.
> Cek versi: `streamlit --version`

---

# UTS Praktikum Algoritma dan Struktur Data
## DwTix: Aplikasi Tiket Japfest UKDW 2026

### Cerita

**Japfest UKDW 2026** tinggal beberapa minggu lagi. Panitia membutuhkan aplikasi **DwTix** untuk mengelola penjualan tiket: pengunjung bisa membeli tiket, panitia (Admin dan Staff) memantau daftar peserta, dan semua orang bisa melihat info event.

Tim sebelumnya sudah membuat kerangka aplikasinya (tampilan halaman, form, data awal), tetapi bagian **sesi login, pembatasan akses halaman, hak mengubah isi halaman event (tambah dan hapus), ubah profile, serta pembelian tiket** belum selesai.

Tugas Anda: lengkapi semua bagian bertanda `# TODO` agar DwTix siap dipakai.

---

### Struktur File

```
Soal/
├── README.md         <- soal (file ini)
├── app.py            <- KERJAKAN: Soal 1 (login & sesi)
├── pages/
│   ├── dashboard.py  <- KERJAKAN: Soal 2
│   ├── event.py      <- KERJAKAN: Soal 2, 5
│   ├── profile.py    <- KERJAKAN: Soal 2, 3
│   └── beli-tiket.py <- KERJAKAN: Soal 2, 4
├── data.py           <- data awal (jangan diubah)
├── logout.py         <- tombol logout (jangan diubah)
├── tampilan.py       <- tabel peserta (jangan diubah)
└── japfest.png
```

### Aturan Pengerjaan

1. Kerjakan **hanya** pada bagian bertanda `# TODO`. Bagian yang bertanda `(SUDAH JADI)` tidak perlu diubah.
2. **Jangan mengubah** `data.py`, `logout.py`, dan `tampilan.py`.
3. Boleh menambah variabel atau fungsi bantu sendiri. Tidak boleh meng-*import* library tambahan.

### Menjalankan

```bash
streamlit run app.py
python3.14 -m streamlit run app.py
```

Gunakan akun di bawah untuk mencoba aplikasi Anda.

---

### Data Awal (`data.py`)

| Username | Password | Role | Data profile |
|---|---|---|---|
| Kiya | 123 | Admin | lengkap |
| Semmi | staff | Staff | belum lengkap |
| Kevin | 321 | Peserta | lengkap |
| Calis | calis123 | Pengunjung | belum lengkap |
| Yumeko | calis123 | Pengunjung | belum lengkap |
| Radit | nugroho123 | Pengunjung | belum lengkap |
| Pak Willy | 123 | Peserta | lengkap |

Profile dianggap **lengkap** jika `email`, `gender`, `phone`, dan `address` semuanya terisi.

Event: **Japfest UKDW 2026**, harga tiket Rp15.000, kuota **4** tiket.

Tiket disimpan di `participant_data_by_id()` sebagai dictionary dengan key ID tiket:

```python
{"ID01": {"user_id": 2, "status_bayar": "Paid", "status_tiket": "Belum Check-In"}}
```

`status_bayar` hanya bernilai `"Paid"` (tiket hasil pembelian) atau `"Invitation"` (tamu undangan). `user_id` merujuk ke `id` pada data user.

---

## Soal

### Soal 1 – Sesi dan Login (`app.py`) · **15 poin**

| Bagian | Ketentuan |
|---|---|
| **1a** Deklarasi sesi | Siapkan `logged_in = False`, `uname = None`, `id = None`, `role = None` di `st.session_state`, **hanya jika belum ada** (supaya tidak ter-reset saat halaman dimuat ulang). Jika sudah login sebelumnya, switch lagi ke event.py jika user mencoba masuk ke app.py / form login.|
| **1b** Cek login | Jika username terdaftar dan password cocok, simpan `logged_in`, `uname`, `id`, `role` ke `st.session_state`. Jika salah, tampilkan `st.error("Login gagal! Silahkan coba kembali.")`. **Username yang tidak terdaftar tidak membuat aplikasi error.** |
| **1c** Arah setelah login | `Admin` dan `Staff` → `pages/dashboard.py`. Role lain → `pages/event.py`. |

Tombol **logout** sudah disediakan di `logout.py`.

---

### Soal 2 – Pengecekan Role Tiap Halaman · **10 poin**

Pasang pengecekan di bagian paling atas **setiap halaman**, memakai `st.switch_page()`:

| Halaman | Belum login | Role yang boleh | Role lain dialihkan ke |
|---|---|---|---|
| `dashboard.py` | `app.py` | Admin, Staff | `pages/event.py` |
| `event.py` | `app.py` | semua role | (tidak ada) |
| `profile.py` | `app.py` | semua role | (tidak ada) |
| `beli-tiket.py` | `app.py` | Peserta, Pengunjung | `pages/dashboard.py` |

> Halaman tidak boleh menampilkan isinya sebelum pengecekan lolos.
>
> Isi `dashboard.py` (tabel peserta, baik yang membeli maupun tamu *Invitation*) **sudah disediakan**; di halaman itu Anda hanya memasang pengecekan akses.

---

### Soal 3 – Ubah Profile (`pages/profile.py`) · **15 poin**

Saat tombol **Ubah Data** diklik, bandingkan isi form dengan data user yang tersimpan:

- Data lama bernilai `None` dianggap sama dengan `""`.
- Jika **tidak ada** yang berubah → `st.info("Belum ada perubahan loh ya")` dan data tidak diubah.
- Jika **ada** yang berubah → simpan **hanya field yang berubah** ke data user, lalu tampilkan `st.success` yang menyebut nama field yang diubah, misalnya `Gokilss, anda mengubah: email, phone`.
- Field lain (`id`, `role`, dst.) tidak boleh tersentuh.


HINT :
1. Buat dictionary sementara data_baru untuk menampung seluruh input dari form, kecuali username karena tidak dapat diubah.
2. buat list kosong untuk menyimpan nama atribut yang mengalami perubahan.
3. lakukan perulangan terhadap setiap pasangan key dan value pada data_baru. Bandingkan value tersebut dengan nilai asli pada key yang sama di dictionary pengguna.
4. Jika nilainya berbeda, masukkan nama key tersebut ke dalam list kosong tadi.
5. Setelah perulangan selesai, periksa apakah list kosong:- Jika kosong, tampilkan pesan bahwa belum ada perubahan.
6. Jika tidak kosong, lakukan perulangan terhadap list untuk memperbarui nilai atribut yang berubah pada dictionary pengguna asli.
7. Tampilkan pesan keberhasilan beserta nama atribut yang diperbarui.


ALTERNATIF:
bisa cek 1 1 hardcoded
---

### Soal 4 – Beli Tiket (`pages/beli-tiket.py`) · **35 poin**

| Bagian | Poin | Ketentuan |
|---|---|---|
| **4a** Create | 25 | Tombol **Beli Tiket**. Tolak dengan `st.error` jika **data profile belum lengkap** atau **kuota habis** (jumlah tiket sudah `>= kuota`). Jika lolos, tambahkan tiket baru dengan ID berurutan (`ID502`, `ID503`, ... mengikuti ID terbesar yang ada) berisi `{"user_id": user_id, "status_bayar": "Paid", "status_tiket": "Belum Check-In"}` lalu tampilkan `st.success`. Jika ditolak, `peserta` tidak boleh berubah. |
| **4b** Read | 10 | Subheader **Tiket Saya** menampilkan **hanya** tiket milik user yang login (ID, status bayar, status tiket). Jika belum punya: `st.info("Kamu belum punya tiket.")`. |

Tips: akun **Kevin** dan **Pak Willy** profile-nya sudah lengkap. Akun lain (misalnya **Radit**) bisa melengkapi profile lewat halaman Profile dulu agar dapat membeli tiket.

---

### Soal 5 – Kelola Isi Halaman Event (`pages/event.py`) · **25 poin**

Halaman event menampilkan tiga daftar: **Sponsor**, **Pengisi Acara**, dan **Rundown**. Tampilan halaman, `selectbox` untuk memilih item yang akan dihapus, `st.form` untuk menambah data, dan bagian *Edit Info Event* **sudah disediakan**. Anda mengerjakan logikanya:

| Bagian | Poin | Ketentuan |
|---|---|---|
| **5a** Hak mengubah | 5 | Tentukan `can_edit` dari role di bagian bawah file: hanya **Admin** dan **Staff** yang boleh mengubah isi halaman. **Peserta** dan **Pengunjung** hanya melihat (tidak ada tombol Hapus, form Tambah, maupun Edit Info Event). |
| **5b** Hapus | 10 | Di bawah `selectbox` pada tiap daftar, buat tombol berlabel `f"Hapus {judul}"` (misalnya **Hapus Sponsor**). Klik → item yang sedang dipilih di `selectbox` dihapus dari `event[key]`, lalu `st.rerun()`. Item lain tidak boleh ikut terhapus. |
| **5c** Tambah | 10 | Saat tombol **Tambah** pada form diklik: jika ada field yang kosong atau hanya berisi spasi → `st.error("Semua field wajib diisi!")` dan data tidak bertambah. Jika semua terisi → tambahkan `data_baru` ke `event[key]`, lalu `st.rerun()`. |

Cek dengan dua akun: **Kiya** (Admin) harus bisa menambah dan menghapus, **Kevin** (Peserta) hanya melihat.

---

## Penilaian

| Soal | Bagian | Poin |
|---|---|---|
| 1 | Sesi dan login | 15 |
| 2 | Pengecekan role tiap halaman | 10 |
| 3 | Ubah profile | 15 |
| 4 | Beli tiket (Create 25, Read 10) | 35 |
| 5 | Kelola isi halaman event (5a 5, 5b 10, 5c 10) | 25 |
| | **Total** | **100** |

- Penilaian dilakukan asisten dengan menjalankan aplikasi dan memeriksa kode.
- Jika **syarat** suatu soal dilanggar, nilai soal tersebut menjadi **0** walaupun hasilnya benar.
- Jangan menulis jawaban yang hanya menyesuaikan contoh (*hard-code*); asisten dapat menguji dengan data lain.

**Selamat mengerjakan, semoga Japfest UKDW 2026 laris manis!**
