import matplotlib.pyplot as plt
import pandas as pd

data_path = "/Users/abdulkadiruygur/Desktop/python kodları/veri analizi/Veri Analizi Projeleri/tenis analiz 1(basit)/atp_tennis.csv"
data = pd.read_csv(data_path)

# Pandas ayarlarını tablo düzenini iyileştirmek için yapılandıralım
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.float_format", lambda x: f"{x:,.2f}")

#en çok maç kazanan 10 oyuncu

df = pd.DataFrame(data)
df['Winner'].value_counts().head(10).plot(kind="barh", title="En Çok Maç Kazanan Oyuncular")

plt.show()





