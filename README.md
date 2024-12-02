# NBA Maç Analizi ve Tahmini

Bu proje, **NBA maç verilerinin analizi**, görselleştirilmesi ve **makine öğrenmesi teknikleriyle tahminleme** yapılmasını içermektedir. Python ve popüler veri analitiği kütüphaneleri kullanılarak hem görsel hem de istatistiksel bir yaklaşım sunulmuştur.

---

## 🚀 Projenin Amaçları
- NBA maçlarının **istatistiksel analizi** ve görselleştirilmesi.
- **Eksik verilerin tespiti** ve işlenmesi.
- Maç sonuçlarını tahmin edebilecek bir **makine öğrenmesi modeli** geliştirilmesi.

---



## 🛠️ Kullanılan Araçlar ve Kütüphaneler
- **Python**: Analiz ve modelleme için.
- **pandas**: Veri işleme ve analiz.
- **matplotlib & seaborn**: Görselleştirme.
- **scikit-learn**: Makine öğrenmesi algoritmaları.
- **Jupyter Notebook**: Çalışma ortamı.

---

## 📊 Yapılan Analizler ve Tahminler
1. **Veri Görselleştirme**:
   - Şehir bazında galibiyet/kayıp analizleri.
   - Sezonlara göre galibiyet trendleri.
2. **Makine Öğrenmesi**:
   - Logistic Regression modeliyle **ev sahibi takımın galibiyet tahmini**.
   - Model doğruluk oranı: **%78**.

---

## 📈 Elde Edilen Sonuçlar
- **Los Angeles**, ev sahibi takımların en fazla galibiyet aldığı şehir olarak öne çıkmıştır.
- Ev sahibi takımların galibiyet oranını tahmin etmek için geliştirilen **Logistic Regression modeli**, verilerde %78 doğruluk oranıyla başarılı bir performans sergilemiştir.

## 📂 Proje Yapısı
```plaintext
.
├── data/
│   ├── games.csv                 # Maç bilgileri
│   ├── games_details.csv         # Maç detayları
│   ├── players.csv               # Oyuncu bilgileri
│   ├── ranking.csv               # Takım sıralamaları
│   ├── teams.csv                 # Takım bilgileri
│   └── games_details_cleaned.csv # İşlenmiş maç detayları
├── notebooks/
│   └── nba_analysis.ipynb        # Jupyter Notebook dosyası
├── README.md                     # Proje açıklamaları
├── requirements.txt              # Kullanılan kütüphaneler
└── models/
    └── prediction_model.pkl      # Makine öğrenmesi modeli dosyası

---

