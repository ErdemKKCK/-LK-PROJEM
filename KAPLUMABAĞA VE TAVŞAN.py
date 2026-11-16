import random
import time

def kaplumbaga_hareketi(pozisyon):
    """Kaplumbağanın hamlesini hesaplar ve yeni pozisyonu döndürür."""
    i = random.randint(1, 10)
    
    if 1 <= i <= 5:      # Hızlı yürüyüş (%50 ihtimal)
        pozisyon += 3
    elif 6 <= i <= 7:    # Kayma (%20 ihtimal)
        pozisyon -= 6
    elif 8 <= i <= 10:   # Yavaş yürüyüş (%30 ihtimal)
        pozisyon += 1
        
    # 1'in altına düşerse 1'e sabitle
    return max(1, pozisyon)

def tavsan_hareketi(pozisyon):
    """Tavşanın hamlesini hesaplar ve yeni pozisyonu döndürür."""
    i = random.randint(1, 10)
    
    if 1 <= i <= 2:      # Uyku (%20 ihtimal)
        pass             # Değişim yok (+0)
    elif 3 <= i <= 4:    # Büyük sıçrama (%20 ihtimal)
        pozisyon += 9
    elif i == 5:         # Büyük kayma (%10 ihtimal)
        pozisyon -= 12
    elif 6 <= i <= 8:    # Küçük sıçrama (%30 ihtimal)
        pozisyon += 1
    elif 9 <= i <= 10:   # Küçük kayma (%20 ihtimal)
        pozisyon -= 2
        
    # 1'in altına düşerse 1'e sabitle
    return max(1, pozisyon)

def yaris_baslat():
    # Başlangıç pozisyonları
    t_pos = 1
    h_pos = 1
    
    print("BANG !!!!!")
    print("AND THEY'RE OFF !!!!!\n")
    
    # Yarış 70. kareye ulaşılana veya geçilene kadar devam eder
    while t_pos < 70 and h_pos < 70:
        # Her saat tıkında hamleleri hesapla
        t_pos = kaplumbaga_hareketi(t_pos)
        h_pos = tavsan_hareketi(h_pos)
        
        # 70 karakterlik boş parkur oluştur
        parkur = [" "] * 70
        
        # Aynı karedeler mi kontrol et
        if t_pos == h_pos:
            # Sınır dışına çıkmayı önlemek için index kontrolü
            idx = min(t_pos - 1, 69)
            parkur[idx] = "O"
            print("".join(parkur) + " OUCH!!!")
        else:
            t_idx = min(t_pos - 1, 69)
            h_idx = min(h_pos - 1, 69)
            
            # Harfleri yerleştir
            parkur[t_idx] = 'T'
            parkur[h_idx] = 'H'
            print("".join(parkur))
            
        # Görsel akışın takip edilebilmesi için kısa bir bekleme (0.2 saniye)
        time.sleep(0.2)
        
    print("\n")
    # Kazananı belirle
    if t_pos >= 70 and h_pos >= 70:
        print("IT'S A TIE! (Berabere!)")
    elif t_pos >= 70:
        print("TORTOISE WINS!!! YAY!!!")
    else:
        print("Hare wins. Yuch.")

# Simülasyonu çalıştırmak için:
yaris_baslat()