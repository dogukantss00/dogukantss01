from tkinter import *
from katalog import katalogg
from tkinter import messagebox

def giriss():
    def urunler():
        kullanıcı_adı = entry1.get()
        sifree = entry2.get()
        kullanici_bulundu = False

        try:
            with open("kullanıcılar.txt", "r") as dosya:
                for satir in dosya:
                    # Satırları ":" karakterine göre böleriz
                    parcalar = satir.strip().split(":")
                    if len(parcalar) == 5:
                        kullanici, sifre, kart, cvv, tur = parcalar
                        # Kullanıcı adı ve şifreyi kontrol ederiz
                        if kullanıcı_adı == kullanici and sifree == sifre:
                            kullanici_bulundu = True
                            break
                    else:
                        print(f"Geçersiz satır formatı: {satir.strip()}")

            if kullanici_bulundu:
                pencere3.destroy()
                katalogg()
            else:
                messagebox.showerror("Hata", "Lütfen bilgilerinizi kontrol edin.")
        except FileNotFoundError:
            messagebox.showerror("Hata", "kullanıcılar.txt dosyası bulunamadı.")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu: {str(e)}")

    pencere3 = Tk()
    pencere3.title("MARKET SATIŞ OTOMASYONU")
    pencere3.geometry("1250x750+300+0")

    label1 = Label(pencere3, text="MARKETİMİZE HOŞGELDİNİZ", font="italic 15")
    label1.pack()

    label2 = Label(pencere3, text="KULLANICI ADI GİRİNİZ", font="italic 15")
    label2.pack()
    entry1 = Entry(pencere3, font="italic 15")
    entry1.pack()
    label3 = Label(pencere3, text="ŞİFRE GİRİNİZ", font="italic 15")
    label3.pack()
    entry2 = Entry(pencere3, font="italic 15", show="*")  # Şifre girişinde gizlilik için
    entry2.pack()
    label4 = Button(pencere3, text="GİRİS YAP", font="italic 15", command=urunler)
    label4.pack()

    pencere3.mainloop()
