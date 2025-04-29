# Uretim_Planlama
# Üretim Planlama Optimizasyonu

# Problem Tanımı:
Bir üretim hattında, n adet iş sırayla yapılmalıdır. Her iş, m farklı makinada işlenebilir. İşlerin makinelerdeki süreleri ve makineler arası geçiş maliyetleri farklılık gösterir.

# Proje Amacı:
İşleri sırayla işleyerek, **işleme süreleri + geçiş maliyetlerini** minimize eden üretim sırasını bulmak.Ve en kısa süreyi döndürmek.

# Kullanılan Yöntem: Dinamik Programlama  
Her iş ve makine için en iyi kararı önceki adıma bakarak veren bir DP (dinamik programlama) tablosu kullanılır. En iyi ihtimali bulmak için tüm olasılıklar değerlendirilir ve en düşük maliyetli seçenek seçilir.
Problemin, tüm olasılıkların değerlendirilip en iyi sonucun bulunması şeklinde çözülmesi; matris zinciri çarpımı problemine yapısal benzerlik gösterir ve benzer şekilde dinamik programlama ile çözülür.
# Kullanılan Araç:
Python,Visual Studio code
# Örnek Çıktı:
```python
is_sureleri = [
    [2, 10],
    [8, 16],
    [4, 6]
]

gecis_maliyetleri = [
    [1, 2],
    [5, 2]
]

![Ekran görüntüsü 2025-04-29 182730](https://github.com/user-attachments/assets/0461fe1d-6239-4fdb-bd39-0e37c4d1695f)

