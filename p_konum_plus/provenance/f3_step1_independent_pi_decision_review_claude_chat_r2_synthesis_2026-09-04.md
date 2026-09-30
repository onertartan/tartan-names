# F3 STEP 1 — Independent PI Decision Review (Claude Chat) — r2 SYNTHESIS

```text
project        = SSA Application-Calibrated Clustering Benchmark / p_konum_plus
artifact       = f3_step1_independent_pi_decision_review_claude_chat_r2_synthesis_2026-09-04.md
date           = 2026-09-04
author_role    = Claude Chat — independent panel member + meta-reviewer (non-normative channel)
status         = NON-NORMATIVE recommendation; non-binding until explicit PI ACCEPT/MODIFY per row
gate_context   = F3 STEP 1 ratification closure (F3_ENTRY_READY = true, F3_EXECUTION_READY = false)

supersedes     = f3_step1_independent_pi_decision_review_claude_chat_2026-09-04.md   (r1)
                 SHA256 f8264874dfaa09032d45f110736e380084c1c226aac081faada91c5a3716d475
                 r1 retained as historical; r2 decision content prevails

active_candidate (per panel documents; NOT accessed in this channel)
  f3_step1_r1_corrected_ratification_candidate_r3_2026-09-03.md
  SHA256 350bc15e5c18e3dddb219e5e6b54926910fbac6b0f98ed8b498f128fe3fb95ad
  r3 literals cited below (delta_4_RMSE = 0.10 with alternatives 0.05/0.20, tau_4b_RMSE = 0.02,
  c_ident = 0.85, c_complete = 0.90, E = 15, K = 5, g = 0, V4_s = 4-probe intersection,
  sex-level statistic = median) are AS REPORTED by ChatGPT-2 / Fugu-2 / Manus-2 — UNVERIFIED (KONTROL)

normative source (not accessed)
  ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
  SHA256 d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3

panel inputs (SHA256 computed in this session)
  Manus.md    = 2bf19dd8c2992b10a847e5e8004b83068167f950b790d38cc3fd33007539a1a7
  minimax.md  = 5edaafbab16ed9c9067c1f4d48e98251c9519aed8e8e99028bb90ee2ef972104
  qwen.md     = 665318e61f2099ba790382075d5100df42f6d7afa9d8316a6d9f618458a2ad4c
  chatgpt.md  = 96afa0480f85e9cc64332970b17e957e682470a6c38ed5bbfddffa4ff2d1201a
  fugu.txt    = ca6d276c174168a3c1539caf93ba84d2fb2047c6af796b009ea0cd5d49e96c56
  Kimi.md     = 6349c5412dd8cc35cc43a13bcb939f39f6e7bdb59e03e61aba0a8ed6c4b80db3
  chatgpt2.md = b6a530c6be992df83b88dc94525bb314382c5bd68e2b91bf01d78443d02dfdb4
  fugu2.md    = 3d9287b67eb077ddcd0a84cea88b410406afc609088e74223c380ff55f756bf7
  manus2.md   = eb0732c891a48901fb07a6fdcb3a53d671c2be73bc3a88e41c74fd4eff091ce6

scope_limits_honoured
  F2_reopened = false · new_primary_generator_proposed = false · DTW_or_elastic_alignment_proposed = false
  R_REV_silently_resolved = false · empirical_outcome_assumed = false
  P03_threshold_value_assumed = false · Ward_CH_frozen_winner_used = false
  candidate_specific_fit_before_ratification_recommended = false

self_hash      = external sidecar (.sha256)
```

---

## 0. r1 → r2 değişiklik özeti

