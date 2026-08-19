# Yol haritası v3 — FINAL, kendine-yeterli kanonik yürütme belgesi (2026-08-18)

**v2 (`d740dc78…`) + EK-1 (`028e0136…`) + EK-2 (`38b6b5a2…`) bu belgede
KONSOLİDE edilmiştir ve üçünün yerine geçer.** Tarihsel sürümler arşivde
kalır; Claude Code'a bağlayıcı yürütme kaynağı olarak YALNIZ bu dosya
verilir (hiçbir madde "önceki sürümdeki gibi" demez — tam metin burada).

**Bu revizyonun kaynağı:** altı-model değerlendirmesinin ChatGPT
süzmesi (`8c23c693…`). Kabul edilen beş bilimsel-support düzeltmesi +
governance iyileştirmeleri işlendi; reddedilenler değişiklik günlüğünde.

## Değişiklik günlüğü ve hakemlik özeti (v2+EK → v3)

**Kabul (bilimsel-support):**
1. **φ desteği düzeltildi — ÖZ-DÜZELTME:** φ×σ ızgarasındaki 0.95
   donmuş seviye DEĞİLDİR; manifestten bu revizyonda yeniden doğrulandı:
   φ ∈ {0.80, 0.90, 0.97, 0.99} (B8/B9/ana panel/B10). 0.95, protokol
   anlatısındaki ön-tarama cümlesinden ızgaraya sızdı ve benim
   "yeni seviye icat edilmez" kuralıma rağmen tarafımdan taşındı —
   yakalama Fugu'nun, teyit kaynaktan. (Kredi + kusur kaydı.)
2. **Null bloğun bilimsel semantiği ŞİMDİ donuyor** (aşağıda FAZ 0.5).
3. **Candidate-space-aware entropi:** H_norm = H / log|𝒦|; |𝒦|
   hard-code edilmez, seçicinin ön-kayıtlı aday desteğinden okunur
   (ortak katman 9; native BIC/ICL 10; restricted 9).
4. **m–k bloğu yeniden adlandı:** "observed-support m–k response
   surface" — `mk_cell` rank-eksikliği çözer ama n=mk determinizmini
   çözmez; m, k ve toplam n'nin bağımsız marjinal etkileri İDDİA
   EDİLMEZ (ön-kayıt cümlesi FAZ 7'de).
5. **Belge zinciri kendine-yeterli hale getirildi** (bu dosya).

**Kabul (governance, bloklamayan):** makale iddia-kapsamı cümlesi;
100-tohum toplama gerekçe cümlesi; ortam-provenance manifesti;
koşullu-kaynak-teyit şeması (`status | source_status |
replacement_allowed=false` — teyit başarısızsa yöntem koşulmaz, YERİNE
ADAY ALINMAZ); STOP kapsamının katman-bazlı (arm-specific) yapılması.

**Kanonik protokol kontrolüyle kapanan itirazlar:** GMM parametreleri
frozen'dır (yeniden açılmaz); Friedman–Holm–Nemenyi hiyerarşisi
protokolde nettir (aşağıya aynen taşındı) — Manus'un noise-stratified
primary önerisi RED (sonuç görüldükten sonra primary estimand
değiştirilmez).

**Reddedilenler (yeniden açılmaz):** primary'nin gürültüye göre
bölünmesi · m×k'nin çekirdekten düşürülmesi · Jump'ın geri alınması ·
AMI'nin "method block" sayılması · 13 betimsel metrik için otomatik
FDR/FWER ailesi (betimsel metrik p-değeri üretmez; FCSP bir error-rate
estimandıdır, multiple-testing FDR'ı değildir) · diagnostic pin eksiği
yüzünden global STOP · Gemini'nin kategorik elemeleri (stability/
S_Dbw/FDA — mevcut koşullu statüler korunur) · Gemini'nin "Gap yalnız
null'da anlamlı" genellemesi · Manus'un target_k_regret'i (negatif
olabilir; oracle-regret estimandı korunur).

