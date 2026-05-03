import matplotlib.pyplot as plt


def main():
    print("==================================================")
    print("      RequiemLaw - Fon Gün-Sonu Getiri Hesaplayıcı   ")
    print("==================================================")

    try:
        num_assets = int(input("Kaç adet varlık (hisse/fon) eklemek istiyorsunuz? : "))
    except ValueError:
        print("Hata: Lütfen geçerli bir sayı girin. (Örn: 9.99)")
        return

    assets = []
    weights = []
    returns = []
    total_weight = 0.0
    estimated_return = 0.0

    print("\nLütfen değerleri girerken küsuratlar için nokta (.) kullanın. Örn: 12.5")

    for i in range(num_assets):
        print(f"\n--- {i + 1}. Varlık ---")
        name = input("Varlık Adı (Örn: THYAO)              : ").upper()

        try:
            weight = float(input(f"{name} Portföy Ağırlığı (%)           : "))
            daily_return = float(input(f"{name} Bugünkü Kapanış Getirisi (%) : "))
        except ValueError:
            print("Hatalı veri girişi, lütfen sayı kullanın.")
            return

        assets.append(name)
        weights.append(weight)
        returns.append(daily_return)

        total_weight += weight

        # Fon getirisine katkı = (Ağırlık / 100) * Getiri
        estimated_return += (weight / 100) * daily_return

    # Eğer girilen varlıkların toplam ağırlığı %100'den azsa, geri kalanı "Diğer" olarak ekleyelim
    # Bu kısmın getirisini 0 olarak kabul ediyoruz (sadece grafikte düzgün görünmesi için)
    if total_weight < 100:
        kalan_agirlik = 100 - total_weight
        assets.append("Diğer (Bilinmeyen/Nakit/Ters-Repo/Teminatlar)")
        weights.append(kalan_agirlik)
        # Diğer kısmının getirisi hesaplamaya dahil edilmedi, tahmini minimum getiriyi buluyoruz.
        print(f"\nBilgi: Girdiğiniz ağırlıkların toplamı %{total_weight:.2f} yapıyor.")
        print(f"Geri kalan %{kalan_agirlik:.2f}'lik kısım hesaplamaya sıfır getiri olarak yansıtıldı.")
    elif total_weight > 100:
        print("\nUyarı: Girdiğiniz ağırlıkların toplamı %100'ü aştı! Lütfen verilerinizi kontrol edin.")

    print("\n==================================================")
    print(f"    GÜN SONU TAHMİNİ FON GETİRİSİ: % {estimated_return:.4f}")
    print("==================================================")

    # --- Grafik Çizimi ---
    # Karanlık tema (görselindeki gibi şık durması için)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(9, 6))

    # Renk paleti ayarı
    colors = plt.cm.tab20.colors

    # Pasta grafiğini oluşturma
    wedges, texts, autotexts = ax.pie(
        weights,
        labels=assets,
        autopct='%1.2f%%',  # Yüzdeleri virgülden sonra 2 basamak gösterir
        startangle=140,
        colors=colors,
        textprops=dict(color="white", fontsize=10),
        explode=[0.05 if i < num_assets else 0 for i in range(len(assets))]  # Girilen hisseleri hafif dışarı taşır
    )

    # Başlık
    ax.set_title("Fon Portföy Dağılımı", color='white', fontsize=16, fontweight='bold', pad=20)

    # Grafiği göster
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()