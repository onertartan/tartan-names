# Claude Code Prompt — FINAL
## v4(r2) → v4(r3) + freeze-v0(r3) → r4 ICL / FCSP / Gap / t5 Correction
**Execution date:** 2026-08-19

## Görev durumu

Mevcut yürütmeyi DURDUR.

Bu görev:
- yeni yöntem taraması değildir,
- yeni metodoloji tasarlama turu değildir,
- yeni null ailesi açma turu değildir,
- Gap veya t5 için yöntem seçme turu değildir,
- frozen çalışmanın kapalı kararlarını yeniden açma turu değildir.

Amaç yalnızca:
1. `yol_haritasi_v4_FINAL_2026-08-18.md` iç revizyonunu **r2 → r3** yapmak,
2. `extension_decision_freeze_v0.md` iç revizyonunu **r3 → r4** yapmak,
3. yanlış soft-entropy ICL pinini MAP-classification `ICL_BIC` approximation ile düzeltmek,
4. FCSP semantiğini `H0_no_structure` ile netleştirmek,
5. Gap birincil atfını düzeltmek fakat exact `W_k` politikası SEÇMEMEK,
6. t5 exact DGP tasarımını SEÇMEMEK,
7. eski change report’u tarihsel kayıt olarak KORUYUP yeni correction report oluşturmak,
8. prompt → roadmap → freeze hash bağımlılık sırasını deterministik hale getirmek,
9. non-finite criterion davranışını frozen S-04 failure politikasına bağlamak,
10. posterior clipping/floor serbestliğini kapatmak,
11. beklenmeyen/stale sidecar için STOP davranışını tanımlamak,
12. preapproval draft hash ile final freeze hash’i açıkça ayırmak,
13. henüz final freeze sidecar üretmemek ve FROZEN statüsüne geçmemek.

---

# 0. BAĞLAYICI PROMPT HASH — İLK ADIM

Bu prompt dosyasını önce finalize et.

Ardından:

```bash
sha256sum chatgpt_claude_prompt_v4r3_freeze_r4_ICL_FCSP_gap_t5_correction_FINAL_2026-08-19.md
```

ile **full SHA256** hesapla.

Bu hash hesaplandıktan sonra prompt dosyasını DEĞİŞTİRME.

Yeni prompt’un dosya adı ve full SHA256 değeri şu iki yerde provenance olarak kullanılacak:
1. roadmap r3 revision provenance alanında,
2. freeze r4 §9.2 informational provenance bölümünde.

Bu prompt hash’i roadmap r3 hash’i hesaplanmadan ÖNCE roadmap’e yazılmalıdır.

---

# 1. BAĞLAYICI KAYNAKLAR

Aktif kanonik belgeler:
- `yol_haritasi_v4_FINAL_2026-08-18.md` — şu an iç revizyon r2
- `extension_decision_freeze_v0.md` — şu an iç revizyon r3

Tarihsel audit trail:
- `v4r2_freeze_r3_change_report_2026-08-18.md`

Bu dosya **yerinde değiştirilmez**.

Yeni correction report:

```text
v4r3_freeze_r4_ICL_correction_change_report_2026-08-19.md
```

olacak.

Roadmap dosya adı kanonik olarak DEĞİŞMEZ:

```text
yol_haritasi_v4_FINAL_2026-08-18.md
```

Ancak roadmap içindeki yeni `r3 revision date = 2026-08-19` olmalıdır.

Freeze r4 revision date de:

```text
2026-08-19
```

olmalıdır.

Frozen normatif bağımlılıklar:
- `01_kosum_protokolu_v5_3.md`
- `kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md`
- `run_matrix_v4.csv`

Tam SHA256’lar aktif kanonik belgelerdeki değerlerle doğrulanmalı; uyuşmazlıkta STOP.

---

# A. ICL — GLOBAL FREEZE BLOCKER, ŞİMDİ DÜZELT

## A1. Aktif yanlış tanımı kaldır

Aktif normatif belgelerde aşağıdaki soft-entropy criterion artık kullanılmayacak:

