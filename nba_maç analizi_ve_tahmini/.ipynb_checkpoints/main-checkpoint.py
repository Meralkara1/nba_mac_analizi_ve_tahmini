import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# games.csv dosyasını oku
games = pd.read_csv("games.csv")

# Sütun isimlerini Türkçeleştirme
games.columns = [
    "Oyun_Günü", "Oyun_No", "Oyun_Durumu", "Ana_Takım_No", "Ziyaretci_Takım_No", 
    "Sezon", "Ana_Takım_No_Kopya", "Ana_Takım_Puan", "Ana_T_Saha_Gol_Yüzdesi", 
    "Ana_T_Serbest_Atış_Yüzdesi", "Ana_T_Üç_Sayı_Yüzdesi", "Ana_T_Assist", 
    "Ana_T_Saha_Gol_Ribaund", "Ziyaretci_Takım_No_Kopya", "Deplasman_Takım_Puan", 
    "Deplasman_Saha_Gol", "Deplasman_Serbest_Atış", "Deplasman_ÜçPuan", 
    "Deplasman_Assist", "Deplasman_Ribaund", "Ana_Takım_Kazanma"
]

# Eksik verilerin sayısını kontrol et
print(games.isnull().sum().sort_values(ascending=False))

# Eksik verilerin görselleştirilmesi
plt.figure(figsize=(12, 8))
sns.heatmap(games.isnull(), cbar=False, cmap="viridis")
plt.title("Eksik Verilerin Görselleştirilmesi", fontsize=16)
plt.xlabel("Sütunlar")
plt.ylabel("Satırlar")
plt.show()

# Sezonlara göre ev sahibi takımın maçı kazanma durumu
plt.figure(figsize=(12, 6))
games.groupby("Sezon")["Ana_Takım_Kazanma"].sum().sort_values(ascending=False).plot.bar(width=0.6, color="#87CEEB")

