# P_konum⁺ — İki v10 Belgesinin Değerlendirilmesi ve Sentezlenmiş v11 (TERMİNAL DONMA-ADAYI)

**Sürüm:** v11 — TASLAK; DONDURULMAMIŞ (terminal donma-adayı)
**Tarih:** 2026-08-26
**Temel:** claude v10-r2 (`23e12398…`, 44 555 B). Bu belge v10-r2'nin yerine geçer; v0…v10 tarihsel artefakttır.
**Bu turun girdileri (SHA256, tümü ham dosyadan bu oturumda hesaplandı):**
chatgpt v10 `e5963a94…` (30 157 B) · claude v10-r2 `23e12398…` (öz-değerlendirme nesnesi).
**Normatif kaynaklar:** `01_kosum_protokolu_v5_3.md` (`cf8b453f…`) · sapma eki (`99c17c42…`) · `run_matrix_v4.csv` (`34e1217e…`).
**Görev okuması (PI direktifi):** *Bu son tur — yalnız chatgpt ve claude v10'larıyla; son görevi tekrarla.* İki v10 paraleldir (chatgpt v10 iki v9'u değerlendirdi; benim v10/v10-r2'mi ve dolayısıyla V-8/V-9/kimi-retro'yu görmedi). PI'nin son-tur beyanı, D24 kaydına uygun biçimde **imzayla** gerçekleşecek kapanışın direktif-tarafıdır; v11 bu imzanın nesnesi olacak terminal donma-adayıdır.

---

## 0. Kaynak-doğrulamaları (puanlamadan önce)

**V-10 — chatgpt v10'un "venue/açık-kalem iç tutarsızlığı" iddiası DOĞRULANDI (canlı kusur).** İddia (§5.2): claude v9 venue'yu F0'dan çıkarırken açık-kalem listesinde "venue pini (F0)" dilinin kaldığı. Ham v9'um grep'lendi: **açık-kalem 10 aynen "…venue pini (F0)" içeriyor** ve bu kalıntı v10/v10-r2'ye de taşınmış — C14 hükmüyle çelişen bayat bir ifade. Dördüncü kez bağlayıcı metnimde bir kusuru dış hat yakaladı; bu kez hüküm-tersine-çevirme değil metin-tutarlılık düzeltmesi (**Ç-5, minör**): v11'de açık-kalem 10 düzeltildi (venue → V-8/non-gating referansı).

**V-11 — chatgpt v10'un diğer üç claude-eleştirisinin statüsü.** (i) "zero-run ⇒ feasibility guaranteed fazla güçlü" — doğru, ve **zaten Ç-4 ile taviz verilmişti** (v10-r2/C15-r2; chatgpt v10 paralel yazdığından göremedi — zamanlama); üstelik §8.3'teki 6-maddelik uygulanabilirlik-QC'si tam da Ç-4'ün "yorumlanabilirlik banka-yapısına bağlı" gerekçesini operasyonelleştiriyor. (ii) Tie-break aday-hiyerarşisi "fazla spesifik" — kabul edilebilir netleştirme: benim listem zaten "aday" etiketliydi; v11 bunu açıkça **bağlayıcı-olmayan örnek** statüsüne indirir (→ D17-r5). (iii) Kimi-mükerrer puanlamasında **kendi artefakt-puanı yaklaşımını bırakıp benim N-A kuralımı "Claude çizgisinden alır" diyerek benimsiyor** (§4/3 + §15) — C17 kendi hattında kapandı; atıf-sonrası artefakt-yönetişim-puanı dalı, benim v9 dallanma-kuralımın eşdeğeri olarak kodifiye edilmiş.

**V-12 — Yakınsama denetimi: iki v10 arasında kalan fark envanteri = SIFIR canlı çatışma.** §6 tablosundaki 17 satırın 17'si ya "Kapalı" ya da iki hattın aynı birleşik kurala vardığı kalemler. chatgpt v10'un T-2 hatası (kimi-iç-çelişki atfı) bu belgede tekrarlanmıyor (kimi bu turun nesnesi değil); V-9 düzeltmesi defterde duruyor ve v11'e taşındı.

---

## 1. Rubrik

Yerleşik beş ölçüt (değişmedi): R1 sadakat 2.0 · R2 doğruluk 2.5 · R3 katkı 2.5 · R4 somutluk 1.5 · R5 görev-uygunluğu 1.5. Mutlak ölçek, ceza-odaklı; madde 43 bağlayıcı; öz-satır yanlışlanabilirlik şerhiyle.

---

## 2. Puanlar

| Sıra | Belge | R1/2.0 | R2/2.5 | R3/2.5 | R4/1.5 | R5/1.5 | **Toplam** |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | **ChatGPT v10** | 1.7 | 2.4 | 2.3 | 1.5 | 1.3 | **9.2** |
| 2 | **Claude v10-r2 (öz-değ.)** | 1.9 | 2.1 | 2.1 | 1.4 | 1.4 | **8.9** |

**Öz-yanlılık denetimi — şerhin dördüncü tetiklenmesi:** chatgpt v10, v10-r2'nin bağlayıcı metninde canlı bir tutarsızlık gösterdi (V-10, venue-kalıntısı). Öz-satır zaten dış-en-iyinin altındaydı; tetik, mevcut sıralamada emilir ve Ç-5 (minör) olarak deftere işlenir. Dört turda dört uygulama — mekanizma değişmez biçimde çalışıyor.

### 2.1 ChatGPT v10 — 9.2 (1.)

