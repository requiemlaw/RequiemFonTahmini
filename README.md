# 📈 RequiemLaw. - Fon Getiri Tahmin Modülü

Bu modül, yatırım fonlarının gün sonu (karanlık oda çıkışı) verilerini kullanarak, resmi fiyatlar açıklanmadan önce **tahmini fon getirisini** hesaplamak ve portföy dağılımını görselleştirmek için geliştirilmiştir.

## 📸 Analiz ve Görselleştirme

Program çalıştırıldığında girilen verileri işler ve gün sonu tahminine ek olarak aşağıdaki gibi fon portföyünü yansıtan kapsamlı bir döküm sunar:

<p align="center">
  <img src="https://github.com/requiemlaw/RequiemFonTahmini/blob/12655107970df4d0272870f79390a3d7d26608e8/ReqFonTahmin.PNG" width="100%" alt="Fon Dağılım Grafiği">
</p>

---

### 🖥️ Veri Girişi ve İşlem Kayıtları
Hisse bazlı veri giriş süreci ve hesaplanan tahmini getiri sonucuna ait python terminal görüntüleri:

<p align="center">
  <img src="https://github.com/requiemlaw/RequiemFonTahmini/blob/12655107970df4d0272870f79390a3d7d26608e8/.idea/inspectionProfiles/ReqFonTahmin2.PNG" width="48%" />
  <img src="https://github.com/requiemlaw/RequiemFonTahmini/blob/12655107970df4d0272870f79390a3d7d26608e8/.idea/inspectionProfiles/ReqFonTahmin1.PNG" width="48%" />
</p>

## 🚀 Özellikler
- **Dinamik Veri Girişi:** Portföydeki varlık sayısı ve isimlerine göre özelleştirilebilir giriş ekranı.
- **Ağırlıklı Getiri Hesaplama:** Varlıkların portföy içindeki ağırlığına göre net getiri katkısını hesaplar.
- **Otomatik Portföy Tamamlama:** Eksik kalan ağırlıkları otomatik olarak "Diğer" kategorisinde toplar.
- **Görsel Analiz:** Matplotlib kullanarak karanlık tema ile uyumlu yüksek çözünürlüklü pasta grafiği oluşturur.

## 🛠️ Kurulum
Projenin çalışması için gerekli kütüphaneyi terminalden kurabilirsiniz:
```bash
pip install matplotlib
```
Python terminale programı çalıştırmak için sağlamanız gereken veri girişi:
```bash
python main.py
```
## Lisans
Copyright © 2026 RequiemLaw. Tüm hakları saklıdır. Bu yazılım "Requiem Terminal" ekosisteminin bir parçasıdır.
