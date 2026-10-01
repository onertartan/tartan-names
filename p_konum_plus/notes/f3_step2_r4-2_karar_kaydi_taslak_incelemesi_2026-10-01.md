# p_konum_plus — F3 STEP-2 r4-2 — PI Karar Kaydı TASLAĞI İncelemesi (yürütücü notu, 2026-10-01)

```text
belge_rolü  = yürütücünün (Claude Code), PI karar kaydı TASLAĞI
              (f3_step2_r4-2_pi_decision_record_DRAFT_2026-10-01.md) üzerine inceleme notu;
              sohbet cevabının belge hâli. TESLİMAT DEĞİLDİR, hiçbir transmission
              listesinde yer almaz; taslağın kendisini DEĞİŞTİRMEZ (taslak PI'ya aittir)
durum       = NON-NORMATIVE / BİLGİLENDİRME
incelenen   = taslağın PI'nın ilettiği kopyası; repo durumu = branch p_konum_plus,
              commit 2e51d11
yürütücünün konumu = taslağın kendi §2 kuralı gereği (status = DRAFT_UNSIGNED, V-2/A-5 yok)
              bu kayıttan HİÇBİR İŞ TÜRETİLMEDİ: D-8 kaydı yapılmadı, durum kaydına
              işleme yok, commit yok
arşiv notu  = bu dosya önce Downloads'a yazılmış, repo arşivine alınırken Downloads
              kopyasının kaybolduğu görülmüş ve yürütücü tarafından KENDİ YAZDIĞI
              içerikten birebir yeniden oluşturulmuştur (2026-10-01)
```

## 1. Doğrulananlar

- **§4'teki beş atıf hash'i, repodaki dosyalara karşı yeniden hesaplandı — beşi de EQUAL:**

| Kayıt | Sonuç |
|---|---|
| D-7 `a3e70509…` | EQUAL |
| D-6 `a92a0518…` | EQUAL |
| D-5 `0cd87ad5…` | EQUAL |
| r4-2 talimatı `d6680338…` | EQUAL |
| A-4 `ad222936…` | EQUAL |

- **Zip hash'i artık bağımsız doğrulandı.** Taslağın §4 notu "zip hash'i yürütücünün
  beyanından alındı; bu oturum onu doğrulamadı" diyordu. Yürütücü zip'i 2026-10-01'de
  yeniden hesapladı: `3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad`
  — taslaktaki değerle birebir. Final metinde bu not "yürütücü tarafından 2026-10-01'de
  yeniden doğrulandı" olarak güncellenebilir.

## 2. ⚠️ PI-1 koşul C-1'de maddi hata — düzeltilmeden imzalanırsa PI-1 kendi koşuluyla düşer

Taslaktaki C-1: *"A-5, (b)'deki beyanı doğrular: r4-2'nin final koşusu baştan tek
süreçti, **yeniden başlatma katmanı kapalıydı** ve T-SINGLE-PROCESS geçti."*

Teslim edilen kayıtların söylediği (results `f2a0a4d5…`, process bloğu; bu inceleme için
yeniden okundu):

```text
final koşu              = attempt 2 / launch 2 (pid 10412)
restart_layer_active    = True        <- katman AÇIKTI (attempt-1 kesintisinden sonra
                                         D-3 §8.2 gereği açılmıştı)
units_read_from_store   = tümü 0      <- süreç store'dan HİÇBİR birim okumadı
store manifest          = 11.869 birimin tamamı pid 10412
```

Yani T-SINGLE-PROCESS'in tutma nedeni "katmanın kapalı olması" değil, **tek sürecin her
şeyi kendisinin hesaplamış ve store'dan sıfır birim okumuş olması**dır. Katman kapalı olan,
kesintiye uğrayan attempt 1'di. A-5, C-1'i lafzıyla denetlerse "katman kapalıydı"
ifadesini YANLIŞ bulur ve PI-1 kendi koşulu gereği düşer — oysa dayanak (b)'deki asıl
beyan doğrudur.

**Önerilen düzeltilmiş C-1 metni:**

> koşul C-1 = A-5, (b)'deki beyanı doğrular: r4-2'nin final koşusunda (attempt 2 /
> launch 2) tek süreç, teslimat 5–8'in her nesnesini kendisi hesapladı ve restart
> store'dan sıfır birim okudu (katman açık olmasına rağmen hiç kullanılmadı);
> T-SINGLE-PROCESS bu nedenle geçerlidir. Doğrulanmazsa PI-1 düşer ve PI'ya döner.

## 3. Küçük tutarlılık notu — §5 imza bloğu

§5'te `imza / onay = Öner (onay: …)` satırı önceden doldurulmuş görünüyor; başlıkta ise
`status = DRAFT_UNSIGNED` duruyor ve A-5 satırı boş. V-2 boş olduğu sürece kayıt zaten
hükümsüzdür; yine de karışıklığı önlemek için imza satırının A-5 verdict'i gelene kadar
boş bırakılması önerilir.

## 4. Bundan sonraki akış (yürütücünün yapacakları)

```text
1. PI, C-1'i düzeltir (ve isterse §4 zip notunu günceller), A-5 denetimini başlatır
   (paket: "...\Ek\r4-2 revizyonu" klasörü veya zip 3a93e558…; başlangıç noktası
   f3_step2_r4-2_transmission_list_2026-09-30.md)
2. A-5 verdict "blocker yok" gelir
3. PI, imzalı final kaydı + A-5'i yürütücüye iletir (V-1 ve V-2 birlikte sağlanmış olur)
4. Yürütücü ancak o zaman: kaydı D-8 olarak ayrı .sha256 sidecar'ıyla repoya alır
   (kendi hash'i içine yazılmaz); PI-1/2/3'ü F3_STEP2 durum kaydına D-8'in hash'iyle
   işler; PI-2 (ii) cümlesini aynen taşır; dondurulmuş/onaylı hiçbir metne dokunmaz;
   QUALIFIED ilan etmez; real_data_access = false kalır; commit yapmaz
V-1 veya V-2 sağlanmadıkça taslaktan hiçbir iş türetilmez (taslağın kendi §2 kuralı).
```
