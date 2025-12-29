import time
import sys
from data.dataset_loader import load_data
from model.model_loader import load_model, predict
from attack.text_attack import build_attacker
from textattack.attack_results import SuccessfulAttackResult, FailedAttackResult

# AG News Class Labels
CLASS_NAMES = ["World", "Sports", "Business", "Sci/Tech"]

def print_header(title):
    print("\n" + "=" * 50)
    print(f" {title}")
    print("=" * 50)

def format_prediction(label_idx):
    return f"{CLASS_NAMES[label_idx]} ({label_idx})"

def run_manual_input(model, tokenizer):
    print_header("MODE INPUT MANUAL")
    print("Masukkan teks berita dalam Bahasa Inggris.")
    print("Ketik 'menu' untuk kembali ke menu utama.\n")
    
    while True:
        try:
            text = input("\n[INPUT] Masukkan Teks > ").strip()
            if text.lower() == 'menu':
                break
            if not text:
                continue
            
            print(f"\n[*] Menganalisis sentimen awal...")
            # Gunakan prediksi model sebagai label 'kebenaran' untuk serangan
            preds = predict([text], model, tokenizer)
            original_label = preds[0]
            print(f"[*] Terdeteksi sebagai: {format_prediction(original_label)}")
            
            print("[*] Menjalankan serangan (Generating Adversarial Example)...")
            attacker = build_attacker(model, tokenizer, [text], [original_label])
            results = attacker.attack_dataset()
            
            for result in results:
                print("\n" + "-" * 30)
                print("HASIL SERANGAN:")
                
                original_class = CLASS_NAMES[result.original_result.ground_truth_output]
                
                if isinstance(result, SuccessfulAttackResult):
                    perturbed_class = CLASS_NAMES[result.perturbed_result.output]
                    print(f"[SUKSES] Serangan Berhasil!")
                    print(f"Original  : {original_class}")
                    print(f"Perturbed : {perturbed_class}")
                    print(f"\nTeks Asli       : {result.original_result.attacked_text.text}")
                    print(f"Teks Berubah    : {result.perturbed_result.attacked_text.text}")
                elif isinstance(result, FailedAttackResult):
                    print(f"[GAGAL] Serangan Gagal (Tidak dapat mengubah prediksi).")
                    print(f"Kelas Tetap: {original_class}")
                else:
                    print(f"[SKIP] {result.__class__.__name__}")
                print("-" * 30)
                
        except KeyboardInterrupt:
            break

def run_dataset_attack(model, tokenizer, limit):
    print_header(f"MODE DATASET (Limit: {limit})")
    print("[*] Memuat dataset...")
    texts, labels = load_data(limit=limit)
    
    print("[*] Membangun attacker...")
    attacker = build_attacker(model, tokenizer, texts, labels)

    print("[*] Memulai serangan...")
    start_time = time.time()
    results = attacker.attack_dataset()
    
    success = 0
    total = 0
    
    print("\n" + "-" * 50)
    print(f"{'INDEX':<6} | {'STATUS':<10} | {'ORIGINAL':<12} -> {'RESULT':<12}")
    print("-" * 50)

    for i, result in enumerate(results):
        total += 1
        original_class = CLASS_NAMES[result.original_result.ground_truth_output]
        status = "SKIP"
        result_class = "-"
        
        if isinstance(result, SuccessfulAttackResult):
            success += 1
            status = "SUKSES"
            result_class = CLASS_NAMES[result.perturbed_result.output]
        elif isinstance(result, FailedAttackResult):
            status = "GAGAL"
            result_class = original_class
        
        print(f"{i+1:<6} | {status:<10} | {original_class:<12} -> {result_class:<12}")

    end_time = time.time()
    duration = end_time - start_time

    print("-" * 50)
    print(f"Total Sampel    : {total}")
    print(f"Berhasil Attack : {success}")
    print(f"Success Rate    : {success / total * 100:.2f}%" if total > 0 else "Success Rate: 0%")
    print(f"Waktu Eksekusi  : {duration:.2f} detik")
    print("-" * 50)
    input("\nTekan Enter untuk kembali ke menu...")

def main():
    print("[*] Loading Model (Hanya sekali di awal)...")
    model, tokenizer = load_model()
    
    while True:
        print_header("AI SECURITY TOOLKIT - UTAMA")
        print("1. Input Manual (Demo Dosen)")
        print("2. Input Dataset (Pilih jumlah)")
        print("3. Auto Mode (Test Cepat 5 sampel)")
        print("4. Keluar")
        
        choice = input("\nPilih Menu (1-4): ").strip()
        
        if choice == '1':
            run_manual_input(model, tokenizer)
        elif choice == '2':
            try:
                limit_str = input("Masukkan jumlah sampel (default 10): ").strip()
                limit = int(limit_str) if limit_str else 10
                run_dataset_attack(model, tokenizer, limit)
            except ValueError:
                print("Input angka tidak valid!")
        elif choice == '3':
            run_dataset_attack(model, tokenizer, limit=5)
        elif choice == '4':
            print("Keluar program.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan.")
