a=int(input("lütfen bozdurmak istediğiniz miktarı giriniz:"))

if(999>a<=99):
    print("bu parayı bozamam.")
    
else:
    z=a//100
    y=a-z*100
    t=y//10
    g=y-t*10
print("""
100TL:{}ADET
10TL:{}ADET
{} tanede 1 TL

""".format(z,t,g))


print("-----------------------------------------------------------------------------------")

a=int(input("lütfen kredi tutarınızı giriniz:"))
toplamgeriödemetutarı=a+(a*34/100)

print(toplamgeriödemetutarı)
print("Her ay odemeniz gereken tutar {}".format(toplamgeriödemetutarı))

print("-----------------------------------------------------------------------------------")


kazanc = float(input("Yıllık kazancınızı girin : "))
    
    
if kazanc <= 20000:
        vergi = kazanc * 0.10
elif kazanc <= 50000:
        vergi = 20000 * 0.10 + (kazanc - 20000) * 0.20
else:
        vergi = 20000 * 0.10 + 30000 * 0.20 + (kazanc - 50000) * 0.30
    
    
net_gelir = kazanc - vergi
    
print("vermeniz gereken vergi miktarı {} size kalan paranın miktarı:{}".format(vergi,net_gelir))

print("-----------------------------------------------------------------------------------")
kurslar = []

while True:
    
    print("1. Kurs Ekle")
    print("2. Tüm Kursları Göster")
    print("3. Çıkış")
    secim = input("Bir seçenek girin: ")

    if secim == '1':
        
        kurs_adi = input("Kurs adını girin: ")
        ders_sayisi = int(input("Ders sayısını girin: "))
        katilimci_sayisi = int(input("Katılımcı sayısını girin: "))

        
        kurslar.append([kurs_adi, ders_sayisi, katilimci_sayisi])
        print(f"{kurs_adi} kursu başarıyla eklendi.\n")

    elif secim == '2':
        
        if not kurslar:
            print("Henüz eklenmiş bir kurs yok.\n")
        else:
            print("\nTüm Kurslar:")
            for kurs in kurslar:
                print(f"Kurs Adı: {kurs[0]}, Ders Sayısı: {kurs[1]}, Katılımcı Sayısı: {kurs[2]}")
            print()

    elif secim == '3':
        print("Çıkılıyor...")
        break

    else:
        print("Geçersiz seçim, tekrar deneyin.")