| Öğe | r1 | r2 | Neden |
|---|---|---|---|
| C4b_status | P03_GATE (7) | **P03_GATE (8)** | Panel 6/7; `delta_4_RMSE = 0.10` r3'te predeclared; tek muhalefet (Qwen) iç tutarsız |
| AGG-L1 | WORSE (6) | **WORSE (7; K1 = median doğrulanırsa 8)** | Ç-1 seyrelme + Ö-5 heterojen failure mekanizması; iki reviewer SEPARATE→WORSE döndü; 5/7 |
| D-P03-6 | 6A + 6B packet'te, MODIFY (6) | **6A ACCEPT + ayrı yönetilen 6B companion (6)** | Ç-3: packet-parsimony itirazı kabul; trigger-1 zamanlaması companion artifact ile korunur |
| D-P03-7 | Option A (9) | **Option A (9)** | Panel 7/7 |
| c_complete | 0.90 (6) | **0.90 (7)** | Dropout bound synthesis'e alındı; K1 = median raporlandı; compounding aritmetiği (Manus-2) |
| Yeni | — | K-05 disclosure (M3) · D-P04 ortak destek (M8, Ö-6) · both-fail branch kontrat metni (M7) | Panel yakınsaması + Manus-2 bulgusu |

Literal değişikliği: **sıfır**. Değişen şey, koşulların raporlama niyeti değil hash'lenebilir kontrat metni olması gerektiğidir.

---

## 1. Karar tablosu

| Decision | Choice | Confidence 0–10 | Main reason | Strongest argument against |
|---|---|---:|---|---|
| C4b status | **A = P03_GATE** | 8 | C4a solver-feasibility ölçer; identifiability'yi setteki tek ölçen C4b. Pencere censoring'i (1880–2025) SSA verisinin yapısal özelliği; kalibrasyon için birinci-derece | Self-referential, common-mode-blind bir istatistiğin hard gate olması; C4b iyi ise edge doğru demek değildir |
| C4 L/R aggregation | **WORSE** (+ per-side report-only) | 7 | Median altında SEPARATE'in yan gate'leri seyrelir ve heterojen tek-taraflı failure'ı kaçırır; max her yörüngenin zor kenarını etiketsiz seçer | LEFT/RIGHT ayrı estimand'dır; max yön bilgisini sıkıştırır; family ile spline'ın max'ı farklı kenardan gelebilir |
| D-P03-6 | **6A** (+ ayrı yönetilen 6B companion önerisi) | 6 | Claim doğru sınırlanır, 906 korunur, screen yok; common-mode riski packet içinde ölçülmez, disclose edilir | Temsiliyet sorusu sayıyla değil disclaimer ile karşılanır; companion reddedilirse risk yalnız sözel sınırlanır |
| D-P03-7 architecture | **Option A** | 9 | Option B tek numerik olayı criterion failure'a çevirir; 5 fold × 2 probe × spline zinciriyle yıkıcı; P-01 plateau'sunu adequacy-dışı eleyiciye dönüştürür | Paired-valid tek başına easy-case advantage'ı önlemez; %10 düşen küme sistematik olarak zor olabilir |
| c_complete | **0.90** | 7 | Adversarial-dropout bound: q = 0.10 medyanı [45., 55.] yüzdelik bandına sınırlar; compounding altında 0.95 numerik Type-I, 0.85 bandı [42.5, 57.5]'e açar | Uniform eşik sub-fit sayısı farklı criterion'larda eşit sertlikte değil (C2: 10 sub-fit, C4b: 4 probe) |

---

## 2. A. Independent recommendation (synthesized)

### A1. C4b_status = P03_GATE — ACCEPT

C4a, truncated veride optimizer'ın Kural T/S'yi sağlayan bir fit üretip üretmediğini ölçer: solver-feasibility. Truncated fit başka bir fonksiyon basin'ine otursa da C4a "başarı" sayar. Aynı veriden aynı fonksiyonun geri gelip gelmediğini yalnız C4b ölçer. REPORT_ONLY seçilirse criterion 4, "censored identifiability" adını taşıyıp identifiability ölçmeyen bir criterion olur.

Zorunluluk: 1880–2025 penceresi sol/sağ censoring'i SSA verisinin yapısal özelliği yapar; kalibrasyon, pencere-kesikli gerçek yörüngelerden parametre tahminidir; truncated veriden stabil tanımlanamayan bir family kalibre edilemez.