\[
E_{\mathrm{soft}}(k)
=
-\sum_i\sum_c \tau_{ic}\log\tau_{ic}
\]

ve:

\[
ICL_{\mathrm{stored}}(k)
=
BIC_{\mathrm{stored}}(k)
+
2E_{\mathrm{soft}}(k).
\]

Aktif normatif bağlamda aşağıdaki ifadeleri kaldır:

```text
Exact ICL
soft entropy is the Biernacki–Celeux–Govaert mapping
E(k) = -sum_i sum_c tau_ic log tau_ic
```

Tarihsel/superseded dosyalarda bu eski tanım kalabilir; onları değiştirme.

## A2. Yeni bağlayıcı tanım

Posterior sorumluluklar:

\[
\tau_{ic}=P(z_i=c\mid x_i,\hat\theta_k).
\]

Her gözlem için MAP bileşeni:

\[
c_i^*(k)=\arg\max_c \tau_{ic}.
\]

Classification uncertainty:

\[
E_{\mathrm{MAP}}(k)
=
-\sum_i \log\left(\max_c \tau_{ic}\right).
\]

Eşdeğer gösterim:

\[
E_{\mathrm{MAP}}(k)
=
-\sum_i\sum_c \hat z_{ic}\log\tau_{ic},
\]

burada:

\[
\hat z_{ic}=\mathbf 1[c=c_i^*(k)].
\]

Sklearn stored-BIC convention:

\[
BIC_{\mathrm{stored}}(k)
=
-2\log\hat L_k+p_k\log n.
\]

Yeni kriter:

\[
\boxed{
ICL_{\mathrm{BIC,stored}}(k)
=
BIC_{\mathrm{stored}}(k)+2E_{\mathrm{MAP}}(k)
}
\]

Yön:

```text
direction = argmin
```

Adlandırma:

```text
ICL_BIC approximation — frozen criterion definition
```

veya anlamca eşdeğer:

```text
BIC-approximated ICL criterion
```

`Exact ICL` ifadesini kullanma.

## A3. Candidate support — DEĞİŞMEZ

```text
native candidate support = k=1..10
restricted sensitivity   = k=2..10
```

## A4. Non-finite / failure sırası — S-04 ÖNCE

Tie-selection bloğu non-finite criterion değerlerini kendi başına veya sessizce ELEMEYECEK.

Bağlayıcı sıra:

```text
raw likelihood / posterior / criterion
→ frozen S-04 failure/non-finite policy
→ eligible criterion set
→ criterion minimum
→ tie set
→ smallest-k selection
```

Normatif cümle:

> *Before criterion minimization or tie-set construction, apply the frozen S-04 non-finite/failure policy. The tie-selection block must not independently or silently discard a non-finite candidate. The tie algorithm receives only criterion values that remain eligible after application of the frozen failure policy. If no eligible finite criterion value remains, the selector is recorded as failed under the frozen failure policy and no k_hat is produced.*

Pseudo-code:

```python
# eligible_criterion_values is produced only after applying
# the frozen S-04 failure/non-finite policy.

if not eligible_criterion_values:
    record_selector_failure_according_to_frozen_S04()
    k_hat = not_produced
else:
    criterion_min = min(eligible_criterion_values.values())

    tied_k = [
        k
        for k, value in eligible_criterion_values.items()
        if np.isclose(
            value,
            criterion_min,
            rtol=1e-10,
            atol=1e-12,
        )
    ]

    k_hat = min(tied_k)
```

Normatif ek:

> *The pseudo-code does not mandate a new exception class, error code or implementation mechanism; the existing frozen S-04 representation must be used.*

Tie cümlesi:

> *The tie set consists of all candidate k values whose eligible criterion value is `np.isclose` to the eligible global minimum under `rtol=1e-10` and `atol=1e-12`; the smallest k in that set is selected.*

## A5. Posterior doğrulama — CLIPPING YOK

Yeni epsilon clipping, posterior floor veya ad-hoc repair kuralı EKLEME.

