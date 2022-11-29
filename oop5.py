"""
Bir ilan sitesi uygulamasını simüle ediniz.
bir emlak adında sınıf oluşturunuz emlak sınıfına ait durumları yani
attr leri hayal gücünüze göre yaratınız.

ardından bir sonsuz döngü içerisinde kullanıcıdan veriş sorarak
emlak nesneleri yaratınız

Örneğin:

1- Emlak Ekle
2- Çıkış yap

şeklinde bir menüde bu sonsuz döngüyü kontrol altına alabilirsiniz


"""

class Emlak:
    def __init__(self,yas,yer,metrekare):
        self.yas = yas
        self.yer = yer
        self.metrekare = metrekare

while True:
    print("""
    1-Emlak Ekle
    0-Çıkış Yap
    """)

    secim = int(input("İşlem numaranızı giriniz: "))

    if secim == 0:
        print("Çıkış yaptınız")
        break

    if secim == 1:
        yas = int(input("yas giriniz: "))
        yer = input("Yer giriniz: ")
        metrekare = int(input("metrekare giriniz: "))
    else:
        print("Hatalı işlem yaptınıız")