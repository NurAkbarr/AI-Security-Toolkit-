# AI Security Toolkit 🛡️

**AI Security Toolkit** adalah aplikasi berbasis Python yang dirancang untuk mendemonstrasikan dan menguji ketahanan model Natural Language Processing (NLP) terhadap serangan adversarial. Melalui antarmuka grafis (GUI) yang interaktif, pengguna dapat melihat bagaimana perubahan kecil pada teks (sinonim, typo, dll.) dapat memanipulasi prediksi model AI.

---

## 🚀 Fitur Utama

- **⚡ Manual Attack**: Uji ketahanan model secara real-time dengan input teks manual.
- **📂 Dataset Batch**: Jalankan serangan pada sekumpulan data (Dataset AG News atau Upload CSV).
- **📊 Visualisasi Forensik**: Bandingkan teks asli dan teks hasil serangan secara berdampingan untuk melihat perbedaannya.
- **📈 Metrik Keamanan**: Hitung *Success Rate* serangan untuk mengukur seberapa rentan model Anda.

---

## 🛠️ Instalasi

Pastikan Anda memiliki Python 3.8+ terinstal.

1.  **Clone Repository**
    ```bash
    git clone https://github.com/NurAkbarr/AI-Security-Toolkit-.git
    cd ai-security-toolkit
    ```

2.  **Buat Virtual Environment (Opsional tapi Disarankan)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *(Pastikan library seperti `streamlit`, `torch`, `textattack`, `pandas` terinstall)*

---

## 💻 Cara Penggunaan

Jalankan aplikasi menggunakan Streamlit:

```bash
streamlit run app.py
```

Akan terbuka jendela browser otomatis di alamat `http://localhost:8501`.

---

## 🔍 Contoh Kasus Konkret

Berikut adalah contoh bagaimana toolkit ini bekerja dalam skenario nyata:

### Skenario: Manipulasi Berita Keuangan

**Tujuan:**
Mengelabui model klasifikasi berita agar salah mengkategorikan berita **Bisnis** menjadi kategori lain (misal: Teknologi atau Dunia), yang dapat berpotensi memanipulasi algoritma analisis sentimen pasar.

**Langkah-langkah Demo:**
1.  Buka menu **Manual Attack**.
2.  Masukkan teks berita asli:
    > *"Stocks rallied yesterday as the tech sector showed unexpected growth despite rising inflation concerns."*
3.  Klik **Jalankan Serangan**.

**Hasil Analisis:**
-   **Prediksi Awal**: `Business` (Benar).
-   **Hasil Serangan**: `Sci/Tech` (Salah / Terkecoh).
-   **Perubahan Teks**:
    -   *Asli*: "Stocks rallied..."
    -   *Manipulasi*: "Shares rallied..." (Mengganti 'Stocks' dengan 'Shares').

Meskipun bagi manusia maknanya sama, model AI terkecoh dan memberikan label yang salah. Ini menunjukkan bahwa model tersebut memiliki kerentanan adversarial.

---

## 👥 Tim Pengembang

-   **Nurul Akbar** - Streamlit Product Developer
-   **Muhamamad Dzaki Abiyyu** - Landing Page Developer
-   **Mikail Rivaldo** - Literature & Documentation

---
*Dibuat untuk keperluan Tugas Akhir / Metode Penelitian.*
