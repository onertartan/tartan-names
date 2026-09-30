# F3 STEP-1 PI Ratification & Freeze Prompt — Karşılaştırmalı Değerlendirme

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Basis:**  
- `Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_20260905.md`
- Audited r4 candidate and prior PI closure recommendation

---

## Genel değerlendirme

**Belge türü ve aşama olarak evet:** r4 bağımsız audit PASS sonrasında Claude Code’a verilmesi gereken sonraki görev gerçekten bir **PI Ratification & Freeze Record** promptudur.

Ancak **bu dosyayı şu haliyle henüz göndermenizi önermiyorum**, çünkü dosya “PI bütün kararları kapattı ve aşağıdaki kararlar binding input’tur” diyor; oysa bu sohbette siz bu kararları henüz açıkça `ACCEPT/MODIFY` olarak kapatmadınız.

Ayrıca dosyadaki PI karar seti benim hazırladığım öneriyle büyük ölçüde aynı olmakla birlikte **bir önemli MODIFY ve bir ek bilimsel karar** içeriyor.

---

## 1. Kararların karşılaştırması

| Karar | Benim önerim | Ekteki prompt | Değerlendirme |
|---|---|---|---|
| `C4b_status` | `P03_GATE` | `P03_GATE` ACCEPT | **Aynı** |
| `AGG-L1` | `WORSE` | `WORSE` ACCEPT | **Aynı** |
| `D-P03-6` ana karar | `6A` | `6A` ACCEPT | **Aynı** |
| `D-P03-7` | Option A | Option A ACCEPT | **Aynı** |
| `c_complete` | `0.90` | `0.90` ACCEPT | **Aynı** |
| D-P04 same-common-support | ACCEPT | ACCEPT | **Aynı** |
| D-P04 common-support floor | **global `c_complete=0.90` uygula** | **MODIFY: ek floor YOK** | **Temel fark #1** |
| Floor failure action | `NOT_COMPARISON_READY + STOP/PI` | `NOT_APPLICABLE` | Önceki farkın doğal sonucu |
| C3 ACF | classical lag-1 ACF | classical lag-1 ACF ACCEPT | **Aynı** |
| SEPARATE | seçilmez | seçilmez; conditional issue `CLOSED_NOT_APPLICABLE` | **Aynı** |
| K-05 | informational disclosure | canonical informational disclosure | **Aynı / daha ayrıntılı** |
| 6B diagnostic | **şimdilik gerekli değil** | **ayrı-governed companion olarak ADOPTED** | **Temel fark #2** |

r4’ün kendisi common-support floor için benim tercih ettiğim seçeneği recommendation, promptun seçtiği “no additional floor” seçeneğini ise bounded alternative olarak bırakmıştı. Yeni prompt açıkça bu bounded alternative’i seçip `MODIFY` yapıyor ve failure-action satırını bunun sonucu olarak emekliye ayırıyor.

---

# 2. En önemli fark: D-P04 common-support floor

### Benim önceki önerim

Ben:

```text
common support >= c_complete = 0.90
```

ve bunun sağlanmaması halinde:

```text
NOT_COMPARISON_READY
STOP / PI governance
```

önermiştim.

Mantığım, iki modeli çok küçük ortak bir altkümede karşılaştırmaktan kaçınmaktı.

### Ekteki dosyanın önerisi

Yeni prompt ise:

```text
same-set recomputation = zorunlu

ama

additional D-P04 common-support floor = YOK
```

diyor.

Her iki aday P03 aşamasında zaten kendi ilgili valid support’unda en az `%90` completeness sağlamak zorunda olduğundan, iki supportun kesişimi inclusion–exclusion ile en az:

\[
0.90+0.90-1=0.80
\]

oluyor.

Yani common set teorik olarak en az `%80`. F ve M için dosya bunu sırasıyla en az 349/435 ve 377/471 olarak da doğru hesaplıyor. Prompt bunun yerine common-support share’in mutlaka raporlanmasını istiyor.