Common-mode blindness gate statüsüne karşı argüman değil, yorum sınırıdır; misspecification tespiti C2/C3'ün görevidir (K4). Type-I/II asimetrisi: REPORT_ONLY'nin Type-II maliyeti F12'ye kadar görünmez ve kalıcıdır; P03_GATE'in Type-I maliyeti both-fail branch ile görünür ve yönetilebilirdir.

`delta_4_RMSE`: r3'te 0.10, predeclared alternatifler 0.05/0.20 (Fugu-2'ye göre). **0.10 korunur.** Fugu-2'nin 0.20 önerisi predeclared alternatifler içinde ve a priori olduğundan ihlal değildir; ama "istiflenen konservatiflik" bir türetim değildir ve kısmen kör bir metrikte toleransı gevşetmek Type-II'yi büyütür. Türetim sunulmadıkça değiştirilmemeli.

Panel: 6/7 GATE. Qwen'in REPORT_ONLY'si "C4a criterion 4'ü tam temsil etmez" diyerek tek identifiability ölçüsünü rapora indirir — iç tutarsız.

Benimsenen ifade (Manus-2): C4b, "frozen family içinde full-data ve truncated-data fitlerinin masked-edge davranışı arasındaki fonksiyonel kararlılığı" ölçer; hiçbir yerde edge accuracy, morphology membership veya parameter stability kanıtı olarak kullanılmaz. → **M1**.

### A2. AGG-L1 = WORSE — ACCEPT

MEAN elenir (tek-taraflı çöküşü ortalamada saklar); POOL elenir (aynı yörüngenin L/R değerleri bağımlı → pseudo-replication).

WORSE vs SEPARATE kararı sex-level istatistiğin türüne bağlıdır. İki r3-erişimli reviewer (Fugu-2, Manus-2) istatistiğin **median** olduğunu raporluyor (K1). Median altında:

- **Ç-1 (seyrelme):** SEPARATE'in sol aggregate'i sağ-anchored adların trivial sol değerleriyle seyrelir; stratumun >%50'si o kenarda anchored değilse yan gate hem family hem spline için trivial geçer — gate gücünü kaybeder.
- **Ö-5 (heterojen failure, Fugu-2):** %30 sol-kötü + %30 sağ-kötü + %40 iyi → SEPARATE'in iki medyanı da "iyi", geçer; WORSE'un medyanı kötü, yakalar.
- **Kalibrasyon estimand'ı:** gerçek censored adlar anchored oldukları kenardan kesiktir; 6A altında morfoloji etiketi olmadığından zor kenarı etiketsiz seçen tek operatör max'tır.

