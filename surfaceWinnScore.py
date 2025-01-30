import matplotlib.pyplot as plt
import pandas as pd

# Veri setini okuma
data_path = "/Users/abdulkadiruygur/Desktop/python kodları/veri analizi/Veri Analizi Projeleri/tenis analiz 1(basit)/atp_tennis.csv"
data = pd.read_csv(data_path)

# DataFrame oluşturma
df = pd.DataFrame(data)

#Feder R. , Nadal R. , Djokovic N. , Murray A. , vs.

# Merak Ettiğiniz Oyuncunun kazandığı maçlar
winner_name = "Djokovic N."
player_data = df[df['Winner'] == winner_name]

#Biz bura da Surface yani belirtilen oyuncu en çok hangi saha da oyun kazanmış

# Bar grafiği çizme
plt.figure()  # Yeni bir figür oluşturuyoruz
player_data['Surface'].value_counts().plot(kind="barh", title=f"{winner_name} En Çok Kazandığı Sahalar (Bar)")


# Grafiği ekranda gösterme
plt.show()