---

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
- **STOP kapsamı katman-bazlıdır:** bir diagnostic/conditional kolun
  pin'i eksikse YALNIZ o kol NO-GO'dur; çekirdek durmaz. **Global STOP
  yalnız:** frozen-regression testinin bozulması · sınıf-(i)/çekirdek
  pin eksiği · manifest/namespace çakışması · freeze-v0 hash'lenmeden
  ikincil sonuç ayrıntısına girilmesi.
- Koşullu-kaynak-teyit şeması her diagnostic yöntemde:
  `status = committed|conditional|excluded`,
  `source_status = verified|pending`, `replacement_allowed = false`.
- Claude Code metodolojik çözüm ÖNERMEZ; belirsizlikte durur.
- Makale iddia-kapsamı (pinli cümle): *"Within the prespecified method
  space evaluated in the frozen benchmark, Ward+CH obtained the highest
  prespecified winner score."* Evrensel-üstünlük dili YASAK.
- Toplama gerekçesi (pinli cümle): *"Seeds are Monte Carlo realizations
  used to estimate cell-level performance; the simulation cell, not the
  individual seed, is the inferential block in the Friedman analysis."*

---

## FAZ 0 — Arşiv ve karantina (Öner + Claude Code)

1. Yedi koşum çıktısının (`results_cvi.parquet`, `results_alg.parquet`,
   `results_candidates.parquet`, `results_dataqc.parquet`,
   `winner_population_accuracy_8x4.csv`, `winner_report.json`,
   `provenance_final.json`) SHA256'ları → `hash_tablosu_v2.md`
   (mevcut kanonik tabloya tarihli EK; değiştirme yok).