Panel: 5/7 WORSE; iki dönüş mekanizma temelli. Kalan SEPARATE oyları yanlış öncüle (MiniMax: W-L'de sağ probe "doğal olarak başarısız" — tersi, sağ maske W-L için trivial) veya seyrelmeyi ele almayan argümana (Qwen) dayanır. SEPARATE bounded alternative olarak kalır; seçilirse C4b'nin P04 scalar'ı ikiye çıkar (`tau_4b_RMSE` iki karşılaştırmaya uygulanır).

Reddedilen: morphology-conditional WORSE; kuralı F1 morphology composition'a göre seçmek (data-dependent design; etiket yok).

Koşullar → **M2**: (a) LEFT/RIGHT C4b sex-level medyanları report-only (r3'te per-side probe-failure share'leri varmış; C4b medyanları eklenir); (b) cross-edge caveat disclosure: family ve spline'ın max'ı aynı yörüngede farklı kenardan gelebilir — zor kenar genelde iki model için de aynı olduğundan ikinci-derece.

### A3. D-P03-6 = 6A — ACCEPT; 6B ayrı yönetilen companion olarak önerilir

6A'nın claim policy'si doğru: 906 korunur, screen yok, claim within-architecture. Panel genelinde mutabakat (Claude, Fugu-1/2, Manus-1/2, ChatGPT-2): **6A + paired-valid completeness common-mode morphology misspecification'ı yönetmez, yalnız claim'i sınırlar.**

r1'de 6B'yi packet'e ekleyerek MODIFY önermiştim. Sentez (**Ç-3**):

- Geçerli itiraz: packet parsimony — r3 RATIFICATION_READY iken yeni tanım + düzeltme döngüsü (Manus-1/2, ChatGPT-2, Fugu-1). Manus-2'nin "action rule'suz diagnostic = yorum serbestliği" itirazı substantif.
- Geçersiz itirazlar: `new_methodology_review = false` ihlali (ChatGPT-2, Fugu-1) — 6B adayda predeclared bounded alternative; firewall ihlali (Kimi) — 6B C-kriterleriyle aynı anda yürür, ratifikasyondan önce değil.
- Karşılığı olmayan argümanım: 6B spline-only ve family-blind olduğundan trigger-1'in (kalibrasyonun frozen varsayımı falsifiye etmesi) F3–F12 harcamasından **önce** test edilebileceği tek yerdir.

Çözüm: D-P03-6 packet satırı **6A, değişmeden**. 6B, packet dışında, R-REV governance altında **companion artifact** olarak önerilir:

```text
6B_companion (recommendation, outside the F3 STEP 1 packet)
  input        = shape-constrained spline benchmark (frozen basis/df/loss) + unconstrained spline, same basis/df/loss
  statistic    = per-trajectory RMSE_constrained / RMSE_unconstrained  (>= 1 by construction: restriction)
  report       = quantiles by sex stratum; no threshold
  consumption  = none in F3 (no gate, no exclusion, no P03/P04/P05 input, no eligibility effect)
  action rule  = null within F3; any use only via explicit PI action under the existing three reopen triggers
  timing       = frozen before F3_EXECUTION_READY; executed alongside C-criteria
  status       = third_generator = false; winner_eligible = false; R-REV resolution = false
```

PI companion'ı reddederse: 6A + güçlendirilmiş disclosure (Ö-5/Fugu-2): "spline-relative kriterler ortak morphology misspecification'ına kördür; temsiliyet sorusu R-REV altında ele alınır; 6B bounded alternative olarak elde tutulur" + Manus-2'nin iki makale cümlesi (tüm eligible yörüngeler dahil, morphology-based dışlama yok / sonuçlar frozen architecture içindeki relatif adequacy'dir, morphology doğrulaması değil).

### A4. D-P03-7 = Option A — ACCEPT

B reddedilir: K = 5 fold tümü zorunlu × 2 probe × spline zinciri altında complete-all, sonucu optimizer şansına rehin bırakır; disclosed P-01 float64 plateau'sunu adequacy-dışı otomatik eleyiciye dönüştürür; ex-post istisna baskısı üretir (Kimi). Panel 7/7.

Paired-valid gerekli ama yetersizdir; family'nin stratumdan ne kadar "vazgeçebileceğini" yalnız c_complete sınırlar — packet bunu açıkça söylemeli.

Koşullar → **M5**: (1) invalid taksonomisi kapalı ve prosedürel — optimizer non-convergence, Kural T/S inadmissibility, saturation plateau, fold failure, probe failure — family ve spline için aynı; büyük-ama-sonlu RMSE invalid değildir (anti-gaming ilkesi: invalidlik numerik prosedürün özelliği olmalı, yörüngenin zorluğunun değil); (2) her spline-relative criterion için spline'ın family-invalid tümleyen kümedeki istatistiği report-only; (3) criterion bazında denominator, valid-result share, paired-valid share, failure taxonomy (Manus-1) ve failure pattern'i (Kimi) — morfoloji etiketi olmadan, F1'in support-temelli descriptor'larıyla.

### A5. c_complete = 0.90 — ACCEPT

Outcome-blind, family-agnostic gerekçe — adversarial-dropout bound (median-tipi istatistik; K1 median raporlandı):

```text
q = 0.10  →  kalan kümenin medyanı orijinal dağılımın [45.0, 55.0] yüzdelik bandında
q = 0.05  →  [47.5, 52.5]
q = 0.15  →  [42.5, 57.5]
share-tipi istatistikte kayma ≈ q mertebesinde
```

Compounding (Manus-2): 5 fold için birlikte 0.90 ≈ fold başına 0.979; 2 probe için ≈ probe başına 0.949; C4b'nin `V4_s`'i dört probe'un (family L/R, spline L/R) kesişimi → tasarımın en talepkâr completeness'i. 0.95 bu yapıda numerik Type-I; 0.85 anti-selection bandını gereksiz açar.

**K-05 (M3):** `|V4_s|/n_s ≥ 0.90 ⇒ family probe success ≥ 0.90 > c_ident = 0.85` ⇒ C4a P03_GATE yolunda structurally non-binding. Bu çelişki değil, baskın eşiktir (Manus-2 doğru). Reddedilenler: C4b completeness'ini 0.85'e hizalama (Fugu-2 — criterion-specific literal ya da payda değişikliği gerektirir); criterion-specific c_complete (MiniMax — literal yüzeyi); "transparent reporting" (ChatGPT-2 — K-05 standardı ratifikasyon kaydında explicit disclosure ister). Ratifikasyon öncesi calibration fit-diagnostic'iyle literal'i "yeniden kontrol" (Fugu-2) reddedilir: `candidate_specific_fit = false`.

Disclosure (**M6**): uniform c_complete sub-fit sayısı farklı criterion'larda eşit sertlikte değildir; 0.90 hiçbir family'nin yapısal özelliğine referansla seçilmemiştir; c_cov ile bağımsızlık beyanı.

---

## 3. B. Reviewer stress test (updated)

**C4b gate.** "İki kez aynı şekilde yanlış olan model geçer; low-df spline'a karşı non-inferiority barı yerde." Dayanır mı: M1 ile evet — parametrik anlamda "identifiability" kelimesi kullanılmazsa; spline en az taahhütlü single-wave model → floor, ceiling değil; mutlak C4b de raporlanır; delta 0.10 predeclared. En zor soru (Manus-2): "C4b iyi ise edge doğru mu?" → cevap **hayır**, ve bu cevap makalede olmalı.

**WORSE.** "Max-then-median iki censoring estimand'ını yorumu zor bir composite'te harmanlıyor; neden SEPARATE değil?" Dayanır mı: M2 ile evet — per-side medyanlar raporlanır; Ö-5 örneği SEPARATE'in kaçırdığı durumu gösterir; cross-edge caveat disclose edilir.

**6A (+companion).** "Mimarinin temsil edemediği yörüngeleri tutup single-wave modeller arasında göreli adequacy hesaplıyorsunuz." Companion ile: mismatch dağılımı sınırın boyutunu gösterir, dayanır. Companion'sız: yalnız scope daraltması olarak dayanır; Manus-2'nin iki cümlesi ve Ö-5 disclosure'ı zorunlu. "Yüksek-mismatch adları çıkarın" ters itirazı: post-hoc olurdu; R-REV ayrı.

**Option A.** "Family en zor %10'u düşürüp yine geçebilir." Dayanır mı: yalnız M5 ile (prosedürel taksonomi + dropped-set raporu + ±5 pp bound).

**0.90.** "Keyfi; c_cov'a eşit olması tesadüf değil." Dayanır mı: dropout bound + compounding + bağımsızlık beyanı ile evet; "aynı ama bağımsız" cümlesiyle hayır.

**P04 (yeni).** "İki generator'ı farklı trajectory kümelerinde karşılaştırıp 0.02 toleransla tie-break yaptınız." Dayanır mı: yalnız M8 ile.

---

## 4. C. Interaction check (updated with r3 literals)

**P03_GATE + WORSE.** WORSE family ve spline'a simetrik uygulanır; konservatiflik delta ve istatistik türünde yaşar. Gerçek etkileşim: `V4_s` dört probe'un kesişimi → C4b completeness tasarımın en talepkâr tabanı ve K-05 dominance'ı (c_ident non-binding). Probe failure C4a'da non-success, C4b'de incompleteness olarak iki kez sayılır — deklarasyonla kabul (M3).

**6A + paired-valid.** Common-mode morphology misspecification'ı yönetmezler; ortogonaldirler. Ölçen tek araç 6B companion'dır (ya da C3 mutlak ölçekliyse o — K4).

**c_complete + C4.** 15-yıl maskenin tanımlayıcı kısmı her model için (spline dahil) kaldırdığı yörünge oranı %10'u aşarsa C4b iki family ve spline için "cannot pass" → data-yapısal both-fail. All-fail branch kontrat metni olmalı: STOP + PI governance, threshold gevşetme yok (ChatGPT-2 bunu "doğru yanıt" olarak yazıyor; r3'te kontrat metni mi, memo mu — K5). Taksonomi "probe fit failed" (invalid) ile "fit succeeded, RMSE büyük" (valid) ayrımını kesin yapmalı.

