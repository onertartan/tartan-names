# F3 STEP-1 PI Ratification & Freeze Prompt v4 — Review

**Project:** `SSA Application-Calibrated Clustering Benchmark / p_konum_plus`  
**Date:** 2026-09-05  
**Reviewed artifact:** `Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_20260905.md`

---

## Genel değerlendirme

v4, v3’e göre belirgin biçimde daha temizdir ve v3 incelemesinde bulunan iki gate-specific blocker ile beş cleanup’ın tamamını doğru biçimde kapatmıştır.

Özellikle:

- K-05 denominator semantiği düzeltilmiştir;
- DISC-F3-05 valid-set semantiği r4 ile uyumlu hale getirilmiştir;
- lineage / custody aralıkları düzeltilmiştir;
- derived numeric examples temizlenmiştir;
- 6B ratio `>=1` ifadesi tanımlı olduğu koşula bağlanmıştır;
- common-support rationale daha savunulabilir hale getirilmiştir;
- PI attestation dispatch-temelli olarak korunmuştur.

Bağımsız hesaplanan v4 SHA256:

```text
bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458
```

Buna rağmen son kontrolde:

```text
global blocker = none
gate-specific blocker = 1
cleanup = 2
```

bulunmuştur.

Bu nedenle zero-defect freeze açısından dar bir:

```text
v4 -> v5
```

exactness / provenance correction önerilmektedir.

Bu yeni methodology cycle değildir.

```text
scientific PI decision change = 0
numeric literal change = 0
new methodology review = false
F2 remains CLOSED
r4 remains read-only
F3 execution remains prohibited
```

---

# 1. Gate-specific blocker — 6B “separate governance” ile §14 next-action çelişkisi

§8, 6B için açık biçimde:

```text
governance = R-REV governance
separate artifact
separate independent audit
```

demektedir.

6B ayrıca:

```text
decision_class = PI_SCIENTIFIC_SCOPE_DECISION
```

olarak F3 STEP-1 packet dışında tutulmaktadır.

Buna rağmen §14 next-action kısmında:

```text
F3 STEP-2 implementation-pin task
(CLASS_C pins:
 ...
 fold scheme;
 6B companion specification)
```

şeklinde 6B companion specification, CLASS_C / F3 STEP-2 task içine dahil edilmektedir.

Bu iki governance ifadesi aynı şeyi söylememektedir.

## Neden önemlidir?

6B:

```text
CLASS_C implementation pin
```

değildir.

Freeze record’un kendi tanımına göre:

```text
separately governed R-REV companion specification
```

niteliğindedir.

Aynı Claude Code session veya task içinde teknik olarak ayrı artifact üretmek mümkün olsa bile, freeze governance bunu aynı CLASS_C task’ının parçası olarak tanımlamamalıdır.

## Önerilen düzeltme

§14 next-action block şu şekilde ayrılmalıdır:

```text
Next actions after independent freeze-record audit PASS:

1. F3 STEP-2 implementation-pin task
   CLASS_C only:
   - ACF library/API verification
   - spline implementation pins
   - probe masks
   - fold-scheme implementation exactness
   - synthetic qualification only

2. Separately governed R-REV 6B companion specification task
   - separate artifact
   - separate provenance
   - separate independent audit
   - specification only
   - no 6B execution
```

Ardından:

```text
F3_EXECUTION_READY remains false until all required
pre-execution governance closures have independently passed.
```

yazılmalıdır.

Bu scientific PI kararını değiştirmez; yalnız governance path’i exact hale getirir.

```text
classification = gate-specific blocker
```

---

# 2. Cleanup — DISC-F3-04 C5 için “paired-valid set” dili

DISC-F3-04 şu mantıkla başlamaktadır:

```text
the completeness requirement is imposed jointly on all sub-fits
that define a criterion's paired-valid set
```

ve sonra:

```text
C2: 10 sub-fits
C4b: 4 probes
C5: 5 folds
```

demektedir.

Ancak r4’te C5:

```text
valid set = crossfit-complete trajectories of the family
family_complete_share >= c_complete
absolute criterion — no pairing
```

olarak tanımlıdır.

Dolayısıyla C5 bir `paired-valid set` değildir.

## Önerilen düzeltme

```text
the completeness requirement is imposed jointly on all sub-fits
that define a criterion's valid / paired-valid set
```

ifadesi kullanılmalıdır.

Bu scientific interpretation’ı değiştirmez.

```text
classification = cleanup
```

---

# 3. Cleanup — `v4 this file` lineage wording’i

§13 freeze-record structure içinde:

```text
execution_prompt_lineage =
...
v4 this file
```

ifadesi yer almaktadır.

Prompt içinde bu anlaşılabilir olsa da, block freeze record’a verbatim geçtiğinde `"this file"` ifadesi freeze record’un kendisini çağrıştırabilir.

## Önerilen daha exact wording

```text
v4 = execution_prompt
     observed SHA256 = <computed from dispatched v4 prompt>
```

veya:

```text
v4 = Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md
     SHA256 = value recorded in execution_prompt field
```

Bu yalnız provenance clarity düzeltmesidir.

```text
classification = cleanup
```

---

# 4. v3 bulgularının closure durumu

| v3 finding | v4 sonucu |
|---|---|
| K-05 `U4_s=n_s` ambiguity | **CLOSED** |
| DISC-F3-05 906 aggregation wording | **CLOSED** |
| stale parent lineage | **CLOSED** |
| custody 1–10 → 1–16 | **CLOSED** |
| extra q examples | **CLOSED** |
| 6B ratio `>=1` unconditional | **CLOSED** |
| common-support overstatement | **CLOSED** |
| PI dispatch attestation | **korunmuş ve doğru** |

---

# 5. Nihai sınıflandırma

```text
global blocker = none

gate-specific blocker =
  F3-STEP1-6B-GOV-01
  6B separate R-REV governance
  vs F3 STEP-2 CLASS_C bundling

cleanup =
  1. DISC-F3-04 valid / paired-valid wording
  2. execution_prompt_lineage "v4 this file" wording

informational =
  all v3 findings successfully closed
```

---

# 6. Puan

```text
v3 ≈ 9.7 / 10
v4 ≈ 9.85 / 10
```

Freeze artifact olduğu için kalan governance çelişkisi bırakılmamalıdır.

---

# 7. Önerilen sonraki adım

```text
v4 -> v5
narrow exactness / provenance cleanup only

PI scientific decisions changed = 0
numeric literal change = 0
new methodology review = false
F2 remains CLOSED
r4 remains read-only
F3 execution remains prohibited
```

v5 yalnız şu üç değişikliği yapmalıdır:

```text
1. Separate 6B R-REV specification from CLASS_C / F3 STEP-2 task
2. DISC-F3-04 "paired-valid set" -> "valid / paired-valid set"
3. execution_prompt_lineage "v4 this file" wording cleanup
```

Bu:

```text
1 governance blocker + 2 cleanup
```

kapandıktan sonra yeni bir substantive review cycle açılmasını gerektiren bir neden görünmemektedir.

Bu durumda:

```text
dispatch_ready = true
```

kararı verilebilir.

F2 yeniden açılmaz.  
r4 rewrite edilmez.  
Yeni methodology review açılmaz.  
F3 execution freeze-record task sırasında başlamaz.
