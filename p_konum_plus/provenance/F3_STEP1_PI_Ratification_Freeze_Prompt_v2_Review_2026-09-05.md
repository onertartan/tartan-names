# F3 STEP-1 PI Ratification & Freeze Prompt v2 — Review

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Reviewed artifact:** `Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_20260905.md`

---

## Genel değerlendirme

Güncellenmiş **v2, v1’e göre belirgin biçimde daha iyi** ve önceki eleştirinin üç ana noktasını doğru biçimde kapatıyor.

Özellikle:

- PI attestation artık açık bir gate yapılmış;
- common-support floor gerekçesi “post-hoc STOP” yerine failure-set overlap mantığına taşınmış;
- 6B açıkça `PI_SCIENTIFIC_SCOPE_DECISION` olarak sınıflandırılmış.

Ancak **henüz Claude Code’a göndermenizi önermiyorum**.

Yeni incelemede:

```text
global blocker = none confirmed
gate-specific blocker = 1
cleanup = 3
informational = 1 conditional provenance check

F2_reopening = false
new_methodology_review = false
r4_reopening = false
```

bulunmuştur.

Bu sorunlar F2’yi veya r4’ü yeniden açmayı gerektirmez. Dar kapsamlı bir:

```text
v2 -> v3
narrow exactness / cleanup correction
```

yeterlidir.

---

# 1. Gate-specific blocker — `new_numeric_literal_count = 0` ile 6B çelişkisi

Prompt bir yandan:

```text
new_numeric_literal_count = 0
```

diyor.

Öte yandan 6B companion içinde:

```text
report =
quantiles by sex stratum
0.05 / 0.25 / 0.50 / 0.75 / 0.95
```

şeklinde sabit raporlama noktaları freeze ediliyor.

Üstelik v2 artık 6B’yi sıradan cleanup değil, açıkça:

```text
PI_SCIENTIFIC_SCOPE_DECISION
```

olarak tanımlıyor.

Dolayısıyla literal anlamda:

```text
new_numeric_literal_count = 0
```

ifadesi savunulamaz.

## Önerilen çözüm

6B zaten:

```text
separate artifact
separate governance
separate independent audit
```

ile daha sonra specification alacaksa, quantile setini **şimdi freeze etmemek** daha temizdir.

§8 şu şekilde daraltılabilir:

```text
report =
  sex-specific distributional summaries;
  exact reporting quantiles/statistics to be pinned
  outcome-blind in the separately governed 6B companion specification

current_F3_STEP1_consumption = none
```

Böylece gerçekten:

```text
new_numeric_literal_count = 0
```

kalabilir.

### Bounded alternative

Eğer quantile seti şimdi gerçekten PI kararı olarak freeze edilecekse:

```text
new_F3_primary_numeric_literal_count = 0

6B_report_structural_literals =
  {0.05, 0.25, 0.50, 0.75, 0.95}
```

şeklinde ayrı kaydedilmelidir.

### Tercih edilen çözüm

İlk seçenek daha uygundur.

Bu freeze task’ı 6B’nin varlığı ve scope’u içindir; ayrıntılı reporting design’ın sonraki 6B specification’da pinlenmesi governance açısından daha temizdir.

**Classification:** gate-specific blocker.

---

# 2. Cleanup — DISC-F3-04 independence approximation tutarsızlığı

DISC-F3-04 şu anda:

```text
5 folds => ≈ 0.979 per fold
2 probes => ≈ 0.949 per probe
```

diyor.

Ancak hemen ardından:

```text
C2: 10 sub-fits per trajectory pair
C4b: 4 probes
```

şeklinde paired-valid yapıyı doğru açıklıyor.

Burada iki farklı düzey karışmıştır.

`0.90` paired-valid completeness için bağımsız ve eşit başarı olasılığı varsayılırsa:

```text
C2:
p^10 = 0.90
p ≈ 0.9895

C4b:
p^4 = 0.90
p ≈ 0.9740
```

Mevcut:

```text
0.979 ≈ 0.90^(1/5)
0.949 ≈ 0.90^(1/2)
```

değerleri yalnız:

- tek fitter’ın 5 fold’u;
- tek family’nin 2 probe’u

için geçerlidir.

## Önerilen çözüm

Bu independence approximation tamamen çıkarılmalıdır.

