# Panduan Deployment AI Security Toolkit

Untuk mengubah aplikasi lokal (`localhost`) menjadi link website yang bisa diakses orang lain, Anda memiliki dua opsi utama:

## Opsi 1: Streamlit Community Cloud (Direkomendasikan) ☁️
Ini adalah cara paling standar, gratis, dan permanen.

### Syarat:
1. Punya akun GitHub.
2. Punya akun Streamlit Community Cloud (bisa login pakai GitHub).

### Langkah-langkah:

1.  **Push Kode ke GitHub**
    Pastikan semua file project Anda sudah di-upload ke repository GitHub (Public).
    *   Jika belum, buat repo baru di GitHub.com.
    *   Push folder `ai-security-toolkit` ini ke sana.
    *   *Pastikan file `requirements.txt` ikut ter-upload!* Ini krusial agar server tahu library apa yang harus diinstall.

2.  **Deploy di Streamlit**
    *   Buka [share.streamlit.io](https://share.streamlit.io/).
    *   Klik **"New App"**.
    *   Pilih Repository GitHub Anda.
    *   Branch: `main` (atau `master`).
    *   Main file path: `app.py`.
    *   Klik **"Deploy!"**.

3.  **Tunggu Proses Build**
    *   Streamlit akan membaca `requirements.txt` dan menginstall semua library.
    *   *Catatan:* Karena `textattack` dan modelnya cukup besar, proses "Spinning up" pertama kali mungkin memakan waktu 5-10 menit.
    *   Setelah selesai, Anda akan dapat link seperti `https://ai-security-toolkit-namaanda.streamlit.app`.

---

## Opsi 2: Ngrok (Cepat / Sementara) ⚡
Gunakan ini jika Anda hanya ingin demo sebentar ke dosen/teman tanpa harus upload ke GitHub. Link akan mati jika laptop Anda dimatikan.

### Langkah-langkah:
1.  Download [Ngrok](https://ngrok.com/download) dan login.
2.  Jalankan aplikasi Streamlit Anda seperti biasa (di port 8501).
3.  Buka terminal baru (CMD/PowerShell), jalankan:
    ```bash
    ngrok http 8501
    ```
4.  Copy link yang diberikan Ngrok (misal `https://abcd-123.ngrok-free.app`) dan kirim ke orang lain.

---

## Tips Penting untuk Deployment

*   **Caching Model:** Karena keterbatasan memori di versi gratis Streamlit Cloud, terkadang model `universal-sentence-encoder` sering gagal didownload. Jika ini terjadi, Anda mungkin perlu melakukan caching manual atau menggunakan model serangan yang lebih ringan di `text_attack.py` (misalnya menggunakan resep yang tidak butuh TensorFlow).
*   **Reboot:** Jika aplikasi di Cloud terasa lambat atau error, coba tombol "Reboot App" di menu Streamlit.
