import pandas as pd

"""!!AMAÇ : belirli bir fiyat aralığındaki ürünleri filtrelemek!!"""

"""                    1- VERI SETI OLUSTURUYORUZ"""


veri = {
        'Ürün': ['Bilgisayar', 'Klavye', 'Mouse', 'Monitör', 'Yazıcı'],
        'Fiyat': [3000, 150, 50, 700, 800],
        'Stok Adedi': [20, 50, 100, 10, 30],
        'Marka': ['HP', 'Logitech', 'Logitech', 'Samsung', 'Epson']
}
        

"""                    2- DATA FRAME OLUŞTURUYORUZ"""
urun_verisi = pd.DataFrame(veri)



 
"""                   3- VERİYİ MANİPÜLE EDİYORUZ"""


# Fiyatı 500 TL ile 1000 TL arasındaki ürünleri filtreleyelim

filtrelenmis_urunler = urun_verisi[(
    urun_verisi['Fiyat']>=500)& (urun_verisi['Fiyat']<=1000)]






print(filtrelenmis_urunler)


