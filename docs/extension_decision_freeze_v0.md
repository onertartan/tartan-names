# extension_decision_freeze_v0.md — Genişletme karar iskeleti (FREEZE)

**Revizyon r2 (2026-08-18, v4-hizalı; talimat `03408f6c…`):** method-space
dışı iki satır (r2-değerlendirme sızıntısı) kaldırıldı; FCSP eligibility
genel bağlayıcı kurala bağlandı; null'un exact bilimsel desteği +
sigma_null pini eklendi; tek-prototip kararı KESİNLEŞTİ
(excluded_from_extension — now-or-never kapısı kapandı); m–k inferential
kapısı kapatıldı; FAZ 5 gating'i eklendi; normatif bağımlılıklar
tam-SHA256'ya çevrildi. Yeni yöntem eklenmedi; kapalı karar açılmadı.
Statü: **ONAY BEKLİYOR** (FROZEN değil).
**Revizyon r3 (aynı gün; talimat `f9869428…`):** self-hash prosedürü
kaldırıldı (harici .sha256); exact ICL tanımı §5'te DONDU; §9
normatif/bilgilendirici olarak ayrıldı; source_status şeması temizlendi.

**Statü:** ONAY BEKLİYOR → Öner onayı bu belgedeki tüm pinlerin İMZASIDIR;
onay sonrası SHA256 + git commit ile DONAR. Donduktan sonra yöntem
LİSTESİ, eligibility atamaları, faktör destekleri, null semantiği ve
yorum kısıtları değişmez; yalnız implementasyon detayı
(`extension_prereg_v1.md` + pin memoları) kendi kapılarında kapanır.

