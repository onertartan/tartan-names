# extension_decision_freeze_v0.md — Genişletme karar iskeleti (FREEZE)

**Statü:** ONAY BEKLİYOR → Öner onayı bu belgedeki tüm pinlerin İMZASIDIR;
onay sonrası SHA256 + git commit ile DONAR. Donduktan sonra yöntem
LİSTESİ, eligibility atamaları, faktör destekleri, null semantiği ve
yorum kısıtları değişmez; yalnız implementasyon detayı
(`extension_prereg_v1.md` + pin memoları) kendi kapılarında kapanır.

**Tarih:** 2026-08-18 · **Kaynak belge:** `yol_haritasi_v3_FINAL_2026-08-18.md`
(`9c8e5d84…`) §FAZ 0.5 · **Zamanlama gerekçesi (bağlayıcı):** bu belge,
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
| t₅ ağır kuyruk | conditional | — | ikinci halka DGP |
| FPCA/B-spline | conditional | — | AYRI representation-sensitivity kolu; bolt-on değil |
| COP | conditional | pending (künye+formül) | teyitsiz koşulmaz |
| crisp-XB | conditional | **pending — yayımlanmış crisp emsal şart** | emsalsiz girmez |

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
- **FCSP-eligible:** yalnız k=1 dönebilen seçiciler (12-pinli Gap ·
  GMM+BIC/ICL · açık k=1-fallback'li stability · Hennig–Lin
  sarmalayıcısı). k=1 dönemeyen ortak CVI'lar "%100 yanlış-pozitif"
  diye DEĞERLENDİRİLMEZ — aday-uzayları gereği estimanda uygun değiller.
- **Tek-prototip null'u (now-or-never kararı):** DAHİL DEĞİL —
  değerlendirildi ve primary null minimal tutularak dışlandı; ileride
  eklenemez. [Öner onay öncesi tersine çevirebilir; çevirirse
  "sensitivity" etiketiyle şimdi yazılır.]
- Ertelenenler (prereg/pin-memo): exact RNG namespace, n/σ/φ düzey
  seçimi (öneri: n'ler A-toplamlarıyla eşleme {30,40,50,60,80}),
  failure alanları, test vektörleri — **null tasarım-memosu Öner
  imzası gerektirir.**

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
2. Exact ICL formülü + saklanan konvansiyonla işaret ilişkisi prereg'de
   yazılır ve küçük sentetik örnekte birim testle doğrulanır.
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
Hesap biçimi: tek 11-seviye **`mk_cell`** kategorik faktörü; kontrastlar
yalnız gözlenen destekte; "full factorial m×k interaction" dili YASAK;
etkileşim inferansı istenirse estimable kontrast matrisi ÖNCEDEN
yazılır. Hücre ağırlığı: eşit (tohum-içi toplama önce). Not: m sınıf
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
- Seed/RNG ilkesi: genişletme YENİ namespace kullanır; donmuş
  (seed_key, tohum) uzayıyla çakışma yasak (exact harita prereg'de).
- Bu belgeden sonra yeni hakemlik/EK döngüsü açılmaz; ayrıntılar
  doğrudan `extension_prereg_v1.md` ve pin memolarına işlenir.

## 9. Referans belgeler (bilgi; bu belgeyle birlikte arşivlenir)

```
9c8e5d84…  yol_haritasi_v3_FINAL_2026-08-18.md   (kanonik yürütme belgesi)
456769cc…  parca_B_claude_nihai_cevap_r2.md      (konsolide yöntem değerlendirmesi)
4c05ecc9…  genisletme_konsolide_nihai_karar_2026-08-16.md
eacbdfb0…  parca_B_cok_model_karsilastirma_2026-08-17.md
8c23c693…  coklu_model_yol_haritasi_nihai_suzme_chatgpt.md
cf8b453f…  01_kosum_protokolu_v5_3.md  ·  99c17c42…  sapma eki S01–S07
34e1217e…  run_matrix_v4.csv (FROZEN)
```

## 10. Onay ve dondurma

- ÖNER ONAYI — tarih/isim: 2026-08-18, Öner
  (Onay, §1.4 average pini, §3 tek-prototip-null kararı ve tüm
  pinlerin imzası yerine geçer.)

Onay sonrası Claude Code'da:
```bash
sha256sum extension_decision_freeze_v0.md
git add extension_decision_freeze_v0.md && git commit -m "extension_decision_freeze_v0: FROZEN (SHA256 <hash>)"
```
Hash bu bölümün altına elle işlenir; belge o andan itibaren
**FROZEN**'dır — değişiklik = yeni tarihli sapma kaydı.

FROZEN SHA256: ______________________________________________
