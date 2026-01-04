# Naskah Presentasi Video Demo AI Security Toolkit

**Durasi Estimasi:** 2-3 Menit
**Format:** Screen Recording dengan Voice Over (VO)

---

## 1. Pembukaan (0:00 - 0:30)

**Visual:**
- Tampilkan halaman awal aplikasi (Landing Page atau Halaman Utama Streamlit `app.py`).
- Zoom in sedikit ke logo atau judul "AI Security Toolkit".

**Audio (Narasi):**
"Halo semua. Pada kesempatan kali ini, kami akan mendemonstrasikan **AI Security Toolkit**, sebuah perangkat lunak yang dirancang untuk menguji keamanan model AI terhadap serangan teks adversarial.
Tujuan utama toolkit ini adalah untuk memperlihatkan bagaimana sebuah model klasifikasi berita bisa 'tertipu' oleh perubahan kecil pada teks, yang bagi manusia terlihat sama, namun bagi AI memiliki makna yang sangat berbeda."

---

## 2. Demo Kasus Konkret: Serangan Manual (0:30 - 1:30)
*(Fokus pada studi kasus Manipulasi Berita Bisnis)*

**Visual:**
1. Kursor klik tab **"⚡ MANUAL ATTACK"**.
2. Pada kolom input teks, hapus teks default dan paste contoh kasus berikut (Berita Bisnis):
   > *"Stocks rallied yesterday as the tech sector showed unexpected growth despite rising inflation concerns."*
   *(Artinya: Saham reli kemarin karena sektor teknologi menunjukkan pertumbuhan tak terduga meskipun ada kekhawatiran inflasi.)*
3. Klik tombol **"🚀 JALANKAN SERANGAN"**.
4. Tunggu loading bar "Mencari celah keamanan...".

**Audio (Narasi):**
"Mari kita masuk ke contoh konkret menggunakan fitur **Manual Attack**.
Di sini saya memasukkan sebuah header berita ekonomi positif: *'Stocks rallied yesterday as the tech sector showed unexpected growth...'*
Secara alami, model AI akan memprediksi ini sebagai kategori **'Business'**.
Sekarang, kita jalankan serangan. Toolkit ini akan secara otomatis mencari sinonim atau perubahan karakter yang halus untuk mencoba mengubah prediksi model."

**Visual (Setelah Hasil Muncul):**
- Sorot bagian **"🛡️ Analisis Awal"** (Harusnya muncul: "Business").
- Sorot bagian **"🎯 Hasil Serangan"** (Jika berhasil, misal berubah jadi "Sci/Tech" atau "World").
- Scroll ke bawah ke **"📝 Perbandingan Forensik"**. Tunjukkan kata yang berubah (misal: "growth" menjadi "expansion" atau "rising" menjadi "escalating").

**Audio (Narasi):**
"Lihat hasilnya. Model awalnya yakin 100% ini berita **Business**.
Namun setelah serangan berhasil, prediksi model berubah menjadi **[Sebutkan Hasil Baru, misal: Sci/Tech]**.
Padahal jika kita baca teks hasil manipulasi di sebelah kanan, maknanya bagi kita manusia masih sama persis. Inilah yang disebut **Adversarial Example**. Celah keamanan ini bisa berbahaya jika digunakan untuk memanipulasi algoritma trading otomatis atau analisis sentimen pasar."

---

## 3. Demo Batch Processing (1:30 - 2:00)

**Visual:**
1. Klik tab **"📂 DATASET BATCH"**.
2. Pilih sumber data **"📚 AG News (Default)"**.
3. Geser slider jumlah sampel ke angka **5** (agar cepat).
4. Klik **"Load & Run Test"**.
5. Biarkan tabel hasil berjalan.

**Audio (Narasi):**
"Selain pengujian manual, toolkit ini juga mendukung pengujian skala besar. Di menu **Dataset Batch**, kita bisa menguji ketahanan model terhadap puluhan atau ratusan sampel sekaligus.
Ini sangat berguna bagi *machine learning engineer* untuk mengevaluasi seberapa *robust* (tangguh) model mereka sebelum di-deploy ke produksi."

---

## 4. Penutup (2:00 - 2:30)

**Visual:**
- Tampilkan ringkasan hasil (Success Rate) di bagian bawah.
- Kembali ke tampilan utama yang bersih.

**Audio (Narasi):**
"Kesimpulannya, AI Security Toolkit memberikan transparansi visual mengenai kerentanan model deep learning. Dengan alat ini, pengembang dapat menyadarai kelemahan model mereka dan melakukan perbaikan lebih lanjut.
Sekian demonstrasi dari kami, terima kasih."
