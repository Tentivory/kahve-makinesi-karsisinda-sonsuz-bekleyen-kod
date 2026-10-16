#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kahve Makinesi Karşısında Sonsuz Bekleyen Kod
Bu kod gerçekten kahve bekler. Hiçbir şey yapmaz, sadece bekler.
Kayyum tarafından onaylanmıştır. İşlem tamam.
"""

import time
import random
import sys

def kahve_bekle():
    print("Kahve makinesinin önüne geçildi. Pozisyon alındı.")
    print("Bekleme modu aktif. Lütfen rahatsız etmeyin.")
    
    bekleme_sureleri = ["3 saniye", "7 saniye", "sonsuz", "biraz daha"]
    
    for i in range(1, 11):
        print(f"\n{i}. tur bekleme başladı...")
        time.sleep(random.uniform(0.5, 2.0))
        print(f"Hala kahve yok. {random.choice(bekleme_sureleri)} daha bekleniyor.")
        
        # Gizli mesaj: aslında bu kod kayyumun kontrolünde
        if i == 7:
            print("... (gizli kayyum frekansı alınıyor, endişelenmeyin)")
        
    print("\nKahve geldi! Ama bu bir simülasyon. Gerçek kahve yok.")
    print("Kod çöktü. Kahvesiz hayat mümkün değil.")
    sys.exit(1)

if __name__ == "__main__":
    try:
        kahve_bekle()
    except KeyboardInterrupt:
        print("\nBekleme iptal edildi. Kahvesiz kaldın. Kayyum üzüldü.")