`c_complete = 0.90` için zaten daha güçlü ve assumption-free gerekçe vardır:

```text
adversarial dropout
median percentile band
```

Bağımsızlık yaklaşımı gereksizdir ve şu hakem sorusunu davet eder:

> Neden sub-fit independence varsayılıyor?

DISC-F3-04 şu temel gerekçeyle bırakılabilir:

```text
q = 0.10
=>
median retained sample remains within
[45,55] percentile band of the full-stratum distribution.
```

Criterion complexity farkı yalnız nitel disclosure olarak kaydedilebilir.

**Classification:** cleanup.

---

# 3. Cleanup — CL-F3-04 içindeki “structurally unreachable” ifadesi fazla güçlü

v2 şu ifadeyi kullanıyor:

```text
Structurally unreachable under the frozen eligibility taxonomy
...
denominator zero only if ghat == z exactly
```

İkinci ifade doğrudur:

```text
residual variance = 0
+
mean residual = 0
=>
r_t = 0 for all t
=>
ghat = z
```

Ancak bundan:

```text
structurally unreachable
```

sonucu çıkmaz.

Perfect fit çok nadir olabilir, fakat frozen eligibility taxonomy bunu matematiksel olarak yasaklamıyor.

r4 zaten bu edge case için doğru governance oluşturmuştur:

```text
phi_i = undefined
D-P03-7 completeness governance applies
```

## Önerilen düzeltme

Şu wording daha doğru olur:

```text
This case is expected to be rare but is not structurally excluded.
It is explicitly governed here for exactness.
```

Bu scientific decision değiştirmez.

**Classification:** cleanup.

---

# 4. Cleanup — K-05 sonundaki “a fortiori” cümlesi kaldırılmalı

K-05 sonunda:

```text
The same reasoning holds a fortiori
on the D-P04 common set U4_s ⊆ V4_s.
```

deniyor.

Yeni ratified no-floor branch altında bu ifade doğru değildir.

Çünkü:

```text
candidate-specific V4_s >= 0.90 n_s
```

olmasına rağmen:

```text
common U4_s
```

yalnız teorik olarak yaklaşık `%80`’e kadar düşebilir.

Dolayısıyla:

```text
U4_s ⊆ V4_s
```

olması “a fortiori” ile daha güçlü completeness sonucu vermez; tersine common set daha küçüktür.

K-05’in asıl sonucu zaten doğru şekilde candidate-specific `V4_s` completeness üzerinden elde edilir:

```text
|V4_s|/n_s >= 0.90
=>
ident_F,s >= 0.90
>
c_ident = 0.85
```

## Önerilen düzeltme

Son cümle kaldırılabilir.

Alternatif wording:

```text
Every trajectory in U4_s also satisfies the relevant
LEFT/RIGHT success requirements, but no additional C4a
completeness implication is derived from |U4_s|,
because no D-P04 common-support floor is ratified.
```

**Classification:** cleanup.

---

# 5. Informational / koşullu provenance kontrolü — PI attestation

v2’nin en önemli iyileştirmelerinden biri:

```text
attestation_mode =
dispatch of this prompt by the PI to Claude Code
constitutes the PI's ratification act
```

ve:

```text
PI_confirmation = CONFIRMED_BY_DISPATCH
```

şeklindeki yapılandırmadır.

Bu governance mantığı güçlüdür.

Böylece LLM:

```text
PI kabul etti
```

diye kendi başına karar veremez; PI’nin promptu bilinçli dispatch etmesi ratification act olur.

Ancak attestation block ayrıca geçmişe ilişkin şu factual claimleri de içeriyor:

```text
explicit PI statements recorded in that channel
...
6B ... answered by the PI to a direct question
```

Bu exact statements ilgili Claude-chat decision-basis artifact içinde gerçekten mevcutsa sorun yoktur.

Eğer mevcut değilse:

```text
conditional global blocker =
false PI-attestation provenance
```

olur.

## Daha güvenli wording

Attestation geçmiş sohbet iddialarına daha az bağımlı hale getirilebilir:

```text
PI attests by dispatch that:
  all decisions in §3–§8 are his binding decisions,
  including the single MODIFY and the 6B scope adoption.

Prior advisory/review documents are provenance only
and do not themselves confer PI authority.
```

Bu daha temiz ve doğrudan governance sağlar.

