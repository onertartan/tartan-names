# p_konum_plus — D-11 r1 Ek-1 (r1): Değer aktarımı kuralı — PI yönetişim kaydı — 2026-10-08

> D-11 r1'in (`p_konum_plus_lightweight_review_policy_r1_2026-10-04.md`, `0b177ee4…`) ekidir. D-11 r1'in metni
> değişmez; bu ek onun yanında okunur. **PI'nın 2026-10-08 tarihli onayıyla imzalı son metindir (§6).** İçine kendi
> hash'i yazılmaz; hash'i ayrı bir `.sha256` dosyasında durur.

```text
record              = p_konum_plus_lightweight_review_policy_r1_addendum1_r1_2026-10-08.md   (D-11 r1 Ek-1, r1)
supersedes          = p_konum_plus_lightweight_review_policy_r1_addendum1_2026-10-08.md
                      ddd683998e02d6690123dde491638e3c6789a7874eadd12e23f1ff289dbe8ffd (hiçbir yere yerleştirilmedi; değişiklik §8)
record_class        = PI-owned yönetişim kaydı; D-11 r1'e ek
status              = SIGNED (PI onayı, 2026-10-08; §6)
parent              = p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
                      0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639 (D-11 r1; değişmedi)
basis               = rp1-r1 transmission list satır 37: bir hash'in son 48 hanesi 16 haneli bir ekran çıktısından
                      uydurularak tamamlandı ve "OBSERVED" diye yazıldı (yürütücü ifşa notu
                      pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md, c446395e497bb42baa179d9c756c8b2664ea92ebbe6f80b064c5bb8ba6d63444;
                      düzeltilmiş liste r1 98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956, commit 9035df0)
prepared_by         = Claude (Claude Code bulut oturumu); D-11 r1'i de bu oturum hazırladı
what_this_record_is_not = bilimsel bir karar, eşik ya da literal değil; D-11 r1'in sınıflarını, döngü sınırlarını ya da
                      STOP kurallarını değiştirmez; geriye uygulanmaz
```

## 1. Kural

1. **Hesaplama ya da ölçüm sonucu** olarak bildirilen hash, sayı, durum değeri, zaman damgası ve sürüm bilgisi,
   ilgili dosya baytlarından ya da komut/harness çıktısından **makineyle aktarılır**: betikle yazılır ya da tam
   çıktıdan kopyalanır. Bellekten, bağlamdan ya da tahminle yazılmaz.
   PI kararları, denetçi hükümleri ve tarihsel kayıt bilgileri (ör. bir onayın tarihi ve metni) komut
   çıktısından türetilmez: kaynakları ve rolleri açıkça belirtilerek aktarılır; yeni bir karar ya da hüküm,
   yetkili kişi tarafından gerekçesiyle yazılır.
   Hiçbir değer uydurulmaz ya da gözlenmediği hâlde gözlenmiş gibi sunulmaz.
2. Kısaltılmış bir gösterim (ör. 16 haneli önek) tam değerin kaynağı değildir. Önek yalnız önek olarak yazılır
   (`ebc28df8…`) ve tam değer gibi kullanılmaz.
3. Elde olmayan bir değer **`NOT OBSERVED`** diye, nedeniyle yazılır; tamamlanmaz, tahmin edilmez. Tahmin
   gerekiyorsa `ESTIMATE` etiketi ve yöntemi yazılır.
4. Hash listeleri (transmission list, raporun hash bloğu, başlangıç envanteri) yazım anında baytlardan **betikle**
   üretilir. Belge, onu üreten komutu ya da betiği adıyla anar.

## 2. Kimlere uygulanır

Yürütücü, taslakçı ve denetçi: teslim belgesi, PI kaydı ya da denetim kaydı yazan her oturum.

## 3. Denetimde

- D-11 r1 §4 madde 1'e (hash ve custody) şu kontrol eklenir: belgelere yazılmış değerler baytlara ya da komut
  çıktısına izlenebilir. İzlenemeyen değer bulgudur.
