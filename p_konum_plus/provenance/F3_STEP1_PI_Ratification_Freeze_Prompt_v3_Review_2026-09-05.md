# F3 STEP-1 PI Ratification & Freeze Prompt v3 — Review

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Reviewed artifact:** `Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_20260905.md`

---

## Genel değerlendirme

v3, v2’ye göre **belirgin biçimde daha temiz ve metodolojik olarak daha güçlüdür**.

Önceki dört ana eleştirinin tümü hedeflenmiş ve esasen doğru kapatılmıştır:

- 6B quantile seti sonraki ayrı specification’a ertelenmiştir;
- independence approximation kaldırılmıştır;
- C3 exact-fit durumu artık `structurally unreachable` olarak tanımlanmamaktadır;
- PI attestation geçmiş sohbetlere değil doğrudan **PI dispatch act**’ine bağlanmıştır.

Bununla birlikte, **Claude Code’a göndermeden önce dar bir v3→v4 exactness/provenance cleanup yapılması önerilir**.

Bu yeni methodology cycle değildir.

```text
F2_reopening = false
new_methodology_review = false
r4_reopening = false
F3_execution = prohibited
```

Bağımsız hesaplanan mevcut v3 SHA256:

```text
4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7
```

v3’ün kaydettiği v2 (`2860fade…`), v1 (`da5a0a13…`) ve iki review hash’i (`c12b2752…`, `07c33063…`) mevcut dosyalarla uyumludur.

---

# 1. Gate-specific blocker — K-05 denominator cümlesi içsel olarak yanlış

K-05 içinde şu satır yer almaktadır:

```text
Denominator declaration:
C4a = 2·n_s per sex ;
C4b completeness = n_s per sex ;
D-P04 C4b common support U4_s = n_s per sex.
```

Ancak hemen sonrasında doğru biçimde:

```text
U4_s ⊆ V4_s may be smaller than V4_s
```

denmektedir.

Dolayısıyla:

```text
U4_s = n_s
```

anlamına gelebilecek wording yanlıştır.

`U4_s` bir **common-valid set**tir ve büyüklüğü `n_s` olmak zorunda değildir. Ratified no-floor branch altında teorik olarak yaklaşık `%80` seviyesine kadar düşebilir.

## Önerilen düzeltme

```text
Denominator declaration:
C4a denominator = 2·n_s per sex;
C4b completeness-share denominator = n_s per sex;
D-P04 C4b common-support-share denominator = n_s per sex,
with |U4_s| as the common-valid support count.
```

Bu yalnız stil düzeltmesi değildir; freeze record’a verbatim girecek exact semantics’i etkilediği için:

```text
classification = gate-specific blocker
```

---

# 2. Gate-specific blocker — DISC-F3-05 “906 enter every criterion's aggregation”

Şu cümle teknik olarak doğru değildir:

```text
All eligible trajectories (906) enter every criterion's aggregation.
```

r4 açıkça C2, C3, C4b ve C5 gibi kriterleri valid subsets üzerinde hesaplamaktadır.

Dolayısıyla 906 trajectory’nin tamamı her kriterin sex-level statistic aggregation’ına doğrudan girmez.

Doğru bilimsel anlam şudur:

- bütün 906 trajectory adequacy governance içinde temsil edilmeye devam eder;
- C1 full-stratum denominator kullanır;
- subset-defined criteria valid / paired-valid support üzerinde statistic hesaplar;
- `n_s` completeness denominator olarak korunur;
- morphology-based exclusion yapılmaz.

## Önerilen replacement

```text
All 906 eligible trajectories remain represented in the F3 adequacy
governance: C1 uses the full stratum denominator; subset-defined
criteria compute their statistics on the frozen valid / paired-valid
sets while retaining n_s as the completeness denominator.
No morphology-based exclusion is permitted.
```

Bu replacement, 6A claim boundary’yi korur ve valid-set yapısını doğru tanımlar.

```text
classification = gate-specific blocker
```

---

# 3. Cleanup — §13 parent prompt hâlâ v1 gösteriyor

v3 header doğru biçimde:

```text
parent_prompt = v2
grandparent_prompt = v1
```

demektedir.

Ancak §13 freeze-record identity structure içinde hâlâ:

```text
execution_prompt_parent =
v1 path + SHA256 da5a0a13…
```

yazmaktadır.

Bu lineage artık yanlıştır.

## Önerilen düzeltme

```text
execution_prompt_parent =
v2 path + SHA256 2860fade…

execution_prompt_grandparent =
v1 path + SHA256 da5a0a13…
```

```text
classification = cleanup
```

---

# 4. Cleanup — §12 custody table hâlâ “items 1–10”

v3 §1 artık **14 custody/provenance item** içermektedir.

Independent audit requirements da doğru şekilde:

```text
items 1–6 exact ; 7–14 recorded
```

demektedir.

Fakat deliverable specification hâlâ:

```text
custody table (§1 items 1–10, observed vs expected)
```

ifadesini kullanmaktadır.

## Önerilen düzeltme

```text
custody table (§1 items 1–14, observed vs expected / recorded
according to their defined custody status)
```

```text
classification = cleanup
```

---

# 5. Cleanup — DISC-F3-04 yeni sayısal örnekler

v3 independence approximation’ı doğru şekilde kaldırmıştır.

Ancak yerine:

```text
q = 0.05 => [47.5, 52.5]
q = 0.15 => [42.5, 57.5]
```

