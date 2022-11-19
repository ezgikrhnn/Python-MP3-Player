#BASIT MP3 CALAR:
'''
class sistemiyle bir mp3 calar yap.
'''

from random import choice # rastgele sarki sec icin en basa bu fonk. yazmaliyiz.

class MP3Calar():
    def __init__(self, sarkiListesi = []): # init fonksiyonu neydi-- bir objemi turettigim zaman calisan fonksiyondu. 
        self.suanCalanSarki = ""
        self.ses = 100
        self.sarkiListesi = sarkiListesi
        self.durum = True # true degeri atiyorum cunku burada bir while dongusu yazacagim.
        

    def sarkiSec(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{}){}".format(sayac,sarki))
            sayac += 1
            secilenSarki = int(input("secmek istediginiz sarkinin numarasini giriniz: "))

        while secilenSarki < 1 or secilenSarki > len(self.sarkiListesi):
            secilenSarki = int(input("secmek istediginiz sarkinin dogru numarasini giriniz: (1-{}) ".format(self.sarkiListesi)))

        self.suanCalanSarki = self.sarkiListesi[secilenSarki-1]

    
    def sesArttir(self):
        if self.ses == 100: #eger ses duzeyi 100 ise hicbir sey yapmasin yani pass cunku zaten en yuksek ses duzeyi 100
            pass
        else:
            self.ses += 10 #degilse 10 arttirsin


    def sesAzalt(self):
        if self.ses == 0:  #eger ses duzeyi 0 ise hicbir sey yapmasin  yani pass cunku zaten en ydusuk ses duzeyi 0
            pass
        else:
            self.ses -= 10  #degilse 10 azaltsin.


    def rastgeleSarkiSec(self):
        rastgeleSarkiSec = choice(self.sarkiListesi)
        self.suanCalanSarki = rastgeleSarkiSec


    def sarkiEkle(self):  # sarki secebilmemiz icin once eklememiz lazim.
        sanatci = input("sanatciyi giriniz:")
        sarki = input("sarkiyi giriniz: ") # ve kullanici buna göre bir sarki girecek ve girilen sarkiyi sarki listeme eklemem gerekiyor.
 
        self.sarkiListesi.append(sanatci + "-" + sarki) # diyerek buradaki liste objeme bir str objesi ekleyecegim.
        
        
    def sarkiSil(self):
        sayac = 1
        for sarki in self.sarkiListesi:
            print("{}) {}".format(sayac,sarki))
            sayac += 1  # ilk degere sayaci ikinci degere sarkiyi gonderiyorum daha sonra sayaci bi arttiriyorum.

            silinecekSarki = int(input("silmek istediginiz sarkinin numarasini giriniz: "))
            
        while silinecekSarki < 1 or silinecekSarki > len(self.sarkiListesi):
            silinecekSarki = int(input("silmek istediginiz sarkinin DOGRU numarasini giriniz: "))
            
            self.sarkiListesi.pop[silinecekSarki - 1] # paranteze bir index degeri girmemiz gerekiyor bos birakirsak en sondakini cikartir.
            # index numarasi sifirdan basladigi icin -1 yaptik

        
    def kapa(self):
        self.durum = False

    def menuGoster(self):
       print("""
       ** Ezgi Karahan MP3 Calar a HOsgeldiniz **
       Sarki Listesi : {}
       Suan Calan Sarki = {}
       Ses Duzeyi : {}
       
       1) sarki sec
       2) ses arttir
       3) ses azalt
       4) rastgele sarki sec
       5) sarki ekle
       6) sarki sil
       7) kapa
       """.format(self.sarkiListesi, self.suanCalanSarki, self.ses))



    def secim(self):
        sec = int(input("seciminizi giriniz: "))
        
        while sec < 1 or sec > 7:
            sec = int(input("sectiginiz deger yanlıs. lutfen belirtilen aralikta deger giriniz: "))
        
        return sec # eger dogru degilse yani 1 2 3 4 5 6 7 ise secim yap

    
    def calistir(self):
        self.menuGoster()
        secim = self.secim()  


        if secim == 1 :
           self.sarkiSec()
        if secim == 2:
           self.sesArttir()
        if secim == 3:
           self.sesAzalt
        if secim == 4:
           self.rastgeleSarkiSec()
        if secim == 5: 
           self.sarkiEkle()
        if secim == 6:
           self.sarkiSil()
        if secim == 7:
           self.kapa()

mp3calar = MP3Calar()
while mp3calar.durum: # dogru true oldugu surece buradaki while dongusu calissin. false olacagi icin sonlanacak
      mp3calar.calistir()

print("program sonlandi") # 7 bastigimda program sonlandı yapar cunku yukaridaki while dongusu yanlistir program sonlanir.

