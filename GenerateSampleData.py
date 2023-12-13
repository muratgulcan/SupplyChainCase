import pandas as pd
import numpy as np

# Parametreler
num_depolar = 5  # Toplam depo sayısı
num_urunler = 10  # Toplam ürün sayısı
max_envanter = 100  # Maksimum envanter seviyesi

# Rastgele depo isimleri oluştur
depolar = [f'Depo {i+1}' for i in range(num_depolar)]

# Rastgele ürün isimleri oluştur
urunler = [f'Ürün {i+1}' for i in range(num_urunler)]

# Rastgele envanter seviyeleri oluştur
envanterler = np.random.randint(0, max_envanter, size=(num_depolar, num_urunler))

# Veri setini DataFrame'e dönüştür
data = pd.DataFrame(envanterler, columns=urunler, index=depolar)

# Veri setini CSV dosyasına kaydet
data.to_csv('envanter_veri_seti.csv')

# Oluşturulan veri setini göster
print(data)