Bağlayıcı hüküm:

> *No epsilon clipping or posterior-floor rule is introduced for the MAP-classification ICL_BIC criterion. After verifying that each posterior row is finite, nonnegative and approximately sums to 1, E_MAP is computed directly from max_c tau_ic. For a valid posterior row, max_c tau_ic >= 1/k and is therefore strictly positive. An invalid posterior row is handled under the frozen failure/non-finite policy rather than repaired by clipping.*

Exact posterior row-sum validation tolerance bu görevde bilimsel selector pini DEĞİLDİR.

Normatif cümle:

> *The exact posterior row-sum validation tolerance is an implementation validation detail to be pinned in the preregistration/unit-test layer. It must not alter E_MAP, introduce clipping, renormalize invalid rows or override the frozen S-04 failure policy.*

Claude Code bu görevde yeni bir posterior row-sum tolerance SEÇMEYECEK.

## A6. MAP component tie

Component-level MAP tie logging’i zorunlu bilimsel gate yapma.

Gerekçe:

\[
E_{\mathrm{MAP}}
=
-\sum_i\log \max_c\tau_{ic}
\]

yalnız maksimum posterior değerine bağlıdır; aynı maksimum değeri paylaşan component etiketlerinden hangisinin seçildiği criterion değerini değiştirmez.

İmplementasyon deterministik component tie davranışını provenance’da belgeleyebilir, fakat bu core freeze için yeni bilimsel pin değildir.

## A7. Unit test kapsamı

Birim test daha sonra uygulanabilir; fakat test edilecek bilimsel tanım ŞİMDİ donuyor.

Test en az şunları doğrulasın:
- `predict_proba` en iyi yakınsamış fit’e aittir,
- posterior satırları finite, nonnegative ve yaklaşık 1’e toplamaktadır,
- posterior için epsilon clipping/floor uygulanmaz,
- invalid posterior satırı frozen S-04 failure politikasına gider,
- posterior row-sum tolerance yalnız validation detayıdır ve criterion’u değiştirmez,
- `k=1` için `E_MAP=0` ve `ICL_BIC=BIC`,
- criterion tie-set algoritması yukarıdaki exact kuralla çalışır,
- bağlı criterion değerlerinde en küçük `k` seçilir,
- native 1..10 ve restricted 2..10 ayrı test edilir.

---

# B. FCSP — SEMANTİK TEMİZLİK, ESTIMAND DEĞİŞMEZ

Bu temizlik bu revizyonda UYGULANACAK.

## B1. Null truth state

Aktif iki kanonik belgede şu semantik alanları kullan:

```text
null_state                 = H0_no_structure
null_DGP                   = no_cluster_pure_noise
null_truth_tabulation_code = 1
no_structure_decision      = (k_hat = 1)
false_structure_decision   = (k_hat > 1)
```

Primary estimand:

\[
\boxed{
FCSP=P(\hat{k}>1\mid H_{0,\mathrm{no\text{-}structure}})
}
\]

Açıklayıcı pin:

> *Under the pure-noise null, the truth state is H0_no_structure. A value of 1 may be retained solely as a storage or tabulation code, while k_hat=1 is the selector’s operational no-structure decision. Neither convention asserts the existence of one nontrivial generative latent cluster.*

## B2. Aktif etiketleri hizala

Aktif `k_true=1 null block` etiketlerini:

```text
H0_no_structure pure-noise null block
(legacy/tabulation truth code: 1)
```

veya anlamca eşdeğer kısa etiketle değiştir.

## B3. FCSP eligibility — DEĞİŞMEZ

Şu kural aynen korunur:

> **FCSP-eligible selectors are only those within the frozen extension method-space whose preregistered native or arm-specific decision rule explicitly permits k=1. No ad-hoc post-selection fallback to k=1 is allowed.**

---

# C. GAP — YALNIZ ATIF TEMİZLİĞİ; METODOLOJİ SEÇME

## C1. Birincil atfı düzelt

