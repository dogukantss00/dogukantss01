from tkinter import *
from tkinter import messagebox, ttk

def yeni_kullanicii():
    global entry11, entry21, entry31, entry41

    def kart():
        def urunler():
            kullanici = entry1.get()
            sifre = entry2.get()
            kart = entry11.get()
            cvv = entry31.get()
            tur = entry41.get()

            # Eğer herhangi bir giriş alanı boşsa, kullanıcıya uyarı ver
            if not (kullanici and sifre and kart and cvv and tur):
                messagebox.showerror("Hata", "Lütfen tüm bilgileri doldurun!")
                pencere2.destroy()
            else:
                dosya_yolu = "kullanıcılar.txt"
                dosya_yolu = "/home/kali/Desktop/KODLAR/MARKET_SATİS_OTOMATİ/kullanıcılar.txt"



                # Dosyayı "a" (append) modunda açarak verileri dosyanın sonuna ekliyoruz
                with open(dosya_yolu, "a") as dosya:
                    deger = f"{kullanici}:{sifre}:{kart}:{cvv}:{tur}\n"  # Her kullanıcı bilgisini yeni bir satıra yazıyoruz
                    dosya.write(deger)
                    messagebox.showinfo("Başarılı", "Kullanıcı başarıyla oluşturuldu!")
                pencere2.destroy()

        label11 = Label(pencere2, text="KART NUMARANIZI GİRİNİZ", font="italic 10")
        label11.pack()
        entry11 = Entry(pencere2, font="italic 10")
        entry11.pack()
        label21 = Label(pencere2, text="SON KULLANMA TARİHİNİ GİRİNİZ", font="italic 10")
        label21.pack()
        entry21 = Entry(pencere2, font="italic 10")
        entry21.pack()
        label31 = Label(pencere2, text="CVV GİRİNİZ", font="italic 10")
        label31.pack()
        entry31 = Entry(pencere2, font="italic 10")
        entry31.pack()
        label41 = Label(pencere2, text="KART TÜRÜNÜ SEÇİNİZ", font="italic 10")
        label41.pack()
        list = ["visa", "mastercard", "papara"]
        values = list
        entry41 = ttk.Combobox(pencere2, values=values, font="italic 10")
        entry41.pack()

        buton = Button(pencere2, text="ONAYLA", font="italic 10", command=urunler)
        buton.pack()

    pencere2 = Tk()
    pencere2.title("MARKET SATIŞ OTOMASYONU")
    pencere2.geometry("1250x750+300+0")

    label1 = Label(pencere2, text="MARKETİMİZE HOŞGELDİNİZ", font="italic 15")
    label1.pack()

    label2 = Label(pencere2, text="KULLANICI ADI GİRİNİZ", font="italic 15")
    label2.pack()
    entry1 = Entry(pencere2, font="italic 15")
    entry1.pack()
    label3 = Label(pencere2, text="ŞİFRE GİRİNİZ", font="italic 15")
    label3.pack()
    entry2 = Entry(pencere2, font="italic 15",show="*")
    entry2.pack()
    label4 = Button(pencere2, text="KREDİ KARTI BİLGİLERİNİZİ GİRMEK İÇİN TIKLAYIN", font="italic 15", command=kart)
    label4.pack()

    pencere2.mainloop()

