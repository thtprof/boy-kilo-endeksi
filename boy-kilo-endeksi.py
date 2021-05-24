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

    if endeks < 0:
        print("Endeks Ortalamaniz: Hata!!")
        print ("Endeksiniz: 0'dan küçük değerler girmeyiniz  ")
    elif endeks > 0 and endeks  <= 18.4:
        print("Endeks Ortalamaniz: ", endeks)
        print ("Endeksiniz: Zayif")
    elif endeks >= 18.5 and endeks <= 24.9:
        print("Endeks Ortalamaniz: ", endeks)
        print ("Endeksiniz: Normal")
    elif endeks >= 25.0 and endeks <= 29.9:
        print("Endeks Ortalamaniz: ", endeks)
        print ("Endeksiniz: Fazla Kilolu")
    elif endeks >= 30.0 and endeks <= 34.9:
        print("Endeks Ortalamaniz: ", endeks)
        print ("Endeksiniz: Sisman(Obez)")



hesapla()