**Sistematik bias.** Beş seçim biçimsel olarak simetrik. Etkileşen tek yapısal asimetri disclosed P-01 float64 saturation plateau'su → degenerate fit sınıflandırması her iki family için aynı ilkeyle predeclared (M5); c_complete'i ayarlama gerekçesi değil. 6B spline-only → family bias yok. `P-01 < P-02` deterministic fallback yalnız tam eşdeğerlikte, disclosed, nötr.

**P03 pairing ⇒ P04 pairing değil (Ö-6, Manus-2).** Her family spline ile kendi paired-valid setinde karşılaştırılır; P04 ise P-01 ve P-02 skalarlarını birbirine karşı karşılaştırır. İki set ayrı ayrı ≥ 0.90·n olsa bile kesişim en az `2·c_complete − 1 = 0.80·n` (F: 392+392−435 = 349, %80.2; M: 424+424−471 = 377, %80.0). `tau_4b_RMSE = 0.02` gibi dar toleranslar destek farkından kaynaklanan medyan kaymalarıyla aşılabilir. İlke: her iki candidate skaları aynı `U_j,s` üzerinde yeniden hesaplanır. Taban PI kararı:

```text
(i)  |U_j,s|/n_s >= c_complete her iki sex'te; aksi halde P04 comparison-ready değil → STOP   (Manus-2)
     + P03 ile simetrik anti-selection gücü
     − P03'ü geçen iki adequate family, setleri örneğin %88 örtüştüğü için STOP'a düşebilir
(ii) ek taban yok; U_j,s üzerinde hesapla; |U_j,s|/n_s zorunlu disclose; garantili alt sınır 0.80
     + q = 0.20'de dropout bandı [40., 60.] — iki family için simetrik
     − karşılaştırma stratumun %80'inde yapılmış olabilir (disclosed)
Eğilim: (ii). "İki adequate generator'ı %85 ortak destekte karşılaştırdık" savunulur;
"ortak destek %88 kaldı diye durdurduk" savunulmaz.
```