gibi yeni sayısal örnekler eklenmiştir.

Bunlar scientific threshold değildir; yalnız derived mathematical examples’dır.

Bu nedenle doğrudan:

```text
new_numeric_literal_count = 0
```

ile çelişmek zorunda değildir.

Buna rağmen provenance açısından gereksiz belirsizlik üretmektedir.

## Tercih edilen çözüm

Yalnız ratified `c_complete=0.90` ile ilişkili:

```text
q = 0.10 => [45,55]
```

örneği bırakılmalı, diğer derived examples kaldırılmalıdır.

### Bounded alternative

Eğer tutulacaksa açıkça:

```text
q=0.05 and q=0.15 values are derived mathematical examples only;
they are not frozen literals, thresholds, or decision parameters.
```

şeklinde etiketlenmelidir.

```text
classification = cleanup
```

---

# 6. Cleanup — 6B ratio `>=1` yalnız tanımlı olduğunda geçerli

6B şu anda:

```text
RMSE_constrained_i / RMSE_unconstrained_i
(>= 1 by construction ...)
```

demektedir.

Aynı block daha sonra:

```text
RMSE_unconstrained_i = 0
=> ratio undefined
```

durumunun sonraki specification’da pinleneceğini söylemektedir.

Bu nedenle theorem daha exact yazılmalıdır.

## Önerilen wording

```text
when both fits are valid and RMSE_unconstrained_i > 0,
RMSE_constrained_i / RMSE_unconstrained_i >= 1
by construction
```

Böylece zero-denominator edge case ile mantıksal gerilim kalmaz.

```text
classification = cleanup
```

---

# 7. Cleanup — common-support rationale’daki küçük overstatement

Şu ifade:

```text
two individually adequate candidates whose failures
fall on different trajectories are not less comparable
```

biraz fazla kategoriktir.

Farklı failure pattern’ları bilimsel olarak yine de bilgilendirici olabilir.

Asıl savunulabilir nokta şudur:

- iki aday bireysel olarak adequacy/completeness kriterini geçtiyse;
- yalnız invalid-set overlap farklılığı nedeniyle;
- bağımsız olarak gerekçelendirilmiş bir overlap requirement yoksa;
- otomatik non-comparability ilan edilmemelidir.

## Daha güvenli wording

```text
two individually adequate candidates should not be declared
non-comparable solely because their invalid sets differ,
absent an independently justified overlap requirement.
```

Kararı değiştirmez; reviewer-defensibility’yi artırır.

```text
classification = cleanup
```

---

# 8. Önceki v2 sorunlarının durumu

| Önceki finding | v3 durumu |
|---|---|
| 6B quantiles vs `new_numeric_literal_count=0` | **düzeltildi** |
| Independence approximation | **düzeltildi** |
| C3 “structurally unreachable” | **düzeltildi** |
| K-05 `a fortiori U4⊆V4` | **düzeltildi** |
| Historical chat-based PI attestation | **düzeltildi** |
| Common-floor overlap rationale | **korunmuş ve güçlü** |
| 6B = explicit PI scope decision | **doğru korunmuş** |

---

# 9. PI attestation değerlendirmesi

PI attestation kısmı v3’ün en güçlü düzeltmelerinden biridir.

Özellikle:

```text
dispatch of this prompt by the PI
constitutes the PI's ratification act
```

ve prior advisory/review belgelerinin PI authority vermediğinin açıkça yazılması governance açısından doğrudur.

Bu yapı:

- LLM’in PI adına karar vermesini engeller;
- ratification act’i somut bir PI action’a bağlar;
- prior reviews’u provenance düzeyinde tutar;
- binding-input status’un kaynağını açıklaştırır.

Bu bölüm için blocker yoktur.

---

# 10. Nihai sınıflandırma

```text
global blocker = none

gate-specific blocker =
  1. K-05 U4_s denominator wording
  2. DISC-F3-05 "906 enter every criterion's aggregation"

cleanup =
  1. §13 execution_prompt_parent v1 -> v2
  2. §12 custody items 1–10 -> 1–14
  3. DISC-F3-04 derived numeric examples
  4. 6B ratio >=1 conditional wording
  5. common-support rationale minor overstatement

informational =
  prior v2 findings successfully closed
```

---

# 11. Puan

```text
v2 ≈ 9.5 / 10
v3 ≈ 9.7 / 10
```

Ancak freeze artifact olduğu için kalan iki exactness çelişkisi bırakılmamalıdır.

---

# 12. Önerilen sonraki adım

```text
v3 -> v4
narrow exactness / provenance cleanup only

PI scientific decisions changed = 0
new methodology review = false
F2 remains CLOSED
r4 remains read-only
F3 execution remains prohibited
```

v4 yalnız şu değişiklikleri yapmalıdır:

```text
1. K-05 denominator wording correction
2. DISC-F3-05 governance/aggregation wording correction
3. §13 lineage correction: parent=v2, grandparent=v1
4. §12 custody range correction: 1–14
5. DISC-F3-04 derived examples cleanup
6. 6B ratio >=1 conditional wording
7. common-support rationale wording softening
```

Bu iki blocker ve beş cleanup kapatıldıktan sonra:

```text
dispatch_ready = true
```

kararı verilebilir.

F2 yeniden açılmaz.  
r4 rewrite edilmez.  
Yeni methodology review açılmaz.  
F3 execution bu freeze-record task sırasında hâlâ başlamaz.
