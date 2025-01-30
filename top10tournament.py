import matplotlib.pyplot as plt
import pandas as pd

# Veri setini okuma
data_path = "/Users/abdulkadiruygur/Desktop/python kodları/veri analizi/Veri Analizi Projeleri/tenis analiz 1(basit)/atp_tennis.csv"
data = pd.read_csv(data_path)

# DataFrame oluşturma
df = pd.DataFrame(data)

# En çok maç kazanan 10 oyuncuyu bulma
top_10_players = df['Winner'].value_counts().head(10).index

# Bu 10 oyuncunun her birinin kazandığı turnıva türlerini sayma
# Bu örnekte 'Tournament' sütununun bulunduğu varsayılmaktadır. Eğer farklı bir isimse, uygun sütun adıyla değiştirmelisiniz.
turnuva_türü_sayilari = pd.DataFrame()


#Seçili Turnuvaları görmek istiyorsanız ;
"""
# Seçilen turnuva türlerini filtreleme (Wimbledon, Australian Open, US Open, French Open)
selected_tournaments = ['Wimbledon', 'Australian Open', 'US Open', 'French Open', 'Masters Cup']

for player in top_10_players:
    player_data = df[(df['Winner'] == player) & (df['Tournament'].isin(selected_tournaments))]
    turnuva_türü_sayilari[player] = player_data['Tournament'].value_counts()
"""

for player in top_10_players:
    player_data = df[df['Winner'] == player]
    turnuva_türü_sayilari[player] = player_data['Tournament'].value_counts()

# Grafiği çizme
turnuva_türü_sayilari.plot(kind='bar', stacked=True, title="Top 10 Oyuncunun Kazandığı Turnuva Türleri")

# Grafiği ekranda gösterme
plt.show()


