# ✅ AI Security Testing Checklist & Framework

## 1. Apa itu Framework ini?
**AI Security Framework** yang digunakan dalam toolkit ini menggunakan metodologi **Adversarial Attack Loop**:
1.  **Input**: Menerima teks asli (Clean Input).
2.  **Attack Generation**: Menggunakan algoritma genetik/greedy untuk memodifikasi teks (Typo, Synonym, Char Swap).
3.  **Validation**: Memastikan makna teks masih relatif sama (Semantic similarity).
4.  **Query**: Mengirim teks hasil modifikasi ke Model Target.
5.  **Evaluation**: Mengecek apakah label prediksi berubah.

---

## 2. Checklist Pengujian Keamanan (Security Audit)

Gunakan checklist ini saat melakukan *pentest* (penetration testing) pada model NLP Anda.

### 🛠️ Tahap Persiapan (Preparation)
- [ ] **Environment**: Pastikan Python 3.8+ dan library terinstall (`pip install -r requirements.txt`).
- [ ] **Model Target**: Pastikan model `distilbert-base-uncased-ag-news` berhasil didownload/di-cache.
- [ ] **GPU Availability**: Cek apakah CUDA tersedia untuk performa lebih cepat (Opsional).

### ⚡ Tahap Pengujian Manual (Exploratory Testing)
Coba skenario serangan berikut untuk melihat sensitivitas model:
- [ ] **Attack 1: Sinonim Bisnis** (Ganti "Money" -> "Cash", "Growth" -> "Expansion").
- [ ] **Attack 2: Typo Kritis** (Ganti "President" -> "Presidnet").
- [ ] **Attack 3: Konteks Ganda** (Masukkan kalimat yang ambigu antara Olahraga dan Politik).

### 📂 Tahap Pengujian Skala Besar (Batch Evaluation)
- [ ] **Load Dataset**: Gunakan dataset `AG News` (5-10 sampel untuk demo cepat).
- [ ] **Run Attack**: Jalankan serangan otomatis.
- [ ] **Analisis Metric**:
    - [ ] *Success Rate* > 50%? (Model rentan).
    - [ ] *Success Rate* < 20%? (Model cukup robust).

### 📊 Tahap Pelaporan (Reporting)
- [ ] **Dokumentasi**: Simpan screenshot hasil perbandingan teks asli vs adversarial.
- [ ] **Rekomendasi**: Sarankan *Adversarial Training* (melatih ulang model dengan data serangan) jika model terbukti rentan.
