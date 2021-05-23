
    
# -*- coding: utf-8 -*-

"""
Vucut Kitle İndeksi Hesaplama
Zayif --- 0-18.4
Normal --- 18.4-24.9
Fazla Kilolu --- 25.0-29.9
Sisman --- 30.0-34.9
Boy, kilo
Kitle İndeksiniz = Kilo/(boy*boy)
"""

def hesapla():
    boy = float(input("Boyunuzu giriniz:"))
    kilo = float(input("Kilonuzu giriniz:"))
    endeks = kilo/((boy/100)**2)
    print(f"Endeks Ortalamaniz: {endeks}")

    if endeks <= 18.4:
        print ("Endeksiniz: Zayif")
    elif endeks >= 18.5 and endeks <= 24.9:
        print ("Endeksiniz: Normal")
    elif endeks >= 25.0 and endeks <= 29.9:
        print ("Endeksiniz: Fazla Kilolu")
    elif endeks >= 30.0 and endeks <= 34.9:
        print ("Endeksiniz: Sisman(Obez)")
    
    
hesapla()