**Tarih:** 2026-08-18 · **Kaynak belge:** `yol_haritasi_v4_FINAL_2026-08-18.md` (tam hash §9'da) §FAZ 0.5 · **Zamanlama gerekçesi (bağlayıcı):** bu belge,
donmuş çalışmanın Friedman/GLMM/SSA-deployment İKİNCİL SONUÇLARI
görülmeden hash'lenir; böylece genişletme yöntem uzayı o sonuçlarla
data-inform EDİLEMEZ. Hash alınmadan ikincil sonuç ayrıntısına girilmez.

**Donmuş çalışmayla ilişki:** bu belge donmuş çalışmaya (protokol v5.3 +
sapma eki, manifest `34e1217e…`, kazanan Ward+CH) DOKUNMAZ; hiçbir koşum
başlatmaz. Statü cümlesi (aynen, İngilizce pinli):

> *"The extension was designed after inspection of the frozen benchmark
> and tests explicitly preregistered robustness and method-space
> questions rather than constituting the original confirmatory
> analysis."*

---

## 1. Method-space (eligibility alanlarıyla; sonuç görüldükten sonra kategori değişmez)

### 1.1 Çekirdek (winner-eligible common layer / kendi katmanı)

| Yöntem/Blok | Kategori | Not |
|---|---|---|
| PAM-Euclidean | winner_eligible=true (common layer, 5. algoritma) | pinler §6 |
| GMM-native BIC/ICL | native_selector (Friedman DIŞI) | pinler §5 |
| k_true=1 null bloğu | null_only | semantik §3 |
| Observed-support m–k response surface | design block | destek §2, dil §7 |
| φ×σ response surface | design block | destek §2 |

### 1.2 Birinci halka

spherical KMeans (winner_eligible=true; **pin-memo kapılı** — memo
imzasız kod yok) · PBM (common CVI; kural: "tek yeni ortak CVI
eklenecekse ilk seçim"; CH/DB artıklık ucu zorunlu) · pairwise
precision/recall/F1 (metrik) · VI-ayrıştırması (metrik).

### 1.3 Diagnostic / koşullu (arm-bazlı gate; eksik pin = o kol NO-GO, çekirdek GO)

| Yöntem | status | source_status | Gate özeti |
|---|---|---|---|
| movMF (vMF karışımı) | conditional | pending (κ-dejenerans lit.) | κ-politikası memo |
| Gap | conditional | verified (Şenbabaoğlu K≥2 + argmax; bioRxiv 002642v3) | 12-kalem gate (prereg'de; deployment-parity dahil) |
| Prediction Strength | conditional | verified (T&W 2005) | kapsam politikası; §8 yasak cümle |
| PAC | conditional | verified (Şenbabaoğlu 2014; M3C operasyonel çerçeve) | varlık iddiası yalnız null blokla |
| Fang–Wang | conditional | pending (künye Manus-DOI'den teyit) | (algoritma, projeksiyon-kuralı) çifti pini |
| S_Dbw | conditional | **pending — yoğunluk-yarıçapı tanımı özgün makaleden** ("3-NN" iddiası şüpheli) | teyitsiz koşulmaz |
| Krzanowski–Lai | conditional | verified (formül) | boşalan-düzeltme notu + W₁₁ sınır kuralı |
| t₅ ağır kuyruk | conditional | not_applicable | ikinci halka DGP |
| FPCA/B-spline | conditional | not_applicable | AYRI representation-sensitivity kolu; bolt-on değil |

**Kaynak-teyit kuralı (bağlayıcı):** `source_status=pending` olan yöntem
koşulmaz; teyit başarısızsa yöntem düşer ve **yerine yeni aday alınmaz**
(`replacement_allowed=false`).

### 1.4 Average linkage (pin — onayla imzalanır)

```
extension_role            = sensitivity_only
winner_eligible           = false
block_D_eligible          = false
SSA_deployment_eligible   = false
```
Gerekçe: Blok-D çapa/dairesellik önlemi korunur; alternatif-çapa
serbestlik derecesi açılmaz. A/B kollarında linkage-duyarlılığı yine
ölçülür.

### 1.5 Excluded (geri alınmaz; aday taraması KAPALI)

jump · DP-means · HDBSCAN · Piccolo AR-mesafesi · cepstral · funHDDC ·
James–Sugar · FCM/XB-yerli kol · GMM-tied · vanilla-Gap-null ·
PAM-L1 (primary rolde) · T-ızgara (primary rolde; φ_T=0.97^(145/(T−1))
normalizasyon formülü doğru olarak kayıtlıdır).

## 2. Faktör destekleri (yeni seviye İCAT EDİLMEZ)

```
phi_support   = {0.80, 0.90, 0.97, 0.99}
sigma_support = {0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0}
```
**Provenance notu:** önceki taslaklardaki φ=0.95 donmuş seviye DEĞİLDİR
(protokol anlatısındaki ön-tarama cümlesinden sızmıştı); manifest
`34e1217e…` üzerinden 2026-08-18'de yeniden doğrulandı: yalnız
{0.8, 0.9, 0.97, 0.99}. φ×σ bloğu referans B/R yapısını sabit tutar
(M_karisik · k_true=5 · ρ=0.615 · n_per=10); yalnız iki destek
çaprazlanır; başka faktör eklenmez.

```
m ∈ {5, 10, 20} · k_true ∈ {3, 4, 5, 6, 8} · 25 ≤ mk ≤ 100
→ 11 gözlenen hücre:
  m=5 : k ∈ {5, 6, 8}      m=10: k ∈ {3, 4, 5, 6, 8}      m=20: k ∈ {3, 4, 5}
```
Gözlenmeyen 4 kombinasyona extrapolation YASAK.

## 3. Null bloğu — bilimsel semantik (ŞİMDİ donuyor)

- **Primary null:** *no-cluster pure-noise null* — deterministik sınıf
  prototipi YOK; donmuş beyaz/AR gürültü üreteci ve seri-bazlı z-norm
  (ddof=0) AYNEN korunur (somutlama: donmuş boru hattının prototipsiz
  hali).
- **Primary endpoint:** **FCSP = P(k̂ > 1 | k_true = 1)** — terim:
  *false cluster-structure selection probability*. "FDR" DENMEZ;
  multiple-testing FDR'ıyla karıştırılmaz (FCSP bir error-rate
  estimandıdır).
- **FCSP eligibility (bağlayıcı kural, aynen):** *FCSP-eligible
  selectors are only those within the frozen extension method-space
  whose preregistered native or arm-specific decision rule explicitly
  permits k=1. No ad-hoc post-selection fallback to k=1 is allowed.*
  Statüler: GMM-native BIC/ICL → eligible (native k=1..10); Gap →
  koşullu-eligible YALNIZ null-arm aday uzayı ve karar kuralı ön-kayıtta
  açıkça k=1 içeriyorsa; stability/diagnostic seçiciler → yalnız kendi
  ön-kayıtlı arm-kuralları k=1 üretiyorsa. k=2..10 ile sınırlı ortak
  CVI'lar FCSP estimandına uygun DEĞİLDİR ve "%100 yanlış-pozitif" diye
  raporlanmaz.
- **Exact bilimsel destek (DONUK — memoya bırakılmaz):**
  ```
  null_semantics        = no_cluster_pure_noise
  n_null                = {30, 40, 50, 60, 80}   <- frozen Blok-A toplamlari
  noise_null            = {white, AR(phi=0.97)}  <- frozen ana gurultu seviyeleri
  sigma_null            = not_applicable
  n_seeds_null          = 100
  single_prototype_null = excluded_from_extension
  ```
  sigma_null gerekçesi (pinli cümle): *Under the pure-noise null,
  multiplicative noise scale is exactly removed by per-series
  z-normalization; therefore sigma is not a null-design factor and is
  not crossed.* (z(σε)=z(ε), her σ>0; nominal σ=1 yalnız hesaplama
  sabitidir, zorluk ekseni olarak raporlanmaz.) Null için ayrıca
  φ∈{0.80,0.90,0.99} duyarlılık ızgarası EKLENMEZ (φ-robustness φ×σ
  bloğunda). Tek-prototip null'u sensitivity olarak da koşulmaz;
  sonradan eklenmez.
- Memoya kalanlar (yalnız hesaplama/uygulama): RNG namespace haritası ·
  output şeması · failure/undefined kodları · test vektörleri · exact
  implementasyon kontrolleri.

## 4. Metrik rolleri (donuk) ve tanım pinleri

- **Primary k-seçim:** P(k̂=k_true) · MAE_k · işaretli bias +
  P(k̂<k_true) / P(k̂>k_true).
- **Secondary dış bölümleme:** ARI · AMI.
- **Diagnostic:** oracle ARI-regret (max_{k∈𝒦} ARI(k) − ARI(k̂)) ·
  VI-ayrıştırması (H(truth|Ĉ), H(Ĉ|truth)) · pairwise P/R/F1 ·
  selection dispersion · failure/undefined/coverage oranları.
- **Selection dispersion:** H_norm = H / log|𝒦|; |𝒦| hard-code
  edilmez, seçicinin ön-kayıtlı aday desteğinden okunur (ortak katman 9;
  native 10; restricted 9) ve manifest alanı olarak saklanır.
- Dil pinleri: ARI/AMI/VI/P-R-F1 "tamamlayıcı"dır ("çözer" DENMEZ);
  ad: "selection dispersion across realizations" ("algorithmic
  stability" DEĞİL); target_k_regret zorunlu metrik DEĞİLDİR (oracle
  regret estimandı esastır). Betimsel metrikler p-değeri üretmez;
  onlardan otomatik FDR/FWER ailesi türetilmez.

## 5. BIC/ICL pinleri

1. **Yön:** *pre-registered optimum direction under the stored
   criterion convention* — ham sklearn BIC **argmin**; dönüştürülmüş
   skor yalnız işaret dönüşümü açıkça tanımlı+saklıysa argmax.
2. **Exact ICL tanımı (DONUK — bilimsel seçici tanımıdır, implementasyon
   detayı değildir; freeze sonrası seçilemez):** saklanan konvansiyon
   sklearn'dür: BIC_stored(k) = −2·log L̂ + p_k·log n (düşük-iyi).
   **ICL_stored(k) = BIC_stored(k) + 2·E(k)**, burada
   E(k) = −Σ_i Σ_c τ_ic·log τ_ic (doğal logaritma; 0·log 0 := 0;
   τ_ic = yakınsamış en-iyi fit'in posterior sorumlulukları,
   `predict_proba`). Yön: BIC ve ICL için **argmin**. Seçim kuralı:
   k̂ = argmin (native 1..10; restricted 2..10); bağ → en küçük k
   (np.isclose, rtol=1e-10, atol=1e-12 — donmuş bağ toleransı).
   Birim test sonra yazılır; test edilecek matematiksel tanım BUDUR.
   (Biernacki, Celeux & Govaert 2000'in düşük-iyi konvansiyona
   eşlenmiş hali.)
3. Native primary aday uzayı **k = 1..10**.
4. **Restricted sensitivity k = 2..10 ŞİMDİ ön-kayıtlıdır** (aynı
   değerlerde kısıtlı optimum; sonuç-sonrası seçim yok).
5. Asimetri cümlesi (aynen): *"BIC/ICL use their native candidate space
   k=1..10; therefore their recovery rates are model-native comparator
   outcomes and are not interpreted as candidate-space-matched estimates
   relative to common CVIs."*
6. GMM parametreleri donmuş protokolden AYNEN (diag · reg_covar=1e-6 ·
   tol=1e-3 · max_iter=500 · n_init=5 · kmeans-init · gmm_seed);
   convergence/non-finite/failure = frozen S-04 deseni. Yeniden açılmaz.

## 6. PAM pinleri

Euclidean · BUILD · SWAP-until-no-improvement · restart YOK ·
random_state inert · k=2–10. **Bağ/permütasyon:** tie-free fikstürlerde
bölüt-düzeyi permütasyon-değişmezliği zorunlu; exact-tie fikstürlerde
objective eşitliği + pinli kütüphane sürümünün deterministik davranışı
belgelenir. `pam_tie_flag` yalnız implementasyon tie-tanısı sunuyorsa
zorunlu; sunmuyorsa Seçenek A: terminal swap-komşuluğu denetimi
(`pam_terminal_tie`; kapsam sınırı provenance'a) veya Seçenek B:
`tie_detection_supported=false` — "tie oluşmadı" VARSAYILMAZ; salt
loglama için custom PAM'a geçilmez. **Ortam pini:** paket (sklearn_extra
vs `kmedoids`/FastPAM) + sürüm prereg'de; FastPAM ise exact-eşdeğerlik
testi. **Ön-kayıtlı redundans ucu:** KMeans-PAM seçilen-k uyumu
hücre-bazlı; ayrışmanın aykırı-analog hücrelerde yoğunlaşması beklenir
(tahmin olarak kayıtlı).

## 7. m–k yorum ve hesap pinleri

Ön-kayıt cümlesi (aynen): *"The m–k extension is interpreted through
the 11 observed (m,k) cells. Because total sample size is
deterministically n=mk, the analysis does not identify independent
marginal effects of m, k, and total n, and no extrapolation is made to
unobserved (m,k) combinations."*
Hesap biçimi (DONUK):
```
mk_analysis_role=response_surface . mk_factor=mk_cell (11 levels)
formal_interaction_test=false . posthoc_interaction_contrast_selection=prohibited
```
*"No formal factorial interaction test is part of this extension. The
m-k block is interpreted as an observed-support response surface over
the 11 preregistered cells; post-hoc selection of interaction contrasts
is prohibited."* "full factorial m×k interaction" dili YASAK. Hücre
ağırlığı: eşit (tohum-içi toplama önce). Not: m sınıf
başına örnek sayısıdır — cluster-size imbalance faktörü DEĞİLDİR
(dengesizlik donmuş Blok-B 3:1/5:1 duyarlılığıdır).

## 8. Yorum kısıtları ve governance (donuk)

- m, k ve toplam n'nin bağımsız marjinal etkileri iddia edilmez.
- Native BIC/ICL, ortak CVI'larla candidate-space-matched primary kıyas
  olarak yorumlanmaz.
- Diagnostic katmanlar donmuş deployment kazananını (Ward+CH) geriye
  dönük DEĞİŞTİRMEZ.
- Genişletme, original confirmatory analiz değildir (statü cümlesi §0).
- Makale iddia-kapsamı (aynen): *"Within the prespecified method space
  evaluated in the frozen benchmark, Ward+CH obtained the highest
  prespecified winner score."*
- Toplama gerekçesi (aynen): *"Seeds are Monte Carlo realizations used
  to estimate cell-level performance; the simulation cell, not the
  individual seed, is the inferential block in the Friedman analysis."*
- PS yasak cümlesi: tek bileşik "PS accuracy" skoru üretilmez; coverage
  ile P(k̂=k_true | PS defined) DAİMA ayrı raporlanır.
- STOP kapsamı katman-bazlı: diagnostic pin eksiği yalnız o kolu
  NO-GO yapar; global STOP yalnız frozen-regression bozulması ·
  çekirdek pin eksiği · manifest/namespace çakışması · bu belge
  hash'lenmeden ikincil sonuca girilmesi.
- **FAZ 5 bağımlılığı:** actual SSA deployment (kümeleme sonucu, k̂,
  üyelik, Transfer-QC yorumu) YALNIZ bu belge hash'lendikten sonra;
  öncesinde yalnız hazırlık (girdi varlığı/SHA256, betik, ortam,
  dry-config).
- Seed/RNG ilkesi: genişletme YENİ namespace kullanır; donmuş
  (seed_key, tohum) uzayıyla çakışma yasak (exact harita prereg'de).
- Bu belgeden sonra yeni hakemlik/EK döngüsü açılmaz; ayrıntılar
  doğrudan `extension_prereg_v1.md` ve pin memolarına işlenir.

## 9.1 Normative frozen dependencies (tam SHA256; uyuşmazlıkta STOP)

```
cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67  01_kosum_protokolu_v5_3.md
99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7  kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md
34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64  run_matrix_v4.csv (FROZEN)
0c80c1894ebe5cba00ed9e76d57aa5131c564365fbcfea1815db31fff39e3915  yol_haritasi_v4_FINAL_2026-08-18.md (r2, kanonik yürütme belgesi)
```

## 9.2 Informational provenance references (non-normative)

```
456769cc…  parca_B_claude_nihai_cevap_r2.md
4c05ecc9…  genisletme_konsolide_nihai_karar_2026-08-16.md
eacbdfb0…  parca_B_cok_model_karsilastirma_2026-08-17.md
03408f6c…  claude_prompt_v3_to_v4_FINAL_7_duzeltme.md (bağlayıcı talimat)
f9869428…  v4_freeze_v0_chatgpt_nihai_degerlendirme.md (bağlayıcı talimat)
```

## 10. Onay ve dondurma

- [ ] **ÖNER ONAYI** — tarih/isim: ______________________
  (Onay, §1.4 average pini, §3 tek-prototip-null kararı ve tüm
  pinlerin imzası yerine geçer.)

Onay sonrası Claude Code'da (self-hash YASAK — hash belge DIŞINDA):
```bash
sha256sum extension_decision_freeze_v0.md > extension_decision_freeze_v0.md.sha256
git add extension_decision_freeze_v0.md extension_decision_freeze_v0.md.sha256
git commit -m "extension_decision_freeze_v0: FROZEN"   # + istenirse tag
```
Freeze hash is stored externally in `extension_decision_freeze_v0.md.sha256`.
Belge o commit'ten itibaren **FROZEN**'dır; değişiklik = yeni tarihli
sapma kaydı.
