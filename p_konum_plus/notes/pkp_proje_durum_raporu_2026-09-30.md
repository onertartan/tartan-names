# p_konum_plus — Proje Güncel Durum Raporu (2026-09-30)

```text
belge_rolü  = PI için güncel durum raporu; yürütücünün sohbet durum mesajının belge hâli.
              TESLİMAT DEĞİLDİR, hiçbir transmission listesinde yer almaz; karar veren şey
              hash'li teslimatlar ve koşu çıktılarıdır
durum       = NON-NORMATIVE / BİLGİLENDİRME
yazım_anı   = r4-2 revizyonu kapandıktan ve p_konum_plus branch'i GitHub'a push
              edildikten sonra
```

## 1. Genel görünüm

| Faz | Durum |
|---|---|
| F2 (fizibilite) | **CLOSED** (FINAL FREEZE r1) |
| F3 STEP-1 | **FROZEN** (freeze record r1 ile onaylı) |
| F3 STEP-2 (yeterlilik değerlendirme) | **r4-2 revizyonu tamamlandı — PARTIAL_PENDING_PI** |
| F3 EXECUTION_READY | false (hiçbir kayıt QUALIFIED ilan etmiyor; yalnız PI edebilir) |
| Gerçek SSA verisi | hiç kullanılmadı (`real_data_access = false`, tüm döngülerde) |