---

## 5. D. Final PI recommendation

```text
C4b_status = P03_GATE
AGG-L1 = WORSE
D-P03-6 = 6A
          [+ separately governed 6B companion recommended (spline-only, frozen-df reuse,
           no threshold, no exclusion, no P03/P04/P05 consumption, no automatic trigger,
           frozen before F3_EXECUTION_READY); if declined: 6A + strengthened disclosure]
D-P03-7 = Option A
c_complete = 0.90

OVERALL_VERDICT =
ACCEPT_WITH_MODIFICATIONS
  (all five literal choices ACCEPT; zero literal changes;
   modifications = contract-text additions to the freeze artifact: M1–M3, M5–M8)

MOST_CONTESTABLE_DECISION =
C4b_status = P03_GATE (reviewer-facing: self-referential, common-mode-blind statistic as
hard gate; survives only with M1 + M3). AGG-L1 panelde 5/7 ile ve mekanizmayla kapanmıştır.
Packet düzeyinde kalan tek açık PI tercihi: D-P04 ortak-destek tabanı (i)/(ii).

MOST_IMPORTANT_REASON =
Pencere censoring'i 1880–2025 SSA verisinin tanımlayıcı yapısal özelliğidir; truncated
yörüngelerden stabil tahmin edilemeyen bir family bu verilerden kalibre edilemez; C4a yalnız
solver feasibility ölçtüğünden C4b gate olmazsa tasarımda identifiability kriteri kalmaz.
Beş literal outcome-blind ve birbiriyle tutarlıdır; kalan iş, baskın eşik (K-05), all-fail
branch ve P04 ortak desteğinin raporlama niyeti değil hash'lenebilir kontrat metni olarak
yazılmasıdır.
```

