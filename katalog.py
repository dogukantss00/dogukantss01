from tkinter import *
import sys
sys.path.append("/home/kali/Desktop/KODLAR/MARKET_SATİS_OTOMATİ/urunler/")
from cerez import buton1
from temizlik import buton2
from elektronik import buton3
from dondurulmus import buton4
from et import buton5
from gida import buton6
from icecek import buton7
from kisisel import buton8
from kozmetik import buton9
from meyve import buton10
from oyuncak import buton11
from sut import buton12
def katalogg():
    pencere4=Tk()
    pencere4.title("MARKET SATIŞ OTOMASYONU")
    pencere4.geometry("1200x750+300+0")
    def kozmetikk():
        buton9()
    def kisisell():
        buton8()
    def oyuncakk():
        buton11()
    def meyvee():
        buton10()
    def temizlikk():
        buton2()
    def gidaa():
        buton6()
    def cerezz():
        buton1()
    def icecekk():
        buton7()
    def ett():
        buton5()
    def dondurulmuss():
        buton4()
    def sutt():
        buton12()
    def elektronikk():
        buton3()

    def frame():
        frame1=Frame(pencere4,bg="white",width=350,height=250)
        frame1.place(x=0,y=0)
        frame1=Frame(pencere4,bg="black",width=350,height=250)
        frame1.place(x=300,y=0)
        frame1=Frame(pencere4,bg="white",width=350,height=250)
        frame1.place(x=600,y=0)
        frame1=Frame(pencere4,bg="black",width=350,height=250)
        frame1.place(x=900,y=0)
        frame1=Frame(pencere4,bg="black",width=350,height=250)
        frame1.place(x=0,y=250)
        frame1=Frame(pencere4,bg="white",width=350,height=250)
        frame1.place(x=300,y=250)
        frame1=Frame(pencere4,bg="black",width=350,height=250)
        frame1.place(x=600,y=250)
        frame1=Frame(pencere4,bg="white",width=350,height=250)
        frame1.place(x=900,y=250)
        frame1=Frame(pencere4,bg="white",width=350,height=250)
        frame1.place(x=0,y=500)
        frame1=Frame(pencere4,bg="black",width=350,height=250)
        frame1.place(x=300,y=500)
        frame1=Frame(pencere4,bg="white",width=350,height=250)
        frame1.place(x=600,y=500)
        frame1=Frame(pencere4,bg="black",width=350,height=250)
        frame1.place(x=900,y=500)
    def buton():
        buton1=Button(pencere4,text="KOZMETİK REYONU",command=kozmetikk)
        buton1.place(x=75,y=85)
        buton1=Button(pencere4,text="KİŞİSEL BAKIM REYONU",command=kisisell)
        buton1.place(x=375,y=85)
        buton1=Button(pencere4,text="OYUNCAK REYONU",command=oyuncakk)
        buton1.place(x=675,y=85)
        buton1=Button(pencere4,text="MEYVE & SEBZE REYONU",command=meyvee)
        buton1.place(x=975,y=85)
        buton1=Button(pencere4,text="TEMİZLİK REYONU",command=temizlikk)
        buton1.place(x=75,y=335)
        buton1=Button(pencere4,text="CEREZ REYONU",command=cerezz)
        buton1.place(x=375,y=335)
        buton1=Button(pencere4,text="GIDA REYONU",command=gidaa)
        buton1.place(x=675,y=335)
        buton1=Button(pencere4,text="İCECEK REYONU",command=icecekk)
        buton1.place(x=975,y=335)
        buton1=Button(pencere4,text="ET & BALIK REYONU",command=ett)
        buton1.place(x=75,y=585)
        buton1=Button(pencere4,text="DONDURULMUS GIDA REYONU",command=dondurulmuss)
        buton1.place(x=350,y=585)
        buton1=Button(pencere4,text="SÜT VE SÜT ÜRÜNLERİ REYONU",command=sutt)
        buton1.place(x=650,y=585)
        buton1=Button(pencere4,text="ELEKTRONİK REYONU",command=elektronikk)
        buton1.place(x=975,y=585)
        
    frame()
    buton()




    pencere4.mainloop()