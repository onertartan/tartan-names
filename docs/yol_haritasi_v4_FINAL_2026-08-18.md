# Yol haritası v4 — FINAL, kanonik yürütme belgesi (2026-08-18)

**Revizyon r2 (aynı gün; bağlayıcı nihai değerlendirme `f9869428…`):**
(1) freeze prosedürü self-hash'ten harici `.sha256` sidecar'a çevrildi;
(2) exact ICL tanımı bilimsel-seçici pini olarak DONDU (FAZ 0.5 §BIC/ICL);
(3) source_status enum'una `not_applicable` eklendi. Yeni yöntem yok;
kapalı karar açılmadı.

**v3'ün (`9c8e5d84…`) yerine geçer.** Revizyon kaynağı: Öner-onaylı
bağlayıcı talimat `claude_prompt_v3_to_v4_FINAL_7_duzeltme.md`
(SHA256 `03408f6c9b699d727172b9d7ade847d1e662fd87c9ef0a9228a149d2bca66aef`).
Kendine-yeterlilik iddiası şu anlamdadır: **genişletme kararları bu
belgede tamdır; donmuş davranışların normatif dış bağımlılıkları
§Normative frozen dependencies'te tam-SHA256 ile pinlidir.**

> **No new candidate method was added and no previously closed
> methodological decision was reopened in v4.**

## Değişiklik günlüğü v3 → v4 (yalnız yedi düzeltme + zorunlu metinsel sonuçları)

1. **COP / crisp-XB sızıntısı temizlendi:** kanonik method-space'te
   yoktular (v3 FAZ 0.5 doğru); eski freeze-v0 taslağına r2
   değerlendirmesinden sızmışlardı — freeze v4'le hizalandı; hiçbir
   statüyle tutulmuyorlar; yerlerine yöntem eklenmedi.
2. **FCSP eligibility method-space ile hizalandı:** Hennig–Lin ve
   ad-hoc "k=1-fallback'li stability" ifadeleri kaldırıldı; genel
   bağlayıcı kural kondu (FAZ 0.5 §Null).
3. **sigma_null = not_applicable pinlendi:** saf-gürültü null'unda
   satır z-norm çarpımsal σ'yı tam iptal eder (z(σε)=z(ε)); σ null
   tasarım faktörü değildir. Ana φ×σ bloğu DEĞİŞMEDİ.
4. **Null bloğun exact bilimsel desteği FAZ 0.5'te donduruldu**
   (n_null · noise_null · n_seeds_null · single_prototype_null =
   excluded_from_extension); FAZ 7B null memosu yalnız
   hesaplama/uygulama detayına indirildi.
5. **Normative frozen dependencies** bölümü eklendi — tam 64-karakter
   SHA256'lar gerçek dosyalardan hesaplandı.
6. **FAZ 5 bağımlılık çelişkisi kapatıldı:** actual SSA deployment
   yalnız freeze-v0 HASH sonrasında; öncesinde yalnız hazırlık.
7. **mk_cell inferential kapısı kapatıldı:**
   formal_interaction_test=false; post-hoc kontrast seçimi yasak;
   "istenirse kontrast matrisi" cümlesi kaldırıldı.

---

## Normative frozen dependencies (tam SHA256; uyuşmazlıkta STOP)

| Belge | Full SHA256 | Normatif kapsam |
|---|---|---|
| `01_kosum_protokolu_v5_3.md` | `cf8b453f0a05e2e6fed0c8b73692c2a5361fdfe60a22b3c9fe8c612e0e13db67` | frozen GMM parametreleri; algoritma/CVI tanımları; seed mimarisi; k̂/bağ/geçersiz-bölütleme politikaları; primary Friedman hiyerarşisi; kayıt şeması |
| `kosum_protokolu_v5_3_sapma_eki_S01_S07_FINAL.md` | `99c17c42711fd27dd2e55baf55f5ed41388b14a39a29e196f8eb1def34a5d0a7` | S-01 (winner/runner-up/SE_MC) · S-02 (GLMM zinciri) · S-03 (manifest/fail-fast) · S-04 (failure) · S-05 (achieved-QC) · S-06 (SSA girdileri, corr_ari) · S-07 (multiplicity kapsamı) |
| `run_matrix_v4.csv` | `34e1217e1d36b7282311ca5e51ec25c2106ac43e75712ade15cfec446458fd64` | frozen faktör desteği / manifest kimliği (FROZEN — in-place değişiklik yasak) |

