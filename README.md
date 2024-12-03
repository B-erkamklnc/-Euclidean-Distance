# Coordinate Distance Finder

Coordinate Distance Finder, kullanıcıdan alınan 2D koordinatlar arasında minimum Öklit mesafeyi hesaplayan ve bu mesafeyi görselleştiren bir Python uygulamasıdır.

---

## Özellikler

- Kullanıcı dostu bir arayüz ile koordinat girişi.
- Öklit mesafelerini otomatik hesaplama.
- Minimum mesafeye sahip noktaların görselleştirilmesi.
- Dinamik hata kontrolü ile kullanıcı girişlerini doğrulama.

---

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. **Projeyi Klonlayın**  
   Terminalde aşağıdaki komutu çalıştırarak projeyi klonlayabilirsiniz:
   ```bash
   git clone https://github.com/B-erkamklnc/Euclidean-Distance.git
   ```

2. **Dizin Değiştirin**
   Klonlanan proje klasörüne gidin:
   ```bash
   cd coordinate-distance-finder
   ```

4. **Gerekli Kütüphaneleri Yükleyin**
    Uygulama için Python ve Matplotlib kütüphanesi gereklidir. Yüklemek için:
    ```bash
    pip install matplotlib
    ```

## Kullanım

Projeyi çalıştırmak için terminale aşağıdaki komutu girin:

```bash
python main.py
```

Program çalıştıktan sonra adımları takip ederek koordinatlarınızı girin. Program minimum Öklit mesafeyi hesaplayacak ve bir grafikle gösterecektir.

### Örnek Çalışma Akışı:

1. Kullanıcıdan kaç doğru parçası olduğu sorulur.
2. Her bir doğrunun koordinatları istenir.
3. Minimum mesafeye sahip noktalar belirlenir ve grafik çizilir.

## Proje Yapısı
`main.py:`
Uygulamanın ana çalışma dosyasıdır. Kullanıcı etkileşimini ve görselleştirmeyi içerir.

`distance_calculator.py:`
Koordinatlar arasındaki Öklit mesafesini hesaplayan ve diğer temel işlemleri sağlayan modüldür.