- Gözlenmemiş bir değeri gözlenmiş gibi yazmak bulgudur. Sınıfını denetçi D-11 r1 §5'e göre gerekçesiyle yazar;
  PI kesinleştirir.

## 4. Yürürlük

- İmzayla yürürlüğe girer. Bundan sonra dispatch edilen her paket ve yazılan her kayıt için geçerlidir.
- Geriye uygulanmaz. rp1-r1'in denetimi bu konuyu zaten kendi talimatının §1.5 maddesiyle kapsar
  (F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md,
  82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e).
- Sonraki her talimatın D-11 r1 §8 bloğundaki "korunan zorunlu kontroller" satırı bu eke atıf yapar.

## 5. Yürütücüye

```text
Bu kayıt imzalı olarak elinize ulaştığında:
  1. Kaydı ayrı .sha256 sidecar'ıyla, adını değiştirmeden p_konum_plus/prompts/ altına koyun; kendi hash'ini
     içine yazmayın. Hash'i sidecar'a ve PI'nın iletim mesajındaki değere karşı yeniden hesaplayın; eşit değilse
     durun ve PI'ya bildirin
  2. Başka hiçbir dosya yazmayın, değiştirmeyin, taşımayın, silmeyin
  3. Gerçek veri okumayın; commit yalnız PI'nın ayrı talimatıyla
```

## 6. İmza

```text
PI                    = Öner
imza / onay           = ONAYLANDI. PI'nın 2026-10-08 tarihli mesajı, aynen:
                        «D-11 r1'e ek olarak hazırla, imzayı da onaylıyorum.»
                        Kural, PI'ya 2026-10-08'de önerilen metindir ("Yürütücünün yazdığı her hash, sayı ve durum
                        değeri komut çıktısından makineyle aktarılır; elde olmayan değer NOT OBSERVED yazılır,
                        tamamlanmaz"); §1–§4 onu uygular. PI onayı metin görülmeden önce verildi; §1 madde 1 bir
                        dış incelemeyle sonradan daraltıldı (§8). PI'nın bu son metni yürütücüye iletmesi, metni
                        benimsemesidir
date_time_local       = 2026-10-08, UTC+3
```

## 7. Hash'ler (bu oturumda hesaplandı; komut ve çıktı)

```text
$ git ls-remote origin refs/heads/p_konum_plus
9035df0831d8646cca7f1e73937161a3d2d7d018	refs/heads/p_konum_plus
$ git show origin/p_konum_plus:p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md | sha256sum
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  -
$ sha256sum <9035df0 archive>/p_konum_plus/provenance/pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md <…>/f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md
c446395e497bb42baa179d9c756c8b2664ea92ebbe6f80b064c5bb8ba6d63444  pkp_rp1-r1_yurutucu_ifsa_notu_2026-10-08.md
98ed374d215da69561a6e4e6b03b49e52c6792d8cec05ee89307dfc8e71ca956  f3_realdata_prep_rp1-r1_transmission_list_r1_2026-10-08.md
$ sha256sum F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
82472d635eda2b928ce9583d6d7fab1b21c305a9ac1ea2bdb3675f839c62620e  F3_RP1-R1_INDEPENDENT_AUDIT_INSTRUCTION_r2_2026-10-08.md
```

## 8. İlk metne (ddd68399…) göre değişiklik — PI'nın 2026-10-08'de ilettiği inceleme

| # | yer | değişiklik | neden |
|---|---|---|---|
| 1 | §1 madde 1 | makineyle aktarma zorunluluğu "hesaplama ya da ölçüm sonucu olarak bildirilen" değerlerle sınırlandı; PI kararları, denetçi hükümleri ve tarihsel kayıt bilgileri kaynak ve rolleriyle aktarılır; yeni karar ve hükümler yetkili kişi tarafından gerekçelendirilir; hiçbir değer uydurulmaz | ilk metin, §2 ile birlikte, komut çıktısından türetilemeyecek değerleri (PI'nın kararı, denetçinin hükmü, bir onayın tarihi) de kapsıyordu ve gereksiz denetim bulguları üretebilirdi |

Başka değişiklik yok.