---

## 6. E. Freeze artifact koşulları (ratification package)

| # | Koşul | Tür | Durum |
|---|---|---|---|
| M1 | C4b: "non-inferiority to shape-constrained benchmark"; "edge self-consistency under censoring — identifiability için gerekli, yeterli değil"; common-mode blindness disclosure + C2/C3 delegasyonu; "C4b iyi ⇒ edge doğru" iddiası yasak | DISCLOSURE | ChatGPT-2 kısmen aldı (claim boundary listesi); "necessary-not-sufficient" ifadesi açık |
| M2 | LEFT/RIGHT C4b sex-level medyanları report-only; cross-edge caveat | REPORT-ONLY + DISCLOSURE | Açık (Fugu-2, Manus-2 de ister) |
| M3 | K-05: `c_ident = 0.85` P03_GATE + WORSE + c_complete 0.90 altında non-binding — ratifikasyon kaydında explicit disclosure; C4a/C4b çift sayım deklarasyonu; `V4_s` payda beyanı | CONTRACT + DISCLOSURE | Açık (ChatGPT-2 "reporting" — yetersiz) |
| M4 | 6B companion artifact (packet dışı, R-REV governance) | GOVERNANCE (PI kararı) | Açık |
| M5 | Kapalı prosedürel invalid taksonomisi (family = spline); büyük-sonlu RMSE ≠ invalid; dropped-set spline istatistiği; criterion bazında denominator / valid share / paired-valid share / failure taxonomy | CONTRACT + REPORT-ONLY | Açık |
| M6 | c_complete gerekçesi = adversarial-dropout bound + compounding; criterion'lar arası eşitsiz sertlik disclosure'ı; c_cov'dan bağımsızlık ve family-bağımsız seçim beyanı | DISCLOSURE | Bound ChatGPT-2'ye alındı; eşitsiz sertlik açık |
| M7 | All-fail / both-fail branch: STOP + PI governance; threshold gevşetme yasak | CONTRACT | ChatGPT-2 beyan ediyor; r3'te kontrat metni mi — K5 |
| M8 | D-P04 ortak destek: her iki candidate skaları aynı `U_j,s` üzerinde; taban (i)/(ii) PI kararı; `|U_j,s|/n_s` disclose | CONTRACT | Yeni; r3'te yoksa GATE-SPECIFIC |

Reddedilen öneriler (benimsenmedi): pilot-run delta kalibrasyonu (MiniMax); ratifikasyon öncesi fit-diagnostic ile c_complete yeniden kontrolü (Fugu-2); criterion-specific c_complete (MiniMax); C4b completeness'ini 0.85'e hizalama (Fugu-2); morphology-conditional WORSE ve F1 composition'a göre kural seçimi (MiniMax); paired-invalid kümeyi "WC-ALC dışı" sayma (MiniMax); REPORT_ONLY (Qwen); "6B firewall ihlali" (Kimi); `delta_4_RMSE = 0.20` (Fugu-2 — PI'nin predeclared alternatifler içindeki hakkı, ama türetimsiz).

---

## 7. F. KONTROL (r3 metninde doğrulanacak)