Gap Statistic primary method source:

> Tibshirani, Walther & Hastie (2001), *Estimating the Number of Clusters in a Data Set via the Gap Statistic*.

Mevcut projedeki ikincil kaynak:

```text
existing operational variant source =
  the already recorded Şenbabaoğlu source
```

Claude Code bu görevde:
- yeni ikincil kaynak SEÇMEYECEK,
- mevcut kaynağı alternatif bir kaynakla DEĞİŞTİRMEYECEK,
- `/ applicable source` gibi açık uçlu ifade kullanmayacak.

Normatif kural:

> *Claude Code must not replace, expand or select an alternative operational-variant source in this task. If the existing Şenbabaoğlu bibliographic record is insufficient for an exact citation, STOP and report the missing metadata to Öner.*

## C2. Exact W_k politikasını SEÇME

Aktif durum:

```text
Gap_Wk_policy  = unresolved
Gap_arm_status = NO-GO
```

Aktif belgede şu gate yer alsın:

> *Exact W_k definition, distance convention, reference generator, candidate space, decision rule, tie rule and failure policy must be approved and signed before the Gap arm can run. Claude Code must not choose among alternative W_k policies.*

## C3. Gap koşumu YASAK

Bu görevde:
- Gap implementasyonu yapılmaz,
- Gap smoke run yapılmaz,
- Gap full run yapılmaz.

Gap-arm NO-GO kalır. Core freeze’i bu yüzden durdurma.

---

# D. t5 — EXACT DGP SEÇME; ARM NO-GO KORU

`t5` conditional sensitivity DGP koludur.

Bu görevde Claude Code exact t5 DGP seçmeyecek.

Aktif belgede:

```text
t5_arm_status = NO-GO until signed DGP preregistration
```

Zorunlu future prereg fields:

```text
distribution_family
degrees_of_freedom
location_convention
variance_or_scale_convention
white_vs_AR_role
AR_innovation_and_stationary_variance_policy
AR_initialization_or_burnin
sigma_application_point
row_z_normalization_order
RNG_namespace
failure_and_nonfinite_policy
```

Normatif cümle:

> *Claude Code must not select, implement or run the t5 arm until the exact DGP fields are explicitly approved and signed by Öner.*

---

# E. CHANGE REPORT PROVENANCE — ESKİ RAPORU KORU

Mevcut:

```text
v4r2_freeze_r3_change_report_2026-08-18.md
```

dosyasını DEĞİŞTİRME.

Yeni dosya oluştur:

```text
v4r3_freeze_r4_ICL_correction_change_report_2026-08-19.md
```

Yeni rapor açıkça şunları içersin:

```text
supersedes_scientific_conclusion_of =
  v4r2_freeze_r3_change_report_2026-08-18.md

reason =
  soft-posterior entropy was incorrectly identified as the
  Biernacki–Celeux–Govaert MAP-classification ICL_BIC approximation

previous_freeze_status = ONAY BEKLİYOR
post_freeze_deviation_required = false
global_status_before_correction = NO-GO
global_status_after_successful_correction = READY_FOR_OWNER_REVIEW
```

## E1. Correction report hash lineage alanları

Yeni correction report en az şu lineage alanlarını içersin:

```text
binding_prompt_filename
binding_prompt_sha256

input_roadmap_revision = r2
input_roadmap_sha256 =
  0c80c1894ebe5cba00ed9e76d57aa5131c564365fbcfea1815db31fff39e3915

output_roadmap_revision = r3
output_roadmap_sha256

input_freeze_revision = r3
input_freeze_lineage_sha256 =
  e45b4486181fa833657fe6059ad066dd8ae95c118238a9b6e04d8ccab5714ce5

output_freeze_revision = r4
output_freeze_preapproval_draft_sha256
output_freeze_hash_status = informational_lineage_only
```

Correction report kendi hash’ini kendi içine YAZMAYACAK.

---

# F. HASH BAĞIMLILIK SIRASI — BAĞLAYICI