## Bu yeni yaklaşımı gördükten sonraki değerlendirmem

Burada **ekteki dosyanın tercihini benim önceki önerimden daha iyi buluyorum.**

Nedeni önemli: `%90` D-P04 common-floor koymak yalnızca “iki aday da yeterli veri üzerinde çalışsın” demiyor. Bunu P03 zaten sağlıyor. Ayrıca iki adayın **başarısız olduğu gözlemlerin büyük ölçüde aynı gözlemler olmasını** da dolaylı olarak şart koşuyor.

Örneğin:

```text
P-01 valid = %90
P-02 valid = %90
```

ama başarısız oldukları %10’luk bölümler tamamen farklıysa:

```text
common valid = %80
```

olabilir.

İki model de P03 completeness açısından başarılı olduğu halde benim önceki `%90 common floor` kuralım D-P04’ü STOP’a götürürdü. Bu, model adequacy’den çok **invalid-support overlap patternini** yeni bir kabul kriterine dönüştürürdü.

Bu nedenle daha temiz governance şu:

```text
P03:
her candidate kendi completeness >= 0.90

D-P04:
yalnız aynı ortak support üzerinde karşılaştır
+
common support büyüklüğünü zorunlu raporla
```

Bu bakımdan promptun `MODIFY` kararı metodolojik olarak kuvvetli.

### Ancak prompttaki gerekçenin bir cümlesini değiştirirdim

Prompt şu gerekçeyi kullanıyor:

> “an additional floor would introduce a STOP branch whose resolution is necessarily post-hoc…”

Bunu yeterince iyi bulmuyorum. Çünkü STOP kuralı outcome-blind şekilde önceden dondurulursa, koşulun daha sonra veriye göre gerçekleşmesi metodolojik olarak “post-hoc rule” değildir.

Daha savunulabilir gerekçe:

> Ek `%90` common-support floor, iki adayın bireysel adequacy/completeness düzeyinin ötesinde, **invalid-support setlerinin birbirleriyle örtüşmesine ilişkin yeni bir gereklilik** getirir. Bu overlap requirement için bağımsız bilimsel gerekçe yoktur. Same-support recomputation karşılaştırılabilirlik sorununu zaten çözer; P03 tarafından garanti edilen minimum `%80` intersection ve zorunlu support disclosure ise kararın veri desteğini görünür kılar.

Ben freeze record’a bu gerekçeyi koymayı tercih ederim.

Bu bir **cleanup**, kararın kendisini değiştirmez.

---

# 3. İkinci fark: 6B companion

Benim önceki önerim:

```text
D-P03-6 = 6A
```

ve:

> 6B mevcut primary adequacy kararı için gerekli değil.

Yeni prompt ise yine 6A’yı ratify ediyor, fakat buna ek olarak:

```text
6B_COMPANION = ADOPTED
```

diyor. Üstelik bunu F3 kararına sokmuyor:

```text
separately governed
report-only
no P03 input
no P04 input
no P05 input
no eligibility effect
no tie-break
third_generator = false
winner_eligible = false
```

Bu nedenle **6A ile doğrudan çelişmiyor**. Ama benim dosyamda olmayan **yeni bir PI bilimsel kararıdır**.

Burada ayrım önemli:

```text
D-P03-6 = 6A
```

ile:

```text
ayrı bir 6B diagnostic companion daha sonra oluşturulsun
```

aynı karar değildir.

### Bilimsel değerlendirmem

6B’nin tanımı aslında yararlı:

\[
rac{RMSE_{\text{constrained}}}{RMSE_{\text{unconstrained}}}
\]

ile shape constraint’in trajectory-level fit maliyetini gösteriyor.

Threshold yok, classification yok ve generator seçimine girmiyor. Bu, “tek-dalga shape-constrained mimari gerçek verinin bazı bölümlerinde ciddi fit maliyeti yaratıyor mu?” sorusuna şeffaf bir diagnostic sağlar.

