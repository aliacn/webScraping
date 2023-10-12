import requests
from bs4 import BeautifulSoup

# 8 adet URL'yi bir dizi içinde saklayın
urls = [
    "https://www.bloomberght.com/doviz/dolar",
    "https://www.bloomberght.com/doviz/euro",
    "https://www.bloomberght.com/altin/altin-ons",
    "https://www.bloomberght.com/emtia/gumus-ons",
    "https://www.bloomberght.com/emtia/platin",
    "https://www.bloomberght.com/emtia/bakir",
    "https://www.bloomberght.com/emtia/aliminyum",
    "https://www.bloomberght.com/emtia/brent-petrol"
]

for url in urls:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        h1_tag = soup.find('h1')

        if h1_tag:
            emtia_adi = h1_tag.text.strip()  # Emtia adını çekiyoruz
            fiyat = h1_tag.find('span', class_='LastPrice').text  # Fiyatı çekiyoruz
            degisim = h1_tag.find('span', class_='PercentChange').text  # Değişimi çekiyoruz
            tarih = h1_tag.find('span', class_='date').text  # Tarihi çekiyoruz

            print("Emtia Adı:", emtia_adi)
            print("Fiyat:", fiyat)
            print("Değişim:", degisim)
            print("Tarih:", tarih)
        else:
            print(f"H1 etiketi bulunamadı: {url}")
    else:
        print(f"Sayfa yüklenirken hata oluştu. HTTP Kodu: {response.status_code} - URL: {url}")
