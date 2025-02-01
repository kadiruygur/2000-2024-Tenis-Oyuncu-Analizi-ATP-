import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Kullanıcıdan oyuncu ismi alma
player_name = input("Oyuncu ismini girin (Örnek: Djokovic N., Nadal R.): ")

# CSV dosyasını yükleme (Dosyanın yolu kullanıcı tarafından belirtilmeli)
file_path = "/Users/abdulkadiruygur/Desktop/python kodları/veri analizi/Veri Analizi Projeleri/tenis analiz 1(basit)/atp_tennis.csv"
df = pd.read_csv(file_path)

# Oyuncunun maçlarını filtreleme
player_matches = df[(df["Player_1"] == player_name) | (df["Player_2"] == player_name)]

# Oyuncunun farklı zeminlerdeki istatistiklerini hesaplama
player_surface_stats = (
    player_matches.groupby("Surface")
    .apply(lambda x: pd.Series({
        "Total Matches": len(x),
        "Wins": (x["Winner"] == player_name).sum(),
        "Win Rate": (x["Winner"] == player_name).sum() / len(x) * 100
    }))
).reset_index()

# Görselleştirme
plt.figure(figsize=(8, 5))
sns.barplot(x="Surface", y="Win Rate", data=player_surface_stats, palette="viridis")
plt.xlabel("Court Surface")
plt.ylabel("Win Rate (%)")
plt.title(f"{player_name}'in Zemin Türlerine Göre Kazanma Oranları")
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