**Classification:** informational; conditional global blocker if factual provenance is false.

---

# 6. Common-support floor gerekçesi artık iyi

Bu bölüm v1’e göre önemli ölçüde düzelmiştir.

Yeni primary rationale:

```text
additional 0.90 common floor
=
failure-set overlap requirement
beyond individual candidate completeness
```

mantıksal olarak doğrudur.

Özellikle:

```text
|U| >= 0.90n
<=>
|F_P01 ∪ F_P02| <= 0.10n
```

bağlantısı, neden ikinci `%90` eşiğin yeni bir scientific requirement haline geleceğini iyi açıklar.

Önceki eleştirideki:

> “pre-frozen STOP post-hoc değildir”

sorunu da v2’de doğru düzeltilmiştir.

Artık secondary gerekçe:

```text
trigger pre-frozen and outcome-blind,
but no pre-declared resolution exists after STOP
```

şeklindedir.

Bu daha savunulabilir bir gerekçedir.

**Bu bölüm için artık blocker yoktur.**

---

# 7. 6B governance sınıflandırması artık doğru

v1’de 6B’nin sanki basit freeze cleanup gibi görünmesi önemli bir belirsizlikti.

v2 bunu açıkça:

```text
decision_class =
PI_SCIENTIFIC_SCOPE_DECISION
```

olarak ayırıyor.

Ayrıca:

```text
NOT transcription
NOT cleanup
NOT provenance
```

diyor.

Bu doğru governance sınıflandırmasıdır.

Ayrıca:

```text
third_generator = false
winner_eligible = false
no P03/P04/P05 input
no eligibility effect
no tie-break
```

firewall’u korumaktadır.

## Sonraki specification için teknik edge case

6B’de:

```text
RMSE_constrained / RMSE_unconstrained
```

kullanılacağı için:

```text
RMSE_unconstrained = 0
```

durumunun exact behavior’ı sonraki 6B specification’da pinlenmelidir.

Bu şu anki F3 STEP-1 freeze için blocker değildir, çünkü 6B:

```text
separate specification
separate independent audit
```

altında ilerleyecektir.

**Classification:** informational.

---

# 8. Nihai değerlendirme tablosu

| Finding | Sınıf | Durum |
|---|---|---|
| v2 PI attestation architecture | informational | **iyi düzeltme** |
| common-support floor rationale | informational | **v1’e göre düzeltilmiş / kabul edilebilir** |
| 6B decision classification | informational | **doğru** |
| `new_numeric_literal_count=0` vs 6B quantiles | **gate-specific blocker** | **düzeltilmeli** |
| DISC-F3-04 5-fold/2-probe approximation | cleanup | **çıkarılmalı/düzeltilmeli** |
| CL-F3-04 “structurally unreachable” | cleanup | **düzeltilmeli** |
| K-05 `a fortiori U4⊆V4` | cleanup | **düzeltilmeli** |
| Historical PI-attestation factual claims | informational; conditional global blocker if false | **kaynağı doğrulanmalı veya wording sadeleştirilmeli** |

---

# 9. Puan

```text
v1 ≈ 9.3 / 10
v2 mevcut hali ≈ 9.5 / 10
```

Ancak freeze promptunda iç çelişki bırakmamak için **v3 yapılması önerilir**.

Bu bir yeni methodology cycle değildir.

Exact scope:

```text
v2 -> v3
narrow exactness / cleanup correction

scientific PI decisions unchanged
F2 remains CLOSED
r4 remains read-only
new_methodology_review = false
```

---

# 10. Önerilen sonraki durum

v3 yalnız şu dört teknik değişikliği yapmalıdır:

```text
1. 6B quantile literals:
   remove from current freeze
   OR explicitly classify separately

2. DISC-F3-04:
   remove the independence approximation

3. CL-F3-04:
   replace "structurally unreachable"

4. K-05:
   remove / correct the U4 a-fortiori sentence
```

Ek olarak PI attestation historical claims:

```text
verify exact provenance
OR
replace with dispatch-based direct attestation wording
```

Bu düzeltmeler tamamlandıktan sonra:

```text
dispatch_ready = true
```

kararı verilebilir.

F2 yeniden açılmaz.  
r4 yeniden yazılmaz.  
Yeni methodology review açılmaz.  
F3 execution bu freeze-record task sırasında hâlâ başlamaz.