```text
K1  sex-level istatistik = median   (Fugu-2, Manus-2 raporu; doğrulanmalı)
    → median değilse A5 gerekçesi ve A2'nin seyrelme argümanı yeniden değerlendirilir
K2  C4b completeness paydası = stratum n   (Manus-2: |V4_s|/n_s; doğrulanmalı)
K3  invalid taksonomisi kapalı ve prosedürel mi
K4  C2/C3 spline-relative mi mutlak mı; C3 residual-structure testi multi-wave/edge sapmasına duyarlı mı (Fugu)
K5  all-fail branch r3'te kontrat metni olarak var mı
    → yoksa freeze artifact'ı için GATE-SPECIFIC
K6  delta_4_RMSE = 0.10 (alternatifler 0.05/0.20) gerekçesi
K7  D-P04 skalarları ortak destekte tanımlı mı
    → değilse M8 GATE-SPECIFIC
K8  per-side probe-failure share raporlaması r3'te mevcut mu (Manus-2: evet) — per-side C4b medyanı eklenir
```

---

## 8. G. Panel disposition

Bağımsız reviewer'lar (aynı ajanın turları tek sayım, son pozisyon):

```text
C4b        GATE  = Claude, ChatGPT, Manus, Fugu, Kimi, MiniMax     | REPORT = Qwen           → 6/7
AGG-L1     WORSE = Claude, ChatGPT, Kimi, Fugu-2, Manus-2          | SEPARATE = Qwen, MiniMax → 5/7
D-P03-6    6A    = 6/7                                             | 6A+6B (r1) = Claude → r2: 6A + companion
D-P03-7    A     = 7/7
c_complete 0.90  = 7/7
```

Puanlar (P/T/C/K/S ortalaması): Manus-2 8.6 · Claude 7.8 (self; çıkar çatışması, 0.5–1 indirim önerilir) · Manus-1 7.6 · ChatGPT-2 7.4 · Fugu-1 7.2 · Fugu-2 7.0 · Kimi 6.4 · ChatGPT-1 5.8 · Qwen 4.6 · MiniMax 3.6.

---

## 9. Ö / Ç kaydı

```text
Ç-1  AGG-L1 kararının sex-level istatistik türüne (K1) bağımlılığı r1'de yazılmamıştı; eklendi
Ç-2  (koşullu) r3 audit'im D-P04'ün candidate-to-candidate paired validity'sini test etmedi;
     r3'te ortak-destek kuralı yoksa "no content-level MODIFY findings" ifadesi D-P04 için eksikti.
     Ceza audit kaydına uygulanır.
Ç-3  D-P03-6: r1'deki "6B packet'e eklenir, MODIFY" pozisyonu → "6A ACCEPT + packet dışı companion".
     Gerekçe: packet-parsimony itirazı geçerli; trigger-1 zamanlama argümanı companion ile korunur.
Ö-1  Fugu-1: C3 duyarlılık teyidi → K4
Ö-2  Manus-1: criterion bazında denominator/attrition raporlaması → M5
Ö-3  Kimi/Fugu: both-fail branch → M7 (KONTROL'den koşula)
Ö-4  ChatGPT-2: AGG-L1 için "estimand niyeti" sorusu — K1 ile birlikte kullanılır
Ö-5  Fugu-2: heterojen tek-taraflı failure örneği → WORSE gerekçesinin kanonik illüstrasyonu
Ö-6  Manus-2: D-P04 ortak-destek ilkesi → M8; taban seçimi PI'ye
```

---

## 10. Firewall beyanı

```text
cross_family_performance_comparison       = false
real_SSA_data_accessed                    = false
P03_threshold_value_assumed               = false
Ward_CH_frozen_winner_used                = false
candidate_specific_fit_recommended        = false   (Fugu-2 / MiniMax önerileri reddedildi)
r3_literals_used                          = as reported by panel; UNVERIFIED (KONTROL)
panel_documents_contained_empirical_outcome = none observed
project_knowledge_search (r1)             = legacy repo/prompt material only; none used
synthetic_or_empirical_execution          = none
```

*End of artifact. Non-normative; binding only upon explicit PI ACCEPT/MODIFY action per row.*
