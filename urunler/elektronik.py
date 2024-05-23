from tkinter import *
from tkinter import messagebox, ttk

# Global değişkenlerin tanımlanması
fiyat1 = 0
fiyat2 = 0
fiyat3 = 0
fiyat4 = 0
fiyat5 = 0
fiyat6 = 0
fiyat7 = 0
fiyat8 = 0
fiyat9 = 0
fiyat10 = 0
fiyat11 = 0
fiyat12 = 0

def buton3():
    def urun1():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=50)
        def sepete_ekle():
            global fiyat1
            girilen_metin = label2.cget("text") + " x"+ combo1.get()
            listbox.insert(END, girilen_metin)
            degerx = labelx.cget("text")
            deger2 = combo1.get()
            fiyat1 = int(deger2) * int(degerx)

            
        label2 = Label(pencere1, text="ürün adı : asd", font="italic 10")
        label2.place(x=120, y=50)
        label3 = Label(pencere1, text="ürün fiyatı : ", font="italic 10")
        label3.place(x=120, y=70)
        labelx = Label(pencere1, text="14 ", font="italic 10")
        labelx.place(x=200, y=70)
        label4 = Label(pencere1, text="ürün adeti : ", font="italic 10")
        label4.place(x=120, y=90)
        combo1 = ttk.Combobox(pencere1, values=values)
        combo1.place(x=200, y=90)
        siparis1 = Button(pencere1, text="sepete ekle", command=sepete_ekle)
        siparis1.place(x=270, y=110)


    def urun2():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=150)
        def sepete_ekle():
            global fiyat2
            girilen_metin = label2.cget("text") + " x"+ combo1.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo1.get()
            fiyat2=int(deger2)*int(degerx)

        label2=Label(pencere1,text="ürün adı : xxd",font="italic 10")
        label2.place(x=120,y=150)
        label6=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label6.place(x=120,y=170)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=200,y=170)
        label7=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label7.place(x=120,y=190)
        combo1=ttk.Combobox(pencere1,values=values)
        combo1.place(x=200,y=190)
        siparis3=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis3.place(x=270,y=210)

    def urun3():

        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=250)        
        def sepete_ekle():
            global fiyat3      
            girilen_metin = label8.cget("text") + " x"+ combo4.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo4.get()
            fiyat3=int(deger2)*int(degerx)
      
        label8=Label(pencere1,text="ürün adı :qq ",font="italic 10")
        label8.place(x=120,y=250)
        label9=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label9.place(x=120,y=270)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=200,y=270)
        label10=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label10.place(x=120,y=290)
        combo4=ttk.Combobox(pencere1,values=values)
        combo4.place(x=200,y=290)
        siparis4=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis4.place(x=270,y=310)

    def urun4():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=350)        
        def sepete_ekle():
            global fiyat4   
            girilen_metin = label11.cget("text") + " x"+ combo5.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo5.get()
            fiyat4=int(deger2)*int(degerx)
       
        label11=Label(pencere1,text="ürün adı :q1 ",font="italic 10")
        label11.place(x=120,y=350)
        label12=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label12.place(x=120,y=370)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=200,y=370)        
        label13=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label13.place(x=120,y=390)
        combo5=ttk.Combobox(pencere1,values=values)
        combo5.place(x=200,y=390)

        siparis5=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis5.place(x=270,y=410)




    def urun5():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=450)        
        def sepete_ekle():
            global fiyat5         
            girilen_metin = label14.cget("text") + " x"+ combo8.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo8.get()
            fiyat5=int(deger2)*int(degerx)
        
        label14=Label(pencere1,text="ürün adı : ",font="italic 10")
        label14.place(x=120,y=450)
        label15=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label15.place(x=120,y=470)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=200,y=470)        
        label16=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label16.place(x=120,y=490)
        combo8=ttk.Combobox(pencere1,values=values)
        combo8.place(x=200,y=490)
        siparis8=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis8.place(x=270,y=510)


    def urun6():

        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=550)        
        def sepete_ekle():
            global fiyat6         
            girilen_metin = label17.cget("text") + " x"+ combo9.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo9.get()
            fiyat6=int(deger2)*int(degerx)
        
        label17=Label(pencere1,text="ürün adı : ",font="italic 10")
        label17.place(x=120,y=550)
        label18=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label18.place(x=120,y=570)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=200,y=570)        
        label19=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label19.place(x=120,y=590)
        combo9=ttk.Combobox(pencere1,values=values)
        combo9.place(x=200,y=590)
        siparis9=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis9.place(x=270,y=610)



    def urun7():

        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=10,y=650)        
        def sepete_ekle():
            global fiyat7          
            girilen_metin = label20.cget("text") + " x"+ combo10.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo10.get()
            fiyat7=int(deger2)*int(degerx)
        
        label20=Label(pencere1,text="ürün adı : ",font="italic 10")
        label20.place(x=120,y=650)
        label21=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label21.place(x=120,y=670)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=200,y=670)        
        label22=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label22.place(x=120,y=690)
        combo10=ttk.Combobox(pencere1,values=values)
        combo10.place(x=200,y=690)
        siparis10=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis10.place(x=270,y=710)


    def urun8():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=610,y=50)        
        def sepete_ekle():
            global fiyat8       
            girilen_metin = label23.cget("text") + " x"+ combo11.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo11.get()
            fiyat8=int(deger2)*int(degerx)
         
        label23=Label(pencere1,text="ürün adı : ",font="italic 10")
        label23.place(x=720,y=50)
        label24=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label24.place(x=720,y=70)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=800,y=70)        
        label25=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label25.place(x=720,y=90)
        combo11=ttk.Combobox(pencere1,values=values)
        combo11.place(x=800,y=90)
        siparis11=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis11.place(x=870,y=110)


    def urun9():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=610,y=150)        
        def sepete_ekle():
            global fiyat9          
            girilen_metin = label26.cget("text") + " x"+ combo12.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo12.get()
            fiyat9=int(deger2)*int(degerx)
        
        label26=Label(pencere1,text="ürün adı : ",font="italic 10")
        label26.place(x=720,y=150)
        label27=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label27.place(x=720,y=170)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=800,y=170)        
        label28=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label28.place(x=720,y=190)
        combo12=ttk.Combobox(pencere1,values=values)
        combo12.place(x=800,y=190)
        siparis12=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis12.place(x=870,y=210)




    def urun10():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=610,y=250)        
        def sepete_ekle():
            global fiyat10       
            girilen_metin = label29.cget("text") + " x"+ combo13.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo13.get()
            fiyat10=int(deger2)*int(degerx)
         
        label29=Label(pencere1,text="ürün adı : ",font="italic 10")
        label29.place(x=720,y=250)
        label30=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label30.place(x=720,y=270)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=800,y=270)        
        label31=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label31.place(x=720,y=290)
        combo13=ttk.Combobox(pencere1,values=values)
        combo13.place(x=800,y=290)
        siparis13=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis13.place(x=870,y=310)



    def urun11():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=610,y=350)
        def sepete_ekle():
            global fiyat11          
            girilen_metin = label32.cget("text") + " x"+ combo14.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo14.get()
            fiyat11=int(deger2)*int(degerx)
         
        label32=Label(pencere1,text="ürün adı : ",font="italic 10")
        label32.place(x=720,y=350)
        label33=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label33.place(x=720,y=370)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=800,y=370)        
        label34=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label34.place(x=720,y=390)
        combo14=ttk.Combobox(pencere1,values=values)
        combo14.place(x=800,y=390)
        siparis14=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis14.place(x=870,y=410)



    def urun12():
        buton1=Button(pencere1,text="asd",width=10,height=5,state=DISABLED)
        buton1.place(x=610,y=450)
        def sepete_ekle():
                   
            girilen_metin = label2.cget("text") + " x"+ combo15.get()
            listbox.insert(END, girilen_metin)
            degerx=labelx.cget("text")
            deger2=combo15.get()
            global fiyat12 
            fiyat12=int(deger2)*int(degerx)
            
                   

        label2=Label(pencere1,text="ürün adı : ",font="italic 10")
        label2.place(x=720,y=450)
        label36=Label(pencere1,text="ürün fiyatı : ",font="italic 10")
        label36.place(x=720,y=470)
        labelx=Label(pencere1,text="14 ",font="italic 10")
        labelx.place(x=800,y=470)    
        label37=Label(pencere1,text="ürün adeti : ",font="italic 10")
        label37.place(x=720,y=490)
        combo15=ttk.Combobox(pencere1,values=values)
        combo15.place(x=800,y=490)
        siparis15=Button(pencere1,text="sepete ekle",command=sepete_ekle)
        siparis15.place(x=870,y=510)
    
    pencere1 = Tk()
    pencere1.title("MARKET SATIŞ OTOMASYONU")
    pencere1.geometry("1250x750+300+0")
    framee = Frame(pencere1, width=250, height=750, bg="grey")
    framee.place(x=1000, y=0)
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    label1 = Label(pencere1, text="OYUNCAK ÜRÜNLERİ", font="italic 15")
    label1.pack()
    urun1()
    urun2()
    urun3()
    urun4()
    urun5()
    urun6()
    urun7()
    urun8()
    urun9()
    urun10()
    urun11()
    urun12()
    listbox = Listbox(pencere1, width=50, height=750)
    listbox.place(x=1000, y=0)

    def kapat():
        pencere1.destroy()
    geri=Button(pencere1,text="GERİ DÖN",font="italic 15",command=kapat)
    geri.place(x=800,y=650)

    def sepet():
        toplam_fiyat = fiyat1 + fiyat2 + fiyat3 + fiyat4 + fiyat5 + fiyat6 + fiyat7 + fiyat8 + fiyat9 + fiyat10 + fiyat11 + fiyat12
        items = []
        for i in range(listbox.size()):
            items.append(listbox.get(i))
        with open("sepet.txt", "a") as dosya:
            for item in items:
                dosya.write(item + "\n")
        with open("fiyat.txt", "a") as dosya:
            dosya.write(str(toplam_fiyat) + "\n")
        listbox.delete(0,END)
    def git():
        pencere1.destroy()
        def odeme():
            messagebox.showinfo("TEŞEKKÜRER","ÖDEMENİZ BAŞARI İLE GERÇEKLEŞMİŞTİR")
            with open("fiyat.txt", "w") as dosya:
                dosya.write("")
            with open("sepet.txt", "w") as dosya:
                dosya.write("")
            pencere2.destroy()
        pencere2 = Tk()
        pencere2.geometry("1200x750+300+0")
        pencere2.title("ÖDEME")
        liste = Listbox(pencere2, width=50, height=750)
        liste.place(x=0, y=0)        
        try:
            with open("sepet.txt", "r") as dosya:
                sepet = dosya.readlines()
                for urun in sepet:
                    liste.insert(END, urun.strip())
            print("Sepet başarıyla yüklendi.")
    

        except FileNotFoundError:
            print("Sepet dosyası bulunamadı.")   
        mevcut_toplam = 0

        # Dosyadaki mevcut değerleri topla
        try:
            with open("fiyat.txt", "r") as dosya:
                for satir in dosya:
                    try:
                        fiyat = float(satir.strip())  # Her satırı ondalık sayıya dönüştürür
                        mevcut_toplam += fiyat
                    except ValueError:
                        print("Geçersiz satır formatı:", satir)
        except FileNotFoundError:
            print("Dosya bulunamadı.")



        # Yeni toplam değeri
        toplam = 0  # Örnek bir yeni toplam değeri, isteğinize göre değiştirin

        # Yeni toplam değeri hesapla
        yeni_toplam = mevcut_toplam + toplam

        # Yeni toplam değerini dosyaya yaz
        with open("fiyat.txt", "a") as dosya:
            dosya.write(str(yeni_toplam) + "\n")



        lbl1=Label(pencere2,text="ÖDENECEK TUTAR:",font="italic 15")
        lbl1.place(x=700,y=100) 
        lbl1=Label(pencere2,text=yeni_toplam,font="italic 15")
        lbl1.place(x=900,y=100)
        lbtn=Button(pencere2,text="ÖDEME YAP",font="italic 15",command=odeme)
        lbtn.place(x=800,y=150)

        pencere2.mainloop()

    buton_ekle = Button(pencere1, text="  sepete ekle ", command=sepet)
    buton_ekle.place(x=1075, y=650)
    buton_onay = Button(pencere1, text=" sepeti onayla", command=git)
    buton_onay.place(x=1075, y=700)

    pencere1.mainloop()