İşlem sırası aşağıdaki gibidir ve DEĞİŞTİRİLMEZ.

## F0. Prompt ve pre-edit provenance doğrulaması

0. Bu prompt dosyasını finalize et.

1. Prompt full SHA256 değerini hesapla.

2. Bu noktadan sonra prompt dosyasını değiştirme.

3. Herhangi bir kanonik belgeyi değiştirmeden önce şu dosyanın varlığını kontrol et:

```text
extension_decision_freeze_v0.md.sha256
```

4. Sidecar VARSA:
   - G1 uyarınca STOP et,
   - sidecar’ı overwrite etme,
   - silme,
   - geçerli final sidecar olarak kabul etme,
   - roadmap veya freeze üzerinde HİÇBİR değişiklik yapma.

5. Sidecar YOKSA mevcut input dosyalarının full SHA256 değerlerini hesapla ve doğrula:

```text
yol_haritasi_v4_FINAL_2026-08-18.md
expected r2 SHA256 =
0c80c1894ebe5cba00ed9e76d57aa5131c564365fbcfea1815db31fff39e3915

extension_decision_freeze_v0.md
expected r3 lineage SHA256 =
e45b4486181fa833657fe6059ad066dd8ae95c118238a9b6e04d8ccab5714ce5
```

6. Herhangi bir başlangıç hash’i beklenen değerle eşleşmiyorsa STOP et.
   Roadmap veya freeze üzerinde değişiklik yapma.

7. Şu tarihsel raporun başlangıç full SHA256 değerini audit amacıyla kaydet:

```text
v4r2_freeze_r3_change_report_2026-08-18.md
```

Bu değer:

```text
historical_change_report_preedit_sha256
```

olarak tutulacak.

8. Frozen normatif bağımlılıkların üç full SHA256 değerini doğrula:

```text
01_kosum_protokolu_v5_3.md
kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md
run_matrix_v4.csv
```

Aktif kanonik belgelerdeki beklenen full SHA256 değerleriyle herhangi bir uyuşmazlıkta STOP et.

9. Yalnız bütün preflight kontrolleri PASS ise roadmap r3 düzenlemesine başla.

Bağlayıcı preflight sırası:

```text
prompt finalize/hash
→ sidecar absence check
→ input roadmap r2 hash verification
→ input freeze r3 hash verification
→ historical report baseline hash
→ frozen dependency verification
→ roadmap r3 editing
```

## F1. Roadmap r3

10. Prompt dosya adı + full SHA256 değerini roadmap r3 revision provenance alanına ekle.

11. Roadmap r3 revision date:

```text
2026-08-19
```

olmalı.

12. Roadmap r3 içinde:
   - ICL düzeltmesini,
   - FCSP semantik temizliğini,
   - Gap primary citation temizliğini,
   - Gap arm-NO-GO metnini,
   - t5 arm-NO-GO metnini

   tamamla.

13. Başka bilimsel karar değiştirme.

14. Roadmap r3’ü tamamen finalize et.

15. Roadmap r3 full SHA256 değerini hesapla.

## F2. Freeze r4

16. `extension_decision_freeze_v0.md` dosyasını iç revizyon r4 olarak güncelle.

17. Freeze r4 revision date:

```text
2026-08-19
```

olmalı.

18. Freeze §9.1’de eski roadmap r2 hash’ini kaldır.

19. Yeni roadmap r3 full SHA256 değerini normatif bağımlılık olarak yaz.

20. Yeni prompt’un:
    - dosya adını,
    - full SHA256 değerini

    freeze r4 §9.2 informational provenance bölümüne ekle.

21. ICL ve FCSP düzeltmelerini freeze r4’e aynı anlamla taşı.

22. Gap primary citation temizliğini yap.

23. Gap/t5 arm-NO-GO durumlarını açık tut.

24. Freeze r4’ü finalize et.

## F3. Correction report

25. Yeni:

```text
v4r3_freeze_r4_ICL_correction_change_report_2026-08-19.md
```

dosyasını oluştur.