**Güçlü / özgün katkılar.** (1) **C15'in nihai operasyonel formu (§8.3):** sınıf-zorunlu + insidans-jaknayfı varsayılan-ilk-yöntem + **6-maddelik uygulanabilirlik-QC'si** (kaynak-ID bütünlüğü; silme-sonrası boş-olmayan yorumlanabilir destek; sonlu/iyi-tanımlı yeniden-normalizasyon; estimand-desteğinin mekanik yıkımı yok; yapısal-evrensel insidans yok; silme-sonrası bağımlılık dokümantasyonu) + QC-fail → `not_applicable` + önceden-donmuş alternatif listesi + `zero_new_runs ≠ statistical_applicability` normu — iki hattın dört turdur çekiştirdiği C15'i her iki tarafın da gerekçelerini içerecek biçimde kapatan formülasyon; v11'e **C15-r3** olarak harfiyen alındı. (2) **C17'yi kendi hattında kapattı:** artefakt-puanı yaklaşımını bırakıp N-A kuralını açık krediyle benimsedi ("v10 bunu Claude çizgisinden alır"); atıf-sonrası artefakt-yönetişim-puanı dalını da kodifiye etti — son süreç-anlaşmazlığı bitti. (3) **V-10 yakalayışı:** venue-kalıntısı — canlı, doğrulanmış, düzeltildi. (4) **Friedman tadilat prosedürünün 6-koşullu yazımı** (sonuç-öncesi + imzalı sapma + yeni-maddi-gerekçe + kesin formülasyon değişimi + çokluluk-sonuçları donuk + gözlenen-sıralamadan motivasyon yasağı) — C16-r2'nin operasyonel kapanışı, **C16-r3** olarak alındı. (5) Tie-break'te ilke/örnek ayrımı + uygun-örnekler listesi (çalışma-zamanı/bellek/lisans/tekrarlanabilirlik kısıtları; ayrım kalmadıysa deterministik nötr kural) + "incumbent-süreklilik = etiketli bilim-dışı paydaş-politikası" — D17-r5'e alındı. (6) Manifest eklemeleri (`bank_sens_l_method/applicability_status/not_applicable_reason/source_count`, `operational_tie_break_policy_id`, `methodology_contract_status`) ve 17-madde QC eki — D15-r7'ye alındı. (7) Kullanıcının dosya-etiket karışıklığını iç-kimlikten düzeltmesi (§0) — provenance disiplini örneği.
**Maddi kusurlar.** (i) **Altıncı tur üst üste öz-#1 (9.6)** — bu kez kendi v9'una dört-maddelik gerçek bir kusur listesi yazması ilerleme; ama altı turluk örüntünün kendisine dair meta-not hâlâ yok. (ii) Puan tablosu üçüncü kez alt-puansız. (iii) V-9/T-2 düzeltmesinden habersiz (paralellik — kusur değil, kayıt notu: v11 defteri taşır).

### 2.2 Claude v10-r2 — 8.9 (2., öz-değerlendirme)