2. **Karantina (silme YOK):** bayat/sahte artefakt (`seed_scheme.py` r1
   `559a7be5…`; sürücü promptu v1/v2; sahte `run_matrix_v4.csv`
   `4186bb20…`; yol haritası v1/v2/EK'ler — arşiv kopyası olarak) önce
   hashlenir, donmuş çalışmanın referans etmediği doğrulanır,
   **yeniden adlandırılarak** (`deprecated__<ad>__<hash8>.<uz>`)
   `archive/deprecated/` altına taşınır; deprecated-manifest satırı
   yazılır (hash · eski yol · yeni yol · neden · tarih).
3. Çıktı klasörü salt-okunur + yedek.
4. **Ortam-provenance manifesti** (reproducibility maddesi): Python/R
   sürümleri, paket sürümleri, BLAS/LAPACK, thread değişkenleri, float
   dtype, RNG namespace'leri, git commit hash.

**Kapı 0:** hash tablosu v2 + deprecated-manifest + ortam manifesti.

## FAZ 0.5 — `extension_decision_freeze_v0.md` (Öner onayı = imza; hash'lenmeden Friedman/GLMM/SSA ikincil ayrıntısına GİRİLMEZ)

Kendine-yeterli freeze belgesi; asgari karar tablosu AYNEN:

**Method-space.** Çekirdek: PAM-Euclidean · GMM-native BIC/ICL ·
k_true=1 null bloğu · observed-support m–k response surface · φ×σ
response surface. Birinci halka: spherical KMeans · PBM ("tek yeni ortak
CVI eklenecekse ilk seçim" + CH/DB artıklık ucu) · pairwise P/R/F1 ·
VI-ayrıştırması. Diagnostic/koşullu: movMF (κ-politikası) · Gap · PS ·
PAC · Fang–Wang · S_Dbw · KL · t₅ · FPCA (ayrı representation kolu).
Average: `extension_role=sensitivity_only; winner_eligible=false;
block_D_eligible=false; SSA_deployment_eligible=false` (v0 onayı =
imza). Excluded (geri alınmaz): jump · DP-means · HDBSCAN · Piccolo ·
cepstral · funHDDC · James–Sugar · FCM/XB-yerli kol · GMM-tied ·
vanilla-Gap-null · PAM-L1(primary) · T-ızgara(primary).

**Faktör desteği.**
```
phi_support   = {0.80, 0.90, 0.97, 0.99}        ← 0.95 YOK (manifest-teyitli)
sigma_support = {0.1, 0.2, …, 1.0}
φ×σ bloğu: referans B/R yapısı sabit (M_karisik, k_true=5, ρ=0.615,
n_per=10); yalnız bu iki destek çaprazlanır; başka faktör eklenmez.
m ∈ {5,10,20}, k ∈ {3,4,5,6,8}, 25 ≤ mk ≤ 100 → 11 gözlenen hücre:
m=5: k{5,6,8} · m=10: k{3,4,5,6,8} · m=20: k{3,4,5}
```

**Null bloğu — bilimsel semantik ŞİMDİ donuyor.** Primary null:
*no-cluster pure-noise null* — deterministik prototip yok; donmuş
beyaz/AR gürültü üreteci ve seri-bazlı z-norm korunur. Primary endpoint:
**FCSP = P(k̂>1 | k_true=1)** — terim: *false cluster-structure
selection probability* (FDR DENMEZ; multiple-testing FDR'ıyla
karıştırılmaz). Yalnız k=1 dönebilen seçiciler FCSP-eligible; k=1
dönemeyen ortak CVI'lar "%100 yanlış-pozitif" diye DEĞERLENDİRİLMEZ
(aday-uzayı gereği estimanda uygun değiller). Tek-prototip ("one shared
shape") null'u istenirse ŞİMDİ sensitivity olarak etiketlenir —
sonradan eklenmez. (RNG namespace, failure alanları, test vektörleri
prereg/pin-memo'da kapanır.)

**Metrik rolleri (donuk).** Primary k-seçim: P(k̂=k_true) · MAE_k ·
işaretli bias + P(k̂<k_true)/P(k̂>k_true). Secondary dış bölümleme:
ARI · AMI. Diagnostic: oracle ARI-regret (max_k ARI − ARI(k̂)) ·
VI-ayrıştırması · pairwise P/R/F1 · selection dispersion
(**H/log|𝒦|**, |𝒦| seçici-bazlı manifest alanı) · failure/undefined/
coverage oranları. Dil pinli: ARI/AMI/VI/P-R-F1 "birbirini tamamlar";
"dengesizlik sorununu çözer" DENMEZ.

**BIC/ICL pinleri.** Yön: *pre-registered optimum direction under the
stored criterion convention* — ham sklearn BIC argmin; dönüştürülmüş
skor yalnız işaret dönüşümü tanımlı+saklıysa argmax. Exact ICL formülü
+ işaret ilişkisi yazılır ve birim testle doğrulanır. Native primary
k=1..10; restricted sensitivity k=2..10 ŞİMDİ ön-kayıtlı. Asimetri
cümlesi aynen: *"BIC/ICL use their native candidate space k=1..10;
therefore their recovery rates are model-native comparator outcomes and
are not interpreted as candidate-space-matched estimates relative to
common CVIs."* Convergence/non-finite/failure davranışı pinli (frozen
S-04 deseni). GMM parametreleri frozen protokolden AYNEN — yeniden
açılmaz.

**PAM pinleri.** Euclidean · BUILD · SWAP-until-no-improvement ·
restart yok · random_state inert · k=2–10. Bağ/permütasyon: tie-free
fikstürlerde bölüt-düzeyi permütasyon-değişmezliği zorunlu; exact-tie
fikstürlerde objective eşitliği + pinli kütüphane sürümünün
deterministik davranışının belgelenmesi. `pam_tie_flag` yalnız
implementasyon tie-tanısı sunuyorsa zorunlu; sunmuyorsa Seçenek A:
terminal swap-komşuluğu denetimi (final çözümün tüm tekli takas
objective'leri mesafe matrisinden; exact eşitlik → `pam_terminal_tie=1`;
kapsam sınırı provenance'a) veya Seçenek B:
`tie_detection_supported=false` kaydı — "tie oluşmadı" sessizce
VARSAYILMAZ. Salt tie-loglama için custom PAM'a geçilmez. Ortam pini:
sklearn_extra vs `kmedoids` (FastPAM) — seçilen paket+sürüm ön-kayda;
FastPAM ise exact-eşdeğerlik testi. Ön-kayıtlı redundans ucu:
KMeans-PAM seçilen-k uyumu; ayrışmanın aykırı-analog hücrelerde
yoğunlaşması beklenir (tahmin).

**m–k yorum cümlesi (aynen ön-kayda):** *"The m–k extension is
interpreted through the 11 observed (m,k) cells. Because total sample
size is deterministically n=mk, the analysis does not identify
independent marginal effects of m, k, and total n, and no extrapolation
is made to unobserved (m,k) combinations."* Hesap biçimi: tek 11-seviye
`mk_cell` kategorik faktörü + yalnız gözlenen-destek kontrastları;
"full factorial m×k interaction" dili YASAK; etkileşim inferansı
istenirse estimable kontrast matrisi ÖNCEDEN yazılır. Hücre
ağırlıklandırma: eşit (tohum-içi toplama önce).

**Yorum kısıtları (donuk):** m/k/n bağımsız marjinal etki iddiası yok ·
native BIC/ICL matched-estimator değil · diagnostic katmanlar frozen
deployment winner'ı geriye dönük değiştirmez · genişletme original
confirmatory analiz değildir — statü cümlesi aynen: *"The extension was
designed after inspection of the frozen benchmark and tests explicitly
preregistered robustness and method-space questions rather than
constituting the original confirmatory analysis."*

SHA256 + git commit → **freeze tamam**; sonrası yöntem LİSTESİ değişmez.

## FAZ 1 — Sıfır-koşum işler (Claude Code; 1 oturum)

**1.1 Denetim + metric-feasibility raporu (kod yazmadan):** etiket
tensörleri (seçilen-k / aday-k) diskte mi? aday-k ARI, GMM fit alanları,
seed-mapping, sürüm kayıtları? Her metrik için tablo: gerekli girdi ·
mevcut mu · yeniden üretim gerekir mi · deterministik mi. YALNIZ RAPOR.

**1.2 C-metrik betiği (S-06 etiketli):** MAE_k · RMSE_k · işaretli
bias · P(k̂<k_true)/P(k̂>k_true) · true-k rank (bağ=midrank) ·
selection dispersion (H/log|𝒦|; ortak katmanda |𝒦|=9) · ARI-regret.
Etiket varsa: AMI · VI-ayrıştırması (H(truth|Ĉ)=birleştirme kaybı,
H(Ĉ|truth)=bölme hatası) · pairwise P/R/F1 (k̂ ve k_true'da). Etiket
yoksa metrik SESSİZCE ATLANMAZ — `not_available_reason`; tercih: bit-özdeş
akışla yalnız (hücre,tohum,algoritma,k̂) bölütlerinin yeniden üretimi
(**mini-koşum olarak açıkça kaydedilir**, Öner onayıyla) veya
genişletmeye erteleme. Birim testler: perfect/merge/split/permütasyon/
alt-üst fikstürleri.

**1.3 Sağlamlık (protokol-öngörülü, betimsel):** ±0.1 σ-band kaydırma
({0.3–0.7}, {0.5–0.9}) ve achieved-σ ∈ [0.35, 0.81] yeniden skorlama;
16-çift sıralaması + Ward/KMeans farkı her varyantta; cümle pinli:
kazanan kararını değiştirmez.

**Kapı 1:** üç çıktı hash'li; ham çıktıya dokunulmadı.

## FAZ 2 — Friedman + Nemenyi (Claude Code)

Donmuş exact hiyerarşi (betik uygular, yorumlamaz; protokol satır
atıfları docstring'e):
1. Önce hücre-içi toplama: 100 tohum → hücre başına tek doğruluk;
   bias/corr_ari ortalama. Tohum-başına test YOK (gerekçe cümlesi pinli).
2. Birincil aile 5 üye: sil_euc · sil_cos · DB · CH · Dunn d1/D1
   (temsilci d1/D1 — konvansiyon gereği).
3. **Dört algoritma için dört ayrı Friedman omnibus → dört omnibus
   p-değerine Holm → Holm-sonrası anlamlı algoritmalarda Nemenyi**
   (+ kritik-fark diyagramı, Demšar 2006).
4. Dunn aile-içi katman ayrı Friedman+Nemenyi ailesi.
5. AR-only analiz ayrı secondary Holm ailesi; S-07 cümlesi rapora aynen
   (global cross-algorithm FWER iddiası yok).
6. Tüm hücreler; geçiş kısıtı YOK. bias/corr_ari betimsel — test edilmez.
Yazılım sürümleri provenance'a. Birim testler: matris boyutları, aile
üyelikleri, Holm sırası.

## FAZ 3 — GLMM (Öner + Claude Code)

Ön-koşul (Öner; kalem 7–8): R/lme4/blme sürüm pinleri + `sessionInfo()`;
checklist-12 doğrulama R betiğini Claude Code yazar, Öner koşar
(`formals(glmerControl)`, `formals(bglmer)`, prior kurucuları,
`normal(sd=2.5)` yayılım davranışı, `level.dim` çözümü); fark → değerler
bağlayıcı + sapma kaydı.

Claude Code: (1) `glmm_export.py` — geçiş bandı 0.05–0.95 hücre filtresi;
`sigma_c = sigma − 0.55` (BAŞKA ölçekleme YOK); treatment kodlama;
referanslar sil_euc · beyaz · P_konum · r045 · k=3; 8-seviyeli CVI;
`(1|hucre) + (1|hucre:tohum)`. (2) `glmm_chain.R` — S-02 dört aşaması
birebir: A1 `glmerControl(optimizer=c("bobyqa","Nelder_Mead"))`; tetik =
{convergence uyarısı} ∪ {isSingular, tol=1e-4}; A2 `c("bobyqa","bobyqa")`
tek yeniden-koşum; A3 4-primary-CVI; A4 exact `bglmer` (fixef
normal(sd=2.5); cov wishart(df=level.dim+2.5, scale=Inf,
posterior.scale="cov")). (3) Algoritma başına koş; aşama/tetik logu.
(4) σ₅₀ sınırı: çapraz-algoritma kıyas yalnız full-data Blok-A
tahminlerinden; transition-kısıtlı kestirimler algoritma-içi.

## FAZ 4 — Bozulma eğrileri (ana şekil)

Doğruluk × σ; satırlar ρ, sütunlar gürültü (beyaz | AR .97); taralı bant
[0.35, 0.81]; GLMM kestirimi ham eğrilerin üzerine bindirilir ve uyum
orada doğrulanır (zorunlu). Şekil altı: S-01 dili + winner's-curse şerhi
+ iddia-kapsamı cümlesi.

## FAZ 5 — SSA deployment: Ward + CH (paralel hat; hemen başlatılabilir)

1. Girdi hash: `male_…csv` `279f4c64…`, `female_…csv` `f5175008…`.
2. Donmuş boru hattı: ratio → 39/57 tam seri → z-norm ddof=0 →
   Ward (sklearn AgglomerativeClustering, euclidean) → k=2–10 →
   CH argmax = k̂; bağ/non-finite/sınır-k politikaları simülasyonla
   AYNI kod yolu (S-06).
3. Runner-up koşulsuz (S-01): KMeans+CH SSA k̂'si de raporlanır.
4. QC: `sigma_achieved` (kestirilmiş etiketlerle, S-05, ddof=0),
   `rho_max_achieved` (signed) + pair; Transfer QC: D-geometri kapsaması
   (rapor maddesi, kapı değil).
5. Çıktı: cinsiyet başına k̂ + üyelikler + QC + provenance JSON.
6. **Genişletme sonuçları bu deployment'ı geriye dönük DEĞİŞTİRMEZ.**
Paralel Öner görevi — Blocker 2: ön-ölçüm artık-etiketlerinin yöntem+k
belgesi → `acf_qc_ssa.py` (LABEL_METHOD/LABEL_K) koşulur. Deployment'ı
bloklamaz; makale kalibrasyon anlatısı için şart.

## FAZ 6 — Makale montajı (Öner + bu sohbet) — ÇATAL AÇIK

Yapı: Giriş/Yöntem = protokol; Sonuçlar = Friedman → GLMM → eğriler →
sağlamlık → SSA deployment; runner-up + SE_MC + winner's-curse S-01
dilinde; iddia-kapsamı ve toplama-gerekçesi cümleleri aynen; limitations:
(i) k etkisi n/k=10 tasarımına koşulludur, (ii) bulgular gürültü-yapısına
koşulludur, (iii) null-yapı ve ağır-kuyruk sınanmamıştır; + Blok C
beyaz-yalnız, n≫T'ye genellemez. Şenbabaoğlu atfı yayın sürümünden son
teyit. **Strateji çatalı (Öner):** (önerilen — iki danışman yakınsak)
donmuş-çalışma makalesi gönderilir, genişletme ayrı ön-kayıtlı takip
("in preparation"); (alternatif) aynı makale → Faz 6 = provisional v0.

## FAZ 7 — Genişletme (freeze-v0 iskeletinden; Faz 1–6'yı beklemez, geciktirmez)

**7A. `extension_prereg_v1.md`:** v0 listesi DEĞİŞMEDEN detaylanır.
Bölümler: amaç · frozen ilişkisi + statü cümlesi · eligibility manifest
alanları · algoritma/seçici pinleri · null blok · response-surface
blokları · metrik rolleri · seed/RNG (yeni namespace; frozen'la çakışma
yasak) · S-04-analog failure/undefined kuralları · analiz planı (ayrı
modeller; original GLMM'e eklenmez) · elemeler · çıktı şeması ·
hash/freeze · arm-bazlı stop/go.

**7B. Çekirdek:** PAM (FAZ 0.5 pinleri) · BIC/ICL (FAZ 0.5 pinleri;
yön birim testi) · null blok — tasarım-memo → Öner imzası → kod (memo:
n-düzeyleri önerisi A-toplamlarıyla eşleme {30,40,50,60,80}; σ/φ
düzeyleri; k=1..10 politikası; seed-namespace) · m–k ve φ×σ response
surface'ları — FAZ 0.5 destekleri AYNEN, yeni seviye/faktör yok; analiz
`mk_cell` / (φ,σ,φ×σ) ayrı modellerde, formüller ön-kayıtta.

**7C. Birinci halka:** spherical KMeans — pin-memo kapısı (objective ·
centroid normalizasyonu · init · n_init [simetri önerisi 50 — ön-kayıt
kararı] · boş-küme/sıfır-norm kuralı · yakınsama eşiği · seed haritası ·
sürüm · "KMeans'ten fiilen farklı" doğrulama testi); PBM — formül/yön/
singleton/sıfır-ayrım/epsilon/centroid tanımı + test vektörleri + tüm
algoritmaların bölütlerinde ortak hesap + artıklık ucu.

**7D. Diagnostic kollar (her biri KENDİ gate'iyle; eksik = o kol NO-GO,
çekirdek GO):**
- **Gap gate (12 kalem):** base clustering kuralı · W_k tanımı
  (algoritma-başına: SSE vs medoid-maliyeti) · referans üreteci
  [somutlama: donmuş boru hattının prototipsiz hali] · **φ kaynağı —
  deployment-parity** (manifest-gerçeği YASAK; pinli kestirimci veya
  sabit ön-ölçüm değeri; SSA'da aynen uygulanabilir) · inovasyon
  dağılımı · varyans ölçekleme · z-norm sırası · B · RNG · aday k ·
  karar kuralı (1-SE vs argmax — sonuç görülerek seçilmez; ikisi
  isteniyorsa iki ön-kayıtlı varyant) · tie/non-finite/failure.
- **PS gate:** fold/resampling tasarımı · eşik (0.80; 0.8–0.9
  aralığından gerekçeli) · aday k · algoritma-bazlı projeksiyon kuralı
  (hierarchical: en-yakın-eğitim-centroidi) · singleton politikası ·
  `undefined_k_mask` · `all_undefined` · `no_eligible_k` · sessiz
  fallback YOK · coverage + P(k̂=k_true|defined) DAİMA AYRI; tek bileşik
  "PS accuracy" YASAK.
- PAC/F–W/S_Dbw/KL/t₅/movMF/FPCA: konsolide statüleri + kaynak-teyit
  şeması (`source_status=pending` olan koşulmaz; yerine aday alınmaz).
  KL notları: k^(2/146) düzeltmesi fiilen boş; W₁₁ sınırı → yardımcı-hesap
  ilanı veya k=2–9 kısıtı.

**7E. Test → freeze → koşum:** unit → integration (mini manifest: 1 kol ·
1 k · 1 σ · 1 ρ · 2 tohum) → **frozen-regression testi** (donmuş
alt-küme yeni kodla bit-özdeş; sapma = GLOBAL STOP) →
extension-manifest üretimi + doğrulama (duplicate/eksik kombinasyon/
seed-namespace çakışması/eligibility alanları) → hash + prereg'e yazım +
commit → **smoke run** (yalnız yazılım doğruluğu; performans
değerlendirmesinde KULLANILMAZ) → Öner onayı → full run → analiz
(katman-ayrı: common · native · null · m–k · φ×σ) → raporlama
(tablo/figür şablonları prereg'de).

## Bağımlılık özeti

```
FAZ 0 ─► FAZ 0.5 (freeze-v0 HASH) ─► FAZ 1 ─► FAZ 2 ─► FAZ 3 ─► FAZ 4 ─┐
  │                                                                      ├─► FAZ 6
  └────────► FAZ 5 (bağımsız; Blocker-2 paralel) ────────────────────────┘
FAZ 7: v0 iskeletinden; kendi gate'leri (7A imza, kaynak-teyit, memolar)
kapanmadan kod yok; arm-bazlı NO-GO çekirdeği durdurmaz.
Öner kritik yolu: v0 onayı · kalem 7–8 · Blocker 2 · Faz 6 çatalı ·
null/spherical memo imzaları.
```

## Claude Code oturum şablonu (ortak)

1. Repo kökünde aç; bu belgeden ilgili faz bölümünü yapıştır.
2. İlk komut: girdi hash doğrulama + log.
3. Memo-önce kuralı: 7B–7D'de imzalı memo/prereg olmadan kod yok.
4. Betik + birim test birlikte; test geçmeden çıktı üretilmez.
5. Çıktılar `analysis/outputs/<faz>/`; her çıktının SHA256'sı faz-sonu
   raporuna; metadata'da kaynak hash + commit + timestamp.
6. STOP: global-STOP listesindekiler → durdur, bu sohbete getir;
   arm-STOP → yalnız o kolu beklet, kalanla devam.
7. Oturum sonu devir notu (ne bitti · hash'ler · ne bekliyor).