## Kesişen kurallar

- Her betik girişte girdi SHA256 loglar; tutmayan hash'te DUR.
- Donmuş çıktı üzerinde sonradan hesap = **S-06 "post-hoc exploratory;
  winner/transfer kararını değiştirmez"** etiketi.
- Yeni yöntem sırası: pin memo → imzalı ön-kayıt → implementasyon →
  testler → smoke → full. Kod yazıldıktan sonra hiperparametre seçilmez.
- Her yöntem ex ante altı kategoriden birine atanır ve manifest alanı
  olarak taşınır: winner-eligible common layer · native-selector ·
  diagnostic · representation-sensitivity · null-only · excluded.
  Sonuç görüldükten sonra kategori değişmez.
- **STOP kapsamı katman-bazlıdır:** diagnostic/conditional kolun pin'i
  eksikse yalnız o kol NO-GO; çekirdek durmaz. **Global STOP yalnız:**
  frozen-regression bozulması · sınıf-(i)/çekirdek pin eksiği ·
  manifest/namespace çakışması · freeze-v0 hash'lenmeden ikincil sonuç
  (Friedman/GLMM ayrıntısı **ve FAZ 5 SSA sonucu**) üretilmesi/okunması.
- Koşullu-kaynak-teyit şeması her diagnostic yöntemde:
  `status = committed|conditional|excluded` ·
  `source_status = verified|pending|not_applicable` · `replacement_allowed = false`
  (teyit başarısızsa yöntem düşer; yerine aday alınmaz).
- Claude Code metodolojik çözüm ÖNERMEZ; belirsizlikte durur.
- Makale iddia-kapsamı (pinli): *"Within the prespecified method space
  evaluated in the frozen benchmark, Ward+CH obtained the highest
  prespecified winner score."*
- Toplama gerekçesi (pinli): *"Seeds are Monte Carlo realizations used
  to estimate cell-level performance; the simulation cell, not the
  individual seed, is the inferential block in the Friedman analysis."*

## FAZ 0 — Arşiv ve karantina (Öner + Claude Code) — TAMAMLANDI (2026-08-18)