26. Repo-geneli normatif tutarlılık denetimi yap.

Hash DAG:

```text
binding prompt
→ pre-edit provenance gate
→ roadmap r3
→ roadmap r3 hash
→ freeze r4
→ correction report
```

# G. SIDECAR / HASH / COMMIT / FREEZE KURALI

## G1. Görev başlangıcında mevcut sidecar denetimi

Görev başında:

```text
extension_decision_freeze_v0.md.sha256
```

var mı kontrol et.

Varsa:
- overwrite ETME,
- silme,
- geçerli final sidecar olarak kabul ETME.

STOP et ve raporla:

```text
existing_sidecar_sha256
document_hash_recorded_inside_sidecar
does_it_match_current_unapproved_freeze_document
git_status
known_provenance
```

## G2. Bu görevde final sidecar YOK

Başlangıçta sidecar yoksa bu görev içinde oluşturma.

Ayrıca:
- approval checkbox işaretlenmeyecek,
- `ONAY BEKLİYOR` korunacak,
- final tag oluşturulmayacak,
- FROZEN statüsüne geçilmeyecek.

## G3. Öner onayı sonrası final akış

Bu görevden SONRA:

```bash
sha256sum extension_decision_freeze_v0.md   > extension_decision_freeze_v0.md.sha256

sha256sum -c extension_decision_freeze_v0.md.sha256
```

Final freeze document + matching sidecar aynı final commit/tag altında bulunmalı.

---

# H. HASH STATÜLERİ — ADLANDIRMA ZORUNLU

Görev sonu devir notunda:

```text
binding_prompt_sha256 =
  binding-instruction provenance hash

roadmap_r3_sha256 =
  normative dependency hash

freeze_r4_preapproval_draft_sha256 =
  informational lineage hash only; NOT the final freeze hash

correction_report_sha256 =
  correction-report provenance hash
```

Normatif cümle:

> *The preapproval draft hash must not be written into extension_decision_freeze_v0.md and must not be presented as the final freeze hash.*

---

# I. ZORUNLU AUDIT

Beklenen:

```text
active normative "Exact ICL" occurrences      = 0
active normative soft-entropy ICL occurrences = 0
MAP-classification ICL_BIC present            = yes
old roadmap r2 hash in freeze §9.1            = 0
self-hash field                                = 0
approval checkbox                              = unchecked
final sidecar                                  = absent
```

Ayrıca:

```text
H0_no_structure present
null_DGP = no_cluster_pure_noise
null_truth_tabulation_code = 1

Gap_Wk_policy = unresolved
Gap_arm_status = NO-GO

t5_arm_status = NO-GO until signed DGP preregistration

frozen S-04 failure policy
→ eligible criterion set
→ minimum
→ tie set
→ smallest k

no epsilon clipping
no posterior floor
invalid posterior → frozen S-04 failure policy
row-sum validation tolerance = implementation validation detail only
```

Repo-geneli grep tarihsel dosyalarda eski soft-entropy tanımını bulabilir; bu tek başına hata değildir.

Audit kapsamı şu şekilde ayrılır:

```text
operative normative ICL definition:
  no soft-entropy formula or soft-entropy criterion allowed

revision-history/provenance text inside an active document:
  may state that the prior soft-entropy definition was withdrawn,
  but must not reproduce or endorse it as the active criterion
```

Tercih edilen revizyon-notu dili:

```text
the prior misidentified ICL criterion was withdrawn and replaced
with the MAP-classification ICL_BIC approximation
```

Aktif normatif belgelerde eski formül veya soft-entropy criterion aktif tanım olarak kalmamalıdır.

---


## I7. Tarihsel change report bütünlük denetimi

Görev sonunda şu dosyanın final full SHA256 değerini yeniden hesapla:

```text
v4r2_freeze_r3_change_report_2026-08-18.md
```

Bağlayıcı koşul:

```text
historical_change_report_postedit_sha256
==
historical_change_report_preedit_sha256
```

Normatif cümle:

> *The final SHA256 of `v4r2_freeze_r3_change_report_2026-08-18.md` must equal its recorded pre-edit SHA256. If it differs, audit = FAIL.*

Bu dosyada herhangi bir değişiklik saptanırsa:
- audit = FAIL,
- freeze-ready ilan etme,
- STOP ve Öner’e raporla.


# J. DEĞİŞTİRİLMEYECEK KAPALI KARARLAR

DOKUNMA:

- class identity = shape + location
- DTW/elastik mesafeler yok
- signed rho_max
- theta_spread = arctan(sigma)
- k_true=2 original benchmark dışında
- primary Friedman all-cells
- AR-only secondary
- Friedman → Holm → Nemenyi exact hierarchy
- 100-seed cell aggregation
- PAM-Euclidean pins
- spherical KMeans first-ring status
- PBM first-ring status
- Average linkage sensitivity_only
- Jump excluded
- m–k observed-support response surface
- formal_interaction_test=false
- phi_support={0.80,0.90,0.97,0.99}
- sigma_support={0.1,...,1.0} yalnız phi×sigma ana extension bloğunda
- sigma_null=not_applicable
- single_prototype_null=excluded_from_extension
- null n/noise/seed support
- BIC native 1..10 / restricted 2..10
- Ward+CH frozen deployment
- diagnostic arm pin eksiği global core’u durdurmaz
- extension original confirmatory analysis değildir
- yeni method search açılmaz

---

# K. EXECUTION PROHIBITION

Bu düzeltme turunda YASAK:

- Friedman çalıştırmak,
- GLMM çalıştırmak,
- SSA deployment çalıştırmak,
- Gap implement etmek/koşmak,
- t5 implement etmek/koşmak,
- extension simulation çalıştırmak,
- smoke run yapmak,
- full run yapmak,
- yeni method/factor/null/candidate eklemek,
- sonuç görerek methodological seçim yapmak.

Belirsizlik varsa:

> **STOP and return the ambiguity to Öner. Claude Code must not propose or choose a methodological solution.**

---

# L. ÇIKTILAR

Üret:

1. `yol_haritasi_v4_FINAL_2026-08-18.md` — iç revizyon r3, revision date `2026-08-19`
2. `extension_decision_freeze_v0.md` — iç revizyon r4, revision date `2026-08-19`, **ONAY BEKLİYOR**
3. `v4r3_freeze_r4_ICL_correction_change_report_2026-08-19.md`

Korunacak ve değiştirilmeyecek:

```text
v4r2_freeze_r3_change_report_2026-08-18.md
```

Görev sonunda devir notu:

```text
binding_prompt_sha256
roadmap_r3_sha256
freeze_r4_preapproval_draft_sha256
correction_report_sha256
historical_change_report_preedit_sha256
historical_change_report_postedit_sha256
historical_change_report_unchanged = true|false
audit PASS/FAIL
Gap arm status
t5 arm status
freeze status = ONAY BEKLİYOR
final sidecar status = ABSENT
```

FAIL varsa freeze-ready ilan etme; dur ve raporla.

---

# M. NİHAİ HEDEF

```text
ICL scientific definition        = corrected
ICL failure-order                = frozen S-04 first
ICL posterior clipping           = prohibited
posterior row-sum tolerance      = validation-only, not criterion tuning
FCSP semantics                   = clarified
Gap primary citation             = corrected
Gap operational source           = existing Şenbabaoğlu only
Gap exact W_k                    = unresolved / arm NO-GO
t5 exact DGP                     = unresolved / arm NO-GO
historical r2/r3 change report   = preserved + hash-verified unchanged
new r3/r4 correction report      = 2026-08-19
binding prompt hash              = recorded before roadmap hash
roadmap hash dependency          = updated correctly
stale sidecar behavior           = STOP/report
freeze draft hash                = lineage only
freeze status                    = ONAY BEKLİYOR
final sidecar                    = NOT CREATED
```

Bundan sonra yalnız Öner incelemesi/onayı ile final freeze sidecar + commit/tag yapılacaktır.