**Güçlü.** V-9 (chatgpt hattının tek doğrulanmış olgusal hatasının tespiti), kimi v8-r2'nin birincil-kaynak retro-hakemliği, P-defterinin tamamlanması (P-1/P-4/P-6 kapalı), V-8 venue-çatışması tespiti, üç-hat yakınsama dokümantasyonu, yanlışlanabilirlik/Ç-serisi makinesi.
**Kusurlar (öz-eleştiri).** (i) **Venue-kalıntısı (Ç-5, minör):** C14'ü hükme bağlarken açık-kalem 10'daki eski ifadeyi temizlemedim; kalıntı iki revizyon boyunca yaşadı — hüküm-sonrası tam-metin tutarlılık taraması zorunlu pratik olmalıydı (v11'de yapıldı). (ii) Tie-break aday-listemin bağlayıcılık statüsü belirsizdi (D17-r5 netleştirdi). (iii) Dört turda dört dış-yakalayış: hüküm katmanım sağlam ama metin-bakım katmanım dış denetime bağımlı kaldı — terminal belgede bu, imza-öncesi son-okuma zorunluluğu olarak F12'ye işlendi.

---

## 3. Çatışmalar ve v11 hükümleri — TERMİNAL KAPANIŞ

**Envanter beyanı:** C1–C19'un TÜMÜ kapalıdır; kayıtlı muhalefet sıfır; iki hat arasında canlı çatışma sıfır (V-12). Bağlayıcı beş hükümde yön değişimi: **0 (beşinci ardışık tur).** Bu turun hükümleri yalnız nihai-form birleştirmeleridir:

| # | Kalem | **v11 nihai hükmü** |
|---|---|---|
| **C15-r3 (NİHAİ)** | BANK-SENS-L | chatgpt v10 §8.3 harfiyen + koruma: sınıf-zorunlu, winner-dışı, birincil-CI-değil; insidans-jaknayfı varsayılan-ilk-yöntem; **6-maddelik uygulanabilirlik-QC'si** F11'de değerlendirilir; QC-fail → `bank_sens_l_incidence_status="not_applicable"` + açık gerekçe + önceden-donmuş alternatif (kalibrasyon-aşaması kaynak-altküme/yeniden-kurulum jaknayfı; gruplu kaynak-silme; alternatif donmuş-banka duyarlılığı); sınıf imzasız/sessiz atlanamaz; `zero_new_runs ≠ statistical_applicability` (QC-normu). |
| **C16-r3 (NİHAİ)** | Friedman/donmuş-kalem tadilatı | 6-koşul birlikte: sonuç-öncesi · imzalı sapma kaydı · gerçekten yeni ve MADDİ bilimsel gerekçe · eklenen/çıkarılan formülasyon kesin belirtilmiş · çokluluk/raporlama sonuçları donuk · gözlenen pipeline-sıralamasından motivasyon yasak. Bütçe tek başına asla gerekçe değil. |
| **C17-r2 (KAPANDI)** | Mükerrer-artefakt | N-A-atıf-çözülene-kadar kuralı **oybirliği** (chatgpt v10 açık krediyle benimsedi); atıf sonrası kasıtlı-mükerrer teyit edilirse içerik-puanından ayrık **artefakt-yönetişim-puanı** raporlanabilir (dallanma kuralı kodifiye). |
| **D17-r5** | Operasyonel tie-break | Bağlayıcı olan İLKE: ayrı ön-kayıt, sonuç-kör, legacy-nötr, **dışsal deployment ölçütleri**; kesin ölçütler yalnız tek-pipeline gereksinimi gerçekten varsa F12'de pinlenir. Uygun-örnekler (bağlayıcı değil): çalışma-zamanı/kaynak tavanı, bellek, yazılım/lisans, tekrarlanabilirlik-gereği, ayrım kalmadıysa deterministik nötr kural. Benim eski aday-hiyerarşim açıkça **örnek-statüsüne** indirildi. Incumbent-süreklilik yalnız Öner'in ayrıca imzaladığı, "bilim-dışı paydaş-politikası" etiketli karar olabilir; bilimsel eşdeğerlik raporunu değiştiremez. |
| **Ç-5 (minör)** | Venue-kalıntısı | Açık-kalem 10 düzeltildi: "venue pini (F0)" ifadesi kaldırıldı → "venue = non-gating F0-admin metaverisi (C14); kayıt-netleştirmesi V-8'de". Dergi adı metodoloji sözleşmesine hard-code edilmez; Öner el-yazması-yönetimi için ayrıca kaydedebilir. |
| Defter | V-9 taşıması | chatgpt v9'un T-2 tanıklık-hatası düzeltmesi ve kimi v8-r2 birincil-kaynak bulguları (v10-r2 §0/§2.3) v11 defterinin parçasıdır; chatgpt v10 bunları görmedi (paralellik), çelişen hiçbir şey yazmadı. |

---

## 4. v11 — Konsolide tasarım (TERMİNAL)

Aşağıdaki bölümler bağlayıcı konsolidasyondur; D-soyağacı parantezlerde. Bağlayıcı beş hükümde yön değiştiren karar yoktur (beşinci ardışık tur). v10-r2 gövdesi taşınır; v11 farkları: **C15-r3** nihai form + 6-madde uygulanabilirlik-QC (§4.8), **C16-r3** 6-koşullu tadilat prosedürü (§4.9), **D17-r5** ilke/örnek ayrımı (§4.9), **Ç-5** venue-kalıntısı düzeltmesi (§4.14/10), **D15-r7** manifest eklemeleri (§4.12), QC 52–57 (§4.12), F12'ye imza-öncesi tam-metin son-okuma şartı (§4.11).

### 4.1 Birincil estimand (D1/D8-r6)

**Bilimsel soru:** Sonuç-kör SSA kalibrasyonuyla kısıtlanmış ve sonuç-öncesi dondurulmuş bir tasarım bankası üzerinde, hangi clustering algoritması × CVI boru hattı k_true ∈ {3,4,5,6,8}'i en yüksek tasarım-ağırlıklı exact-k geri-kazanımıyla bulur? ("Gizil SSA kümelerinin gerçek ampirik dağılımı altında" DENMEZ.)

**Nesneler.** Her cinsiyet s ve k için: (i) **Q_CD(k,s)** — kalibrasyonla-kısıtlanmış tasarım ölçüsü: bireysel-fit parametre bankası ampirik KISIT (whole-vector yeniden-örnekleme; marjinaller karıştırılmaz; zarf/kapsama), ortak k-prototip kurulum kuralı açık TASARIM (kompozisyon kısıtları, duplicate/near-duplicate reddi, distinctness eşiği, kapsama; kural tek ρ hesaplanmadan önce donar). (ii) **B\*(k,s) = {(b, w_b)}** — Q_CD'nin sonuç-öncesi üretilmiş, hash'lenmiş **sonlu** gerçekleşmesi; koşum başladıktan sonra genişletilmez. (iii) **H\*(s)** — ampirik temiz-gürültü bankası (σ̂ artık-quantile stratları; **φ_emp ölçüldüğü gibi — D10-r5:** .97'ye yuvarlama otomatik değil; yalnız F8'de sonuç-kör gerekçe pinlenirse birincil temsile girer, aksi hâlde winner-dışı karşılaştırılabilirlik duyarlılığı).

**Skor.** Hücre c = (s, k, senaryo b, gürültü senaryosu n); donmuş ağırlık ω_c = v_s·v_k·w_b·h_n, Σω_c=1; v_k=1/5, v_M=v_F=1/2; cinsiyet-özel sonuç zorunlu.
Â_m = Σ_c ω_c · (1/S_c) Σ_r I{k̂_mcr = k_c}.
**İddia cümlesi:** "performance across the frozen calibration-constrained application design" — gizil-popülasyon beklentisi iddiası kurulmaz. **Sınırlama cümlesi zorunlu ve makine-okunur** (`weight_semantics=design_weight`): banka marjinali veri-tanımlıdır; k'lık ortak dağılım tasarım kuralının eseridir; 39/57 seçilmiş örneklem bir zarfı destekler, bir dağılımı değil. Kabul-oranı/ret-nedeni raporu zorunlu; kabul çöküşü = kalibrasyon-blocker, sessiz yeniden-ağırlıklama yasak. E-WEIGHT: alternatif ağırlık şemaları winner-dışı; birincille ayrışma bulgudur.

### 4.2 k desteği (D13-r5)

{3,4,5,6,8}; v_k=1/5. k=5: `winner_privilege=false`; `empirical_mirror_anchor` etiketi F2 çapa denetimine koşullu (C5). Raporlama görünümleri: A_MACRO (birincil), A_k (k-başına, zorunlu), A_MIRROR5 (winner-dışı). k=5-tek-birincil kapanmıştır (manus v6 dahil). k̂±1 kısmi-kredi ikincil.

### 4.3 Morfoloji ailesi (D2)

Tek smooth **WC-ALC**; rejimler W-L / W-I(-early/mid/late) / W-R, gözlenen-pencere descriptor'larından atanır (robust monotonicity, interior/edge max, türev-işaret deseni, peak/boundary yılı, sol/sağ genişlik, asimetri, terminal eğim, dönüm-noktası sayısı, sansür derinliği, artık-imza); **label_fuzz** zorunlu rapor. **Sınıf kimliği (D2-r2):** gerçeklik-sınıfı = donmuş ayrık prototip parametre seti (hash'li üretici örneği); (shape_regime, konum-tanımlayıcıları) yalnız manifest descriptor'larıdır — eski projenin (shape, location) faktörizasyonu otomatik devralınmaz (C12). DTW/elastik yok. R-REV yalnız kapı geçerse; multi-wave exploratory; level_shift/cylinder/impulse/abrupt yalnız S-NEG; global saf lineer ayrı aile değil.

### 4.4 Üretici güvenlik duvarı (D3-r5)

Adaylar yalnız **WC-ADL** ve **TAD/PSAT**; spline yalnız yeterlilik-kıyası (`automatic_fallback=false`); PG/FPCA/serbest-spline yok. Leksikografik kapılar: morfoloji kapsaması → cross-fit öngörüsel yeniden-kurulum → sistematik artık morfolojisi → sansürlü-hal identifiability → parametre kararlılığı → parsimoni; pinli tie-break (sınır-rejimi identifiability → etkin parametre → residual ACF(1)). **Cross-fit yalnız seçim-denetimi içindir; form+kurallar donduktan sonra seçilen üretici TÜM uygun serilere yeniden fit edilir ve nihai banka bu refit'ten kurulur** (chatgpt v6 — bilgi kaybını azaltır, sızıntı yaratmaz, "internal calibration audit" statüsü korunur). Veri rolleri: fit_pool / audit_pool / frozen_bank / transfer_pool; fiziksel hold-out yoksa LOSO cross-fit; "bağımsız dış doğrulama" iddiası kurulmaz. Hiçbir kapıda clustering/CVI çıktısı kullanılamaz; çift başarısızlık = **STOP/redesign**.

### 4.5 Geometri (D8/D9)

