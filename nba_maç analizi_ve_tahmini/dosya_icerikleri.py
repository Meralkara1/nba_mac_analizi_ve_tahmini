import pandas as pd

# Dosya adlarını değişkenlere kaydet
files = ["games_details.csv", "games.csv", "players.csv", "ranking.csv", "teams.csv"]

# Her dosyayı tek tek okuyup ilk birkaç satırı ve sütun isimlerini yazdır
for file in files:
    print(f"\n----- {file} -----")
    try:
        # CSV dosyasını oku
        data = pd.read_csv(file)
        
        # Dosya sütunlarını ve ilk birkaç satırı göster
        print("Sütunlar:")
        print(data.columns)
        print("\nİlk 5 Satır:")
        print(data.head())
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")