Dolayısıyla:

**6B companion’a bilimsel olarak karşı değilim.**

Fakat governance açısından bunu şu anki ratification promptuna koymanın tek şartı, bunun **sizin bilinçli PI kararınız olmasıdır**.

Şimdi eklenmesi ancak yeni explicit PI kararıyla meşru olur.

---

# 4. Promptun benim dosyamdan daha güçlü olduğu yerler

Yeni prompt bazı bakımlardan benim closure dosyamdan daha iyi hazırlanmış.

Özellikle:

- tüm r4 satırlarını tek tek kapatıyor;
- `C4b=P03_GATE`, `WORSE`, `Option A`, `0.90`, classical ACF gibi kararları exact olarak yazıyor;
- K-05’i gerçekten seçilen `P03_GATE + WORSE + 0.90 + 0.85` dalına indiriyor;
- SEPARATE problemini ortadan kaldırmıyor, yalnız selected branch olmadığı için `CLOSED_NOT_APPLICABLE` yapıyor;
- r3/r4’ü rewrite etmek yerine r4’ü hash ile incorporate ediyor;
- freeze record + provenance report + external sidecar istiyor;
- `F3_EXECUTION_READY=false` bırakıyor.

Bunlar governance açısından doğru.

---

# 5. Dikkat ettiğim ek bir nokta

Dosya kendisini:

```text
ratification transcription / freeze-record creation
```

olarak tanımlasa da yalnız transcription yapmıyor.

Ayrıca:

```text
CL-F3-01 .. CL-F3-05
DISC-F3-01 .. DISC-F3-05
6B companion
```

gibi yeni binding wording/disclosure ekleri de freeze ediyor.

Çoğu yararlı ve ana methodology’yi değiştirmiyor. Fakat özellikle `6B_COMPANION` sıradan provenance cleanup değildir; **PI scientific scope decision** niteliğindedir.

Dolayısıyla Claude Code’un bunları “PI zaten karar verdi” diye kabul etmesi ancak gerçekten sizin kararınızsa doğru olur.

---

# 6. Sonuç

Benim değerlendirmem:

**Belgenin genel yapısı: 9.3/10**

**PI kararlarının metodolojik kalitesi: 9.2/10**

**Benim önceki öneri paketimle uyum: yaklaşık %85–90.**

Asıl iki fark:

1. **D-P04 common floor:**  
   Ben `%90 floor + STOP` önermiştim.  
   Bu dosya `no additional floor + mandatory disclosure` seçiyor.  
   **Yeni gerekçeyi gördükten sonra bu dosyanın kararını tercih ediyorum**, fakat “post-hoc STOP” gerekçesini yukarıdaki daha doğru overlap-criterion gerekçesiyle değiştirirdim.

2. **6B companion:**  
   Ben primary closure için gerekli görmemiştim.  
   Bu dosya onu ayrı-governed, winner-ineligible diagnostic olarak adopt ediyor.  
   **Metodolojik olarak kabul edilebilir ve faydalı**, ama sizin ayrıca explicit PI kararınız olmalıdır.

Dolayısıyla **şu haliyle doğrudan Claude Code’a göndermeden önce tek governance eksiği sizin açık PI iradenizdir**. Dosya “PI kararları BINDING INPUT” diyor. Ben veya başka bir LLM bu statüyü sizin adınıza veremeyiz.

Eğer sizin kararınız gerçekten:

```text
D-P04_COMMON_SUPPORT_FLOOR =
MODIFY → no additional floor + mandatory disclosure

D-P04_COMMON_SUPPORT_FAILURE_ACTION =
NOT_APPLICABLE

6B_COMPANION =
ADOPTED as separately governed report-only diagnostic
```

ise, geri kalan temel kararlar zaten benim önerilerimle aynı ve **bu ratification/freeze promptu doğru sonraki Claude Code görevidir**.
