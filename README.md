# Hamming Kodu Simülatörü

Hamming kodu ile ikili (binary) verinin nasıl kodlandığını, tek bit hata oluştuğunda hatanın nasıl bulunup düzeltildiğini gösteren, Python ve Tkinter ile yazılmış masaüstü simülatörü.

## Özellikler

- İkili veriyi Hamming koduyla kodlama (eşlik bitlerini otomatik hesaplar)
- İstenen konumdaki biti bozarak hata simülasyonu
- Bozuk veride hatalı biti bulma ve düzeltme
- Geçersiz girişlerde (binary olmayan veri, aralık dışı konum) uyarı mesajı

## Hamming Kodu Nasıl Çalışır?

Hamming kodunda eşlik (parity) bitleri, 2'nin kuvveti olan konumlara (1, 2, 4, 8, ...) yerleştirilir. Her eşlik biti, kendi kapsadığı konumlardaki bitlerin eşlik kontrolünü yapar. Çözme sırasında eşlik kontrollerinin hatalı çıkan konumları toplanır ve bu toplam, bozulan bitin konumunu doğrudan verir. Konum sıfırsa hata yoktur.

## Gereksinimler

- Python 3
- Tkinter (Python ile birlikte gelir, ek kurulum gerekmez)

## Çalıştırma

```bash
python mimari.py
```

## Kullanım

1. **Veriyi giriniz** alanına ikili bir veri yazın (ör. `1011`) ve **Encode** düğmesine basın.
2. **Hata Konumu** alanına bozulacak bitin konumunu yazın ve **Hatayı Simüle Et** düğmesine basın.
3. **Decode** düğmesine basarak hatanın bulunup düzeltildiğini görün.

## Örnek

| Adım | Değer |
|---|---|
| Girilen veri | `1011` |
| Kodlanmış veri (7 bit) | `0110011` |
| 5. bit bozulunca | `0110111` |
| Çözme sonucu | `1011` (hata 5. konumda tespit edilip düzeltilir) |

## Dosyalar

- `mimari.py`: Kodlama, çözme ve arayüz kodu