Düzeltme zinciri: r1 → r2 → r3 (denetim A-1) → r4 (denetim A-2/A-3) → r4-1 (denetim A-4,
verdict PASSED, 0 blocker) → **r4-2 (A-4'ün 6 temizlik maddesi; kapandı, denetimi bekliyor)**.

## 2. r4-2 revizyonunun sonucu (bugün kapandı)

Kapsam D-7 §3: R41A-01 … R41A-06; R41A-08 uygulanmadı. Altısı da **yalnız gerçekten
çalışıp geçen testlerle** kapatıldı:

| Madde | Kapanış kanıtı |
|---|---|
| R41A-01 (a)(b) | Üç spline-pending bayrağı artık HER `STOP_EXACTNESS_PENDING`'de kuruluyor ve olayın kendi tag'ini taşıyor; bildirilmiş spline arızası sıradan arıza (SCEN-B pin'i korunur). **Kriter-bazlı okuma PI tarafından kabul edildi** ve register satırı PIN-SPLINE-PENDING-TAG-SCOPE ile rapor §4'te açıkça yazıldı |
| R41A-01 (c) | T-SPL-PENDING-REALPATH (ZORUNLU): gerçek karar yolu, yalnız iki fit motoru stub'lı; **9/9 vaka**, tüm global'ler restore-assert'li, PENDING hücre asla verdict taşımıyor |
| R41A-01 (d) | T-NONREG-R4-1 (ZORUNLU): r4-1 sonuçlarına karşı **37 nesne + tüm stop'lar, whitelist'siz — 0 bulgu**; RUN1 kanonik `556106e7…` ve residual `3ee624f3…` adlandırılmış değer olarak DEĞİŞMEDİ |
| R41A-02 | Attempt-numaralı custody (ikisi de diskte; `supersedes_custody_sha256` dolu), **düzenlemeden ÖNCE karantina kopyası** (hash birebir — rekonstrüksiyon yok), launch-numaralı log çiftleri (hiçbiri üzerine yazılmadı) |
| R41A-03 | `end_state.PI_dispatch_record_hash` = **D-7 gözlemlenen** (`a3e70509…`); S-R2-1 kaynağı (D-5) kendi alanında; üç assertion'la kanıtlı |
| R41A-04 | Rapor §6 hash bloğu: tüm r4-2 teslimatları + r4-1 raporunun eksik bıraktığı üç hash (`45a10494…`, `fedd964a…`, `ee5b4862…`) |
| R41A-05 | ERRATUM-3: r3 log 6–8. satırlar vs revizyon-4 custody çelişkisi; altı aday parmak izi YENİDEN HESAPLANDI, r3 final store SAYILDI (tam iki prefix; `f882b922` karşılığı yok); her çıkarım çıkarım olarak işaretli |
| R41A-06 | INJ-U-POST kaydının doğru tarifi: **iki pair — (F,P01,0) ve (M,P01,0)**; kayıt-düzeyi sex = ilk isabetin (F); kod değişmedi |

**Koşu:** 2 attempt / 2 launch. Attempt 1 dış kesinti (hatasız, store birimi yok);
attempt 2 / launch 2 **tek süreçte** (pid 10412) 11.869 birimin ve tüm sonuçların tamamını
hesapladı → **T-SINGLE-PROCESS geçerli**. DETERMINISM=True; 36/36 beklenti; 30/30 test;
coverage 64 satır, 0 downgrade; doğal UNRELATED olay 0. Sonuçlar `f2a0a4d5…`.

## 3. Teslimatlar

| Ne | Nerede |
|---|---|
| r4-2 teslim klasörü (54 dosya, 27 sidecar çifti — tamamı doğrulandı) | `C:\Users\Neo\Downloads\28 Eylül\r4-2 teslim` |
| **Denetçi kopyası (bu istekle çıkarıldı; 54/54, 0 uyuşmazlık)** | `C:\Users\Neo\Downloads\28 Eylül\30 Eylul\Ek\r4-2 revizyonu` |
| Tek zip (yalnız taşıma için; denetçi içteki her dosyayı kendi sidecar'ına karşı doğrular) | `C:\Users\Neo\Downloads\28 Eylül\f3_step2_r4-2_delivery_2026-09-30.zip` — **sha256 `3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad`**, 1.409.226 bayt |

Klasörün içeriği: teslimat 1–12 (harness, YENİDEN KULLANILAN r4-1 generator+manifest,
attempt-1 ve attempt-2 custody kayıtları, telemetri, results, residual, test-evidence,
register, rapor, envanter, attempt log) + A/B/D/D′ + transmission listesi + her iki
launch'ın stdout/stderr çifti + attempt-1 kesinti notu ve korunan attempt-1 harness
byte'ları + üç dispatch enstrümanı (r4-2 talimatı, D-7, A-4) — hepsi `.sha256` sidecar'lı.

## 4. GitHub (PI'nın paket-sonrası ayrı talimatıyla)

`p_konum_plus` branch'i **github.com/onertartan/tartan-names**'e push edildi ve doğrulandı
(yerel == uzak == `2e51d11`; push edilmemiş commit yok; çalışma ağacı temiz). 5 yeni
commit: F2–r4 arşivi; byte-exact `.gitattributes` kuralı + kapsamın arşive daraltılması;
r4-1 paketi; r4-2 paketi. Restart store'ları (`.pkl` birimleri) `.gitignore` ile bilinçli
dışarıda — her birim, commit'lenen store-manifest CSV'lerinde hash-listeli. Push öncesi
bütünlük kanıtı: **115 pinli dosyada blob == disk == sidecar, 0 uyuşmazlık.** r4-2 paketi
içinde commit yapılmadı ("Commit yapma"); depo işlemi paket kapandıktan sonra PI'nın ayrı
talimatıyla yapıldı ve r4-2 raporu §8'de böyle kayıtlıdır.

## 5. Açık kalanlar — hepsi PI kararı, hiçbiri bu revizyonun işi değil

1. **r4-2 paketinin bağımsız denetimi (A-5).** Paket ve zip hazır; yürütücü kendi
   çıktısını denetleyemez (prior exposure D-7'de açık).
2. **T-R2-2 narrowed_evidence.** r4-2'nin kendisi tek süreçte koştu, ama r4 döngüsünün
   geçmişi restart katmanı kullandı; alanın boşalması ayrı bir PI kararı/koşusu ister.
3. **"A.5 (iii) inadmissible refit" UNCOVERED satırı.** Frozen koda dokunmadan
   kapatılamaz (Y-16); D-7 §5 kalıcı kayıtlı sınırlama olarak öngörüyor — kabulü PI'ya ait.
4. İstenirse: `p_konum_plus` → `main` PR'ı (`github.com/onertartan/tartan-names/pull/new/p_konum_plus`).

```text
QUALIFIED hiçbir kayıtta ilan edilmedi; yalnız PI, bağımsız denetim sonrası ilan edebilir.
real_data_access = false
```
