import streamlit as st
import torch
import pandas as pd
import time
from data.dataset_loader import load_data
from model.model_loader import load_model, predict
from attack.text_attack import build_attacker
from textattack.attack_results import SuccessfulAttackResult, FailedAttackResult

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Security Toolkit",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MODERN UI STYLING ---
st.markdown("""
<style>
    /* Global Font & Colors */
    :root {
        --primary-color: #4CAF50;
        --danger-color: #FF5252;
        --bg-color-dark: #0E1117;
        --card-bg: #262730;
    }
    
    .stApp {
        background-color: var(--bg-color-dark);
    }
    
    /* Custom Card Design */
    .custom-card {
        background-color: var(--card-bg);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-bottom: 20px;
        border: 1px solid #363945;
    }
    
    .card-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #FAFAFA;
        margin-bottom: 15px;
        border-bottom: 1px solid #444;
        padding-bottom: 10px;
    }

    /* Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    /* Success/Fail Badges */
    .badge-success {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        background-color: rgba(76, 175, 80, 0.2);
        color: #66BB6A;
        border: 1px solid #4CAF50;
        font-weight: bold;
    }
    
    .badge-fail {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        background-color: rgba(255, 82, 82, 0.2);
        color: #FF8A80;
        border: 1px solid #FF5252;
        font-weight: bold;
    }

    /* Comparison Box */
    .comparison-container {
        display: flex;
        gap: 20px;
        margin-top: 15px;
    }
    
    .text-box {
        flex: 1;
        padding: 15px;
        border-radius: 8px;
        background-color: #1E1E1E;
        border-left: 4px solid #555;
    }
    
    .text-box.original { border-left-color: #2196F3; }
    .text-box.attacked { border-left-color: #FF5252; }

</style>
""", unsafe_allow_html=True)

CLASS_NAMES = ["World", "Sports", "Business", "Sci/Tech"]

@st.cache_resource
def get_model():
    """Load model once and cache it."""
    with st.spinner("🤖 Menginisialisasi Model AI Security..."):
        model, tokenizer = load_model()
    return model, tokenizer