1. Yedi koşum çıktısının SHA256'ları → `hash_tablosu_v2.md` (kanonik
   tabloya tarihli EK). 2. Karantina (silme YOK): bayat/sahte artefakt
   hashlenir, donmuş çalışmanın referans etmediği doğrulanır,
   `deprecated__<ad>__<hash8>.<uz>` adıyla `archive/deprecated/` altına
   taşınır; deprecated-manifest satırı yazılır. 3. Çıktı klasörü
   salt-okunur + yedek. 4. Ortam-provenance manifesti (Python/R,
   paketler, BLAS/LAPACK, thread, dtype, RNG namespace'leri, commit).

## FAZ 0.5 — `extension_decision_freeze_v0.md` (Öner onayı = imza; HASH'lenmeden Friedman/GLMM ayrıntısına ve FAZ 5 SSA sonucuna GİRİLMEZ)

**Method-space.** Çekirdek: PAM-Euclidean · GMM-native BIC/ICL ·
k_true=1 null bloğu · observed-support m–k response surface · φ×σ
response surface. Birinci halka: spherical KMeans (pin-memo kapılı,
winner-eligible) · PBM ("tek yeni ortak CVI eklenecekse ilk seçim" +
CH/DB artıklık ucu) · pairwise P/R/F1 · VI-ayrıştırması.
Diagnostic/koşullu: movMF (κ-politikası) · Gap · PS · PAC · Fang–Wang ·
S_Dbw · KL · t₅ · FPCA (ayrı representation kolu). Average:
`extension_role=sensitivity_only; winner_eligible=false;
block_D_eligible=false; SSA_deployment_eligible=false`. Excluded (geri
alınmaz): jump · DP-means · HDBSCAN · Piccolo · cepstral · funHDDC ·
James–Sugar · FCM/XB-yerli kol · GMM-tied · vanilla-Gap-null ·
PAM-L1(primary) · T-ızgara(primary).

**Faktör destekleri (yeni seviye İCAT EDİLMEZ).**
```
phi_support   = {0.80, 0.90, 0.97, 0.99}        ← 0.95 YOK (manifest-teyitli)
sigma_support = {0.1, 0.2, …, 1.0}               ← yalnız φ×σ bloğu için
m ∈ {5,10,20} · k_true ∈ {3,4,5,6,8} · 25 ≤ mk ≤ 100 → 11 gözlenen hücre:
  m=5: k{5,6,8} · m=10: k{3,4,5,6,8} · m=20: k{3,4,5}
```
φ×σ bloğu referans B/R yapısını sabit tutar (M_karisik · k_true=5 ·
ρ=0.615 · n_per=10); başka faktör çaprazlanmaz. Gözlenmeyen (m,k)
kombinasyonlarına extrapolation YASAK.

**Null bloğu — exact bilimsel destek (DONUK).**
```
null_semantics        = no_cluster_pure_noise
n_null                = {30, 40, 50, 60, 80}     ← frozen Blok-A toplamları (10×k_true)
noise_null            = {white, AR(phi=0.97)}    ← frozen ana gürültü faktörünün iki seviyesi
sigma_null            = not_applicable
n_seeds_null          = 100
single_prototype_null = excluded_from_extension  ← sensitivity olarak da koşulmaz; sonradan eklenmez
```
- **sigma_null gerekçesi (pinli cümle):** *Under the pure-noise null,
  multiplicative noise scale is exactly removed by per-series
  z-normalization; therefore sigma is not a null-design factor and is
  not crossed.* (Cebir: x=σε → z(x)=(σε−σε̄)/(σs_ε)=z(ε), her σ>0
  için.) İmplementasyon nominal σ=1 kullanabilir — yalnız hesaplama
  sabitidir; null zorluk ekseni olarak σ RAPORLANMAZ.
- Null için ayrıca φ∈{0.80,0.90,0.99} duyarlılık ızgarası EKLENMEZ —
  φ-robustness ayrı φ×σ bloğunda; null minimal ve yorumlanabilir kalır.
- **Primary endpoint:** **FCSP = P(k̂ > 1 | k_true = 1)** — terim:
  *false cluster-structure selection probability* ("FDR" DENMEZ;
  multiple-testing FDR'ıyla karıştırılmaz).
- **FCSP eligibility (bağlayıcı kural, aynen):** *FCSP-eligible
  selectors are only those within the frozen extension method-space
  whose preregistered native or arm-specific decision rule explicitly
  permits k=1. No ad-hoc post-selection fallback to k=1 is allowed.*
  Statüler: GMM-native BIC/ICL → eligible (native aday uzayı k=1..10);
  Gap → koşullu-eligible YALNIZ null-arm aday uzayı ve karar kuralı
  ön-kayıtta açıkça k=1 içeriyorsa; stability/diagnostic seçiciler →
  yalnız kendi ön-kayıtlı arm-kuralları k=1 üretiyorsa. k=2..10 ile
  sınırlı ortak CVI'lar FCSP estimandına uygun DEĞİLDİR ve "%100
  yanlış-pozitif" diye raporlanmaz.

**Metrik rolleri (donuk).** Primary k-seçim: P(k̂=k_true) · MAE_k ·
işaretli bias + P(k̂<k_true)/P(k̂>k_true). Secondary dış: ARI · AMI.
Diagnostic: oracle ARI-regret · VI-ayrıştırması · pairwise P/R/F1 ·
selection dispersion (**H/log|𝒦|**; |𝒦| seçici-bazlı manifest alanı:
ortak 9 · native 10 · restricted 9) · failure/undefined/coverage.
Dil pinleri: metrikler "tamamlayıcı"dır; ad "selection dispersion
across realizations"; target_k_regret zorunlu değil; betimsel
metriklerden otomatik FDR/FWER ailesi türetilmez.

**BIC/ICL pinleri.** Yön: *pre-registered optimum direction under the
stored criterion convention* — ham sklearn BIC **argmin**; dönüştürülmüş
skor yalnız işaret dönüşümü tanımlı+saklıysa argmax. Exact ICL tanımı DONUK (freeze §5'tekiyle aynı):
ICL_stored(k)=BIC_stored(k)+2·E(k), E(k)=−ΣΣτ·logτ (doğal log,
0log0:=0, τ=predict_proba); yön argmin; bağ → en küçük k (donmuş
isclose toleransı). Birim test sonra; tanım freeze sonrası seçilemez. Native primary k=1..10;
restricted sensitivity k=2..10 ŞİMDİ ön-kayıtlı. Asimetri cümlesi
(aynen): *"BIC/ICL use their native candidate space k=1..10; therefore
their recovery rates are model-native comparator outcomes and are not
interpreted as candidate-space-matched estimates relative to common
CVIs."* GMM parametreleri ve failure davranışı normatif bağımlılıklardan
AYNEN — yeniden açılmaz.

**PAM pinleri.** Euclidean · BUILD · SWAP-until-no-improvement ·
restart YOK · random_state inert · k=2–10. Tie-free fikstürlerde
bölüt-düzeyi permütasyon-değişmezliği zorunlu; exact-tie fikstürlerde
objective eşitliği + pinli kütüphane davranışının belgelenmesi.
`pam_tie_flag` yalnız implementasyon tie-tanısı sunuyorsa zorunlu;
değilse Seçenek A: terminal swap-komşuluğu denetimi
(`pam_terminal_tie`; kapsam sınırı provenance'a) veya Seçenek B:
`tie_detection_supported=false` — "tie oluşmadı" varsayılmaz; salt
loglama için custom PAM'a geçilmez. Ortam pini: paket
(sklearn_extra vs `kmedoids`/FastPAM) + sürüm prereg'de; FastPAM ise
exact-eşdeğerlik testi. Ön-kayıtlı redundans ucu: KMeans-PAM seçilen-k
uyumu (ayrışmanın aykırı-analog hücrelerde yoğunlaşması: tahmin).

**m–k pinleri (DONUK).**
```
mk_analysis_role                       = response_surface
mk_factor                              = mk_cell (11 levels)
formal_interaction_test                = false
posthoc_interaction_contrast_selection = prohibited
```
Yorum cümleleri (aynen): *"The m–k extension is interpreted through the
11 observed (m,k) cells. Because total sample size is deterministically
n=mk, the analysis does not identify independent marginal effects of m,
k, and total n, and no extrapolation is made to unobserved (m,k)
combinations."* · *"No formal factorial interaction test is part of
this extension. The m–k block is interpreted as an observed-support
response surface over the 11 preregistered cells; post-hoc selection of
interaction contrasts is prohibited."* Analiz: 11-seviye `mk_cell`
üzerinden surface-heterojenlik/omnibus değerlendirme + hücre-bazlı
tahminler + önceden tanımlı betimsel karşılaştırmalar; eşit hücre
ağırlığı; "full factorial m×k interaction" dili YASAK. Not: m sınıf
başına örnek sayısıdır — cluster-size imbalance faktörü DEĞİLDİR.

**Yorum kısıtları:** m/k/n bağımsız marjinal etki iddiası yok · native
BIC/ICL matched-estimator değil · diagnostic katmanlar frozen
deployment kazananını (Ward+CH) geriye dönük değiştirmez · genişletme
original confirmatory analiz değildir — statü cümlesi (aynen): *"The
extension was designed after inspection of the frozen benchmark and
tests explicitly preregistered robustness and method-space questions
rather than constituting the original confirmatory analysis."*

**Freeze prosedürü (self-hash YASAK):** hash belge DIŞINDA tutulur —
`sha256sum extension_decision_freeze_v0.md > extension_decision_freeze_v0.md.sha256`
→ her iki dosya birlikte `git add` + commit (+ tag). Belge içine
kendi hash'i YAZILMAZ. Freeze sonrası yöntem listesi/destekler
değişmez.

## FAZ 1 — Sıfır-koşum işler (Claude Code; 1 oturum)

**1.1 Denetim + metric-feasibility raporu (kod yazmadan):** etiket
tensörleri (seçilen-k / aday-k) diskte mi? aday-k ARI, GMM fit
alanları, seed-mapping, sürüm kayıtları? Her metrik için tablo: gerekli
girdi · mevcut mu · yeniden üretim gerekir mi · deterministik mi.
YALNIZ RAPOR.

**1.2 C-metrik betiği (S-06 etiketli):** MAE_k · RMSE_k · işaretli
bias · P(k̂<k_true)/P(k̂>k_true) · true-k rank (bağ=midrank) ·
selection dispersion (H/log|𝒦|; ortak katmanda |𝒦|=9) · ARI-regret.
Etiket varsa: AMI · VI-ayrıştırması (H(truth|Ĉ)=birleştirme kaybı,
H(Ĉ|truth)=bölme hatası) · pairwise P/R/F1 (k̂ ve k_true'da). Etiket
yoksa metrik SESSİZCE ATLANMAZ — `not_available_reason`; tercih:
bit-özdeş akışla yalnız (hücre,tohum,algoritma,k̂) bölütlerinin yeniden
üretimi (**mini-koşum olarak açıkça kaydedilir**, Öner onayıyla) veya
genişletmeye erteleme. Birim testler: perfect/merge/split/permütasyon/
alt-üst fikstürleri.

**1.3 Sağlamlık (protokol-öngörülü, betimsel):** ±0.1 σ-band kaydırma
({0.3–0.7}, {0.5–0.9}) ve achieved-σ ∈ [0.35, 0.81] yeniden skorlama;
16-çift sıralaması + Ward/KMeans farkı her varyantta; cümle pinli:
kazanan kararını değiştirmez.

## FAZ 2 — Friedman + Nemenyi (Claude Code)

Donmuş exact hiyerarşi (betik uygular, yorumlamaz; protokol satır
atıfları docstring'e): (1) hücre-içi toplama önce — 100 tohum → hücre
başına tek doğruluk; bias/corr_ari ortalama; tohum-başına test YOK.
(2) Birincil aile 5 üye: sil_euc · sil_cos · DB · CH · Dunn d1/D1
(temsilci konvansiyon gereği). (3) **Dört algoritma için dört ayrı
Friedman omnibus → dört omnibus p-değerine Holm → Holm-sonrası anlamlı
algoritmalarda Nemenyi** (+ CD diyagramı, Demšar 2006). (4) Dunn
aile-içi katman ayrı aile. (5) AR-only ayrı secondary Holm ailesi;
S-07 cümlesi rapora aynen. (6) Tüm hücreler; geçiş kısıtı YOK;
bias/corr_ari betimsel. Yazılım sürümleri provenance'a. Birim testler:
matris boyutları, aile üyelikleri, Holm sırası.

## FAZ 3 — GLMM (Öner + Claude Code)

Ön-koşul (Öner; kalem 7–8): R/lme4/blme sürüm pinleri + `sessionInfo()`;
checklist-12 doğrulama R betiğini Claude Code yazar, Öner koşar; fark →
değerler bağlayıcı + sapma kaydı. Claude Code: (1) `glmm_export.py` —
geçiş bandı 0.05–0.95; `sigma_c = sigma − 0.55` (başka ölçekleme YOK);
treatment kodlama; referanslar sil_euc · beyaz · P_konum · r045 · k=3;
8-seviyeli CVI; `(1|hucre) + (1|hucre:tohum)`. (2) `glmm_chain.R` —
S-02 dört aşaması birebir (A1 bobyqa+Nelder_Mead; tetik = convergence ∪
isSingular tol=1e-4; A2 bobyqa+bobyqa tek yeniden-koşum; A3
4-primary-CVI; A4 exact bglmer: fixef normal(sd=2.5), cov
wishart(df=level.dim+2.5, scale=Inf, posterior.scale="cov")).
(3) Algoritma başına; aşama/tetik logu. (4) σ₅₀ sınırı: çapraz-algoritma
kıyas yalnız full-data Blok-A tahminlerinden.

## FAZ 4 — Bozulma eğrileri

Doğruluk × σ; satırlar ρ, sütunlar gürültü (beyaz | AR .97); taralı
bant [0.35, 0.81]; GLMM kestirimi ham eğrilerin üzerine bindirilir ve
uyum orada doğrulanır (zorunlu). Şekil altı: S-01 dili + winner's-curse
+ iddia-kapsamı cümlesi.

## FAZ 5 — SSA deployment: Ward + CH (**freeze-v0 HASH'ine bağımlı**)

**Bağımlılık (bağlayıcı):** FAZ 0 → FAZ 0.5 HASH → FAZ 5. Freeze-v0
hash'lenmeden: SSA kümeleme sonucu ÜRETİLMEZ; `k_hat` OKUNMAZ; üyelik
üretilmez/yorumlanmaz; Transfer-QC sonucu yorumlanmaz. Freeze öncesi
yalnız hazırlık serbesttir: girdi dosyası varlığı + SHA256 doğrulama ·
betik varlığı · ortam/paket kontrolü · dry configuration validation.

Freeze sonrası koşum: (1) Girdi hash (tam):
`279f4c64f370c004fca3f62601cf50e9d7a2cdde1bb65d2d9ab32a69bef54dd2`
(male) · `f517500abd9a14b6bc48f53fe96586c617f28b10da622be859f2975f4bf737b7`
(female). (2) Donmuş boru hattı: ratio → 39/57 tam seri → z-norm
ddof=0 → Ward (sklearn AgglomerativeClustering, euclidean) → k=2–10 →
CH argmax = k̂; bağ/non-finite/sınır-k politikaları simülasyonla AYNI
kod yolu (S-06). (3) Runner-up koşulsuz (S-01): KMeans+CH SSA k̂'si de
raporlanır. (4) QC: `sigma_achieved` (kestirilmiş etiketlerle, S-05,
ddof=0) · `rho_max_achieved` (signed) + pair · Transfer QC: D-geometri
kapsaması (rapor maddesi). (5) Çıktı: cinsiyet başına k̂ + üyelikler +
QC + provenance JSON. (6) Genişletme sonuçları bu deployment'ı geriye
dönük DEĞİŞTİRMEZ. Paralel Öner görevi — Blocker 2: ön-ölçüm
artık-etiketlerinin yöntem+k belgesi → `acf_qc_ssa.py` koşulur
(deployment'ı bloklamaz; makale kalibrasyon anlatısı için şart).

## FAZ 6 — Makale montajı (Öner + bu sohbet) — ÇATAL AÇIK

Yapı: Giriş/Yöntem = protokol; Sonuçlar = Friedman → GLMM → eğriler →
sağlamlık → SSA deployment; runner-up + SE_MC + winner's-curse S-01
dilinde; iddia-kapsamı ve toplama-gerekçesi cümleleri aynen;
limitations: (i) k etkisi n/k=10 tasarımına koşulludur, (ii) bulgular
gürültü-yapısına koşulludur, (iii) null-yapı ve ağır-kuyruk donmuş
çalışmada sınanmamıştır; + Blok C beyaz-yalnız, n≫T'ye genellemez.
Şenbabaoğlu atfı yayın sürümünden son teyit. **Strateji çatalı
(Öner):** (önerilen — iki danışman yakınsak) donmuş-çalışma makalesi
gönderilir, genişletme ayrı ön-kayıtlı takip; (alternatif) aynı makale
→ Faz 6 = provisional v0.

## FAZ 7 — Genişletme (freeze-v0 iskeletinden; kendi gate'leri)

**7A. `extension_prereg_v1.md`:** freeze-v0 listesi/destekleri
DEĞİŞMEDEN detaylanır. Bölümler: amaç · frozen ilişkisi + statü
cümlesi · eligibility manifest alanları · algoritma/seçici pinleri ·
null blok · response-surface blokları · metrik rolleri · seed/RNG
(yeni namespace; frozen'la çakışma yasak) · S-04-analog
failure/undefined kuralları · analiz planı (ayrı modeller; original
GLMM'e eklenmez) · elemeler · çıktı şeması · hash/freeze · arm-bazlı
stop/go.

**7B. Çekirdek:** PAM (FAZ 0.5 pinleri) · BIC/ICL (FAZ 0.5 pinleri;
yön birim testi) · **null blok — bilimsel destek FAZ 0.5'te DONUK;
tasarım-memo yalnız hesaplama/uygulama detayı kapatır:** RNG namespace
haritası · output şeması · failure/undefined kodları · test vektörleri ·
exact implementasyon kontrolleri (n/noise/sigma/seed-sayısı/
single-prototype memoya BIRAKILMAZ) · m–k ve φ×σ response surface'ları
— FAZ 0.5 destekleri AYNEN; analiz `mk_cell` (formal etkileşim testi
YOK) / (φ, σ, φ×σ) ayrı modellerde, formüller ön-kayıtta.

**7C. Birinci halka:** spherical KMeans — pin-memo kapısı (objective ·
centroid normalizasyonu · init · n_init [simetri önerisi 50 — ön-kayıt
kararı] · boş-küme/sıfır-norm kuralı · yakınsama eşiği · seed haritası ·
sürüm · "KMeans'ten fiilen farklı" doğrulama testi); PBM — formül/yön/
singleton/sıfır-ayrım/epsilon/centroid tanımı + test vektörleri +
ortak hesap + artıklık ucu.

**7D. Diagnostic kollar (arm-bazlı gate; eksik = o kol NO-GO, çekirdek
GO):** Gap gate 12 kalem (base clustering kuralı · algoritma-başına W_k
tanımı · referans üreteci [donmuş boru hattının prototipsiz hali] ·
**φ kaynağı — deployment-parity: manifest-gerçeği YASAK; pinli
kestirimci veya sabit ön-ölçüm değeri** · inovasyon dağılımı · varyans
ölçekleme · z-norm sırası · B · RNG · aday k [null-arm'da k=1 dahilse
FCSP-eligible] · karar kuralı [1-SE vs argmax; sonuç görülerek
seçilmez] · tie/non-finite/failure). PS gate: fold/resampling · eşik
0.80 (0.8–0.9 aralığından gerekçeli) · aday k · algoritma-bazlı
projeksiyon kuralı (hierarchical: en-yakın-eğitim-centroidi) ·
singleton politikası · `undefined_k_mask` · `all_undefined` ·
`no_eligible_k` · sessiz fallback YOK · coverage +
P(k̂=k_true|defined) DAİMA AYRI; tek bileşik "PS accuracy" YASAK.
PAC/F–W/S_Dbw/KL/t₅/movMF/FPCA: statüleri + kaynak-teyit şeması
(`pending` koşulmaz; yerine aday alınmaz). KL notları: k^(2/146)
düzeltmesi fiilen boş; W₁₁ sınırı → yardımcı-hesap ilanı veya k=2–9.

**7E. Test → freeze → koşum:** unit → integration (mini manifest:
1 kol · 1 k · 1 σ · 1 ρ · 2 tohum) → **frozen-regression testi**
(donmuş alt-küme yeni kodla bit-özdeş; sapma = GLOBAL STOP) →
extension-manifest üretimi + doğrulama (duplicate/eksik kombinasyon/
seed-namespace çakışması/eligibility alanları) → hash + prereg'e yazım
+ commit → **smoke run** (yalnız yazılım doğruluğu; performans
değerlendirmesinde KULLANILMAZ) → Öner onayı → full run → analiz
(katman-ayrı: common · native · null · m–k · φ×σ) → raporlama
(tablo/figür şablonları prereg'de).

## Bağımlılık özeti (DAG)

```
FAZ 0 ─► FAZ 0.5 (freeze-v0 HASH)
             ├─► FAZ 1 ─► FAZ 2 ─► FAZ 3 ─► FAZ 4 ─► FAZ 6
             ├─► FAZ 5 ────────────────────────────► FAZ 6
             └─► FAZ 7 (kendi prereg/memo gate'leriyle)
FAZ 5, freeze-v0 hash'inden ÖNCE sonuç üretmez (yalnız hazırlık).
Öner kritik yolu: v0 onayı · kalem 7–8 · Blocker 2 · Faz 6 çatalı ·
spherical memo imzası (null memosu artık yalnız implementasyon —
imza yükü hafifledi).
```

## Claude Code oturum şablonu (ortak)

1. Repo kökünde aç; bu belgeden ilgili faz bölümünü yapıştır.
2. İlk komut: girdi hash doğrulama + log (normatif bağımlılıklar dahil).
3. Memo-önce kuralı: 7B–7D'de imzalı memo/prereg olmadan kod yok.
4. Betik + birim test birlikte; test geçmeden çıktı üretilmez.
5. Çıktılar `analysis/outputs/<faz>/`; SHA256'lar faz-sonu raporuna;
   metadata'da kaynak hash + commit + timestamp.
6. STOP: global-STOP → durdur, bu sohbete getir; arm-STOP → yalnız o
   kolu beklet, kalanla devam.
7. Oturum sonu devir notu (ne bitti · hash'ler · ne bekliyor).
