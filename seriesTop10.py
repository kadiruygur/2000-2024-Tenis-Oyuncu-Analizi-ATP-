import matplotlib.pyplot as plt
import pandas as pd

# Veri setini okuma
data_path = "/Users/abdulkadiruygur/Desktop/python kodları/veri analizi/Veri Analizi Projeleri/tenis analiz 1(basit)/atp_tennis.csv"
data = pd.read_csv(data_path)

# DataFrame oluşturma
df = pd.DataFrame(data)

# En çok maç kazanan 10 oyuncuyu bulma
top_10_players = df['Winner'].value_counts().head(10).index

# Bu 10 oyuncunun her birinin kazandığı seri türlerini sayma
# Bu örnekte 'Series' sütununun bulunduğu varsayılmaktadır. Eğer farklı bir isimse, uygun sütun adıyla değiştirmelisiniz.
seri_sayilari = pd.DataFrame()

for player in top_10_players:
    player_data = df[df['Winner'] == player]
    seri_sayilari[player] = player_data['Series'].value_counts()

# Grafiği çizme
seri_sayilari.plot(kind='barh', stacked=True, title="Top 10 Oyuncunun Kazandığı Seri Türleri")

# Grafiği ekranda gösterme
plt.show()
