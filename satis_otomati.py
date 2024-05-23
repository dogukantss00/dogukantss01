from tkinter import *
from  yeni_kullanici import yeni_kullanicii
from kullanici_girisi import giriss
def yeni_user():
    yeni_kullanicii()
pencere1=Tk()
pencere1.title("MARKET SATIŞ OTOMASYONU")
pencere1.geometry("1250x750+300+0")

def giris():
    pencere1.destroy()
    giriss()

frame1=Frame(pencere1,bg="white",width=620,height=750)
frame1.place(x=0,y=0)
frame1=Frame(pencere1,bg="black",width=630,height=750)
frame1.place(x=625,y=0)

label1=Label(pencere1,text="MARKETİMİZE HOŞGELDİNİZ",font="italic 25")
label1.pack()
buton1=Button(pencere1,text="YENİ KULLANICI OLUŞTUR",width=25,height=10,bg="black",command=yeni_user,fg="white")
buton1.place(x=200,y=100)
buton2=Button(pencere1,text="GİRİŞ YAP",width=25,height=10,bg="white",command=giris)
buton2.place(x=800,y=100)




pencere1.mainloop()