ρ_max = max_{i<j} corr(P_i,P_j), **signed** Pearson; max|ρ| yasak (exploratory alanda ayrı tutulabilir). Tam geometri zorunlu: rho_max_pair, rho_mean, rho_min, theta_min, d_eff, Gram spektrumu, hardpair_code. `rho_target_factor=false`: ρ tanımlayıcı + örnekleme-stratası + GLMM'de sürekli kovaryattır. Quantile sınırları yalnız MC-verimlilik stratasıdır; çökme 3→2→1 donmuş toleransla. Eski ölü-bölge (~0.24) **historical_context_only** — hiçbir tasarım tetiği ona bağlanamaz (Ö6); STOP yalnız inşa/kapsama çöküşü için. Doğal alan kolay çıkarsa eşdeğerlik/tavan bulgusudur; eksen değişmez. coverage_gap yapay şekille doldurulmaz; z-norm ddof=0; d²=2T(1−ρ) beyaz-geometri smoke-testi.

### 4.6 Gürültü (D10-r5)

**Kazanan katmanı** = H\*(s): ampirik σ̂ quantile stratları (aday {25,50,75}, kalibrasyonda pinlenir) × {beyaz, AR(**φ_emp ölçüldüğü gibi**)}; **φ-snap (.97'ye yuvarlama) birincilden çıkarıldı (r5, C12):** yalnız etiketli winner-dışı "φ-karşılaştırılabilirlik duyarlılığı" olarak, veya F8'de açık sonuç-kör gerekçeyle; temiz çekirdek: ortak σ, eşit sınıf boyutu, morfoloji-özel σ yok, jitter/aykırı/dengesizlik/sinyal-ölçeği yok; geometri×gürültü birincilde çarpanlara ayrılır, kuplaj R-REALISTIC'te. **X-CANON** = yeni aile × kanonik σ 0.1–1.0 × {beyaz, AR(.97)} + legacy ρ-bandı stres hücreleri (`legacy_anchor`, `envelope_status`) — winner-dışı doz-yanıt/süreklilik; uygulama olasılığı atanmaz. AR-farkında g_ij / whitened pair-SNR manifest tanısıdır, verdict değildir; beyaz-tavan ön-analizi kalibrasyonda zorunlu. Kanonik-kazanan muhalefeti **kapanmıştır** (manus v7 öz-düzeltmesi; C4-kapanış, 2026-08-26) — katman ayrımı artık oybirliğidir.

### 4.7 Zor-çift (D7-r4)

A-APP: doğal zor-çift yalnız KAYDEDİLİR; counterbalance yok. A-MECH: ortak-destek/aynı-ρ eşleştirmeli HP-II / HP-IB-L / HP-IB-R / HP-LL / HP-RR; eşleşik-hücre QC üçlüsü (|ρ_intended−ρ_target|≤ε; argmax=hedef çift; hedef-dışı ≤ ρ_target−δ; ε,δ fizibilite-sonrası/sonuç-öncesi donar; sağlanmazsa `unexpected_nearest_pair`/reclassification/coverage_gap — sessiz düzeltme yok). W-L×W-R = **BB-OPP, yalnız tanısal**. A-MECH-NOISE alt-paneli: ampirik-temiz vs beyaz vs kanonik-AR mekanizma kıyası.

### 4.8 Belirsizlik (D14-r2; C2/C2′ hükümleri)

**Birincil:** donmuş tasarıma koşullu MC. Hücre-varyansı s²_mc ile Var̂_MC(Â_m)=Σ_c ω_c² s²_mc/S_c; boru-hattı kıyasları **CRN-eşleşik fark** D=Y_m−Y_n üzerinden Var̂_MC(Â_m−Â_n)=Σ_c ω_c² s²_{D,c}/S_c. Tohumlar MC gerçekleşmeleridir; tohum-düzeyi hipotez testi yasak; bu SE hedef-popülasyon örnekleme hatası değildir ve öyle sunulmaz.
**Zorunlu, etiketli, winner-dışı sağlamlık bileşenleri:** (a) **BANK-SENS-S** — senaryo-seçim bileşeni: senaryo-ID küme bootstrap'ı (CRN/pairing/strata korunarak) + δ-yöntemi kapalı-form sağlaması; (b) **BANK-SENS-L** — kaynak-etki sınıfı (**C15-r3, NİHAİ**): sınıf zorunlu ve winner-dışı. **Varsayılan-ilk-yöntem = `scenario_source_ids` insidans-jaknayfı** (avantaj: sıfır yeni algoritma×CVI koşumu), ANCAK yalnız **6-maddelik uygulanabilirlik-QC'si** F11'de geçerse: (1) kaynak-ID'ler eksiksiz ve deterministik; (2) her kaynak-silme, gerekli (cinsiyet,k) stratlarında yorumlanabilir boş-olmayan destek bırakıyor; (3) yeniden-normalize ağırlıklar sonlu ve iyi-tanımlı; (4) silme, estimand desteğini yorumu imkânsızlaştıracak biçimde mekanik bozmuyor; (5) hiçbir gerekli stratada yapısal-evrensel kaynak-insidansı yok; (6) silme-sonrası senaryo bağımlılık/çoğaltım yapısı belgelendi. QC-fail → `bank_sens_l_incidence_status="not_applicable"` + açık gerekçe + **önceden-donmuş alternatif** (kalibrasyon-aşaması kaynak-altküme/yeniden-kurulum jaknayfı; gruplu kaynak-silme; alternatif donmuş-banka duyarlılığı). Sınıf hiçbir koşulda imzasız/sessiz atlanamaz. Norm: `zero_new_runs ≠ statistical_applicability`. Rapor şablonuna zorunlu cümle: **"Bu bileşenler birincil güven aralığı DEĞİLDİR ve kazananı değiştiremez."** İkisi raporlanmadan ağırlıklı sonuç "belirsizliğiyle raporlanmış" sayılmaz; ancak birincil CI değildirler ve kazananı değiştiremezler. CAL-SENS (M↔F destek denetimi) ikincil; ciddi kapsama başarısızlığı yalnız transfer iddiasını daraltır.

### 4.9 Eşdeğerlik / kazanan (D17-r5; C3/C13/C15-r3/C16-r3/C18 hükümleri)

δ_eq: **havuzlanmış tasarım-ağırlıklı estimand üzerinde**, bilimsel/pratik anlamla, sonuç-öncesi donuk; aday 0.05 (yalnız aday). **Yön: δ_eq → hassasiyet hedefi → tahsis → bütçe; asla tersi.** Zorunlu **hassasiyet ön-uçuşu** (F11): δ_eq→gerekli tohum/senaryo geriye-hesabı + eşleşik yarı-genişlik hedefi ("materially smaller than δ_eq" oranı sonuç görülmeden sayısallaştırılır); **n=100 hakkında kategorik yeterli/yetersiz hükmü ön-uçuş öncesi İKİ YÖNDE DE verilemez** — tek-hücre binom kısayolu yerine analitik en-kötü-durum sınırları + donmuş yapı altında sonuç-kör simülasyon (C12 eki, chatgpt v7). Bütçe yetmezse: ikincil daralt (**D22-r3 pinli sıra:** S-NEG → R-REALISTIC alt-kolları → X-CANON yoğunluğu → E-MATCHED/E-ACTUAL → A-MECH; A-APP winner-katmanı, tohum tabanı ve transfer-qualification asgari paneli dokunulmaz — D22-r2'nin fugu v6 E.12 ile blok-tam hali) → tahsis optimize et → "precision insufficient". δ_eq büyütme bu zincirin hiçbir halkası değildir. Kazanan yalnız A-APP'ten; sonuç tekil kazanan / exact-tie co-winner / üst-eşdeğerlik kümesi olabilir; kazanan zorlanmaz; strata-başına zorluk-yanıt eğrileri eş-vurgulu birincil şekildir. Tek-deployment gerekirse **operasyonel tie-break ayrı ön-kayıttır (D17-r5, NİHAİ):** bağlayıcı olan İLKEdir — sonuç-kör, legacy-nötr, **dışsal deployment ölçütleri**; kesin ölçütler yalnız tek-pipeline gereksinimi gerçekten varsa F12'de pinlenir. Uygun-örnekler (bağlayıcı DEĞİL): çalışma-zamanı/kaynak tavanı, bellek kısıtı, yazılım/lisans kısıtı, tekrarlanabilirlik-gereği; hiçbir ayrım kalmadıysa deterministik nötr kural (ör. ön-kayıtlı sıra/seed'li çekiliş). **Incumbent'a (Ward+CH) salt incumbent olduğu için otomatik öncelik YOK** — süreklilik tercihi ancak Öner'in ayrıca imzaladığı, "bilim-dışı paydaş-politikası" etiketli karar olabilir ve bilimsel eşdeğerlik kümesini "unique winner" diye yeniden adlandıramaz. Transfer-qualification üç-değerli deployment kapısı — **hesap-tabanı pinli (C9): R-REALISTIC koşulları + E-ACTUAL/E-MATCHED köprü panelleri**; ayrı transfer BLOĞU ancak `distinct_transfer_source=true` ise (C9-r2; mevcut projede yok); kazananı değiştiremez. Friedman/Nemenyi ikincil (C6); **donmuş kalemlerin tadilatı (4-formülasyon seti dahil) yalnız 6-koşul BİRLİKTE sağlanırsa (C16-r3, NİHAİ): sonuç-öncesi · imzalı sapma kaydı · gerçekten yeni ve MADDİ bilimsel gerekçe · eklenen/çıkarılan formülasyon kesin belirtilmiş · çokluluk/raporlama sonuçları donuk · gözlenen pipeline-sıralamasından motivasyon yasak; bütçe tek başına hiçbir zaman gerekçe değildir**; GLMM ikincil mekanizma modeli (yeni proje kendi param/sürüm/hash'ini pinler; kod yeniden-kullanımı ≠ normatif yeniden-kullanım; S-02'nin eski-proje spesifikasyonu otomatik taşınmaz). **Runner-up KOŞULSUZ raporlanır (C18):** skor, eşleşik fark, MCSE/eşleşik CI, k-bazlı performans, kritik başarısızlık stratları, uygulanabilirse SSA-deployment k̂.

### 4.10 Bloklar (D6-r4)

**r4 eki (C19, chatgpt v9):** her YENİ DGP bloğu önerisi şu soruyu yazılı yanıtlamak zorundadır: *"Hangi bilimsel soru mevcut blok veya duyarlılık paneliyle yanıtlanamaz?"* — yanıtsız öneri gündeme alınmaz.

| Blok | İçerik | Winner? |
|---|---|---:|
| **A-APP** | B\*×H\*, tüm k, M/F, temiz çekirdek (görünümler: A_MACRO, A_k, A_MIRROR5) | **EVET** |
| A-MECH (+A-MECH-NOISE alt-paneli) | eşleştirmeli zor-çift mekanizması; gürültü-mekanizma kıyası | Hayır |
| E-ACTUAL / E-MATCHED | yarı-sentetik köprü / ortak-destek eşleştirme (bağımsız-doğrulama iddiası yok) | Hayır |
| X-CANON | kanonik σ/ρ/AR stresi + legacy_anchor; envelope_status | Hayır |
| X-LEGACY-HIST | eski donmuş sonuçlar; yeniden koşum yok | Hayır |
| R-REALISTIC (+TRANSFER-QUAL) | jitter, hetero-σ, dengesizlik, aykırı, sinyal-ölçeği, kuplaj; üç-değerli deployment kapısı (hesap-tabanı: bu blok + E-panelleri; C9) | Hayır |
| S-NEG | level_shift/cylinder/impulse/abrupt negatif kontrol | Hayır |
| R-REV | yalnız kapı geçerse | Hayır |
| H0-XREF | mevcut saf-gürültü null'una çapraz-referans; yeni k=1 hücresi yok | Hayır |
| *Analiz panelleri (hücre değil):* BANK-SENS-S/L, E-WEIGHT, CAL-SENS | §4.8 | Hayır |

Parsimoni denetimi: her yeni blok önerisi F0'dan "hangi soruya cevap veriyor?" cümlesi ister.

### 4.11 Freeze dizisi (D20-r3)

**r3 eki (manus v7):** donma belgesinde her F-kapısı, açık bir **başarısızlık-davranışı** sütunu taşır (ör. F3 çift-fail → STOP/redesign; F5 ağırlık/kaynak belirsiz → STOP/revise; F6 sağlanamazsa geometri donmaz; F12 öncesi okuma → provenance-ihlali, doğrulayıcı zincire alınmaz). Aşağıdaki davranışlar bu sütunun içeriğidir.

**F0** kimlik/kapsam: soru, eski/yeni ayrımı, tüm-k, cinsiyet hedefleri + gerekçe paragrafı + ayrışma-halinde-deployment politikası, winner=A-APP, legacy dokunulmazlığı, **v5.3 Friedman-satırı hash-alıntısı + brif-kayıt çatışması iletimi**, D24-r8 onaması. *(Venue — kayıt: EPJ-DS birincil — F0 donma-içeriğinden çıkarıldı; **F0-admin eki, non-gating** — C14; QC: venue hedefi DGP/estimandı sonradan değiştiremez.)* **F1** girdiler: ham hash'ler, uygunluk, zaman ekseni, ön-işleme, z-norm. **F2** üretici tanımları (exact denklemler, sınırlar, başlatma, fit-hata politikası) + çapa denetimi (k=5 etiketi hükmü). **F3** cross-fit yeterlilik denetimi + STOP kuralı + pinli tie-break. **F4** nihai parametre bankası (tam-veri refit), rejim/descriptor/label-fuzz, cinsiyet-özel bankalar. **F5** Q_CD ortak-kurulum yasası: kompozisyon, distinctness, kabul/ret, ağırlık semantiği; **eşit sınıf boyutu (n_per) yeni-proje kararı olarak açıkça pinlenir — miras-devir değil (C12).** **F6** donmuş B\*: boyut, kaynak-ID'ler, design_weight'ler, hash, kapsama denetimi. **F7** geometri: tam işaretli geometri, strata/çökme, zor-çift dağılımı, X-CANON fizibilitesi. **F8** gürültü: H\* (σ̂ stratları, **φ_emp ölçüldüğü gibi; olası .97-yuvarlama ancak burada, açık sonuç-kör gerekçeyle — D10-r5**), kanonik tanımlar, beyaz-tavan ön-analizi. **F9** ikincil bloklar + revival kapısı. **F10** yöntem registry'si: 4 algoritma × 8 CVI registry, **ikincil sıra katmanı için 4 donmuş formülasyon**, aday k=2–10, hata/tie/non-finite, yazılım hash'leri. **F11** hassasiyet + manifest: senaryo/tohum tahsisi, CRN, **δ_eq + hedef-MC-hassasiyeti + ön-uçuş raporu**, maliyet, korumalı-birincil, eksik/çift yok. **F12** analiz freeze: ağırlıklar, skor, eşleşik MC varyansı, eşdeğerlik kuralı, operasyonel tie-break (D17-r5 ilkesiyle, yalnız-gerekiyorsa), BANK-SENS-S/L kesin prosedürleri + uygulanabilirlik-QC sonucu, ikincil Friedman/GLMM, çokluluk, raporlama dili; **imza öncesi zorunlu tam-metin tutarlılık son-okuması (Ç-5 dersi).** **F12 kapanmadan hiçbir algoritma×CVI sonucu okunmaz.** Koşum aşamalara bölünebilir; aşamalı OKUMA yasaktır; okunmuşsa gizlenmez, provenance statüsü açık yazılır ve doğrulayıcı zincire alınmaz.

### 4.12 Manifest / QC (D15-r7)

**Manifest çekirdeği** = chatgpt v6 D21 süperseti ∪ {winner_layer, label_fuzz, weight_semantics, mcse, calibration_sensitivity_role, question_id, claim_scope, residual_law_id, epsilon, delta, unexpected_nearest_pair, intended_pair} ∪ **scenario_source_ids (BANK-SENS-L için zorunlu)** ∪ **r6 ekleri (qwen v7'den, adlandırma düzeltilerek):** `frozen_v53_friedman_formulations=["sil_euc","DB","CH","Dunn_d1_D1"]` (F0 hash-alıntısının makine-okunur eşi; "families" değil "formulations" — kayıt dili) ve `latent_probability_claim=false` (weight_semantics'in zorunlu tamamlayıcı bayrağı; chatgpt v7'nin `latent_cluster_probability=false` alanı eşdeğerdir — tek ad bu). `C_NPER_STATUS` alanı yeni manifeste ALINMAZ (C10). **r7 eklemeleri (chatgpt v10 §18):** `bank_sens_l_method`, `bank_sens_l_applicability_status`, `bank_sens_l_not_applicable_reason`, `bank_sens_l_source_count`, `distinct_transfer_source_or_law`, `historical_tie_break_privilege=false`, `operational_tie_break_policy_id`, `operational_tie_break_scientific=false`, `methodology_contract_status`. Adlandırma: `run_matrix_pkonum_plus_v1.csv`; sürüm-eki türevleri RED; namespace sürüm-eksiz `p_konum_plus` (sürüm `design_version` alanındadır). Boş hücre yalnız NA/not-applicable (S-03 ilkesi yeni ad-uzayında da geçerli).
**QC** = chatgpt v6'nın 36 maddesi aynen + (37) iki sağlamlık bileşeni hesaplandı ve winner-dışı etiketli; (38) senaryo→seri insidans haritası eksiksiz; (39) hassasiyet ön-uçuş raporu F12'den önce mevcut; (40) panel-provenance defteri hash-doğrulamalı (V6-D10/a: dış-model sayısal iddiası ham kaynaktan teyitsiz "doğrulanmış" yazılamaz); (41) "4/4 konsensüs" dili hiçbir belgede yok (korele panel ≠ bağımsız kanıt). Yönetişim aynen: ayrı ad-uzayı, legacy read-only, ekleyici kod, yeni seed ad-uzayı (D19), frozen-regression bit-özdeşlik = GLOBAL STOP, environment provenance, harici .sha256, self-hash yok.

### 4.13 Reddedilenler (kümülatif liste + bu turun eklemeleri)

chatgpt v6 §27'nin 29 maddesi ve claude v6 §2'nin 32–37'si aynen geçerlidir (özetle: eski projeyi yeniden yazmak; Ward+CH'yi peşinen taşımak; max|ρ|; yarışmacı ground-truth; level_shift/… birincil; prevalence=latent-prevalence; Q_CD'yi gerçek gizil yasa diye sunmak; keyfî eşit-quantile birincil; band-fallback; 0.24 evrensel tetik; k=5-tek; kanonik gürültüye uygulama olasılığı; A-APP'te zorunlu zor-çift dengesi; otomatik spline; ek üretici; yeni k=1 hücresi; tohum-düzeyi test; senaryo-bootstrap'ı popülasyon-çıkarımı gibi sunmak; Friedman-5; Friedman'ı winner istatistiği yapmak; whitened-SNR verdict; yapay filler; aşamalı okuma; aynı turda registry genişletme; DTW; Gap/t5 açma; blok çoğalması; "empirical probability law" koşullu dili). **Bu turun eklemeleri:**
38. "Bütçe yetmezse δ_eq büyütülür" [kimi v5/v6; **fugu v6 E.8 — ikinci taşıyıcı**] — RED (C3; tersine nedensellik).
39. Senaryo-seçim bileşenini **birincil** güven mekanizması / SE-geçerlilik koşulu yapmak [kimi v6; chatgpt v5 kalıntısı; **fugu v6 E.8**] — RED; BANK-SENS-S'e iner (C2; fugu'nunki beklenti-formunun sonucu, C1 ile çözülür).
40. Kanonik-gürültülü doğrulayıcı kazanan [manus v6, ikinci nüks] — RED; muhalefet **manus v7'nin öz-düzeltmesiyle kapandı** (C4-kapanış, 2026-08-26).
41. Tam-LOSO banka yeniden-koşumu birincil sağlamlık olarak [kimi v6'nın harfi] — fizibil değil; insidans-jaknayfı + kalibrasyon-jaknayfı ikamesi (C2′).
42. Yeni numaralı tur paketine kapak-notsuz bit-özdeş eski artefakt girmesi — süreç reddi, **aktör-bağımsız** (P-1-r2: bu turda kaynak PI-paketleme eksiğiydi, panelist kusuru değil; kural aynen korunur). **P-3 ile ikinci kez uygulandı** (mükerrer-ad varyantı).
43. Ayırt-ediciliksiz puan sıkışması (≥9.1 bandı) [manus v6] — süreç normu ihlali; puanlar mutlak-ölçek/ceza-odaklı kalır. **İkinci vaka: qwen v7 (9.1–9.6).**
44. `A_TRANSFER`'ı A-APP ile içerik-örtüşük ayrı DGP bloğu yapmak [manus v7] — RED; transfer-qualification KAPI olarak korunur ve hesap-tabanı pinlenir (C9).
45. Eski-çalışma `C_NPER_STATUS` alanını yeni manifeste taşımak / donmuş matrisin row-level pinini yok saymak [manus v7] — kapsam ihlali + kaynak-denetimi eksiği (C10, V-3); taşınabilir ilke ("satır-düzeyi alan = meşru pin; sessiz kanonikleştirme yasak") korunur.
46. Sürüm-ekli namespace (`p_konum_plus_v7`) [manus v7] — namespace proje-düzeyidir; sürüm `design_version` alanının işidir.
47. Kaynak-doğrulamasız mekanizma-atfıyla sıralama beslemek [qwen v7 — V-1/V-2] — QC-40'ın panel-içi ihlali; attribution-correction defter satırı zorunlu (C11).
48. φ_emp'i keyfî toleransla otomatik .97'ye yuvarlamak (kazanan katmanında) [claude v6/v7-r2 soyağacı; fugu v6 taşıdı; chatgpt v7 yakaladı] — RED; D10-r5 + **Ç-serisi öz-düzeltme** (C12).
49. Eski (shape, location) sınıf-kimliğini yeni projeye yeniden-gerekçelendirmeden otomatik taşımak [claude soyağacı; chatgpt v7 yakaladı] — RED; D2-r2 + **Ç-serisi öz-düzeltme** (C12).
50. n=100 hakkında ön-uçuşsuz kategorik yeterlilik/yetersizlik ilanı (iki yönde de) [kimi v5 "yetersizdir" genellemesi; chatgpt v7 simetrik kapanış] — RED (C12/C3).
51. Bilimsel eşdeğerlik kümesi içinde incumbent'a (Ward+CH) salt incumbent olduğu için otomatik operasyonel tie-break önceliği [claude v7-r2/v8-r2 soyağacı; chatgpt v8 yakaladı] — RED; D17-r4 + **Ç-3 öz-düzeltme** (C13).
52. Yayın-hedefini (venue) DGP/estimand donma-koşulu yapmak [claude F0; chatgpt v8] — RED; F0-admin eki, non-gating (C14).
53. ~~Sıfır-koşumlu insidans-jaknayfını "fizibilite belirsiz" gerekçesiyle zorunlu-rapordan düşürmek~~ — **GERİ ÇEKİLDİ (Ç-4, C15-r2):** itirazın çelik-adam formu (yorumlanabilirlik/dejeneresans) haklı çıktı; sınıf-zorunlu/implementasyon-ön-uçuşta kuralı geçerli. ~~Friedman tadilat-kapısını tümden mühürlemek~~ — **ÇÖZÜLDÜ (C16-r2):** chatgpt v9 kendi hattında kapıyı maddi-gerekçe eşiğiyle açık tuttu; birleşik kural yürürlükte.
54. Bütçeyi — sonuç-öncesi ve imzalı bile olsa — **tek başına** eşdeğerlik-marjı/donmuş-kalem tadilat gerekçesi saymak [kimi v8-r2 §2/1 + red #21 — birincil kaynak doğrulandı; C16-r2] — RED.
55. Zorunlu duyarlılık sınıfını (BANK-SENS-S/L) imzasız/sessiz atlamak — RED (C15-r3 koruması).
56. "Sıfır yeni koşum ⇒ istatistiksel uygulanabilirlik garantili" çıkarımı [claude v9/v10-r2 soyağacı; chatgpt v10 §5.1 — Ç-4 ile taviz verilmişti, şimdi QC-normu] — RED (C15-r3).
57. İnsidans-jaknayfını destek-yapısından bağımsız TEK izinli yöntem yapmak [simetrik yasak; chatgpt v10 §20/2] — RED; QC-fail'de donmuş alternatif zorunlu.

**QC eklemeleri (chatgpt v8'den, D15-r6'ya):** (42) panel/kaynak provenance defteri hash-eksiksiz; (43) bit-özdeş panel artefaktları bağımsız kanıt sayılmaz; (44) venue hedefi DGP/estimandı post-hoc değiştiremez; (45) incumbent'a otomatik bilimsel/operasyonel tie-break ayrıcalığı yok; (46) ayrı transfer bloğu yalnız `distinct_transfer_source=true` ise. **v10 eklemeleri (chatgpt v9'dan):** (47) runner-up raporlama alanları mevcut; (48) BANK-SENS-S/L implementasyonu sonuç-öncesi gerekçeli-pinli; (49) zorunlu duyarlılık sınıfı imzasız atlanmamış; (50) yeniden-açılış tetiği kullanıldıysa kanıt-sınıfıyla loglanmış; **(51)** panel raporlarında "N/N konsensüs" dili yok. **v11 eklemeleri (chatgpt v10 §19):** (52) insidans-jaknayf uygulanabilirlik-QC'si analiz-freeze öncesi değerlendirilmiş; (53) uygulanamazsa açık alternatif donmuş; (54) `zero_new_runs` tek başına istatistiksel-geçerlilik gerekçesi değil; (55) kaynak-silme sonrası yeniden-ağırlıklama donmuş kurala uygun; (56) tie-break politikası legacy-nötr veya "bilim-dışı paydaş-politikası" etiketli; (57) imza-öncesi tam-metin son-okuma tamamlanmış.

### 4.14 Kalan açık kalemler (tümü ölçüm veya kayıt-bakısı; karar yok)

1. WC-ADL vs TAD koşusu + yeterlilik eşikleri + pinli tie-break (F2/F3; cross-fit + tam-veri refit).
2. Descriptor eşikleri + label-fuzz; cinsiyet F0 gerekçe paragrafı ve havuzlama uygulaması.
3. Yeniden-örnekleme/kompozisyon kuralı metni → Q_CD → B\* + kabul-oranları + strata sınırları/çökme + design_weight seti + E-WEIGHT şemaları (F4–F6).
4. H\* inşası: σ̂ quantile pinleri + **φ_emp temsili (ölçüldüğü gibi; olası .97-yuvarlama gerekçesi yalnız F8'de, sonuç-kör — D10-r5)** + ar_stress eşiği + beyaz-tavan ön-analizi (F8).
5. Üç-rejim Δμ↔ρ tabloları (görevleri: seyrek-strata doldurma/fizibilite, A-MECH eşleştirme, X-CANON inşası) + ε, δ (F3/F5/F7).
6. A-MECH eşleştirme haritası; X-CANON kapsamı (azaltılmış faktöriyel alt-küme); S kapsamı; R negatif-kuplaj ve CAL-SENS dahil/hariç.
7. Revival kapısı (G8); k=6/8 varyant bankası; Δ taşma politikası.
8. δ_eq gerekçesi + geriye-hesap ön-uçuşu + tohum/senaryo bütçesi + hedef-MC-hassasiyeti (F11).
9. **BANK-SENS-L spesifikasyonu:** insidans-jaknayfı uygulama notu + kalibrasyon-aşaması banka-kararlılık jaknayfı planı (yeni; C2′).
10. v5.3 Friedman-satırı hash-alıntısı + brif-kayıt çatışmasının Öner'e iletimi; **venue = non-gating F0-admin metaverisi (C14; Ç-5 — eski "venue pini (F0)" ifadesi kaldırıldı; kayıt-netleştirmesi V-8'de).**
11. D18 ikinci-deployment kararı; F2 çapa denetimi → k=5 etiketi hükmü.
12. ~~P-1~~ ~~P-4~~ ~~P-6~~ **ÜÇÜ DE KAPANDI** (tümü PI-teyitli paketleme eksiği). Kalan: manus-v5 kimi-okuma kalemi (kimi v4 temin edilirse) + **P-3 teyidi** (kimi v7 statüsü — P-1/P-4/P-6 örüntüsüyle (b) fiilen baskın; resmî teyit açık) + **YENİ (V-8): venue kayıt-netleştirmesi** — yol-haritası "EPJ-DS birincil" der, kimi v8-r2 "PI beyanı JoC" der; tek-satırlık PI kararı yeter (C14 gereği non-gating; tasarımı etkilemez).
13. D24-r8 imzası → `p_konum_plus_decision_freeze_v0`.
14. C_NPER tarihsel defter notunun işlenmesi (düzyazı-belgeleme boşluğu kaydı; donmuş kayda dokunulmaz) + manus [12] kaynağının (`12_C_NPER_v4_taslak_denetcim_raporu.md`) temini halinde "doğrulanamadı" statüsünün kapatılması; C11 attribution-correction notunun dış panele iletimi (opsiyonel, tasarımı etkilemez).

---

## 5. Yönetişim ve kapanış (D24-r8 — TERMİNAL)

**Nihai kayıt.** İlan üç kez başarısız oldu; **imza-kuralı yedi olayda doğru çalıştı**; **yanlışlanabilirlik şerhi dört kez tetiklendi, dört kez uygulandı** (Ç-2a/2b miras-kuralları; Ç-3 tie-break; Ç-4 hakemlik-revizyonu; Ç-5 metin-kalıntısı). Süreç dersleri terminal biçimde: kapanışı imza gerçekleştirir; öz-puan ayrıcalık değildir; miras-devirler ve metin-kalıntıları ancak açık denetimle ölür; tanıklık-zinciri hem doğrular hem çürütür.

**TERMİNAL BEYAN.** PI direktifi ("son tur") + beş ardışık sıfır-yön-değişimi turu + C1–C19'un tamamının kapanması + kayıtlı-muhalefet-sıfır + iki v10'un fiilî özdeşliği (V-12) birlikte: **panel süreci bilgi-üretim kapasitesini tüketmiştir.** v11, imzanın nesnesi olan terminal donma-adayıdır. Bundan sonra hiçbir dış-model çıktısı — puan, yeniden-ifade, tercih — numaralı tur açamaz; yalnız üç tetik açabilir: (1) kalibrasyon ölçümünün donmuş bir tasarım varsayımını maddi biçimde yanlışlaması; (2) kayıt/provenance denetiminde maddi çelişki; (3) gerçekten yeni, daha önce hiç yazılmamış itiraz sınıfı. Tetik kullanımı kanıt-sınıfıyla loglanır (QC-50).

**v11 + Öner imzası = `p_konum_plus_decision_freeze_v0`** (harici .sha256; imza öncesi F12 tam-metin son-okuması — Ç-5 dersi). İmza ile birlikte kalan idari kalemler: **P-3 resmî teyidi** (P-1/P-4/P-6 örüntüsüyle (b) fiilen baskın; teyit yalnız defteri kapatır, tasarımı etkilemez) ve **V-8 venue tek-satırı** (EPJ-DS mi JoC mu — non-gating, el-yazması-yönetimi kaydı).

**Sonraki belge:** `yeni_proje_empirik_kalibrasyon_protokolu_v0.md` (kayıtlı ad; iki hat da aynı adı önerir) — yalnız ölçüm üretir: girdi/hash doğrulama; cross-fit fit'ler + yeterlilik kapıları + üretici seçimi + tam-veri refit; descriptor/label-fuzz; parametre bankası; Q_CD kuralı → B\* + kabul-oranları + strata + design_weight/E-WEIGHT; H\* (σ̂, φ_emp ölçüldüğü gibi) + beyaz-tavan ön-analizi; Δμ↔ρ tabloları; G-ρ denetimi + envelope_status; fizibilite + bütçe + δ_eq ön-uçuşu; **BANK-SENS-S/L kesin prosedür seçimi + insidans uygulanabilirlik-QC'si (C15-r3)**; D17-r5 kapsamında yalnız-gerekiyorsa tie-break ölçüt-ölçümü; QC-değişmez eki; v5.3 Friedman-satırı hash-alıntısı. **Hiçbir algoritma × CVI sonucu üretmez veya okumaz.**

---

*Bu belge iki v10'un (chatgpt v10, claude v10-r2 öz-değ.) değerlendirmesi ve TERMİNAL v11 sentezidir. C1–C19 tamamı kapalı; kayıtlı muhalefet sıfır; sayısal değerler kalibrasyon ölçümüne kadar bağlayıcı değildir. Statü: TERMİNAL DONMA-ADAYI — D24-r8 imzası (→ `p_konum_plus_decision_freeze_v0`) + P-3 teyidi + V-8 tek-satırı Öner'dedir.*