# Grafik başlıkları ve etiketleri
plt.title("Sezonlara Göre Ev Sahibi Takımın Galibiyet Sayıları", fontsize=16)
plt.xlabel("Sezon", fontsize=12)
plt.ylabel("Galibiyet Sayısı", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Grafiği göster
plt.tight_layout()
plt.show()


# Puan Kıyaslama Fonksiyonu
def Puan_Kıyasla(puan):
    if pd.isnull(puan):  # Eğer puan eksikse
        return "Bilinmiyor"
    elif puan >= 120:
        return "Harika Puan"
    elif 50 <= puan < 120:
        return "İyi Puan"
    else:
        return "Yeterince İyi Değil"

# Yeni sütunu oluştur
games["Puan_Durumu"] = games["Ana_Takım_Puan"].apply(Puan_Kıyasla)

# Kategorilerin sayısını ve grafiğini görselleştirme
plt.figure(figsize=(8, 5))
games["Puan_Durumu"].value_counts().plot.bar(
    width=0.8, color="#8A2BE2", label="Puan Durumu"
)

# Grafik başlıkları ve etiketler
plt.title("Ana Takım Puan Durumu Dağılımı", fontsize=14)
plt.xlabel("Puan Durumu", fontsize=12)
plt.ylabel("Sayı", fontsize=12)
plt.legend()
plt.xticks(rotation=0)

# Grafiği göster
plt.tight_layout()
plt.show()


# Genel kazanma ve kaybetme durumlarını inceleme
genel_kazanc = games.groupby("Ana_Takım_Kazanma").size()
print(genel_kazanc)

# Görselleştirme
plt.figure(figsize=(8, 4))
genel_kazanc.plot.bar(
    width=0.5, color="#5F9EA0", title="Ev Sahibi Takımların Genel Kazanma Durumu"
)
plt.ylabel("Maç Sayısı")
plt.xlabel("0 = Kaybetti, 1 = Kazandı")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()

# Takım bazında kazanma ve kaybetme sayıları
takim_bazinda_kazanc = games.groupby(["Ana_Takım_No"])["Ana_Takım_Kazanma"].value_counts()
print(takim_bazinda_kazanc)

# Görselleştirme
plt.figure(figsize=(20, 10))
takim_bazinda_kazanc.unstack().plot(
    kind="bar", stacked=True, color=["#FF6F61", "#6B8E23"], width=0.7, figsize=(20, 8)
)

# Grafik başlıkları ve etiketler
plt.title("Takım Bazında Ev Sahibi Maç Kazanma ve Kaybetme Durumu", fontsize=16)
plt.xlabel("Takım No", fontsize=12)
plt.ylabel("Maç Sayısı", fontsize=12)
plt.legend(["Kaybetti (0)", "Kazandı (1)"], title="Durum", loc="upper right")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



# Kazanan ve kaybeden grupların oluşturulması
grup = games.groupby('Ana_Takım_Kazanma')
kazanma_durumu = grup.get_group(1)  # Kazanan oyunlar

# Ortalama hesaplama fonksiyonu
def ortalama_bul(grup, sütun):
    return grup[sütun].mean()

# İç saha ve deplasman için ortalamalar
İc_Saha = [
    ortalama_bul(kazanma_durumu, 'Ana_Takım_Puan'),
    ortalama_bul(kazanma_durumu, 'Ana_T_Assist'),
    ortalama_bul(kazanma_durumu, 'Ana_T_Saha_Gol_Ribaund')
]

Deplasman = [
    ortalama_bul(kazanma_durumu, 'Deplasman_Takım_Puan'),
    ortalama_bul(kazanma_durumu, 'Deplasman_Assist'),
    ortalama_bul(kazanma_durumu, 'Deplasman_Ribaund')
]

# Veriler ve görselleştirme
text = ['Puanlar', 'Asist', 'Rebaund']
text2 = np.arange(len(text))

plt.bar(text, İc_Saha, width=0.25, color='#4169E1', label='İç Sahada Kazanılan Oyunlar')
plt.bar(text2 + 0.25, Deplasman, width=0.25, color='#DC143C', label='Deplasmanda Kazanılan Oyunlar')

# Başlık ve etiketler
plt.title("İç Saha ve Deplasman Performansının Kıyaslanması", fontsize=14)
plt.ylabel("Ortalama Değerler", fontsize=12)
plt.xlabel("Kategoriler", fontsize=12)
plt.legend()
plt.tight_layout()
plt.show()

# Sezon bazında iç saha galibiyetleri
plt.figure(figsize=(12, 6))
plt.ylabel("Galibiyet Sayısı", fontsize=12)
games.groupby("Sezon")["Ana_Takım_Kazanma"].value_counts().sort_values(ascending=False).plot.bar(
    width=0.50, color="#87CEEB", title="Sezonlara Göre İç Sahada Galibiyet Sayısı"
)
plt.tight_layout()
plt.show()



# Tüm sayısal sütunlar için tanımlayıcı istatistikler
print(games.describe())

# Sadece kategorik sütunlar için tanımlayıcı istatistikler
print(games.describe(include='object'))



# Tarihlerde en çok maç oynanan günler
print(games["Oyun_Günü"].value_counts().head())

# Görselleştirme (İlk 10 tarih için)
games["Oyun_Günü"].value_counts().head(10).plot.bar(color="#8A2BE2", figsize=(10, 5))
plt.title("En Çok Maç Oynanan Günler", fontsize=14)
plt.ylabel("Maç Sayısı", fontsize=12)
plt.xlabel("Tarih", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# games_details.csv dosyasını oku
games_details = pd.read_csv("games_details.csv")

# Veri seti boyutunu kontrol et
print(f'Oyun dosyasında {games_details.shape[0]} satır ve {games_details.shape[1]} sütun bulunuyor.')

# Sütun isimlerini listele
print("Orijinal Sütun İsimleri:")
print(games_details.columns.tolist())

# Sütun isimlerini Türkçeleştirme
games_details.columns = [
    'Oyun_No', 'Takım_No', 'Takım_Kısaltması', 'Oynanan_Şehir', 
    'Oyuncu_No', 'Oyuncu_İsmi', 'Oyuncu_Pozisyonu', 'Başlangıç_Pozisyonu', 
    'Yorum', 'Oynanan_Dakika', 'Saha_Gol_Dk', 'Saha_Hedef', 
    'Alan_Hedef', 'Saha_Üç_Sayı_Yüzdesi', 'Denenen_Üç_Sayılık_Yüzdesi', 
    'Üç_Sayılık_Yüzdesi', 'Yapılan_Serbest_Atış', 'Serbest_Atış_Denemesi', 
    'Serbest_Atış_Yüzdesi', 'Hücüm_Ribaundları', 'Savunma_Ribaundları', 
    'Ribaund', 'Asist', 'Yıldızı_Parlayan', 'Engellenen_Cekimler', 
    'Devir', 'Kişisel_Faul', 'Oyuncu_Puan', 'Artı_Eksi'
]

print("Türkçeleştirilmiş Sütun İsimleri:")
print(games_details.columns.tolist())

# Veri seti hakkında genel bilgi
print("\nVeri Seti Genel Bilgileri:")
games_details.info()

# Eksik değerlerin sayısını kontrol et
missing_values = games_details.isnull().sum().sort_values(ascending=False)
print("\nEksik Değerlerin Sütunlara Göre Dağılımı:")
print(missing_values)

# Eksik verilerin görselleştirilmesi
plt.figure(figsize=(16, 12))  # Daha büyük bir grafik boyutu
sns.heatmap(games_details.isnull(), cbar=False, cmap='viridis', yticklabels=False)  # Y eksenindeki etiketleri gizledik
plt.title("Eksik Verilerin Görselleştirilmesi", fontsize=18, fontweight='bold')  # Başlığı büyüttük
plt.xlabel("Sütunlar", fontsize=14)  # X eksenini etiketledik
plt.xticks(rotation=45, ha='right', fontsize=12)  # X ekseni etiketlerini döndürdük ve hizaladık
plt.tight_layout()  # Düzeni optimize ettik
plt.show()


# X eksenindeki etiketleri döndürerek daha okunabilir hale getirme
plt.xticks(rotation=45, ha='right', fontsize=12)  # Etiketler 45 derece döndürüldü ve hizalama yapıldı
plt.yticks(fontsize=12)  # Y eksenindeki etiketlerin boyutu artırıldı
plt.tight_layout()  # Grafik düzenini optimize etme
plt.show()

# Eksik veri işleme: 'Oyuncu_Pozisyonu' sütunundaki eksik verileri "Yedek" olarak doldur
games_details['Oyuncu_Pozisyonu'].fillna('Yedek', inplace=True)

# Sadece sayısal sütunlardaki eksik verileri sütunların ortalama değeriyle doldur
games_details.fillna(games_details.select_dtypes(include=['float64', 'int64']).mean(), inplace=True)

# Eksik veri işleme sonrası kontrol
print("\nEksik Değerlerin İşlemden Sonraki Durumu:")
print(games_details.isnull().sum())

# Temel istatistiksel özet
print("\nSayısal Sütunların Tanımlayıcı İstatistikleri:")
print(games_details.describe())

print("\nKategorik Sütunların Tanımlayıcı İstatistikleri:")
print(games_details.describe(include='object'))

# Eksik verilerin işlenmiş haliyle yeni bir CSV dosyası kaydetmek için
games_details.to_csv("games_details_cleaned.csv", index=False)
print("\nEksik veriler işlenmiş ve 'games_details_cleaned.csv' olarak kaydedilmiştir.")

# Takım Kısaltmasına Göre Maksimum Faul Değerleri
max_fouls = games_details.groupby("Takım_Kısaltması").agg({"Kişisel_Faul": "max"})

# Maksimum faul değerlerini yazdır
print(max_fouls)

# Grafiğin oluşturulması
plt.figure(figsize=(12, 6))
max_fouls["Kişisel_Faul"].value_counts().plot.bar(
    width=0.5, color="#F57C02", edgecolor="black"
)

# Grafik başlık ve etiketleri
plt.title("Takım Kısaltmasına Göre Maksimum Fauller", fontsize=14, fontweight="bold")
plt.ylabel("Takım Sayısı", fontsize=12)
plt.xlabel("Maksimum Faul Değeri", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()

# Grafiği göster
plt.show()


# Maçların oynandığı şehirlerin listesi
print("Oynanan Şehirler:")
print(games_details["Oynanan_Şehir"].unique())

# Maçlarda oynayan basketbolcuların isimleri
print("\nBasketbolcular:")
print(games_details["Oyuncu_İsmi"].unique())

# Şehir Bazında Oyuncu Puanlarının Görselleştirilmesi
plt.figure(figsize=(12, 6))
games_details.groupby("Oynanan_Şehir")["Oyuncu_Puan"].sum().plot.bar(color="#87CEEB", width=0.5)
plt.title("Şehir Bazında Oyuncu Puanları", fontsize=14, fontweight="bold")
plt.ylabel("Toplam Oyuncu Puanı", fontsize=12)
plt.xlabel("Şehirler", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Players.csv Dosyasının Analizi
players = pd.read_csv("players.csv")
players.columns = ["Oyuncu_İsmi", "Takım_No", "Oyuncu_No", "Sezon"]

print(f"\nPlayers Dosyasındaki Satır ve Sütun Sayısı: {players.shape}")
players.info()

# Players İçerisindeki Benzersiz Oyuncuların Listesi
print("\nPlayers Dosyasındaki Oyuncular:")
print(players["Oyuncu_İsmi"].unique())

# Ranking.csv Dosyasının Analizi
ranking = pd.read_csv("ranking.csv")
ranking.columns = [
    "Takım_No", "Lig_No", "Sezon_No", "Puan_Tarihi", "Konferans", "Takım",
    "Sezonda_Oynanan_Maç", "Sezonda_Kazanılan_Maç", "Sezonda_Kaybedilen_Maç",
    "Kazanç", "Ev_Rekoru", "Yol_Rekoru", "Oyuna_Dönüş"
]

print(f"\nRanking Dosyasındaki Satır ve Sütun Sayısı: {ranking.shape}")
ranking.info()

# Konferans Bazında Kazanç Oranı Görselleştirme
plt.figure(figsize=(12, 6))
ranking.groupby("Konferans")["Kazanç"].mean().plot.bar(color="#F57C02", width=0.5)
plt.title("Konferans Bazında Ortalama Kazanç Oranı", fontsize=14, fontweight="bold")
plt.ylabel("Ortalama Kazanç Oranı", fontsize=12)
plt.xlabel("Konferans", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Takım Kısaltmasına Göre Maksimum Faullerin Görselleştirilmesi
max_fouls = games_details.groupby("Takım_Kısaltması").agg({"Kişisel_Faul": "max"})
plt.figure(figsize=(12, 6))
max_fouls["Kişisel_Faul"].plot.bar(color="#6A5ACD", width=0.5)
plt.title("Takım Kısaltmasına Göre Maksimum Fauller", fontsize=14, fontweight="bold")
plt.ylabel("Maksimum Faul Değeri", fontsize=12)
plt.xlabel("Takım Kısaltması", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Players ve Ranking Dosyalarının Birleştirilmesi (Gerekirse)
merged_data = pd.merge(players, ranking, how="inner", on="Takım_No")
print("\nBirleştirilmiş Verinin İlk 5 Satırı:")
print(merged_data.head())


# Teams.csv Dosyasının Yüklenmesi ve İncelenmesi
teams = pd.read_csv("teams.csv")

# Sütun İsimlerini Türkçeleştirme
teams.columns = [
    "Lig_No", "Takım_No", "Min_Şampiyonluk_Yılı", "Max_Şampiyonluk_Yılı", 
    "Kısaltma", "Takma_Ad", "Kuruluş_Yılı", "Ana_Şehir", "Arena", 
    "Arena_Büyüklüğü", "Takım_Sahibi", "Takım_Genel_Müdür", 
    "Baş_Antrenör", "Lig"
]

# Teams Dosyasının Genel Özellikleri
print(f"Teams dosyasında {teams.shape[0]} satır ve {teams.shape[1]} sütun bulunuyor.")
teams.info()

# Teams Dosyasının İlk 5 Satırı
print("\nTeams Dosyasının İlk 5 Satırı:")
print(teams.head())

# Şehir Bazlı Takım Kazanma Oranının Analizi
games = pd.read_csv("games.csv")
games_details = pd.read_csv("games_details.csv")

# Sütun İsimlerini Türkçeleştirme
games.columns = [
    "Oyun_Günü", "Oyun_No", "Oyun_Durumu", "Ana_Takım_No", 
    "Ziyaretci_Takım_No", "Sezon", "Ana_Takım_No_Kopya", 
    "Ana_Takım_Puan", "Ana_T_Saha_Gol_Yüzdesi", 
    "Ana_T_Serbest_Atış_Yüzdesi", "Ana_T_Üç_Sayı_Yüzdesi", 
    "Ana_T_Assist", "Ana_T_Saha_Gol_Ribaund", 
    "Ziyaretci_Takım_No_Kopya", "Deplasman_Takım_Puan", 
    "Deplasman_Saha_Gol", "Deplasman_Serbest_Atış", 
    "Deplasman_ÜçPuan", "Deplasman_Assist", "Deplasman_Ribaund", 
    "Ana_Takım_Kazanma"
]

games_details.columns = [
    "Oyun_No", "Takım_No", "Takım_Kısaltması", "Oynanan_Şehir", 
    "Oyuncu_No", "Oyuncu_İsmi", "Oyuncu_Pozisyonu", "Başlangıç_Pozisyonu",
    "Yorum", "Oynanan_Dakika", "Saha_Gol_Dk", "Saha_Hedef", 
    "Alan_Hedef", "Saha_Üç_Sayı_Yüzdesi", "Denenen_Üç_Sayılık_Yüzdesi", 
    "Üç_Sayılık_Yüzdesi", "Yapılan_Serbest_Atış", "Serbest_Atış_Denemesi", 
    "Serbest_Atış_Yüzdesi", "Hücüm_Ribaundları", "Savunma_Ribaundları", 
    "Ribaund", "Asist", "Yıldızı_Parlayan", "Engellenen_Cekimler", 
    "Devir", "Kişisel_Faul", "Oyuncu_Puan", "Artı_Eksi"
]

# Verilerin Birleştirilmesi
merged_df = pd.merge(games, games_details, how="outer", on="Oyun_No")

# Şehir Bazında Takımın Kazanma Oranı
plt.figure(figsize=(20, 10))
merged_df.groupby("Oynanan_Şehir")["Ana_Takım_Kazanma"].value_counts().unstack().plot(
    kind="bar", stacked=True, color=["#87CEEB", "#FF6F61"], figsize=(20, 10), width=0.7
)

# Grafik Etiketleme
plt.title("Şehir Bazında Takım Kazanma ve Kaybetme Oranları", fontsize=16, fontweight="bold")
plt.xlabel("Oynanan Şehir", fontsize=14)
plt.ylabel("Maç Sayısı", fontsize=14)
plt.legend(["Kaybetti (0)", "Kazandı (1)"], title="Kazanan Durum", loc="upper right")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sonuçların Yorumu
print("\nGrafik Yorumu:")
print("Los Angeles'ta oynanan maçlarda ev sahibi takımların daha fazla galibiyet aldığı görülmektedir.")
print("En az kazanan şehir ise 'New Orleans/Oklahoma City' olmuştur.")