def main():
    # --- HEADER SECTION ---
    col_logo, col_title = st.columns([1, 5])
    with col_logo:
        st.markdown("# 🛡️")
    with col_title:
        st.title("AI Security Toolkit")
        st.caption("Advanced Adversarial Attack Simulation & Robustness Testing")

    # --- SIDEBAR INFO ---
    with st.sidebar:
        st.markdown("### ⚙️ System Status")
        try:
            model, tokenizer = get_model()
            device_name = "GPU (CUDA) 🚀" if torch.cuda.is_available() else "CPU 🐢"
            st.success(f"**Engine Active**\n\nDevice: {device_name}")
        except Exception as e:
            st.error(f"System Error: {e}")
            return

        st.divider()
        st.info("""
        **Panduan Singkat:**
        1. **Manual Input**: Tes satu kalimat untuk demo cepat.
        2. **Dataset**: Tes massal menggunakan data AG News atau CSV sendiri.
        """)

    # --- TABS ---
    tab1, tab2 = st.tabs(["⚡ MANUAL ATTACK", "📂 DATASET BATCH"])

    # === TAB 1: MANUAL INPUT ===
    with tab1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Demo Serangan Real-time</div>', unsafe_allow_html=True)
        
        user_input = st.text_area("Masukkan Berita (Bhs Inggris):", 
                                "The government announced new tax regulations for international trade agreements.",
                                height=120,
                                placeholder="Ketik berita di sini...")
        
        c1, c2, c3 = st.columns([1, 1, 2])
        if c1.button("🚀 JALANKAN SERANGAN", type="primary", key="btn_manual"):
            if not user_input.strip():
                st.toast("Mohon isi teks terlebih dahulu!", icon="⚠️")
            else:
                progress_container = st.container()
                
                # 1. Prediction
                with progress_container:
                     st.info("🔍 Menganalisis Konten...")
                     start_pred = predict([user_input], model, tokenizer)[0]
                
                # 2. Attack
                with st.spinner("⚔️ Mencari celah keamanan (Adversarial Search)..."):
                    attacker = build_attacker(model, tokenizer, [user_input], [start_pred])
                    results = attacker.attack_dataset()
                    result = results[0]

                # 3. Results Layout
                st.markdown("---")
                
                res_col1, res_col2 = st.columns(2)
                
                # Original Status
                with res_col1:
                    st.markdown("**🛡️ Analisis Awal**")
                    original_cls = CLASS_NAMES[result.original_result.ground_truth_output]
                    st.markdown(f"<h3>{original_cls}</h3>", unsafe_allow_html=True)
                
                # Attack Result
                with res_col2:
                    st.markdown("**🎯 Hasil Serangan**")
                    if isinstance(result, SuccessfulAttackResult):
                        perturbed_cls = CLASS_NAMES[result.perturbed_result.output]
                        st.markdown(f"<h3 style='color:#FF5252'>{perturbed_cls}</h3>", unsafe_allow_html=True)
                        st.markdown('<div class="badge-success">✅ VULNERABLE (Berhasil Di-hack)</div>', unsafe_allow_html=True)
                    elif isinstance(result, FailedAttackResult):
                        st.markdown(f"<h3 style='color:#4CAF50'>{original_cls}</h3>", unsafe_allow_html=True)
                        st.markdown('<div class="badge-fail">🛡️ ROBUST (Aman)</div>', unsafe_allow_html=True)
                    else:
                        st.markdown("Skipped")

                # Text Diff View
                st.markdown("### 📝 Perbandingan Forensik")
                
                if isinstance(result, SuccessfulAttackResult):
                    org_text = result.original_result.attacked_text.text
                    adv_text = result.perturbed_result.attacked_text.text
                else: 
                    org_text = result.original_result.attacked_text.text
                    adv_text = "Tidak ada perubahan (Serangan Gagal)"

                st.markdown(f"""
                <div class="comparison-container">
                    <div class="text-box original">
                        <small>TEKS ASLI</small><br>
                        {org_text}
                    </div>
                    <div class="text-box attacked">
                         <small>HASIL MANIPULASI</small><br>
                        {adv_text}
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)


    # === TAB 2: DATASET BATCH ===
    with tab2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Konfigurasi Pengujian Batch</div>', unsafe_allow_html=True)

        data_source = st.radio("Sumber Data:", ["📚 AG News (Default)", "📂 Upload File CSV"], horizontal=True)
        
        texts = []
        labels = []
        
        if data_source == "📚 AG News (Default)":
            limit = st.slider("Jumlah Sampel:", 5, 100, 10)
            if st.button("Load & Run Test", type="primary"):
                 with st.spinner("Memuat dataset..."):
                     texts, labels = load_data(limit=limit)
                     run_batch_attack(model, tokenizer, texts, labels)

        else: # CSV Upload
            uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
            if uploaded_file:
                df = pd.read_csv(uploaded_file)
                st.dataframe(df.head(3), wait_for_loading=False)
                
                text_col = st.selectbox("Pilih Kolom Teks:", df.columns)
                limit_csv = st.number_input("Batasi Jumlah Baris (0 = Semua):", min_value=0, value=5)
                
                if st.button("🚀 Proses File CSV", type="primary"):
                    with st.spinner("Memproses CSV..."):
                        # Data Prep
                        if limit_csv > 0:
                            texts = df[text_col].astype(str).tolist()[:limit_csv]
                        else:
                            texts = df[text_col].astype(str).tolist()
                        
                        # Generate Dummy Labels from Prediction (Since user might not have labels)
                        st.info("Generating ground truth labels from model prediction...")
                        preds = predict(texts, model, tokenizer)
                        labels = preds
                        
                        run_batch_attack(model, tokenizer, texts, labels)
        
        st.markdown('</div>', unsafe_allow_html=True)

def run_batch_attack(model, tokenizer, texts, labels):
    st.markdown("### 📊 Proses Serangan Berjalan")
    
    # Containers for live updates
    prog_bar = st.progress(0)
    status_metric = st.empty()
    table_container = st.empty()
    
    attacker = build_attacker(model, tokenizer, texts, labels)
    results = attacker.attack_dataset()
    
    data_log = []
    success = 0
    total = len(texts)
    
    for i, result in enumerate(results):
        prog_bar.progress((i + 1) / total)
        
        # Determine Status
        status = "SKIP"
        orig = CLASS_NAMES[result.original_result.ground_truth_output] if result.original_result else "?"
        final = "-"
        
        if isinstance(result, SuccessfulAttackResult):
            status = "✅ SUKSES"
            success += 1
            final = CLASS_NAMES[result.perturbed_result.output]
        elif isinstance(result, FailedAttackResult):
            status = "❌ GAGAL"
            final = orig
            
        data_log.append({
            "ID": i+1,
            "Status": status,
            "Original": orig,
            "Final": final,
            "Text Snippet": result.original_result.attacked_text.text[:60] + "..."
        })
        
        # Update Table Live
        table_container.dataframe(pd.DataFrame(data_log), use_container_width=True)

    # Final Summary
    st.success("✅ Pengujian Selesai!")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Sampel", total)
    c2.metric("Berhasil Di-hack", success)
    rate = (success/total)*100 if total > 0 else 0
    c3.metric("Success Rate", f"{rate:.1f}%")

if __name__ == "__main__":
    main()
