# F3 real-data preparation RP1 — Independent audit

```text
record = f3_realdata_prep_rp1_independent_audit_gpt_codex_DRAFT_r1_2026-10-05.md
auditor = GPT (Codex)
auditor_id = gpt_codex
session = this ChatGPT/Codex audit session; work begun 2026-10-04, record completed 2026-10-05 UTC
revision = DRAFT r1; new child record; no prior record rewritten
status = NON-NORMATIVE
no PI acceptance implied
repository = onertartan/tartan-names
branch = p_konum_plus
examined_commit = b6d2483d4bbd991167bb633d8d96647cc553bde2
comparison_base = fadf771c75396a0d242f75f0c3ce7f3f0f4ed7e7
verdict = NOT PASSED
open_global_blockers = 0 observed
open_gate_specific_blockers = 3
real_data_access_by_auditor = false
algorithm_x_CVI_computation_by_auditor = false
repository_write_or_commit_by_auditor = false
```

## 1. Kimlik, kapsam ve hüküm

Bu kayıt, PI'nin verdiği `F3_RP1_INDEPENDENT_AUDIT_INSTRUCTION_2026-10-04.md` uyarınca RP1 paketini denetler. İlk sohbet mesajındaki STEP-2 r2 denetiminin yerine yeni bir r2 hükmü üretmez. Geçerli kaynak RP1 talimatı, D-9 ve D-10'dur; D-11 r1 RP1'e uygulanmadı. Frozen upstream yeniden açılmadı; bilimsel literal, 6B içeriği veya gerçek veriye ilişkin sonuç üretilmedi.

**Önceki maruziyet:** Bu konuşmada projenin önceki audit/dispatch süreçleri ve talimatları tartışılmıştır. Bu nedenle bu çalışma kör denetim değildir. Auditor RP1 executor'ı değildir; bu incelemede başka bir auditor'ın RP1 hükmü kullanılmadı. Önceki A-1…A-5 kayıtları yalnız istenen standing input/baseline rolleriyle ele alındı. Modelin erişilebilir kimliği GPT/Codex'tir; ayrıca doğrulanmamış bir model sürümü veya sağlayıcı varyantı ileri sürülmez.

**Hüküm: NOT PASSED.** Teslim edilen baytlarda üç teknik kapanış eksiktir:

1. F1 loader'ın ürettiği senaryo gerçek hesaplama tüketicisine bağlanmamıştır; context kimliklerinin testi de tüketicide kullanılan kimlikleri doğrulamamaktadır.
2. Zorunlu F1 QC testi, açıkça istenen non-finite durumları ve bazı diğer hata dallarını sınamamaktadır; payda kontrolünün PASS alanı gözlenen sonuçtan türetilmemektedir.
3. Non-regression kapısı yalnız results JSON üzerinde çalışmaktadır; talimatın istediği telemetry ve test-evidence alan karşılaştırmaları kapının içinde yoktur.

Bunlar RP1 hazırlık/bağlama kapısına özgüdür. **Teslim edilmiş bilimsel sonuçlarda r4-2'ye göre bir S farkı saptanmadı [A].** Custody uyuşmazlığı saptanmadı [A]. Bu iki olumlu sonuç, eksik hazırlık kodunu veya eksik kapı testini kapatmaz. Yeni bir bilimsel tercih önermiyorum; üç madde teknik düzeltme yetkisi **X** içindedir. PI adına bağlama veya qualification kararı verilmez.

### Kanıt ve checklist dili

- **[A]** Teslim edilen dosya baytlarında auditor tarafından hesaplanan hash, statik inceleme veya bağımsız dosya karşılaştırması.
- **[A-S]** Auditor ortamında çalıştırılan sentetik/keşif kontrolü. Executor'ın Windows koşusunun bağımsız yeniden üretimi değildir.
- **[X]** Executor'ın tarihsel koşu/proses iddiası; teslim kaydı okunmuş olsa da olay bağımsız gözlenmemiştir.
- **PASS / FAIL / PENDING / NOT PERFORMED**, belirtilen dar kontrolün durumudur. Örneğin test kaydında PASS yazdığının doğrulanması, testin bağımsız koşulduğu anlamına gelmez.

## 2. Custody ve girdi provenance'ı

[A] Kaynaklar yukarıdaki sabit commit'ten alınmış, indirilen içeriklerin Git blob SHA1 değerleri doğrulanmış, ardından dosya SHA256 değerleri yeniden hesaplanmıştır. Eklerde hesaplama betikleri, gerçek çıktılar, beklenen/hesaplanan/sidecar eşleştirmeleri ve tam girdi hash listesi bulunur. Git blob SHA1 ile dosya SHA256 birbirinin yerine kullanılmamıştır.

| Kontrol | Executor claim | Independent verification | Durum / tier |
|---|---|---|---|
| Transmission paketi | Dosyalar ve sidecar'lar eşit | 44 kontrol: listelenen dosyalar ve transmission kaydının kendi sidecar kontrolü; uyuşmazlık yok | PASS [A] |
| Standing pins | Sabit kaynaklar aynı | Harness'tan çıkarılan 26 path/hash pini baytlardan eşleşti | PASS [A] |
| Start-state inventory | 123 kayıt eşit | 123/123 dosya mevcut ve hesaplanan hash envanter değerine eşit | PASS [A] |
| Parent immutability | Önceki paketler değişmedi | Base tree'deki 1.389 blob için silme/değiştirme yok; 990 ek blobun tamamı `p_konum_plus/` altında | PASS [A] |
| Final harness ↔ attempt-5 custody | Aynı kod çalıştı | Final dosya hash'i custody'deki hash'e eşit; tarihsel çalıştırma bağlantısı log iddiasıyla sınırlı | Bayt eşitliği PASS [A]; fiili geçmiş koşu [X] |
| W-3'ün launch-5'ten önce oluşması | Preexecution; kaydedilen mtime/start sırası uygun | Hash ve metin tutarlı; custody içinde bağımsız doğrulanabilir kesin creation timestamp yok | PENDING [X] |
| Store payload'ları | 12.453 birim, pid 33100 | Manifest/read-log incelendi; fiziksel store repo içinde değil | Metadata PASS [A]; payload doğrulaması NOT PERFORMED |

Dört eski standing dosyasının indirilen setinde sidecar yoktur: F2 harness r3, spline harness r2, F1 freeze record ve F1 input hash table. Bunların beklenen SHA256 değerleri mevcut ve bayt eşleşmeleri PASS'tir. Bunlara **sidecar PASS verilmedi**. RP1 transmission'daki zorunlu sidecar'ların eksikliğiyle karıştırılmamalıdır; eski kayıt sidecar'ları bir sonraki mevcut düzeltmeye eklenebilir (RP1A-06, cleanup).

Önemli hesaplanmış hash'ler:

| Girdi | Hesaplanan SHA256 [A] |
|---|---|
| Audit instruction | `1f411fb2de44493971a6c4a425a71a5fb14441e3f567b8e087e015c4f37f738a` |
| RP1 instruction | `a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5` |
| D-9 | `1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3` |
| D-10 | `4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34` |
| RP1 harness | `39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09` |
| r4-2 harness | `b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730` |
| RP1 results | `ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882` |
| F2 engine | `01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077` |
| Spline engine | `b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d` |

F1 hash tablosunda sadece `sha256` içerik sütunu karşılaştırma amacıyla kullanıldı. Oradaki raw dosya yolları izlenmedi; raw dosyalar ve eligible trajectory manifest açılmadı. Tablonun kendi custody hash'i opak dosya baytlarından hesaplandı. Hash eşitsizliği tek başına içerik benzemediğini kanıtlamaz: sentetik üretici de incelendi ve 875 sentetik dosyanın yeniden üretilen baytlarla eşitliği görüldü [A/A-S]. Gerçek isim/yörünge içeriğine karşı benzerlik analizi yapılmadı.

## 3. Kod ve contract incelemesi

Aşağıda `H` = `calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py`; yollar sabit commit'teki `p_konum_plus/` köküne göredir. Satır numaraları bu final dosyaya aittir.

### 3.1 r4-2 → RP1 diff kapsamı

[A] 23 unified diff hunk'ı bulundu. Tam diff ekte tutuldu. Bazı hunk'lar birden fazla C maddesinin bitişik eklerini içerir; bunları gerçekte tek maddeymiş gibi etiketlemedim. Ayrıca RP1 §1/§5/§8/§9'un açıkça istediği dispatch, dosya adı ve non-regression ekleri yalnız C-1…C-6 etiketlerine sığmaz. Audit instruction §2.2'nin “her hunk tam bir C” biçimsel şartı bu noktalarda sağlanmaz (RP1A-06); buna rağmen yönetici talimatta açıkça yetkilendirilmiş ekleri izinsiz bilimsel değişiklik saymadım.

| Hunk | RP1 başlangıç satırı | Yetki/kapsam eşleştirmesi [A] |
|---|---:|---|
| 1 | 126 | C-6: attempt/restart provenance ve launch adları |
| 2 | 226 | C-1 read accounting; C-2 scope/key kayıtları |
| 3 | 275 | C-2 duplicate-write kontrolü |
| 4 | 298 | C-2 namespaced key |
| 5 | 336 | C-1…C-5 + §5 zorunlu test listesi |
| 6 | 386 | §8 RP1 teslim adları |
| 7 | 412 | C-1/C-3 sabitleri + §1/§5 baseline pinleri |
| 8 | 514 | C-6 T-RP-1 |
| 9–10 | 1092, 1101 | C-5 family observability sayacı |
| 11–13 | 1239, 1264, 1296 | C-5 spline observability ve cache payload alanı |
| 14 | 2714 | C-3 loader/QC; C-4 context tablosu; C-5 gözlenebilirlik; C-1 store-read testi |
| 15 | 3207 | C-2 INJ-EXC iki ayrı namespace |
| 16 | 3654 | C-3 false-switch assert; C-6 launch guard |
| 17 | 3771 | §1 standing input hash gate |
| 18 | 3826 | C-1/C-3/C-4/C-5 test wiring |
| 19 | 4617 | C-1 store-read CSV ve sayım assertion'ı |
| 20 | 4766 | §9 D-10 kimliği |
| 21 | 4838 | C-1…C-5 report-only alanları |
| 22 | 4878 | C-6 narrowed_evidence |
| 23 | 4900 | §5 non-regression + §9 status/dispatch wiring |

[A] `run_real_scenario` fonksiyonunun AST'si r4-2 ile aynı. Bu, bilimsel tüketicide değişiklik olmadığını destekler; fakat yeni F1 girdisinin tüketiciye bağlanmadığını da ortaya çıkarır. Frozen engine hash'leri değişmemiştir. 6B uygulaması eklenmemiştir.

[A] Attempt-4 → final diff dört hunk'tır: provenance yorumları/attempt ve supersedes sabitleri, store-read CSV yazımı ve assertion, results içindeki read-log path/hash/count alanları. Yeni bilimsel evaluator değişikliği yoktur. Bu dar kapsam içinde PASS; “yalnız tek executable satır değişti” şeklinde bir iddia yoktur.

### 3.2 C-3 pipeline ve C-4 bağlantısı

| F1 freeze §8.1 adımı | Kod karşılığı | Bağımsız sonuç |
|---|---|---|
| 1 format | `f1_load_raw_dir`, yıllık dosya ve üç sütun kontrolleri | Mevcut [A] |
| 2 semantics | sex/name-length/integer/publication-floor kontrolleri | Mevcut [A]; bazı hata dalları zorunlu testte yok |
| 3 national | national `yob<year>.txt` layout | Hazırlanan loader bu layout'u tüketiyor [A] |
| 4 axis | 1880–2025; `F1_T=146` | Mevcut [A] |
| 5–6 eligibility/retain | Her yılda mevcut sex/name'leri seçme | Mevcut [A]; gerçek 906-satır manifest eşleştirme wiring'i yok |
| 7 released-record share | Payda tüm yayınlanmış isimler üzerinden | Kod doğru [A]; partial-name test assertion'ı zayıf |
| 8 QC | duplicate/denominator/finite/nonnegative kontrolleri | Guard'lar mevcut [A]; tam test coverage yok |
| 9 variance | ddof=0 std, zero-variance STOP | Mevcut [A] |
| 10 normalize | `(x-mean)/std` | Mevcut [A] |
| 11 post-Z | finite/mean/std/norm; tolerance 1e-8 | Mevcut [A]; norm `sqrt(len(z))`, loader domain'inde len=146 |

[A] `f1_build_scenarios` (H:2845–2868) `real_x` ve `real_mask_ids` üretir; strata'ya `("F1REAL", "F_Zq00", 0.0)` benzeri tuple koyar. Ancak `run_real_scenario` (H:2123–2126) her durumda `gen.make_traj(kind, seed, sigma)` çağırır; `real_x`/`real_mask_ids` tüketilmez. Teslim edilen üretici yalnız sentetik bump türlerini işler ve seed'i PCG64'e verir.

[A-S] Teslim edilen loader testinin ürettiği **yalnız sentetik** senaryoyu değişmemiş tüketiciye verdiğimde, ilk fit başlamadan şu hata çıktı:

```text
TypeError SeedSequence expects int or sequence of ints for entropy not F_Zq00
```

[A] C4 dry tablosu (H:2871–2886) ve testi 144 `(fixture_id, mask_id, family)` üçlüsünü doğrular; aynı tabloda yalnız **48 ayrı `(fixture_id,mask_id)` çifti** vardır. Talimat C-4 çiftin family dahil context başına ayırt edilmesini ister. Daha önemlisi, dry kimlikler gerçek tüketicide kullanılmamaktadır. Bu nedenle `T-CONTEXT-ID-UNIQUE = PASS` kaydı işleyen yol için kanıt değildir.

[A] `F1_ELIGIBLE_MANIFEST_PATH/HASH` sabitlerinin hiçbir AST Load kullanımı yoktur. `f1_verify_raw_files` yalnız kendisine verilen listeyi dolaşır; eksik bir listeyi bütün frozen paketmiş gibi reddeden kapsam kontrolü ve eligible manifest byte reproduction bağlantısı görülmedi. Gerçek manifest kapısının ilk **çalıştırılması** daha sonraki gerçek-veri döngüsüne aittir; burada gerçek dosya açılmasını istemiyorum. Eksik olan hazırlanan yolun sözleşmeyi uygulayan kod ve sentetik bağlantı testidir. “Contract'ta adı yoksa STOP” yorumu, senaryo kurucuda uygulanmış bir assertion ile desteklenmiyor.

### 3.3 Zorunlu QC testi

[A] Teslim edilen F1 test kaydında 13 case vardır. `NONFINITE_PRE_Z`, `NONFINITE_POST_Z`, `NEGATIVE_SHARE`, `BAD_SEMANTICS`, `RAW_FILE_MISSING`, `Z_STD_QC`, `Z_NORM_QC` dalları zorunlu testte ayrı beklenen sonuçla sınanmamıştır. Özellikle non-finite C-3'te açıkça adlandırılmıştır. Norm ve std guard'ları arasında matematiksel bağımlılık varsa erişilemez dal da açıkça açıklanabilir; sessizce tam coverage denemez.

[A] H:2937–2943 `denominator_includes_partial` için `ok=True` sabittir. `got` hesabındaki `denom > eligible_sum - 1` eşit paydayı da kabul eder; partial isim dışarıda kalırsa test bunu güvenilir biçimde yakalamaz. Bu **test kusurudur**; mevcut payda kodunun yanlış hesaplandığı iddiası değildir.

[A-S] Ayrı keşif çağrısında NaN/Inf → `NONFINITE_PRE_Z`, negatif değer → `NEGATIVE_SHARE` gözlendi. Guard'ın çalışması eksik zorunlu test kaydını kapatmaz.

### 3.4 Non-regression kapsamı

[A] H:4915–5129 T-NONREG-R4-2 sonuç JSON'unu karşılaştırır. `R4_2_TELEMETRY_PATH` ile `R4_2_TEST_EVIDENCE_PATH` yalnız H:3782–3783 hash-precondition listesinde kullanılır. İçeriklerinin §5 uyarınca her alanı karşılaştırılmaz.

[A] Inline `EXPECTATIONS_E` **19 prefix** içerir. CSV'de **39 E satırı + 1 S satırı** bulunur. “39 önceden beyan edilmiş entry” ile “19 beyan kapsamına atanmış 39 gözlenen fark” aynı şey değildir. C-2'nin istediği INJ-EXC test-evidence capture sayısının açık ön-beyanı da saptanmadı. Capture sayısının 16 olması gerektiğini ileri sürmüyorum: teslim edilmiş test evidence'da unit-phase sayı **8 → 8**, run1/run2 capture dizileri **1 → 1**'dir.

[A] Auditor'ın ayrıca yaptığı statik karşılaştırmada:

- 37/37 evaluation nesnesi ve bütün STOP kayıtları r4-2 ile eşit.
- Canonical belge, teslim edilmiş evaluations/stops ve logda PASS olan iki pin değeri kullanılarak yeniden serileştirildi: `556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77`.
- Residual dosyası hash'i `3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f`; baseline ile eşit.
- Ana telemetry: 12.298 → 12.298 satır; yalnız 2.042 satırda `wall_clock_seconds` farklı; diğer hücreler aynı.
- Test evidence'da değişen altı top-level alan: `exc_captures_unit_phase`, `exc_injection_fixtures`, `spline_call_telemetry_sample_count`, `exc_captures`, `tests_run`, `exc_captures_run2`.

Bunlar bilimsel drift bulgusu değildir. Eksik olan, executor kapısının vaat edilen üç teslimi exact beklentilerle değerlendirmesidir. `tests_run` gibi geniş bir prefix'in otomatik E sayılması, bir gelecek test başarısızlığını kabul etmek için kullanılamaz.

## 4. Yeniden çalıştırma ve ortam

| Alan | Executor [X: results environment] | Auditor [A-S] |
|---|---|---|
| Platform | Windows-10-10.0.19045-SP0 | Linux-6.18.44-x86_64-with-glibc2.39 |
| Python | 3.11.7 | 3.12.14 |
| NumPy | 1.26.4 | 2.3.5 |
| SciPy | 1.14.1 | 1.17.0 |
| OMP / OPENBLAS / MKL threads | 1 / 1 / 1 | 1 / 1 / 1 |
| Launch | Final attempt-5, pid 33100 | 901 |

[A-S] Orijinal harness baytları disposable kopyada çalıştırıldı. Hardcoded `G:/PycharmProjects/pkp-worktree` yolu için yalnız kopya içinde uygun dizin kuruldu; kaynak değiştirilmedi. F1 hash tablosu bu çalışma kopyasına konmadı. Komut/ortam ve stdout/stderr ekte verilmiştir.

[A-S] Giriş kontrolleri F2/spline hash'lerini ve 731/261 grid'i okuduktan sonra W-3 ortam kontrolü **exit 1** ile durdurdu:

```text
AssertionError: W-3 STOP: custody record code_env_fingerprint = a33c98202ae1591d but observed 05a4d06e206bb623
```

Bu engel atlatılmadı; custody veya harness düzenlenmedi. Tam bilimsel RUN1/RUN2 ve zorunlu suite auditor ortamında **NOT PERFORMED after preflight**. Yeni S sonucu üretilmediği için ortama atfedilecek bir sayısal S farkı da ileri sürülmez.

[A-S] Ayrı modül düzeyi keşif kontrolleri: `T-F1-LOADER-SYNTH`'ın mevcut 13 case'i geçer, dry `T-CONTEXT-ID-UNIQUE` 144 üçlüyü benzersiz bulur; ancak tüketici handoff'u yukarıdaki TypeError ile durur. Bunlar tam-suite PASS'i veya Windows bitwise reproduction değildir.

[X] Teslim edilen registry'de 35 mandatory testin tümü ran/passed, toplam 36 test vardır. Auditor bu kayıt değerlerini doğruladı [A]; aynı 35 testi kendi ortamında koşmadı. Teslim `RUN1==RUN2` iddiası [X] olarak kalır; tek teslim edilmiş bilimsel gövdeden her iki bağımsız koşu yeniden oluşturulamaz.

## 5. Store, namespace ve proses hesabı

### 5.1 Sayım birimleri

[A] Audit instruction §4.2, optimizer telemetry satırları ile store-read birimlerini doğrudan toplamayı önerir. Bunlar farklı birimlerdir: bir spline-mode 1 primary ve bazen 1 fallback optimizer çağrısı üretir; coarse sonuç checkpoint'leri ayrıca vardır. Bu nedenle `12.502 + 146 = 12.453` türü eşitlik geçerli değildir. Aşağıdaki dönüşüm uygulanmıştır; talimatın sayım ifadesi bu ayrımı içerecek şekilde okunmalıdır.

| Store key ailesi / scope | Plan/koddan türetim | Manifest gözlemi [A] |
|---|---|---:|
| Base spline mode | RUN1+RUN2: 2×(16+14)×146; FIX-A5: 4×146 | 9.344 |
| INJ pass1 | 3×146 | 438 |
| INJ pass2 | 3×146, ayrı namespace | 438 |
| T-STORE-READ | 146 fresh mode; sonra aynı 146'nın deliberate reread'i | 146 |
| onestart | A5 32; benign 8; duplicate 522; full-grid 994; SCEN-A 256; SCEN-B 254; diğer unit 15 | 2.081 |
| coarse checkpoints | realscen 4 + nr aggregate 1 + unit aggregate 1 | 6 |
| **Toplam unique stored units** | **10.366 mode + 2.081 onestart + 6 coarse** | **12.453** |

[A] onestart sayılarına NR/fixture planındaki gerçek start bankaları esas alındı; ana telemetry'deki kopyalanmış rapor satırları doğrudan computation sayılmadı. Conditional fallback sayısını plan tek başına sabitlemez: fallback'in gerçekten çağrıldığı teslim telemetry'sinden kontrol edilir.

[A] Per-call CSV'de 12.502 satır, fakat bunların **164'ü** T-STORE-READ ikinci okumasında cache'den yeniden eklenmiş birebir kopyadır; wall-clock dahil aynıdır. Cache branch H:1240–1259 saklanmış `tel_calls` satırlarını tekrar append eder. Ayrı fresh çağrıları gösteren kayıt sayısı **12.338**'dir: 10.406 trust-constr (10.366 spline-mode primary + 40 NR primary) ve 1.932 SLSQP fallback. Replay 164 = 146 primary + 18 fallback. Bu ledger hesabıdır; fiziksel çağrıların bağımsız gözlenmesi değildir.

[A] Raw phase sayıları `nr_gates=388`, `unit_tests=1602`, `run1=5256`, `run2=5256`. T-STORE-READ, CURRENT_PHASE değiştirilmeden çağrıldığı için `nr_gates` içinde görünür: 388 = gerçek NR 60 + TSTORE fresh 164 + replay 164. Bu etiketleme cleanup'ıdır (RP1A-04).

### 5.2 Store-read ve INJ-EXC

[A] Read-log: **146 satır**; results `total_rows=146`; fine_counts toplamı **146**; hepsi `tstoreread__|splmode|33100`. Manifest'te 12.453 farklı path ve tüm pid alanlarında `33100` vardır. Key/read-log tutarlılığı PASS.

[A] INJ pass1 ve pass2 key scope'ları ayrı ve 438'er mode içerir; read-log'da bu scope'lardan okuma yoktur. Per-call toplamları S1=330, S2=326, unrelated=328'dir. Saptanan 164 duplicate yalnız T-STORE-READ'dedir. Bu veri, teslim kaydında pass2'nin pass1 store'undan servis edilmediğini destekler; fiziksel store payload'ları olmadan bütün geçmiş çalışmayı bağımsız doğrulamaya dönüştürülemez [X].

[A] Register'ın T-KEY tablosu scope toplamlarını verir; talimatın istediği key-family başına sex/trajectory/family/context/phase alan eşlemesi eksiktir. Kod disjointness kontrolünü özellikle INJ iki pass'e uygular. Mevcut koşuda ek collision saptanmadı; bütün gelecekteki gerçek context'ler için garanti verilmedi. Register'daki `realscen` için “yalnız dry context” açıklaması da doğru değildir: dört SCEN-A/B RUN1/RUN2 coarse synthetic checkpoint vardır. Gerçek veri açılması anlamına gelmez.

### 5.3 Attempt geçmişi

[A] Log beş harness attempt'i anlatır; attempt3'te iki ayrı proses bulunduğundan **altı process start** vardır. Attempt3 pid23540'ın stdout'u yeniden kullanılan launch3 adı nedeniyle kaybolmuş; kalan launch3 logu pid26784'e aittir. Bu kayıp açıkça belirtilmiştir. Final attempt5 pid33100 olarak kaydedilir. Custody/supersedes hash zincirindeki indirilen dosyalar eşleşmektedir.

[X] Attempt3'ün “ctx22” erratum'u fiziksel karantina store'u gerektirir; repo'da olmayan payload'lara dayanarak auditor PASS verilmedi. Dosya zamanları ve executor'ın kesin start/end geçmişi bağımsız dış timestamp kaynağıyla doğrulanamadı. Final kayıtların tutarlı olması geçmiş log kaybını geri getirmez; açıklanmış eski kayıp tek başına burada global blocker yapılmadı.

## 6. Item-by-item checklist

| Madde | Executor claim | Independent verification | Durum / tier |
|---|---|---|---|
| C-1 store-read accounting | Düzeltildi, test PASS | 146/log/results/fine_counts eşit; replay satırları ayrı açıklanmalı | Çekirdek kayıt PASS [A]; test yeniden koşusu NOT PERFORMED; cleanup 04 |
| C-2 namespaces | İki pass bağımsız; key testi PASS | 438+438 ayrı key; read-log'da EXC yok; kapsam tablosu ve capture ön-beyanı eksik | Kısmi PASS [A]; 03/04 açık; tarihsel execution [X] |
| C-3 F1 path | Hazır, OFF | Loader mevcut; tüketiciye bağlantı yok; mandatory QC eksik | FAIL [A], ek handoff [A-S]; 01/02 |
| C-4 context ids | 144 unique | 144 üçlü fakat 48 çift; consumer bağımsız dry tablo | FAIL [A/A-S]; 01 |
| C-5 observability | Frozen alanlardan report-only | F2 classify_endpoint L265–315 ve spline run_tc/solver_config L343–405 alanları incelendi; sayaçlar scientific object'e girmiyor | Alan erişilebilirliği PASS [A]; gerçek inadmissible-refit reachability NOT PERFORMED |
| C-6 restart | ACTIVE_FROM_START, narrowed | T-RP-1 ve T-R2-2 final narrowed_evidence içinde | PASS [A]; fiziksel single-process geçmişi [X] |
| C-7 / S-f | 6B excluded | Yeni 6B hesaplama yolu saptanmadı | PASS [A] |
| §5 nonregression | 0 S, 0 U | S eşitliği yeniden hesaplandı; vaat edilen üç-dosya karşılaştırması uygulanmıyor | FAIL [A]; 03 |
| §3 start inventory | Tam | 123 hash eşit; r4-2/r4-1/r4 satırları ve R41A-04 erratum mevcut | PASS [A] |
| §8 response/diff | Teslim tamam | P1…P9 ayrı; C1…C6 tek birleşik response satırı; ayrı executor diff teslimi yok | FAIL cleanup [A]; 06 |
| §9 rp1_status | PREPARED_PENDING_INDEPENDENT_AUDIT | Test flag'lerinden bu etiket üretilmiş; gerçek 01–03 bulguları open_findings dışında | FAIL [A]; bağımsız hüküm NOT PASSED; corrected status executor işi |
| Coverage | Downgrade yok | 64 satır; downgrade listesi boş; A.5(iii) inadmissible refit UNCOVERED olarak korunmuş | Kayıt PASS [A]; bu satırın reachability'si doğrulanmadı |
| Firewall | real_data_access=false; readiness/start/commit=false | Switch false ve başlangıç assert'i; opened-file listesinde yasak girdiler yok; D-9 geçmiş statüsüne atıf yeni declaration değildir | Statik/kayıt PASS [A]; tüm tarihsel OS erişimleri [X] |
| §7 estimate | ESTIMATE, yaklaşık 85,4 saat | MINI_BANK ölçümü/full-bank anlatımı uyumsuz | Informational [A]; 05 |
| Tam independent rerun | — | W-3 environment mismatch'te durdu | NOT PERFORMED after preflight [A-S] |

C-5 için önemli sınır: bildirilen conjunction'ların mevcut frozen output alanlarından hesaplanabildiği doğrulandı. Her olası “sayısal tamamlanmış ama inadmissible refit” olayının eksiksiz yakalandığı veya lattice witness bulunduğu doğrulanmadı. Delivered test'te witness bulunmadığı zaten yazılıdır. Spline `primary_status` yalnız genel “optimizer temiz döndü” cümlesi değil, frozen `run_tc`'nin status/finite endpoint/finite objective conjunction'ıdır. Gözlenebilirlik açıklamasının kapsamı bu mevcut alanlarla sınırlıdır.

## 7. Açık bulgular

| ID | Classification | Yer ve kanıt | Gate effect | Closure action | Authority |
|---|---|---|---|---|---|
| RP1A-01 | gate-specific blocker | H:2123–2126, 2845–2886, 3025ff; builder consumer'a bağlanmıyor; C4 yalnız dry üçlüleri test ediyor [A/A-S] | RP1 prepared/binding ve sonraki gerçek-veri yolunun hazır olduğu kabulü engellenir | `real_x`/mask ids'yi gerçek consumer'a bağla; gerçek veri kullanmadan mandatory synthetic handoff/context testi ekle; complete deferred hash/manifest gate'ini hazırla; adı olmayan contract parametresinde STOP/report uygula | X |
| RP1A-02 | gate-specific blocker | H:2802–2842, 2897–3022; eksik nonfinite/QC dalları, sabit `ok=True` denominator case [A] | T-F1-LOADER-SYNTH tamlığı kabul edilemez | QC dallarına explicit expected/got assertions; partial-name paydayı doğru beklenen değere eşitle; erişilemez dalı gerekçelendir; mandatory testi çalıştır | X |
| RP1A-03 | gate-specific blocker | H:3782–3783, 4915–5129; yalnız JSON nonregression; 19 prefix/39 E ayrımı; capture ön-beyanı eksik [A] | §5 no-U/no-S nonregression ve D-9 binding precondition tamamlanmaz | Final results, telemetry, test evidence'ın her alanını karşılaştır; S strict, E dar ve önceden belirli, kalan fark U; capture sayı beklentisini yaz; değişen her alanı raporla | X |
| RP1A-04 | cleanup | H:1240–1259, test çağrı sırası; percall CSV ve key register [A] | Tek başına gate bloke etmez; muhasebe yorumunu daraltır | Fresh/replay satırlarını ayırt et; phase/units açıklamasını düzelt; key-family field mapping ve realscen açıklamasını mevcut register'a ekle | X |
| RP1A-05 | informational | §7 size estimate; SCEN-A MINI_BANK, family başına context'te 4 start [A] | Gate etkisi yok; süre planı güvenilirliği sınırlı | 85,4 saati ölçülen kapsamla etiketle; full-bank planlanacaksa uygun sentetik timing kullan, bilimsel ayar seçme | X |
| RP1A-06 | cleanup | Response/diff/attempt wording, standing sidecar ve mixed-hunk mapping [A] | Tek başına gate bloke etmez | C1…C6 ayrı response satırları; mevcut diff teslimi; 5 attempt/6 process ayrımı; “verified”i executor self-check diye sınırla; eski eksik sidecar'ları kaydet/tamamla; mixed/§5 hunks'u doğru etiketle | X |
| RP1A-07 | informational | W-3 stop; absent physical stores; historical timestamps/ctx22 [A-S/X] | İlave bilimsel başarısızlık bulgusu değil; bağımsız kanıtın sınırı | Kayıtta NOT PERFORMED/[X] korunsun; gerekiyorsa uygun ortamda sentetik independent rerun ve mevcut store kanıtı sağlansın; PI binding kararı bu sınırı görsün | X (kanıt), T (PI acceptance) |

RP1A-05 ayrıntısı: SCEN-A'da her sex için 8 context × 2 family × 4 start = 64 family optimizer kaydı vardır. Full-bank anlatımı ise 732 P01 + 262 P02 start/context, yani 8×994=7.952 start/trajectory gerektirir. Ölçülen MINI_BANK iş yükü bunu temsil etmez. Buradan basit lineer çarpımla yeni bir saat tahmini üretmedim; spline maliyeti ve diğer koşullar ayrıca önemlidir.

### Yalnız açık kalan S/T/X register

| Authority | Açık iş | Bu kaydın sınırı |
|---|---|---|
| S | Yeni S kararı talep edilmiyor | Eksik contract değeri gerçekten ortaya çıkarsa executor seçmez, raporlar |
| X | RP1A-01, 02, 03 teknik kapanış; 04/06 aynı mevcut düzeltmeye eklenebilir | Yeni geniş tasarım/audit döngüsü talep edilmez; değişen yolları ve zorunlu nonregression'ı hedeflemek yeterlidir |
| X | RP1A-05/07 kanıt ve planlama sınırlarının doğru etiketlenmesi | Bilgi maddeleri tek başına işi durdurmaz |
| T | D-9 §2(a) kapsamında harness bağlama/acceptance PI'da kalır | Bu kayıt kabul önerisi değildir; açık gate blocker'lar varken koşullar tamamlandı denmez |

## 8. NOT PERFORMED ve kesin sınırlar

1. Tam auditor RUN1/RUN2 ve zorunlu suite: W-3 farklı ortam fingerprint'i nedeniyle preflight sonrasında çalışmadı.
2. Windows bitwise reproduction; SciPy/NumPy/Python eşleştirilmiş bağımsız full run: yapılmadı.
3. Fiziksel restart payload hash'leri, store'un başlangıçta boşluğu, her payload'ın gerçek writer pid'si: store repo dışında, yapılmadı. CSV alan değerleri doğrulandı.
4. Attempt3 ctx22 forensics ve kayıp stdout recovery: fiziksel karantina store'u yok; yapılmadı.
5. Custody'nin fiilen launch'tan önce yazıldığının bağımsız timestamp kanıtı: bulunmadı; declaration [X].
6. Gerçek SSA/F1 raw-file verification, 906 eligible row reproduction, gerçek fitting ve algorithm×CVI: kapsam gereği yapılmadı. Bu yasaklar aşılmadı.
7. Gerçek içerikle sentetik içerik benzerliği: raw dosyalar açılmadı; yalnız hash-equality exclusion ve sentetik üretici incelemesi yapıldı.
8. Mevcut fixture dışında inadmissible-refit reachability, yeni bilimsel eşik veya 6B: yapılmadı.

## 9. PI'ya sonuç

**D-9 §2(a) için teslim edilen bilimsel S değerlerinin r4-2 ile eşitliği [A] doğrulandı; ancak eksik non-regression kapsamı ve RP1A-01…03 açık gate blocker'ları nedeniyle preconditions bütünü karşılanmış değildir. Bu independent audit tamamlandı ve hükmü NOT PASSED'tir; Windows→Linux/Python/NumPy/SciPy farkı nedeniyle tam auditor rerun yapılmamıştır.**

Aşağıdaki ekler bu tek kaydın parçasıdır. Bu dosyanın kendi hash'i içine yazılmaz; dış `.sha256` sidecar kullanılır.

## Ek A — Çalıştırılan komutlar ve araçlar

Kaynak alma: GitHub connector, sabit commit'te recursive Git trees ve blob içerikleri; alınan bloblar `decode_downloads.py` ile Git blob SHA1 kontrolünden sonra yerel alındı. Repository'ye yazılmadı. Analiz araçları: Python standard library (`hashlib`, `ast`, `json`, `csv`, `difflib`, `collections`), `rg`, `sed`, shell, NumPy/SciPy. Aşağıdaki dosyalar auditor'ın çalışma betikleridir; executor kodu değildir.

```bash
python rp1_audit/evidence/core_checks.py > rp1_audit/evidence/core_checks.out
python rp1_audit/evidence/extended_checks.py > rp1_audit/evidence/extended_checks.out
python rp1_audit/evidence/final_checks.py > rp1_audit/evidence/final_checks.out
# İsolated synthetic probe source ve alınan çıktı aşağıdadır.
# Tam launch için kullanılan executable, cwd ve thread/launch ortamı Ek A.6'dadır.
```

Core ve extended betiklerinde canonical hash'in iki pin değeri, teslim edilmiş final launch logundaki iki PASS kaydından alınmıştır. Bu yeniden serileştirme teslim belgesini doğrular; yeni fit değildir. Betik stdout'undaki `determinism_claim` özellikle bir claim alanıdır. `PIN_VALUES` satırı bir kaynak işaretidir, ek bağımsız execution iddiası değildir.

## Ek A.1 — core_checks.py

```python
from pathlib import Path
import ast,csv,hashlib,json,difflib,collections,platform,sys
R=Path(__file__).resolve().parents[1]; P=R/'received/p_konum_plus'; E=R/'evidence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
src=(P/'calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py').read_text();tree=ast.parse(src)
pins={}; constants={}
for n in tree.body:
 if isinstance(n,ast.Assign) and len(n.targets)==1 and isinstance(n.targets[0],ast.Name):
  try: constants[n.targets[0].id]=ast.literal_eval(n.value)
  except (ValueError,TypeError):pass
for k,v in constants.items():
 if k.endswith('_PATH') and isinstance(v,str):
  h=constants.get(k[:-5]+'_HASH')
  if h and isinstance(h,str) and len(h)==64 and k not in ('F1_ELIGIBLE_MANIFEST_PATH',):pins[v]=h
T=P/'provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md'; listed={}
for line in T.read_text().splitlines():
 if line.startswith('|'):
  cols=[c.strip().strip('`') for c in line.split('|')[1:-1]]
  if len(cols)>=3 and len(cols[2])==64 and all(c in '0123456789abcdef' for c in cols[2]):listed['p_konum_plus/'+cols[1]]=cols[2]
listed['p_konum_plus/'+str(T.relative_to(P))]=None
checks=[]
for kind,items in [('transmission',listed),('standing pins',pins)]:
 for rel,exp in items.items():
  f=R/'received'/rel; sc=Path(str(f)+'.sha256');got=sha(f) if f.exists() else None
  sh=sc.read_text().split()[0] if sc.exists() else None
  checks.append(dict(kind=kind,path=rel,observed=got,expected=exp,sidecar=sh,result='PASS' if got and (exp is None or exp==got) and (sh is None and kind=='standing pins' or sh==got) else 'FAIL'))
(E/'custody.json').write_text(json.dumps(checks,indent=2))
print('CUSTODY',dict(collections.Counter(x['result'] for x in checks)), 'transmission',len(listed),'standing',len(pins));print('CUSTODY_FAILURES',[x for x in checks if x['result']!='PASS'])
head={x['path']:x for x in json.loads((E/'tree_head.json').read_text())['tree'] if x['type']=='blob'}
base={x['path']:x for x in json.loads((E/'tree_base.json').read_text())['tree'] if x['type']=='blob'}
changed=[p for p in base if p not in head or base[p]['sha']!=head[p]['sha'] or base[p]['mode']!=head[p]['mode']]
added=[p for p in head if p not in base];print('PARENTS',{'base_blobs':len(base),'modified_or_deleted':changed,'added_blobs':len(added),'additions_outside_project':[p for p in added if not p.startswith('p_konum_plus/')]})
(E/'parent_diff.json').write_text(json.dumps(dict(changed=changed,added=added),indent=2))
for tag,old in [('r4-2',P/'calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py'),('attempt4',P/'quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py')]:
 text=''.join(difflib.unified_diff(old.read_text().splitlines(True),src.splitlines(True),fromfile=old.name,tofile='rp1',n=3));(E/('diff_'+tag+'.txt')).write_text(text);print('DIFF',tag,'hunks',sum(l.startswith('@@') for l in text.splitlines()),'lines',len(text.splitlines()))
d=json.loads((P/'calibration/f3_step2_results_rp1_2026-10-02.json').read_text());b=json.loads((P/'calibration/f3_step2_results_r4-2_2026-09-30.json').read_text());te=json.loads((P/'calibration/f3_step2_test_evidence_rp1_2026-10-02.json').read_text());bt=json.loads((P/'calibration/f3_step2_test_evidence_r4-2_2026-09-30.json').read_text())
js=lambda v:json.dumps(v,sort_keys=True)
ea={x['fixture_id']:x for x in d['evaluations']};eb={x['fixture_id']:x for x in b['evaluations']};dd=[k for k in ea.keys()|eb.keys() if js(ea.get(k))!=js(eb.get(k))];st=sorted(map(js,d['stops']))==sorted(map(js,b['stops']))
can_doc=dict(evals=d['evaluations'],stops=d['stops'],pins=dict(mask_full=True,fs=True));hc=hashlib.sha256(js(can_doc).encode()).hexdigest()
print('S_NONREG',{'r4_2_count':len(eb),'rp1_count':len(ea),'evaluation_differences':dd,'stops_equal':st,'computed_canonical':hc,'declared_canonical':d['run1_canonical_sha256'],'determinism_claim':d['determinism'],'residual_sha256':sha(P/'calibration/f3_step2_residual_series_rp1_2026-10-02.json')})
exp={}
for n in ast.walk(tree):
 if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='EXPECTATIONS_E' for t in n.targets):exp=ast.literal_eval(n.value)
nr=list(csv.DictReader((P/'calibration/f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv').open()));print('EXPECTATIONS_E',len(exp),'CSV',len(nr),'classes',dict(collections.Counter(x.get('classification') for x in nr)));(E/'expectations_E.json').write_text(json.dumps(exp,indent=2))
print('MANDATORY_REGISTRY',len(constants['MANDATORY_TESTS']),[(k,d['tests_run'].get(k)) for k in constants['MANDATORY_TESTS'] if d['tests_run'].get(k)!={'ran':True,'passed':True}], 'tests_total',len(d['tests_run']))
print('F1_TEST_CASES',list(d['f1_loader_synth']['cases']))
pc=list(csv.DictReader((P/'calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv').open()));sm=list(csv.DictReader((P/'calibration/f3_step2_rp1_restart_store_manifest_2026-10-02.csv').open()));sl=list(csv.DictReader((P/'calibration/f3_step2_rp1_store_read_log_2026-10-02.csv').open()))
families=collections.Counter(); scopes=collections.Counter()
for row in sm:
 s=row['path'].split('__',1)[1];family=next((f for f in ('onestart','splmode','realscen','nrgates_all','unittests_all') if f in s),s);scope='excpass1__' if s.startswith('excpass1__') else 'excpass2__' if s.startswith('excpass2__') else 'tstoreread__' if s.startswith('tstoreread__') else '(base)';families[scope+'|'+family]+=1;scopes[scope]+=1
print('STORE_COUNTS',len(sm),dict(families),'unique_paths',len({x['path'] for x in sm}),'pids',dict(collections.Counter(x['pid'] for x in sm)))
print('PER_CALL',len(pc),'phases',dict(collections.Counter(x['phase'] for x in pc)),'methods',dict(collections.Counter(x['method'] for x in pc)))
print('STORE_READ',len(sl),d['store_read_accounting'],'all_writers_readers_33100',all(x['writer_pid']==x['reader_pid']=='33100' for x in sl))
duplicates=[(n,k) for k,n in collections.Counter(tuple(sorted(r.items())) for r in pc).items() if n>1];print('PER_CALL_EXACT_DUPLICATE_GROUPS',len(duplicates))
(E/'core_summary.json').write_text(json.dumps(dict(S_evaluation_differences=dd,stops_equal=st,canonical_computed=hc,store_family_counts=families,store_scope_counts=scopes,percall_phase_counts=collections.Counter(x['phase'] for x in pc),percall_duplicate_groups=len(duplicates)),indent=2))
```

## Ek A.1 çıktı

```text
CUSTODY {'PASS': 70} transmission 44 standing 26
CUSTODY_FAILURES []
PARENTS {'base_blobs': 1389, 'modified_or_deleted': [], 'added_blobs': 990, 'additions_outside_project': []}
DIFF r4-2 hunks 23 lines 1339
DIFF attempt4 hunks 4 lines 121
S_NONREG {'r4_2_count': 37, 'rp1_count': 37, 'evaluation_differences': [], 'stops_equal': True, 'computed_canonical': '556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77', 'declared_canonical': '556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77', 'determinism_claim': True, 'residual_sha256': '3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f'}
EXPECTATIONS_E 19 CSV 40 classes {'S': 1, 'E': 39}
MANDATORY_REGISTRY 35 [] tests_total 36
F1_TEST_CASES ['BAD_FORMAT', 'COUNT_BELOW_PUBLICATION_FLOOR', 'DUPLICATE_KEY', 'MISSING_YEAR', 'RAW_FILE_HASH_MISMATCH', 'TOLERANCE_BREACH', 'ZERO_DENOMINATOR', 'ZERO_VARIANCE', 'denominator_includes_partial', 'eligible_count', 'gate_pass', 'partial_excluded', 'z_qc_pass']
STORE_COUNTS 12453 {'excpass1__|splmode': 438, 'excpass2__|splmode': 438, '(base)|nrgates_all': 1, '(base)|onestart': 2081, '(base)|realscen': 4, '(base)|splmode': 9344, 'tstoreread__|splmode': 146, '(base)|unittests_all': 1} unique_paths 12453 pids {'33100': 12453}
PER_CALL 12502 phases {'nr_gates': 388, 'unit_tests': 1602, 'run1': 5256, 'run2': 5256} methods {'SLSQP': 1950, 'trust-constr': 10552}
STORE_READ 146 {'fine_counts': {'tstoreread__|splmode|33100': 146}, 'store_read_log_path': 'p_konum_plus/calibration/f3_step2_rp1_store_read_log_2026-10-02.csv', 'store_read_log_rows': 146, 'store_read_log_sha256': '6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1', 'total_rows': 146} all_writers_readers_33100 True
PER_CALL_EXACT_DUPLICATE_GROUPS 164
```

## Ek A.2 — extended_checks.py

```python
from pathlib import Path
import ast,csv,hashlib,json,collections,re
R=Path(__file__).resolve().parents[1];P=R/'received/p_konum_plus';E=R/'evidence';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
tree=json.loads((E/'tree_head.json').read_text())['tree'];by={x['path']:x for x in tree if x['type']=='blob'}
inv=(P/'provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md').read_text();rows=[];missing=[]
for line in inv.splitlines():
 if not line.startswith('|'):continue
 cols=[c.strip(' `') for c in line.split('|')[1:-1]];hashes=re.findall(r'\b[0-9a-f]{64}\b',line);paths=re.findall(r'(?:calibration|provenance|quarantine|prompts)/[^\s|`]+',line)
 if not hashes or not paths:continue
 rel='p_konum_plus/'+paths[0];f=R/'received'/rel;got=sha(f) if f.exists() else None;rows.append(dict(path=rel,expected=hashes[-1],observed=got,match=got==hashes[-1]))
 if not got and rel in by:missing.append(by[rel])
(E/'inventory_checks.json').write_text(json.dumps(rows,indent=2));(E/'inventory_missing.json').write_text(json.dumps(list({x['path']:x for x in missing}.values())))
print('INVENTORY',len(rows),'available',sum(x['observed'] is not None for x in rows),'mismatch',[x for x in rows if x['observed'] and not x['match']],'missing',len(missing))
d=json.loads((P/'calibration/f3_step2_results_rp1_2026-10-02.json').read_text());b=json.loads((P/'calibration/f3_step2_results_r4-2_2026-09-30.json').read_text());te=json.loads((P/'calibration/f3_step2_test_evidence_rp1_2026-10-02.json').read_text());bt=json.loads((P/'calibration/f3_step2_test_evidence_r4-2_2026-09-30.json').read_text())
doc=dict(evals=d['evaluations'],stops=d['stops'],pins=dict(mask_full=True,fs=True));ch=hashlib.sha256(json.dumps(doc,sort_keys=True).encode()).hexdigest();print('ACTUAL_CANONICAL_REBUILT',ch,'equal',ch==d['run1_canonical_sha256'])
print('PIN_VALUES','source main pins and log must substantiate True/True; log prints PIN-MASKED-OBJECTIVE and PIN-FEATURE-START-MASKED PASS')
tel=list(csv.DictReader((P/'calibration/f3_step2_telemetry_rp1_2026-10-02.csv').open()));base=list(csv.DictReader((P/'calibration/f3_step2_telemetry_r4-2_2026-09-30.csv').open()));diff=collections.Counter()
for a,c in zip(base,tel):
 for k in a.keys()|c.keys():
  if a.get(k)!=c.get(k):diff[k]+=1
print('TELEMETRY_NONREG',len(base),len(tel),dict(diff))
print('TEST_EVIDENCE_DIFF_TOPLEVEL',[k for k in te.keys()|bt.keys() if te.get(k)!=bt.get(k)])
print('EXCEPTION_CAPTURE_LENGTHS', {k:(len(bt.get(k,[])),len(te.get(k,[]))) for k in ('exc_captures','exc_captures_unit_phase','exc_captures_run2')})
pc=list(csv.DictReader((P/'calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv').open()));counts=collections.Counter(tuple(sorted(x.items())) for x in pc);dup=[dict(k) for k,v in counts.items() if v>1];print('DUPLICATE_ROWS',len(dup),'extra_rows',sum(v-1 for v in counts.values()),'fixtures',dict(collections.Counter(x['fixture'] for x in dup)))
for f in ('INJ-EXC-CAPTURE-S1','INJ-EXC-CAPTURE-S2','INJ-EXC-UNRELATED-TYPE','T-STORE-READ'):
 rs=[x for x in pc if x['fixture']==f];print('PERCALL_FIXTURE',f,len(rs),dict(collections.Counter(x['method'] for x in rs)))
print('SCEN_CALLS',dict(collections.Counter((x['phase'],x['fixture'],x['method']) for x in pc if x['phase'] in ('run1','run2'))))
print('MAIN_TELEMETRY_FAMILY_COUNTS',dict(collections.Counter((x['fixture'],x['fitter'],x['mask_id'].split(':')[0]) for x in tel)))
root=P/'calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02';fix=list(root.rglob('yob*.txt'));hashfile=P/'manifests/f1_input_hash_table_2026-08-28.csv';rawhashes=set()
with hashfile.open() as f:
 reader=csv.DictReader(f);hc=next(k for k in reader.fieldnames if k.lower()=='sha256');rawhashes={row[hc] for row in reader}
fh={str(p.relative_to(root)):sha(p) for p in fix};print('SYNTHETIC',len(fh),'sha256_matches_raw',len(set(fh.values())&rawhashes),'generator_regenerated_equal',sum((R/'component_synthetic'/p).exists() and sha(R/'component_synthetic'/p)==h for p,h in fh.items()))
(E/'synthetic_hashes.json').write_text(json.dumps(fh,indent=2,sort_keys=True))
opened=d['opened_files_audit_derived'];bad=[x for x in opened if '/data/raw/' in x.replace('\\','/') or 'f1_eligible_trajectory_manifest' in x or 'f1_input_hash_table' in x];print('DELIVERED_OPENED_FILE_AUDIT',len(opened),'forbidden',bad)
print('COVERAGE',len(d['coverage']),'downgrades',d['coverage_downgraded_rows'],'uncovered',[x for x in d['coverage'] if str(x[-1]).startswith('UNCOVERED')])
(E/'extended_summary.json').write_text(json.dumps(dict(canonical=ch,telemetry_fields_changed=diff,telemetry_rows=len(tel),percall_replay_rows=sum(v-1 for v in counts.values()),synthetic_files=len(fh),forbidden_opened=bad),indent=2))
```

## Ek A.2 çıktı

```text
INVENTORY 123 available 123 mismatch [] missing 0
ACTUAL_CANONICAL_REBUILT 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 equal True
PIN_VALUES source main pins and log must substantiate True/True; log prints PIN-MASKED-OBJECTIVE and PIN-FEATURE-START-MASKED PASS
TELEMETRY_NONREG 12298 12298 {'wall_clock_seconds': 2042}
TEST_EVIDENCE_DIFF_TOPLEVEL ['exc_captures_run2', 'exc_injection_fixtures', 'exc_captures_unit_phase', 'spline_call_telemetry_sample_count', 'tests_run', 'exc_captures']
EXCEPTION_CAPTURE_LENGTHS {'exc_captures': (1, 1), 'exc_captures_unit_phase': (8, 8), 'exc_captures_run2': (1, 1)}
DUPLICATE_ROWS 164 extra_rows 164 fixtures {'T-STORE-READ': 164}
PERCALL_FIXTURE INJ-EXC-CAPTURE-S1 330 {'trust-constr': 292, 'SLSQP': 38}
PERCALL_FIXTURE INJ-EXC-CAPTURE-S2 326 {'trust-constr': 292, 'SLSQP': 34}
PERCALL_FIXTURE INJ-EXC-UNRELATED-TYPE 328 {'trust-constr': 292, 'SLSQP': 36}
PERCALL_FIXTURE T-STORE-READ 328 {'trust-constr': 292, 'SLSQP': 36}
SCEN_CALLS {('run1', 'SCEN-A', 'trust-constr'): 2336, ('run1', 'SCEN-A', 'SLSQP'): 444, ('run1', 'SCEN-B', 'trust-constr'): 2044, ('run1', 'SCEN-B', 'SLSQP'): 432, ('run2', 'SCEN-A', 'trust-constr'): 2336, ('run2', 'SCEN-A', 'SLSQP'): 444, ('run2', 'SCEN-B', 'trust-constr'): 2044, ('run2', 'SCEN-B', 'SLSQP'): 432}
MAIN_TELEMETRY_FAMILY_COUNTS {('SCEN-A', 'P-01', 'run1'): 64, ('SCEN-A', 'P-02', 'run1'): 64, ('SCEN-A', 'SPL', 'run1'): 2336, ('SCEN-B', 'P-01', 'run1'): 68, ('SCEN-B', 'P-02', 'run1'): 67, ('SCEN-B', 'SPL', 'run1'): 2046, ('SCEN-A', 'P-01', 'run2'): 64, ('SCEN-A', 'P-02', 'run2'): 64, ('SCEN-A', 'SPL', 'run2'): 2336, ('SCEN-B', 'P-01', 'run2'): 68, ('SCEN-B', 'P-02', 'run2'): 67, ('SCEN-B', 'SPL', 'run2'): 2046, ('INJ-EXC-CAPTURE-S1', 'SPL', 'exc'): 292, ('INJ-EXC-CAPTURE-S2', 'SPL', 'exc'): 292, ('INJ-EXC-UNRELATED-TYPE', 'SPL', 'exc'): 292, ('FIX-A5-TRUE', 'P-01', 'a5true'): 16, ('FIX-A5-TRUE', 'P-02', 'a5true'): 16, ('FIX-A5-TRUE', 'SPL', 'a5true'): 584, ('FIX-STARTS-FULL', 'P-01', 'full'): 732, ('FIX-STARTS-FULL', 'P-02', 'full'): 262, ('FIX-STARTS-DUP', 'P-02', 'dup'): 522}
SYNTHETIC 875 sha256_matches_raw 0 generator_regenerated_equal 875
DELIVERED_OPENED_FILE_AUDIT 26087 forbidden []
COVERAGE 64 downgrades [] uncovered [['A.5 (iii) inadmissible refit', 'UNCOVERED(no construction of a numerically-complete inadmissible refit without touching frozen code -- Y-16)', 'n/a', 'UNCOVERED(no construction possible without touching frozen code)']]
```

## Ek A.3 — component_probes.py

```python
from pathlib import Path
import os,sys,importlib.util,json,collections,numpy as np
R=Path(__file__).resolve().parents[1];run=R/'run';root=run/'G:/PycharmProjects/pkp-worktree';os.chdir(run)
h=root/'p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py'
s=importlib.util.spec_from_file_location('audited_rp1',h);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
# Importing does not call main(). No custody check is disabled and no source is edited.
# These are isolated exploratory function calls, NOT an end-to-end accepted run.
gs=importlib.util.spec_from_file_location(m.GEN_MODULE_NAME,root/m.GEN_PATH);gen=importlib.util.module_from_spec(gs);sys.modules[m.GEN_MODULE_NAME]=gen;gs.loader.exec_module(gen)
out,sc=m.t_f1_loader_synth(str(R/'component_synthetic'))
print('T-F1-LOADER-SYNTH isolated [A-S]',json.dumps(out,sort_keys=True))
print('T-CONTEXT-ID-UNIQUE isolated [A-S]',json.dumps(m.t_context_id_unique(sc),sort_keys=True))
table=m.f1_context_id_table(sc);print('CONTEXT_PAIRS',len(table),len(set(table)),len(set((r[0],r[1]) for r in table)))
try:m.run_real_scenario(None,None,None,sc[0],'auditor_synthetic_only',[])
except Exception as e:print('SYNTHETIC_LOADER_TO_CONSUMER',type(e).__name__,str(e))
for token,x in [('nan_pre',np.full(146,np.nan)),('inf_pre',np.full(146,np.inf)),('negative_pre',np.arange(146)-1)]:
 try:m.f1_normalize({('F','Synthetic'):x});print(token,'NO_FAILURE')
 except Exception as e:print(token,type(e).__name__,str(e))
print('opened_real_input', [p for p in m.OPENED_FILES_AUDIT if '/data/raw/' in p.replace('\\','/') or 'f1_eligible_trajectory_manifest' in p or 'f1_input_hash_table' in p])
```

## Ek A.3 çıktı

```text
T-F1-LOADER-SYNTH isolated [A-S] {"BAD_FORMAT": {"expected": "BAD_FORMAT", "got": "BAD_FORMAT", "ok": true}, "COUNT_BELOW_PUBLICATION_FLOOR": {"expected": "COUNT_BELOW_PUBLICATION_FLOOR", "got": "COUNT_BELOW_PUBLICATION_FLOOR", "ok": true}, "DUPLICATE_KEY": {"expected": "DUPLICATE_KEY", "got": "DUPLICATE_KEY", "ok": true}, "MISSING_YEAR": {"expected": "MISSING_YEAR", "got": "MISSING_YEAR", "ok": true}, "RAW_FILE_HASH_MISMATCH": {"expected": "RAW_FILE_HASH_MISMATCH", "got": "RAW_FILE_HASH_MISMATCH", "ok": true}, "TOLERANCE_BREACH": {"expected": "Z_MEAN_QC", "got": "Z_MEAN_QC", "ok": true}, "ZERO_DENOMINATOR": {"expected": "ZERO_DENOMINATOR", "got": "ZERO_DENOMINATOR", "ok": true}, "ZERO_VARIANCE": {"expected": "ZERO_VARIANCE", "got": "ZERO_VARIANCE", "ok": true}, "denominator_includes_partial": {"expected": true, "got": true, "ok": true}, "eligible_count": {"expected": 6, "got": 6, "ok": true}, "gate_pass": {"expected": true, "got": true, "ok": true}, "partial_excluded": {"expected": true, "got": true, "ok": true}, "pass_": true, "z_qc_pass": {"expected": true, "got": true, "ok": true}}
T-CONTEXT-ID-UNIQUE isolated [A-S] {"all_unique": true, "expected_rows": 144, "pass_": true, "rows": 144}
CONTEXT_PAIRS 144 144 48
SYNTHETIC_LOADER_TO_CONSUMER TypeError SeedSequence expects int or sequence of ints for entropy not F_Zq00
nan_pre F1QCFailure NONFINITE_PRE_Z F_Synthetic
inf_pre F1QCFailure NONFINITE_PRE_Z F_Synthetic
negative_pre F1QCFailure NEGATIVE_SHARE F_Synthetic
opened_real_input []
```

## Ek A.4 — final_checks.py

```python
from pathlib import Path
import ast, hashlib, json, re
R=Path(__file__).resolve().parents[1]; P=R/'received/p_konum_plus'; E=R/'evidence'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for p in sorted((R/'received').rglob('*')):
 if p.is_file(): rows.append(f'{sha(p)}  {p.relative_to(R/"received")}')
u=R.parent/'upload/F3_RP1_INDEPENDENT_AUDIT_INSTRUCTION_2026-10-04.md'
rows.append(f'{sha(u)}  upload/{u.name}')
(E/'input_sha256.out').write_text('\n'.join(rows)+'\n')
print('BYTE_HASH_INVENTORY',len(rows),'files; input_sha256.out')
print('AUDIT_INSTRUCTION_SHA256',sha(u))
h=P/'calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py';b=P/'calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py'
t=ast.parse(h.read_text());bt=ast.parse(b.read_text());fs=lambda t:{n.name:ast.dump(n,include_attributes=False) for n in t.body if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))}
f,g=fs(t),fs(bt);print('UNCHANGED_CONSUMER_AST',f['run_real_scenario']==g['run_real_scenario'])
for name in ['F1_ELIGIBLE_MANIFEST_PATH','F1_ELIGIBLE_MANIFEST_HASH','R4_2_TELEMETRY_PATH','R4_2_TEST_EVIDENCE_PATH']:
 print('AST_LOAD_SITES',name,[n.lineno for n in ast.walk(t) if isinstance(n,ast.Name) and isinstance(n.ctx,ast.Load) and n.id==name])
print('REAL_DATA_MODE_ASSIGNMENTS',[(n.lineno,ast.unparse(n)) for n in ast.walk(t) if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='REAL_DATA_MODE' for x in n.targets)])
c=json.loads((E/'custody.json').read_text());i=json.loads((E/'inventory_checks.json').read_text())
assert all(x['result']=='PASS' for x in c)
assert len(i)==123 and all(x['match'] for x in i)
for x in c: assert sha(R/'received'/x['path'])==x['observed']
for x in i: assert sha(R/'received'/x['path'])==x['observed']
print('RECHECK_CUSTODY',len(c),'PASS; INVENTORY',len(i),'PASS')
print('STANDING_SIDECARS_ABSENT',[x['path'] for x in c if x['sidecar'] is None])
```

## Ek A.4 çıktı

```text
BYTE_HASH_INVENTORY 1212 files; input_sha256.out
AUDIT_INSTRUCTION_SHA256 1f411fb2de44493971a6c4a425a71a5fb14441e3f567b8e087e015c4f37f738a
UNCHANGED_CONSUMER_AST True
AST_LOAD_SITES F1_ELIGIBLE_MANIFEST_PATH []
AST_LOAD_SITES F1_ELIGIBLE_MANIFEST_HASH []
AST_LOAD_SITES R4_2_TELEMETRY_PATH [3782]
AST_LOAD_SITES R4_2_TEST_EVIDENCE_PATH [3783]
REAL_DATA_MODE_ASSIGNMENTS [(455, 'REAL_DATA_MODE = False')]
RECHECK_CUSTODY 70 PASS; INVENTORY 123 PASS
STANDING_SIDECARS_ABSENT ['p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py', 'p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py', 'p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md', 'p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv']
```

## Ek A.5 — Blob decoding/hash kontrol betiği

```python
import base64,hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
written=0
for f in (root/'cache').glob('*.json'):
    d=json.loads(f.read_text())
    data=base64.b64decode(d['content']) if d['encoding']=='base64' else d['content'].encode('utf-8')
    got=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if got!=d['sha']: raise ValueError(f'GIT_BLOB_MISMATCH {f} {got} != {d["sha"]}')
    for rel in d['paths']:
        p=root/'received'/rel;p.parent.mkdir(parents=True,exist_ok=True)
        if not p.exists():p.write_bytes(data);written+=1
print(f'decoded_new_files={written}; Git blob SHA1 equality checked for every cached byte stream')
```

## Ek A.6 — Auditor launch ortamı ve komutu

```json
{
  "platform": "Linux-6.18.44-x86_64-with-glibc2.39",
  "python": "3.12.14",
  "numpy": "2.3.5",
  "scipy": "1.17.0",
  "OMP": "1",
  "OPENBLAS": "1",
  "MKL": "1",
  "launch": 901,
  "returncode": 1,
  "command": [
    "/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python",
    "/workspace/scratch/fb7cafb760a8/rp1_audit/run/G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py"
  ],
  "cwd": "/workspace/scratch/fb7cafb760a8/rp1_audit/run",
  "filesystem_mapping": "G:/PycharmProjects/pkp-worktree relative directory inside disposable copy; no source modification"
}
```

## Ek A.6 stdout

```text
LAUNCH_NUMBER = 901 ; logs = p_konum_plus/calibration/f3_step2_rp1_launch901_stdout_2026-10-02.log / p_konum_plus/calibration/f3_step2_rp1_launch901_stderr_2026-10-02.log
REAL_DATA_MODE = False
PIN-F2-IMPORT-HASH = 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077
PIN-SPLINE-IMPORT-HASH = b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d
PIN-SPLINE-LOADER prelude nodes = 21 (authorized list match: True)
PID = 14 ; START = 2026-10-05T10:21:27.108057 ; CMDLINE = /workspace/scratch/fb7cafb760a8/rp1_audit/run/G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py ; INTERPRETER = /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
RESTART_LAYER_ACTIVE = True
GRID_SIZES = P-01 731 ; P-02 261
FIXTURE_MANIFEST_SHA256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
MANIFEST_REUSED_UNCHANGED_FROM_R4_1 = true (regenerated in memory and verified equal; file not rewritten)
```

## Ek A.6 stderr

```text
Traceback (most recent call last):
  File "/workspace/scratch/fb7cafb760a8/rp1_audit/run/G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py", line 5163, in <module>
    main()
  File "/workspace/scratch/fb7cafb760a8/rp1_audit/run/G:/PycharmProjects/pkp-worktree/p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py", line 3747, in main
    assert recorded == observed, (
           ^^^^^^^^^^^^^^^^^^^^
AssertionError: W-3 STOP: custody record code_env_fingerprint = a33c98202ae1591d but observed 05a4d06e206bb623
```

## Ek B — Custody eşleştirme tablosu

`—` = ayrı expected veya sidecar değeri yok; o sütun için PASS iddiası yok. Standing pin kontrolü hash eşitliğidir; transmission kontrolü sidecar eşitliğini de gerektirir.

| Set / dosya | Expected | Computed | Sidecar | Sonuç |
|---|---|---|---|---|
| transmission / `p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py` | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 | 39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py` | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv` | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | PASS |
| transmission / `p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt5_2026-10-02.md` | 7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9 | 7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9 | 7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9 | PASS |
| transmission / `p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt1_2026-10-02.md` | f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb | f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb | f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb | PASS |
| transmission / `p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt2_2026-10-02.md` | f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4 | f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4 | f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4 | PASS |
| transmission / `p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt3_2026-10-02.md` | 239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a | 239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a | 239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a | PASS |
| transmission / `p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt4_2026-10-02.md` | 49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165 | 49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165 | 49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_telemetry_rp1_2026-10-02.csv` | 836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f | 836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f | 836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_results_rp1_2026-10-02.json` | ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882 | ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882 | ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_residual_series_rp1_2026-10-02.json` | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_test_evidence_rp1_2026-10-02.json` | 809e9d043d136371fafcd158d5955853f61e67490db370d1d56761b7f8e6578d | 809e9d043d136371fafcd158d5955853f61e67490db370d1d56761b7f8e6578d | 809e9d043d136371fafcd158d5955853f61e67490db370d1d56761b7f8e6578d | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1_2026-10-04.md` | dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066 | dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066 | dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066 | PASS |
| transmission / `p_konum_plus/provenance/f3_step2_correction_report_rp1_2026-10-04.md` | bf72d3e5284639972d33cb21ee87e026015fda1dc3e4eb91e85a3a038455159c | bf72d3e5284639972d33cb21ee87e026015fda1dc3e4eb91e85a3a038455159c | bf72d3e5284639972d33cb21ee87e026015fda1dc3e4eb91e85a3a038455159c | PASS |
| transmission / `p_konum_plus/provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md` | a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d | a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d | a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d | PASS |
| transmission / `p_konum_plus/provenance/f3_realdata_prep_rp1_attempt_log_2026-10-04.md` | d015c3cdc505cdf816764633e885605ce2b8c305fabaf4ebe9cf1406e24a458c | d015c3cdc505cdf816764633e885605ce2b8c305fabaf4ebe9cf1406e24a458c | d015c3cdc505cdf816764633e885605ce2b8c305fabaf4ebe9cf1406e24a458c | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv` | 2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084 | 2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084 | 2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_restart_store_manifest_2026-10-02.csv` | ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733 | ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733 | ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_store_read_log_2026-10-02.csv` | 6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1 | 6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1 | 6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv` | 6b98e427a819f0464adf1ca100183905ae51f24de140cc4bd4c1a9bda42d5739 | 6b98e427a819f0464adf1ca100183905ae51f24de140cc4bd4c1a9bda42d5739 | 6b98e427a819f0464adf1ca100183905ae51f24de140cc4bd4c1a9bda42d5739 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv` | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv` | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/SYNTH_FIXTURE_MANIFEST.json` | 63452ff4a8f2ad99820eac509e074fb3c3a2cfb10ea765dd0f310baa6ee387b4 | 63452ff4a8f2ad99820eac509e074fb3c3a2cfb10ea765dd0f310baa6ee387b4 | 63452ff4a8f2ad99820eac509e074fb3c3a2cfb10ea765dd0f310baa6ee387b4 | PASS |
| transmission / `p_konum_plus/provenance/f3_realdata_prep_rp1_c5_observability_statement_2026-10-04.md` | 5d36806b1036c4169870622e73a0f2c78b4c9c943c29c8902e4e83c6cd6a4d3d | 5d36806b1036c4169870622e73a0f2c78b4c9c943c29c8902e4e83c6cd6a4d3d | 5d36806b1036c4169870622e73a0f2c78b4c9c943c29c8902e4e83c6cd6a4d3d | PASS |
| transmission / `p_konum_plus/provenance/f3_realdata_prep_rp1_size_estimate_2026-10-04.md` | 6d8dbe067d54c50e213779e70b30c260def5ac75e516b4bfc5436cca5e9bd541 | 6d8dbe067d54c50e213779e70b30c260def5ac75e516b4bfc5436cca5e9bd541 | 6d8dbe067d54c50e213779e70b30c260def5ac75e516b4bfc5436cca5e9bd541 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch1_stdout_2026-10-02.log` | 445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f | 445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f | 445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch1_stderr_2026-10-02.log` | c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b | c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b | c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch2_stdout_2026-10-02.log` | d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7 | d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7 | d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch2_stderr_2026-10-02.log` | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch3_stdout_2026-10-02.log` | 7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d | 7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d | 7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch3_stderr_2026-10-02.log` | 915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45 | 915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45 | 915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch4_stdout_2026-10-02.log` | c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698 | c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698 | c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_launch4_stderr_2026-10-02.log` | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_launch5_stdout_2026-10-02.log` | cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715 | cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715 | cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715 | PASS |
| transmission / `p_konum_plus/calibration/f3_step2_rp1_launch5_stderr_2026-10-02.log` | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md` | 2357898e6d7314a5b950fc356def73a4e78ce7d27a6e67b863b6041d7784be1b | 2357898e6d7314a5b950fc356def73a4e78ce7d27a6e67b863b6041d7784be1b | 2357898e6d7314a5b950fc356def73a4e78ce7d27a6e67b863b6041d7784be1b | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md` | 029fcc980513e74c142250cb9ccc51051a541af71a9dd9a85364aa705d20ca0c | 029fcc980513e74c142250cb9ccc51051a541af71a9dd9a85364aa705d20ca0c | 029fcc980513e74c142250cb9ccc51051a541af71a9dd9a85364aa705d20ca0c | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md` | 527fd2495bd4642b956ea18b760beca5a1168449cd55214bc7f6b7bb9a49a1d3 | 527fd2495bd4642b956ea18b760beca5a1168449cd55214bc7f6b7bb9a49a1d3 | 527fd2495bd4642b956ea18b760beca5a1168449cd55214bc7f6b7bb9a49a1d3 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md` | 73d9040bb3ed4aaf5d72dda0fd04a6189b11c38e843429e009b4641f3a79e530 | 73d9040bb3ed4aaf5d72dda0fd04a6189b11c38e843429e009b4641f3a79e530 | 73d9040bb3ed4aaf5d72dda0fd04a6189b11c38e843429e009b4641f3a79e530 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py` | 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2 | 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2 | 08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py` | 0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5 | 0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5 | 0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5 | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py` | d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d | d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d | d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d | PASS |
| transmission / `p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py` | 47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561 | 47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561 | 47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561 | PASS |
| transmission / `p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md` | — | 858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9 | 858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9 | PASS |
| standing pins / `p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py` | 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 | 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 | — | PASS |
| standing pins / `p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py` | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d | b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d | — | PASS |
| standing pins / `p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json` | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | PASS |
| standing pins / `p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json` | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | PASS |
| standing pins / `p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json` | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | PASS |
| standing pins / `p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv` | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | PASS |
| standing pins / `p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json` | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | PASS |
| standing pins / `p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md` | a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5 | a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5 | a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5 | PASS |
| standing pins / `p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md` | 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34 | 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34 | 4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34 | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md` | 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 | 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 | 1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3 | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md` | aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae | aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae | aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md` | 9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575 | 9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575 | 9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575 | PASS |
| standing pins / `p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md` | 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0 | 5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0 | — | PASS |
| standing pins / `p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv` | aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac | aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac | — | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md` | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 | da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498 | PASS |
| standing pins / `p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md` | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 | 5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5 | PASS |
| standing pins / `p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md` | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 | e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387 | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md` | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | 0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851 | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md` | 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6 | 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6 | 11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6 | PASS |
| standing pins / `p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md` | 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 | 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 | 283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330 | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md` | a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 | a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 | a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0 | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md` | b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a | b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a | b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md` | 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9 | 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9 | 9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9 | PASS |
| standing pins / `p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md` | d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe | d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe | d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md` | a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb | a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb | a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb | PASS |
| standing pins / `p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md` | ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82 | ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82 | ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82 | PASS |

## Ek C — Start-state inventory bağımsız kontrol

| Dosya | Expected | Computed | Equal |
|---|---|---|---|
| `p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py` | b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 | b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 | True |
| `p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py` | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | True |
| `p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv` | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | True |
| `p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md` | ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e | ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e | True |
| `p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md` | 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1 | 766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1 | True |
| `p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv` | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d | True |
| `p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json` | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba | True |
| `p_konum_plus/calibration/f3_step2_residual_series_r4-2_2026-09-30.json` | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | True |
| `p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json` | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf | True |
| `p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md` | c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c | c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c | True |
| `p_konum_plus/provenance/f3_step2_correction_report_r4-2_2026-09-30.md` | 7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6 | 7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6 | True |
| `p_konum_plus/provenance/f3_step2_r4-2_start_state_inventory_2026-09-30.md` | 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5 | 66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5 | True |
| `p_konum_plus/provenance/f3_step2_r4-2_attempt_log_2026-09-30.md` | b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65 | b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65 | True |
| `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv` | 7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c | 7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c | True |
| `p_konum_plus/calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv` | 1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95 | 1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95 | True |
| `p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv` | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | 0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d | True |
| `p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv` | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | True |
| `p_konum_plus/provenance/f3_step2_r4-2_transmission_list_2026-09-30.md` | 711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606 | 711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606 | True |
| `p_konum_plus/calibration/f3_step2_r4-2_launch1_stdout_2026-09-30.log` | 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 | 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 | True |
| `p_konum_plus/calibration/f3_step2_r4-2_launch1_stderr_2026-09-30.log` | d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 | d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 | True |
| `p_konum_plus/calibration/f3_step2_r4-2_launch2_stdout_2026-09-30.log` | 3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7 | 3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7 | True |
| `p_konum_plus/calibration/f3_step2_r4-2_launch2_stderr_2026-09-30.log` | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613 | True |
| `p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md` | a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe | a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py` | 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 | 9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74 | True |
| `p_konum_plus/quarantine/f3_step2_r4-2_launch1_stdout_2026-09-30.log` | 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 | 5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083 | True |
| `p_konum_plus/quarantine/f3_step2_r4-2_launch1_stderr_2026-09-30.log` | d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 | d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123 | True |
| `p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py` | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f | 4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f | True |
| `p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py` | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | 68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830 | True |
| `p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv` | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe | True |
| `p_konum_plus/provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md` | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d | 3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d | True |
| `p_konum_plus/calibration/f3_step2_telemetry_r4-1_2026-09-29.csv` | 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 | 85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167 | True |
| `p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json` | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | 6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385 | True |
| `p_konum_plus/calibration/f3_step2_residual_series_r4-1_2026-09-29.json` | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | True |
| `p_konum_plus/calibration/f3_step2_test_evidence_r4-1_2026-09-29.json` | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd | f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd | True |
| `p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md` | 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 | 45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671 | True |
| `p_konum_plus/provenance/f3_step2_correction_report_r4-1_2026-09-29.md` | e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e | e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e | True |
| `p_konum_plus/provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md` | fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 | fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2 | True |
| `p_konum_plus/provenance/f3_step2_r4-1_attempt_log_2026-09-29.md` | ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 | ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739 | True |
| `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv` | 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 | 22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88 | True |
| `p_konum_plus/calibration/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv` | cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 | cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1 | True |
| `p_konum_plus/calibration/f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv` | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | 41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a | True |
| `p_konum_plus/calibration/f3_step2_r4-1_run_stdout_2026-09-29.log` | 77120f5be87da8dada1cdad47f7840427922ba212464499950b1263f0747ecf4 | 77120f5be87da8dada1cdad47f7840427922ba212464499950b1263f0747ecf4 | True |
| `p_konum_plus/calibration/f3_step2_r4-1_run_stderr_2026-09-29.log` | 9b678df6d6be6c0b9b5d96d0c358da4ec24debd5a7114a02e60a2f26a4608aa1 | 9b678df6d6be6c0b9b5d96d0c358da4ec24debd5a7114a02e60a2f26a4608aa1 | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md` | 7ff79add1a72219a64a64f73cb5f14160148a120582715e400435ba4434dcab4 | 7ff79add1a72219a64a64f73cb5f14160148a120582715e400435ba4434dcab4 | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md` | e27b29b2ae8746aa7dce2700aa11d942b8ed1f1db429a482845623fee7e9f6e2 | e27b29b2ae8746aa7dce2700aa11d942b8ed1f1db429a482845623fee7e9f6e2 | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md` | 3adbd089c03c8212e56f9c275b5785562a3289e2bf2b4977b71ee1b34473e2aa | 3adbd089c03c8212e56f9c275b5785562a3289e2bf2b4977b71ee1b34473e2aa | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py` | 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 | 280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2 | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_attempt1_stdout_2026-09-29.log` | f0398c8e7350e5eb7a5d6f7168decdeea88da5bdf12be06c9654bb4813c8d546 | f0398c8e7350e5eb7a5d6f7168decdeea88da5bdf12be06c9654bb4813c8d546 | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_attempt1_stderr_2026-09-29.log` | 8fa1cab46ecfc0f92cb2df6301c4cab9a8e4b2079ce1a7fed4e1fb323e171b94 | 8fa1cab46ecfc0f92cb2df6301c4cab9a8e4b2079ce1a7fed4e1fb323e171b94 | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_attempt2_stdout_2026-09-29.log` | 9381d124f61d1435e6d107320e127246798ae23f34d5b01dabadcb48c34fd7cf | 9381d124f61d1435e6d107320e127246798ae23f34d5b01dabadcb48c34fd7cf | True |
| `p_konum_plus/quarantine/f3_step2_r4-1_attempt2_stderr_2026-09-29.log` | 83c1e4a49778cdd973fa40838a7997317cea45e687afeadebba89d22a1a9b253 | 83c1e4a49778cdd973fa40838a7997317cea45e687afeadebba89d22a1a9b253 | True |
| `p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py` | 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c | 54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c | True |
| `p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py.sha256` | e70cd58d63cd00119202ef7c17becfe989a2a1d7067f118c4a798af639bd31e3 | e70cd58d63cd00119202ef7c17becfe989a2a1d7067f118c4a798af639bd31e3 | True |
| `p_konum_plus/calibration/f3_step2_fixture_generator_r4_2026-09-24.py` | 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c | 393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c | True |
| `p_konum_plus/calibration/f3_step2_fixture_generator_r4_2026-09-24.py.sha256` | cf655df0c60b7b88dfc532342cb0f6e5c536b558d40ec557b5f3e2cccbdec51d | cf655df0c60b7b88dfc532342cb0f6e5c536b558d40ec557b5f3e2cccbdec51d | True |
| `p_konum_plus/calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv` | c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 | c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8 | True |
| `p_konum_plus/calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv.sha256` | fec2eadf0c3dbc590cf7691dca4750486fef1778ae2131ae9cbf4a85c5004ed1 | fec2eadf0c3dbc590cf7691dca4750486fef1778ae2131ae9cbf4a85c5004ed1 | True |
| `p_konum_plus/provenance/f3_step2_r4_preexecution_custody_2026-09-24.md` | 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f | 0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f | True |
| `p_konum_plus/provenance/f3_step2_r4_preexecution_custody_2026-09-24.md.sha256` | 8af35f8226f13400184974282d9d10d0904398390c0d7a7f8541650137f68076 | 8af35f8226f13400184974282d9d10d0904398390c0d7a7f8541650137f68076 | True |
| `p_konum_plus/calibration/f3_step2_telemetry_r4_2026-09-24.csv` | 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 | 11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910 | True |
| `p_konum_plus/calibration/f3_step2_telemetry_r4_2026-09-24.csv.sha256` | 61cc185d764c6a4386652f724f94a324b14e735a8fc3dad5cc12ddd04e113b8b | 61cc185d764c6a4386652f724f94a324b14e735a8fc3dad5cc12ddd04e113b8b | True |
| `p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json` | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374 | True |
| `p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json.sha256` | 6d94e20735b065f9ccda216d3adcbb55daba209f04b5caf56bdc4dde4595e527 | 6d94e20735b065f9ccda216d3adcbb55daba209f04b5caf56bdc4dde4595e527 | True |
| `p_konum_plus/calibration/f3_step2_residual_series_r4_2026-09-24.json` | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | 3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f | True |
| `p_konum_plus/calibration/f3_step2_residual_series_r4_2026-09-24.json.sha256` | 2de333210441f033375a8f63f7a2969f164c94b2ebbba7a7688d553907be16f7 | 2de333210441f033375a8f63f7a2969f164c94b2ebbba7a7688d553907be16f7 | True |
| `p_konum_plus/calibration/f3_step2_test_evidence_r4_2026-09-24.json` | 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 | 118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2 | True |
| `p_konum_plus/calibration/f3_step2_test_evidence_r4_2026-09-24.json.sha256` | 8a86e0637b6aa250d728ce5cc537642042757f99c54cf6d2300fe31b80e169e5 | 8a86e0637b6aa250d728ce5cc537642042757f99c54cf6d2300fe31b80e169e5 | True |
| `p_konum_plus/calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md` | 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 | 0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4 | True |
| `p_konum_plus/calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md.sha256` | c559334743875f4aa1d5222d509133c30a9355bbc97b787e5cca8158f417aaca | c559334743875f4aa1d5222d509133c30a9355bbc97b787e5cca8158f417aaca | True |
| `p_konum_plus/provenance/f3_step2_correction_report_r4_2026-09-27.md` | 5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 | 5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848 | True |
| `p_konum_plus/provenance/f3_step2_correction_report_r4_2026-09-27.md.sha256` | 572ddd0bc6abbc5f739d72c2282313c741b9d76d410f455df48e61b39da0b1b9 | 572ddd0bc6abbc5f739d72c2282313c741b9d76d410f455df48e61b39da0b1b9 | True |
| `p_konum_plus/provenance/f3_step2_r4_attempt_log_2026-09-24.md` | 8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 | 8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69 | True |
| `p_konum_plus/provenance/f3_step2_r4_attempt_log_2026-09-24.md.sha256` | d82c3fdc80f069293845e28b43cfeaa2531c90ca3c740fce4967bf588ab54bf3 | d82c3fdc80f069293845e28b43cfeaa2531c90ca3c740fce4967bf588ab54bf3 | True |
| `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv` | d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 | d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5 | True |
| `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv.sha256` | ea9e877f5663d45915832dfc9c91231d06ab631ae083bacbadfde1d67a8d1395 | ea9e877f5663d45915832dfc9c91231d06ab631ae083bacbadfde1d67a8d1395 | True |
| `p_konum_plus/calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv` | f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 | f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1 | True |
| `p_konum_plus/calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv.sha256` | 58458ee9d11d9417131dd66fb13dcb3c99d007c4b3058005ccfcd7420ebc12d0 | 58458ee9d11d9417131dd66fb13dcb3c99d007c4b3058005ccfcd7420ebc12d0 | True |
| `p_konum_plus/calibration/f3_step2_adequacy_harness_r3_2026-09-22.py.sha256` | 756fcf5b466903a812f408f2008676b3f8597acbc63ea2fccc1d30a9b3c1a85b | 756fcf5b466903a812f408f2008676b3f8597acbc63ea2fccc1d30a9b3c1a85b | True |
| `p_konum_plus/calibration/f3_step2_fixture_generator_r3_2026-09-22.py.sha256` | 7761a2f4324384975f5e143c370951f817726cf40af38f3f88d4a34279a598d3 | 7761a2f4324384975f5e143c370951f817726cf40af38f3f88d4a34279a598d3 | True |
| `p_konum_plus/calibration/f3_step2_fixture_manifest_r3_2026-09-22.csv.sha256` | 955f010c3c9c21db66e48dcd2ae19e2bcea2bf0409fbae6e963a36ff63e5b872 | 955f010c3c9c21db66e48dcd2ae19e2bcea2bf0409fbae6e963a36ff63e5b872 | True |
| `p_konum_plus/provenance/f3_step2_r3_preexecution_custody_2026-09-22.md.sha256` | feace2bed9cef15ecc34e164c1c8e56bc704f77a490db85090bcaa2f1518b5f8 | feace2bed9cef15ecc34e164c1c8e56bc704f77a490db85090bcaa2f1518b5f8 | True |
| `p_konum_plus/calibration/f3_step2_telemetry_r3_2026-09-22.csv.sha256` | 8a801fde61fa5e13fc0ec268f39d6d1ff120a9094302d273a92032bf534cff65 | 8a801fde61fa5e13fc0ec268f39d6d1ff120a9094302d273a92032bf534cff65 | True |
| `p_konum_plus/calibration/f3_step2_results_r3_2026-09-22.json.sha256` | 714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35 | 714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35 | True |
| `p_konum_plus/calibration/f3_step2_residual_series_r3_2026-09-22.json.sha256` | 91dd3b85ff1e4ad3a08e231cf32d0c38db1599da1d70847519508721da50d2ee | 91dd3b85ff1e4ad3a08e231cf32d0c38db1599da1d70847519508721da50d2ee | True |
| `p_konum_plus/calibration/f3_step2_test_evidence_r3_2026-09-22.json.sha256` | 5e99371a02ef30024ca32c90c6c254df49578ac01a714797d334669bee0ceb12 | 5e99371a02ef30024ca32c90c6c254df49578ac01a714797d334669bee0ceb12 | True |
| `p_konum_plus/provenance/f3_step2_correction_report_r3_2026-09-24.md.sha256` | 152db9556126c54e67c8cfbc3a144468f7bad5ca7111e15b8550b1d1f8111893 | 152db9556126c54e67c8cfbc3a144468f7bad5ca7111e15b8550b1d1f8111893 | True |
| `p_konum_plus/provenance/f3_step2_r3_start_state_inventory_2026-09-22.md.sha256` | ce2cbe70a5112531a35c673b0f5eacfd35b627b701f291be2990d72267b4e5ea | ce2cbe70a5112531a35c673b0f5eacfd35b627b701f291be2990d72267b4e5ea | True |
| `p_konum_plus/provenance/f3_step2_r3_attempt_log_2026-09-22.md.sha256` | ffc90aabe0de6fb8bb2ac7de3c855032b979ad80122a94927d158e0c292166f1 | ffc90aabe0de6fb8bb2ac7de3c855032b979ad80122a94927d158e0c292166f1 | True |
| `p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r3_2026-09-22.csv.sha256` | 790cf31adb25b33bd8feb82c3cc00046f61470ecf02a499c581b92a4cc7373fe | 790cf31adb25b33bd8feb82c3cc00046f61470ecf02a499c581b92a4cc7373fe | True |
| `p_konum_plus/calibration/f3_step2_r3_restart_store_manifest_2026-09-22.csv.sha256` | d5539e0064f5aa9ce190eec144c64e32e7b858f763358f65a42b8f86747065e9 | d5539e0064f5aa9ce190eec144c64e32e7b858f763358f65a42b8f86747065e9 | True |
| `p_konum_plus/quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md` | 78e6627d94bae3bc7b20f5b6d998b7ff733ea3f37e18fab3b1d58826430a93c9 | 78e6627d94bae3bc7b20f5b6d998b7ff733ea3f37e18fab3b1d58826430a93c9 | True |
| `p_konum_plus/quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md` | 88558b260227aa0830a7bc65be9301f8e70965c6cfcc8901c09985cb02de661c | 88558b260227aa0830a7bc65be9301f8e70965c6cfcc8901c09985cb02de661c | True |
| `p_konum_plus/quarantine/f3_step2_r3_independent_audit_corrections_note_2026-09-23.md` | 9db9079f3fe05944fc25188a423b44ce0a2020baa87a0876465beb505ced985f | 9db9079f3fe05944fc25188a423b44ce0a2020baa87a0876465beb505ced985f | True |
| `p_konum_plus/quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md` | 3a1ad5aa694f52dd15f8e50b689df992f5688715d9f183c706e65b6112dc3470 | 3a1ad5aa694f52dd15f8e50b689df992f5688715d9f183c706e65b6112dc3470 | True |
| `p_konum_plus/quarantine/f3_step2_r3_auditor_transmittal_note_corruption_incident_2026-09-23.md` | 683108f3e6960fc1a4e18bd0f80679624e255dd4520a9b6f7bd2f71a3435fcad | 683108f3e6960fc1a4e18bd0f80679624e255dd4520a9b6f7bd2f71a3435fcad | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py` | 6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31 | 6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31 | True |
| `p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md` | c8d47629ea56e8228a3ac7358ca4c4cd10d339403a32e6a54ed314966f6688bd | c8d47629ea56e8228a3ac7358ca4c4cd10d339403a32e6a54ed314966f6688bd | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py` | 891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd | 891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd | True |
| `p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.md` | a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0 | a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0 | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py` | f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5 | f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5 | True |
| `p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md` | e67bd9d79eed56f78092b460a54a586195ab72703ed937489872935c815d5905 | e67bd9d79eed56f78092b460a54a586195ab72703ed937489872935c815d5905 | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py` | 99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a | 99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a | True |
| `p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md` | 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657 | 2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md` | 0ebaaaeb15afff233758ccb073e71df3840ea0edc7b5fa2df9ae066c8608c4a4 | 0ebaaaeb15afff233758ccb073e71df3840ea0edc7b5fa2df9ae066c8608c4a4 | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py` | f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418 | f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418 | True |
| `p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.md` | 307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441 | 307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md` | 1f1e0e080930be80311ff7a1ff08f75984991a0fb3e05c905ce0b2e5889bf818 | 1f1e0e080930be80311ff7a1ff08f75984991a0fb3e05c905ce0b2e5889bf818 | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py` | 20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306 | 20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306 | True |
| `p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT2_INTERRUPTED.md` | 856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78 | 856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md` | e467d95ffa8995738b2cba45b18322c95c03c1c09a138fce44c8c49843136815 | e467d95ffa8995738b2cba45b18322c95c03c1c09a138fce44c8c49843136815 | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py` | 814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f | 814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f | True |
| `p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.md` | 51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f | 51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md` | 3ba2075f986300486f69f3958a4ed28edce06ac9b13e326b879a03c582d7f831 | 3ba2075f986300486f69f3958a4ed28edce06ac9b13e326b879a03c582d7f831 | True |
| `p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py` | 90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805 | 90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805 | True |
| `p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.md` | cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273 | cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt1_stdout_2026-09-24.log` | 40b3a53d2a4628ce3736585d17ea63aeea93f19a16f0c0e67b7c3e6262fca006 | 40b3a53d2a4628ce3736585d17ea63aeea93f19a16f0c0e67b7c3e6262fca006 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt2_stdout_2026-09-26.log` | 71a0bfd2c1914ff93edd4aec3d3efdec95c318cc7e04ddc8b41ea169ef201dd1 | 71a0bfd2c1914ff93edd4aec3d3efdec95c318cc7e04ddc8b41ea169ef201dd1 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt3_stdout_2026-09-26.log` | fbbcc5e6c7d8c627d6109a3dd93466fc8a229cdd5f0cd33849cc0ef57a7cccef | fbbcc5e6c7d8c627d6109a3dd93466fc8a229cdd5f0cd33849cc0ef57a7cccef | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt4_stdout_2026-09-26.log` | 3b87122312f6d4908fa540d989f728a41ede07b37506a7c0b980b9fe45000328 | 3b87122312f6d4908fa540d989f728a41ede07b37506a7c0b980b9fe45000328 | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt5_stdout_2026-09-26.log` | ca429b22c2920fd91ae86abafd552de0f5f6c7706d7fd37d42c05e337814467e | ca429b22c2920fd91ae86abafd552de0f5f6c7706d7fd37d42c05e337814467e | True |
| `p_konum_plus/quarantine/f3_step2_r4_attempt6_stdout_2026-09-27.log` | 3130cb5f14e0f44abb216c2515a098ddd220c8b16c928b2b1411d79863561d2f | 3130cb5f14e0f44abb216c2515a098ddd220c8b16c928b2b1411d79863561d2f | True |
| `p_konum_plus/quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv` | 7a77da84978577de2483efbe8baa0f98cce6a7d6ca616153e21980ca67b127b1 | 7a77da84978577de2483efbe8baa0f98cce6a7d6ca616153e21980ca67b127b1 | True |
| `p_konum_plus/quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv.sha256` | 9fe259d5d96a05b8e8e6ae3abbda648d23fb3f4b01d07db9ce4fbddd94858896 | 9fe259d5d96a05b8e8e6ae3abbda648d23fb3f4b01d07db9ce4fbddd94858896 | True |

## Ek D — r4-2 → final RP1 tam diff

```diff
--- f3_step2_adequacy_harness_r4-2_2026-09-30.py
+++ rp1
@@ -126,48 +126,77 @@
 # (not just a name), the store is one disclosed, empty-at-first directory,
 # and every stored unit carries the pid/start-time of the process that
 # computed it -- this is what Y-01 corrects relative to r2's layer.
-# r4-2 attempt 2 (D-3 §8.2/§8.3): the restart layer is ACTIVE, introduced
-# after the FIRST genuine interruption of this revision -- attempt 1/launch 1
-# passed every precondition/gate (incl. T-SPL-PENDING-REALPATH in-run) and
-# stopped with no error at "PROGRESS SPL ctx 13 SCEN-A run1:F0:fold1" when
-# the host process exited outside the harness's control; no results and no
-# store unit were written. See
-# quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md.
-# R41A-02(b) was applied AT the transition: the attempt-1 bytes were copied
-# to quarantine BEFORE this edit and the copy equals the custody-named hash
-# (9e4d2803...) -- preserved bytes, not a reconstruction. The r4-2 store is
-# its own directory, EMPTY at attempt 2's first launch; the r4-1 and r4
-# stores stay where they are, untouched and unread (instruction §4).
+# rp1 attempt 5 (T-RP-1 = ACTIVE_FROM_START, D-10 §2; rp1 instruction C-6):
+# the restart layer stays ACTIVE -- for rp1 only, this replaces D-3 §8.3's
+# "Attempt 1 runs without it"; every other §8.3 rule (keys, store,
+# provenance, separation, interruption, check, progress, wording) applies
+# unchanged.
+# Attempt 1 (pid 11116) STOPPED on a genuine code defect in T-NONREG-R4-2's
+# own bookkeeping (3 representation bugs, none scientific); fixed for
+# attempt 2. See quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md.
+# Attempt 2 (pid 13328) RAN TO A CLEAN EXIT 0 but was missing "T-RP-1" from
+# end_state.narrowed_evidence (a delivered-field defect, fixed for attempt 3).
+# See quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md.
+# Attempt 3 (pid 23540, interrupted; resumed as pid 26784) was hit by TWO
+# further defects, both the executor's: (a) the resume reused launch number
+# 3 instead of a new one, so the interrupted process's console output was
+# overwritten -- an R41A-02(c) violation (disclosed, not hidden;
+# computational provenance survives via the store manifest; the
+# interruption itself landed at SPL ctx 22, SCEN-A run1:M0:fold0, mid-write
+# on the P-02 fitter variant -- corrected here from this comment's own
+# earlier "ctx 20", which the attempt-3 quarantine note also still carries
+# uncorrected; see the attempt log's erratum line for the forensic evidence);
+# (b) the resumed process then STOPPED on a genuine logic bug in
+# T-STORE-READ-ACCOUNTING itself: it assumed fit1 always computes fresh,
+# which fails on a resume where fit1's 146 modes were themselves already
+# cached by the interrupted process. Fixed for attempt 4: the test's
+# invariant no longer requires fit1 to write anything; it only requires fit2
+# to be served ALL modes from the store, which holds whether fit1 was a
+# fresh compute or itself a cache hit. See
+# quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md.
+# Attempt 4 (pid 26524) RAN TO A CLEAN EXIT 0 -- T-NONREG-R4-2 passed
+# (s_findings=0, u_findings=0), T-STORE-READ-ACCOUNTING passed cold
+# (fit1_reads=0, served_to_fit2=146), narrowed_evidence correct. The
+# executor then found, by a deliverable-by-deliverable scan against rp1
+# instruction §8 ordered by the PI, that STORE_READ_LOG_PATH (the B'
+# deliverable C-1 names: "a new deliverable lists every read") was declared
+# as a path constant but never written to -- STORE_READ_LOG stayed an
+# in-process list, counted (total_rows) but never persisted as a CSV. A
+# delivered-file omission, same class as attempt 2's narrowed_evidence gap;
+# fixed for attempt 5 by writing the CSV with a row-count assert against
+# total_rows and the fine_counts sum.
+# None of the four defects (attempts 1-4) touched any scientific content
+# (evaluations/stops/canonical/residual/determinism).
+# The rp1 store is its own directory, EMPTY at attempt 5's first launch; the
+# r4-2/r4-1/r4 stores stay where they are, untouched and unread.
 RESTART_LAYER_ACTIVE = True
 
-# r4-2 attempt 2 supersedes the attempt-1 harness AND names the attempt-1
-# custody record's hash (R41A-02(a): supersedes_custody_sha256 filled from
-# attempt 2 on -- the field r4-1 could never fill because its records were
-# overwritten; this revision's per-attempt names preserve them).
-SUPERSEDES_HARNESS_SHA256 = "9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74"
-SUPERSEDES_CUSTODY_SHA256 = "ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e"
-SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md"
-ATTEMPT_NUMBER = 2
+# rp1 attempt 5 supersedes the attempt-4 harness (the STORE_READ_LOG B'
+# deliverable fix).
+SUPERSEDES_HARNESS_SHA256 = "47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561"
+SUPERSEDES_CUSTODY_SHA256 = "49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165"
+SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md"
+ATTEMPT_NUMBER = 5
 # R41A-02(c): every launch writes its OWN stdout/stderr pair with a
 # launch-numbered name; no log file is ever overwritten. The launch number
-# comes from the ENVIRONMENT (F3_R42_LAUNCH, set by the caller alongside the
+# comes from the ENVIRONMENT (F3_RP1_LAUNCH, set by the caller alongside the
 # redirection), NOT from a source constant: a resumed launch of the SAME
 # attempt must not change the harness bytes, or it would change the
 # fingerprint and orphan the attempt's own store units. The value is
 # disclosed in the process block and the attempt log; the caller refuses an
 # existing log pair before starting the process.
-LAUNCH_NUMBER = int(os.environ.get("F3_R42_LAUNCH", "0"))
+LAUNCH_NUMBER = int(os.environ.get("F3_RP1_LAUNCH", "0"))
 # (asserted >= 1 at the top of main(); importing the module for unit tests
 # does not require the variable)
 LAUNCH_STDOUT_PATH = (f"p_konum_plus/calibration/"
-                      f"f3_step2_r4-2_launch{LAUNCH_NUMBER}_stdout_2026-09-30.log")
+                      f"f3_step2_rp1_launch{LAUNCH_NUMBER}_stdout_2026-10-02.log")
 LAUNCH_STDERR_PATH = (f"p_konum_plus/calibration/"
-                      f"f3_step2_r4-2_launch{LAUNCH_NUMBER}_stderr_2026-09-30.log")
+                      f"f3_step2_rp1_launch{LAUNCH_NUMBER}_stderr_2026-10-02.log")
 
 import pickle
 # r4-2's OWN restart store. Created empty only if an interruption activates
 # the restart layer; the r4-1 and r4 stores are never read or moved.
-RESTART_STORE_DIR = "p_konum_plus/calibration/.r4-2_restart_store_2026-09-30"
+RESTART_STORE_DIR = "p_konum_plus/calibration/.rp1_restart_store_2026-10-02"
 _CODE_ENV_FINGERPRINT = [None]     # set once in main(), after W-3 hashes are known
 
 
@@ -197,13 +226,48 @@
     return fp + "__" + name
 
 
+# ---------------- C-2 (rp1): KEY NAMESPACES -------------------------------
+# A pass/test label folded into EVERY key written while the scope is set, so
+# two DIFFERENT computations never share a key (T-KEY-NAMESPACE). The INJ-EXC
+# passes and T-STORE-READ-ACCOUNTING set it; the run labels (run1/run2), the
+# NR-gate and unit-test coarse keys already namespace themselves by name.
+KEY_SCOPE = [""]
+
+# ---------------- C-1 (rp1): STORE-READ ACCOUNTING (R42A-03 (b)) -----------
+# Every ckpt_load HIT is counted by (scope-or-phase, key family, reader pid)
+# and logged with the full key and the pid/start_iso of the WRITER process.
+# A-5 C-31: D-3 §8.3 asks for store reads to be reported at full granularity;
+# r4-2 reported only coarse per-phase counters.
+STORE_READ_LOG = []            # rows of the B' deliverable
+READS_FINE = {}                # (scope_or_phase, family, reader_pid) -> count
+WRITES_THIS_PROCESS = set()    # T-KEY-NAMESPACE: no duplicate write per process
+WRITES_BY_SCOPE = {}           # scope -> set(full keys)   (pass-disjointness)
+
+
+def _key_family(name):
+    """The key family of a unit name (T-KEY-NAMESPACE table rows)."""
+    base = name.split("__", 1)[1] if name.startswith(("excpass", "tstoreread")) else name
+    for fam in ("onestart", "splmode", "realscen", "nrgates_all", "unittests_all"):
+        if base.startswith(fam):
+            return fam
+    return base.split("_", 1)[0]
+
+
 def ckpt_load(name):
     if not RESTART_LAYER_ACTIVE:
         return None
+    name = KEY_SCOPE[0] + name
     p = os.path.join(RESTART_STORE_DIR, _ckpt_safe_name(_full_key(name)) + ".pkl")
     if os.path.exists(p):
         with open(p, "rb") as f:
             payload = pickle.load(f)
+        scope = KEY_SCOPE[0] or (CURRENT_PHASE[0] or "unphased")
+        fam = _key_family(name)
+        READS_FINE[(scope, fam, PID)] = READS_FINE.get((scope, fam, PID), 0) + 1
+        STORE_READ_LOG.append(dict(
+            scope_or_phase=scope, key_family=fam, key=name,
+            writer_pid=payload.get("pid"), writer_start=payload.get("start_iso"),
+            reader_pid=PID, reader_start=PROCESS_START_ISO))
         return payload["value"]
     return None
 
@@ -211,6 +275,15 @@
 def ckpt_save(name, obj):
     if not RESTART_LAYER_ACTIVE:
         return
+    name = KEY_SCOPE[0] + name
+    # T-KEY-NAMESPACE (C-2): two different computations never share a key.
+    # Within ONE process a key is computed at most once (a ckpt_load hit
+    # skips the compute), so a second save of the same key is a namespace
+    # violation, not a legitimate recompute.
+    assert name not in WRITES_THIS_PROCESS, (
+        "T-KEY-NAMESPACE STOP: duplicate write of key %r in one process" % name)
+    WRITES_THIS_PROCESS.add(name)
+    WRITES_BY_SCOPE.setdefault(KEY_SCOPE[0] or "(base)", set()).add(name)
     _restart_store_init()
     p = os.path.join(RESTART_STORE_DIR, _ckpt_safe_name(_full_key(name)) + ".pkl")
     tmp = p + ".tmp"
@@ -225,6 +298,7 @@
     None if not in the store / restart layer inactive."""
     if not RESTART_LAYER_ACTIVE:
         return None
+    name = KEY_SCOPE[0] + name
     p = os.path.join(RESTART_STORE_DIR, _ckpt_safe_name(_full_key(name)) + ".pkl")
     if os.path.exists(p):
         with open(p, "rb") as f:
@@ -262,6 +336,9 @@
     # r4-2 (R41A-01): the real-path routing test and the non-regression
     # check against the r4-1 results are MANDATORY this revision.
     "T-SPL-PENDING-REALPATH", "T-NONREG-R4-1",
+    # rp1 (instruction §4-§5): the C-item tests and the r4-2 non-regression.
+    "T-STORE-READ-ACCOUNTING", "T-KEY-NAMESPACE", "T-F1-LOADER-SYNTH",
+    "T-CONTEXT-ID-UNIQUE", "T-INADMISSIBLE-OBSERVABLE", "T-NONREG-R4-2",
 ]
 
 UNITS_COMPUTED_THIS_PROCESS = {"run1": 0, "run2": 0, "nr_gates": 0, "unit_tests": 0,
@@ -309,23 +386,23 @@
 # r4-2 correction revision inside the r4 cycle (non-retroactivity: every
 # r4-2 deliverable is a NEW file tagged r4-2; nothing under r4 or r4-1 is
 # touched, renamed or moved).
-DATE_TAG = "2026-09-30"
+DATE_TAG = "2026-10-02"
 MANIFEST_PATH = MANIFEST_REUSED_PATH          # reused unchanged (§5 item 3)
 # R41A-02(a): ONE custody file PER ATTEMPT, the name carrying the attempt
 # number, so no custody record is ever overwritten. main() only VERIFIES the
 # record of its own attempt; the external W-3 writer creates it.
 CUSTODY_PATH = (f"p_konum_plus/provenance/"
-                f"f3_step2_r4-2_preexecution_custody_attempt{ATTEMPT_NUMBER}_{DATE_TAG}.md")
-TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_telemetry_r4-2_{DATE_TAG}.csv"
-RESULTS_PATH = f"p_konum_plus/calibration/f3_step2_results_r4-2_{DATE_TAG}.json"
-RESIDUAL_PATH = f"p_konum_plus/calibration/f3_step2_residual_series_r4-2_{DATE_TAG}.json"
-TEST_EVIDENCE_PATH = f"p_konum_plus/calibration/f3_step2_test_evidence_r4-2_{DATE_TAG}.json"
-PERCALL_TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-2_{DATE_TAG}.csv"
-ATTEMPT_LOG_PATH = f"p_konum_plus/provenance/f3_step2_r4-2_attempt_log_{DATE_TAG}.md"
-STORE_MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_r4-2_restart_store_manifest_{DATE_TAG}.csv"
-REGISTER_PATH = f"p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-2_{DATE_TAG}.md"
-NONREG_PATH = f"p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4_{DATE_TAG}.csv"
-NONREG_R41_PATH = f"p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4-1_{DATE_TAG}.csv"
+                f"f3_step2_rp1_preexecution_custody_attempt{ATTEMPT_NUMBER}_{DATE_TAG}.md")
+TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_telemetry_rp1_{DATE_TAG}.csv"
+RESULTS_PATH = f"p_konum_plus/calibration/f3_step2_results_rp1_{DATE_TAG}.json"
+RESIDUAL_PATH = f"p_konum_plus/calibration/f3_step2_residual_series_rp1_{DATE_TAG}.json"
+TEST_EVIDENCE_PATH = f"p_konum_plus/calibration/f3_step2_test_evidence_rp1_{DATE_TAG}.json"
+PERCALL_TELEMETRY_PATH = f"p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1_{DATE_TAG}.csv"
+ATTEMPT_LOG_PATH = f"p_konum_plus/provenance/f3_step2_rp1_attempt_log_{DATE_TAG}.md"
+STORE_MANIFEST_PATH = f"p_konum_plus/calibration/f3_step2_rp1_restart_store_manifest_{DATE_TAG}.csv"
+REGISTER_PATH = f"p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1_{DATE_TAG}.md"
+NONREG_PATH = f"p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4_{DATE_TAG}.csv"
+NONREG_R41_PATH = f"p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-1_{DATE_TAG}.csv"
 # the audited r4 results, for the R4A-01(f) non-regression comparison
 # (read-only, pinned by the start-state inventory)
 R4_RESULTS_PATH = "p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json"
@@ -335,6 +412,55 @@
 # block prints
 R4_1_RESULTS_PATH = "p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json"
 R4_1_RESULTS_HASH = "6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385"
+# --- rp1 (D-9 §2 (a) / rp1 instruction §5): the audited r4-2 results are ---
+# --- THIS cycle's non-regression baseline (T-NONREG-R4-2, classes S/E/U) ---
+R4_2_RESULTS_PATH = "p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json"
+R4_2_RESULTS_HASH = "f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba"
+R4_2_TELEMETRY_PATH = "p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv"
+R4_2_TELEMETRY_HASH = "ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d"
+R4_2_TEST_EVIDENCE_PATH = "p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json"
+R4_2_TEST_EVIDENCE_HASH = "c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf"
+NONREG_R42_PATH = f"p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-2_{DATE_TAG}.csv"
+# C-1: the per-read store log (deliverable B')
+STORE_READ_LOG_PATH = f"p_konum_plus/calibration/f3_step2_rp1_store_read_log_{DATE_TAG}.csv"
+# §5 class E: the expectations manifest, WRITTEN BEFORE THE RUN (external
+# file; the harness only READS it -- an E difference not matching a
+# declaration in this file is a finding)
+EXPECTATIONS_E_PATH = f"p_konum_plus/calibration/f3_step2_rp1_expectations_{DATE_TAG}.json"
+# this cycle's dispatched pin set (rp1 instruction §1 / D-10 §1)
+RP1_INSTRUCTION_PATH = "p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md"
+RP1_INSTRUCTION_HASH = "a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5"
+D10_DISPATCH_RECORD_PATH = "p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md"
+D10_DISPATCH_RECORD_HASH = "4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34"
+D9_PATH = "p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md"
+D9_HASH = "1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3"
+D8_PATH = "p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md"
+D8_HASH = "aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae"
+# A-5, the r4-2 independent audit -- input, not directive
+AUDIT_A5_PATH = "p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md"
+AUDIT_A5_HASH = "9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575"
+# the F1 freeze record -- read for its hash only; never opened for content
+# in rp1 (C-3). The F1 manifest/hash-table constants above are COPIED from
+# its §0/§7, not read from the manifests themselves.
+F1_FREEZE_RECORD_PATH = "p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md"
+F1_FREEZE_RECORD_HASH = "5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0"
+
+# ---------------- C-3: REAL-DATA INPUT PATH -- present, switched OFF --------
+# rp1 instruction C-3 / D-10 S-e = SYNTHETIC_ONLY_IN_RP1. The switch is
+# asserted False at the top of main() in EVERY rp1 launch; with it False no
+# F1 path is opened (the opened-file audit shows it). The F1 paths and hashes
+# below are CONSTANTS COPIED from the F1 freeze record §0/§7
+# (calibration/f1_input_freeze_record_2026-08-28.md, 5eceb198...) -- the
+# files themselves are NEVER read, opened or hash-checked in rp1.
+REAL_DATA_MODE = False
+F1_ELIGIBLE_MANIFEST_PATH = "p_konum_plus/manifests/f1_eligible_trajectory_manifest_2026-08-28.csv"
+F1_ELIGIBLE_MANIFEST_HASH = "8a6034eb6bf57ba65e6ebb0b7409e7d96ec2c482efe19052ac92fca271cdcc32"
+F1_INPUT_HASH_TABLE_PATH = "p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv"
+F1_INPUT_HASH_TABLE_HASH = "aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac"
+F1_ELIGIBLE_ROWS = 906          # F 435 / M 471 (freeze record §0)
+F1_ELIGIBLE_ROWS_F = 435
+F1_ELIGIBLE_ROWS_M = 471
+F1_POST_Z_TOLERANCE = 1e-8      # freeze record §8.2
 
 FORBIDDEN_RESULT_KEYS = ("winner", "selected", "generator_selected")
 
@@ -388,6 +514,11 @@
 # this cycle's own two PI fields, read from D-5 (verbatim)
 S_R2_1 = "PI_RULE"
 T_R2_2 = "AUTHORIZE_RESTART"
+# rp1's own PI field, read from D-10 S2 (T-RP-1): the restart layer is
+# active from attempt 1, replacing D-3 S8.3's "attempt 1 runs without it"
+# for rp1 only. Enters narrowed_evidence BY VALUE, exactly as T-R2-2 does
+# (rp1 instruction C-6; D-3 S5/S8.3).
+T_RP_1 = "ACTIVE_FROM_START"
 # EXACT-03 (S-R2-1 = DEFERRED_THIS_CYCLE, r3) is CLOSED this cycle: D-5 is
 # its source (D-5 S4(d)). Retained as a constant only for cross-referencing
 # the closed finding in the r4 report/register, never as an active tag.
@@ -961,6 +1092,8 @@
         cached_start = ckpt_load(onekey)
         if cached_start is not None:
             canonical, cls, tel = cached_start
+            if family_start_inadmissible_completed(cls):   # rp1 C-5
+                INADMISSIBLE_COMPLETED["family_starts"] += 1
         else:
             with masked_objective(f2m, None if full else obs):
                 canonical, cls, tel, ev = f2m.run_one_start(
@@ -968,6 +1101,8 @@
                     fault_inject_primary=inject_fault,
                     fault_inject_fallback_nonfinite=inject_fault)
             ckpt_save(onekey, (canonical, cls, tel))
+            if family_start_inadmissible_completed(cls):   # rp1 C-5
+                INADMISSIBLE_COMPLETED["family_starts"] += 1
         # X-11(b)/R3A-02, r4: family telemetry rows carry L (the masked
         # objective value of THIS start's endpoint) and the endpoint's
         # frozen predicates/failure codes -- both already computed by F2
@@ -1104,7 +1239,12 @@
         mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)
         cached_mode = ckpt_load(mkey)
         if cached_mode is not None:
-            v, rss, c, src, pst, cap_recs, tel_calls = cached_mode
+            # rp1 C-5: the 8th element carries the mode's report-only
+            # completed-but-not-accepted flag, so a resumed process counts
+            # identically to the one that computed the unit.
+            v, rss, c, src, pst, cap_recs, tel_calls, _inad = cached_mode
+            if _inad:
+                INADMISSIBLE_COMPLETED["spline_modes"] += 1
             for cr in cap_recs:
                 EXC_CAPTURES.append(cr)
                 # ANY unrelated capture (TEST_ONLY included) makes the
@@ -1124,6 +1264,7 @@
             n_calls_before = len(SPLINE_TELEMETRY_CALLS)
             A = spl["amat"](m)
             mode_unrelated = False
+            tel = None
             try:
                 c, tel = spl["solver_config"]("SOLVER-B", x, obs, A)
                 v = spline_valid_from_tel(tel)
@@ -1155,7 +1296,13 @@
             if mode_unrelated:
                 cap_recs = cap_recs + [EXC_CAPTURES[-1]]
             tel_calls = SPLINE_TELEMETRY_CALLS[n_calls_before:]
-            ckpt_save(mkey, (v, rss, c, src, pst, cap_recs, tel_calls))
+            # rp1 C-5 (report-only, existing fields of the frozen drivers'
+            # tel): clean optimizer return not accepted by the frozen rule.
+            _inad = bool(not mode_unrelated
+                         and spline_mode_completed_not_accepted(tel))
+            if _inad:
+                INADMISSIBLE_COMPLETED["spline_modes"] += 1
+            ckpt_save(mkey, (v, rss, c, src, pst, cap_recs, tel_calls, _inad))
         per_mode.append((m, v, rss, c))
         per_mode_valid.append(bool(v))
         # Y-07: real per-call telemetry, not -1/0.0 placeholders, where a
@@ -2567,6 +2714,491 @@
                     "CONTRACT_VIOLATION_INCONSISTENT_U (D-3 Y-03(iii))")
 
 
+# ================= C-3 (rp1): F1 LOADER -- real-data input path ============
+# Implements the F1 frozen pipeline (freeze record 5eceb198..., §8.1 steps
+# 1-11, §8.2 post_z_tolerance = 1e-8) and builds the scenario structure
+# run_real_scenario consumes. REAL_DATA_MODE stays False in every rp1 launch
+# (asserted in main()); in rp1 the loader runs ONLY on generated raw-format
+# files (S-e = SYNTHETIC_ONLY_IN_RP1). Every per-scenario parameter the real
+# path needs and the ratified contract does not name is a STOP, never a
+# choice (rp1 instruction C-3).
+F1_YEAR_MIN, F1_YEAR_MAX = 1880, 2025
+F1_T = F1_YEAR_MAX - F1_YEAR_MIN + 1          # 146, the frozen axis
+
+
+class F1QCFailure(Exception):
+    """A QC failure of the frozen F1 pipeline: the branch name is the
+    message's first token. STOP semantics -- never re-tuned, never imputed."""
+
+
+def f1_verify_raw_files(raw_dir, hash_table_rows):
+    """The LATER-CYCLE gate (C-3): every raw file verified against the hash
+    table, missing or differing => the process ENDS. In rp1 this function is
+    exercised only by T-F1-LOADER-SYNTH on synthetic files with a hash table
+    the test itself builds; the REAL table (aa86f1ea...) is never read."""
+    for fname, expected in hash_table_rows:
+        p = os.path.join(raw_dir, fname)
+        if not os.path.exists(p):
+            raise F1QCFailure("RAW_FILE_MISSING %s" % fname)
+        got = hashlib.sha256(open(p, "rb").read()).hexdigest()
+        if got != expected:
+            raise F1QCFailure("RAW_FILE_HASH_MISMATCH %s %s" % (fname, got))
+    return True
+
+
+def f1_load_raw_dir(raw_dir):
+    """Steps 1-7 of the frozen chain on a directory of yob<year>.txt files
+    (SSA national layout: name,sex,count; names 2-15 chars; count >= 5).
+
+    Returns (shares, denominators): shares[(sex, name)] = list of 146 floats
+    (released-record share per year), only for FULLY eligible trajectories;
+    denominators[(year, sex)] = sum of counts over ALL published names.
+    """
+    years = list(range(F1_YEAR_MIN, F1_YEAR_MAX + 1))
+    counts, published = {}, {}
+    for y in years:
+        p = os.path.join(raw_dir, "yob%d.txt" % y)
+        if not os.path.exists(p):                       # step 1
+            raise F1QCFailure("MISSING_YEAR %d" % y)
+        seen = set()
+        with open(p, "r", encoding="ascii") as f:
+            for ln, line in enumerate(f, 1):
+                line = line.strip()
+                if not line:
+                    continue
+                parts = line.split(",")
+                if len(parts) != 3:                     # step 1
+                    raise F1QCFailure("BAD_FORMAT yob%d.txt line %d" % (y, ln))
+                name, sex, cnt = parts
+                if sex not in ("F", "M") or not (2 <= len(name) <= 15) \
+                        or not cnt.isdigit():           # step 2
+                    raise F1QCFailure("BAD_SEMANTICS yob%d.txt line %d" % (y, ln))
+                c = int(cnt)
+                if c < 5:                               # step 2 (published => count >= 5)
+                    raise F1QCFailure("COUNT_BELOW_PUBLICATION_FLOOR yob%d.txt line %d" % (y, ln))
+                key = (y, sex, name)
+                if key in seen:                         # step 8 (duplicate)
+                    raise F1QCFailure("DUPLICATE_KEY yob%d.txt %s" % (y, name))
+                seen.add(key)
+                counts[key] = c                         # step 3: national-only by construction
+                published.setdefault((sex, name), set()).add(y)
+    # step 4: the 1880-2025 annual index is `years`; step 5-6: FULL support
+    eligible = sorted(k for k, ys in published.items() if len(ys) == F1_T)
+    # step 7: released-record share, denominator = ALL published names of (year, sex)
+    denom = {}
+    for (y, sex, name), c in counts.items():
+        denom[(y, sex)] = denom.get((y, sex), 0) + c
+    shares = {}
+    for sex, name in eligible:
+        shares[(sex, name)] = [
+            _f1_share(counts[(y, sex, name)], denom.get((y, sex), 0), y, sex)
+            for y in years]
+    return shares, denom
+
+
+def _f1_share(count, denominator, year, sex):
+    """Step 7 value + step 8 denominator QC. Unreachable-by-construction from
+    well-formed files (an eligible trajectory's year has a published record,
+    so its denominator is positive); the guard exists for the frozen chain's
+    step-8 contract and T-F1-LOADER-SYNTH exercises it directly."""
+    if denominator <= 0:                                # step 8 (denominator)
+        raise F1QCFailure("ZERO_DENOMINATOR %d %s" % (year, sex))
+    return count / denominator
+
+
+def f1_normalize(shares):
+    """Steps 8-11 on the eligible shares: finite/nonnegative QC, zero-variance
+    QC, row-wise z-normalization (mean, std ddof=0), post-normalization QC
+    with post_z_tolerance = 1e-8 (freeze record §8.2, verbatim checks)."""
+    out = {}
+    for key in sorted(shares):
+        x = np.asarray(shares[key], dtype=float)
+        if not np.all(np.isfinite(x)):                  # step 8 (finite)
+            raise F1QCFailure("NONFINITE_PRE_Z %s_%s" % key)
+        if np.any(x < 0):                               # step 8 (nonnegative)
+            raise F1QCFailure("NEGATIVE_SHARE %s_%s" % key)
+        sd = x.std(ddof=0)
+        if sd == 0.0:                                   # step 9
+            raise F1QCFailure("ZERO_VARIANCE %s_%s" % key)
+        z = (x - x.mean()) / sd                         # step 10
+        f1_post_z_qc(z, "%s_%s" % key)                  # step 11
+        out[key] = z
+    return out
+
+
+def f1_post_z_qc(z, label):
+    """Step 11, the §8.2 literal: finite(z); |mean| <= tol;
+    |std_ddof0 - 1| <= tol; | ||z||_2 - sqrt(146) | <= tol."""
+    tol = F1_POST_Z_TOLERANCE
+    if not np.all(np.isfinite(z)):
+        raise F1QCFailure("NONFINITE_POST_Z %s" % label)
+    if abs(float(np.mean(z))) > tol:
+        raise F1QCFailure("Z_MEAN_QC %s" % label)
+    if abs(float(np.std(z, ddof=0)) - 1.0) > tol:
+        raise F1QCFailure("Z_STD_QC %s" % label)
+    if abs(float(np.linalg.norm(z)) - math.sqrt(len(z))) > tol:
+        raise F1QCFailure("Z_NORM_QC %s" % label)
+    return True
+
+
+def f1_build_scenarios(z_by_traj):
+    """The scenario structure run_real_scenario consumes, from normalized
+    trajectories. Per-scenario parameters NOT chosen here: the start bank,
+    masks, folds and (empty) injection list come from the ratified contract
+    exactly as the synthetic path uses them -- start_bank = "FULL_LATTICE"
+    (the frozen full start lattice), the frozen fold/probe masks, and NO
+    injections on real data. A parameter the contract does not name => STOP
+    (none is known; the assertion documents the rule).
+
+    C-4 (A-5 R42A-09): every (fixture_id, mask_id) is unique per sex,
+    trajectory, family and context -- the mask id carries sex, the
+    per-sex trajectory index AND the trajectory id, so no context can read
+    another context's captures.
+    """
+    strata = {"F": [], "M": []}
+    real_x, mask_ids = {}, {}
+    for (sex, name) in sorted(z_by_traj):
+        ti = len(strata[sex])
+        strata[sex].append(("F1REAL", "%s_%s" % (sex, name), 0.0))
+        real_x[(sex, ti)] = np.asarray(z_by_traj[(sex, name)], dtype=float)
+        mask_ids[(sex, ti)] = "%s%d:%s_%s" % (sex, ti, sex, name)
+    sc = dict(fixture_id="F3-REAL", strata=strata,
+              start_bank="FULL_LATTICE", injections=[],
+              real_x=real_x, real_mask_ids=mask_ids)
+    return [sc]
+
+
+def f1_context_id_table(scenarios):
+    """C-4 / T-CONTEXT-ID-UNIQUE: the dry-constructed list of every
+    (fixture_id, mask_id, family) identity the real mode would fit."""
+    rows = []
+    contexts = (["full"] + ["fold%d" % k for k in range(5)]
+                + ["probeL", "probeR"])
+    for sc in scenarios:
+        for sx in SEXES:
+            for ti in range(len(sc["strata"][sx])):
+                base = sc["real_mask_ids"][(sx, ti)]
+                for fam in ("P-01", "P-02", "SPL"):
+                    for ctx in contexts:
+                        rows.append((sc["fixture_id"],
+                                     "real:%s:%s" % (base, ctx), fam))
+    return rows
+
+
+# ---------------- C-3/C-4 tests: synthetic raw files only (S-e) -------------
+def _synth_raw_write(d, rows_by_year):
+    os.makedirs(d, exist_ok=True)
+    for y, rows in rows_by_year.items():
+        with open(os.path.join(d, "yob%d.txt" % y), "w", encoding="ascii",
+                  newline="\n") as f:
+            for r in rows:
+                f.write("%s,%s,%d\n" % r)
+
+
+def t_f1_loader_synth(out_dir):
+    """T-F1-LOADER-SYNTH (rp1 C-3) -- MANDATORY.
+
+    Raw-format files in the SSA national yob<year>.txt layout, GENERATED from
+    a manifest-declared RNG (PCG64 seed 20261002), small, not resembling or
+    calibrated to any F1 trajectory (v6 L936): synthetic names, counts in
+    [5, 9999]. Exercises every step of §8.1 and every QC failure branch;
+    every expected outcome is written here BEFORE the loader runs. The file
+    hash gate (f1_verify_raw_files) is exercised on a hash table the test
+    builds for its own files -- the real F1 tables are never read (S-e).
+    """
+    rng = np.random.Generator(np.random.PCG64(20261002))
+    years = range(F1_YEAR_MIN, F1_YEAR_MAX + 1)
+    names = [("Zq%02d" % i, sx) for i in range(3) for sx in ("F", "M")]
+    partial = ("Partial", "F")           # misses one year => NOT eligible
+    base = {}
+    for y in years:
+        rows = []
+        for nm, sx in names:
+            rows.append((nm, sx, int(rng.integers(5, 9999))))
+        if y != 1950:
+            rows.append((partial[0], partial[1], int(rng.integers(5, 9999))))
+        base[y] = rows
+    cases, results = [], {}
+
+    def expect(label, build, exc_token):
+        cases.append((label, build, exc_token))
+
+    # happy path -- expected: 6 eligible (3 names x 2 sexes), partial excluded
+    good_dir = os.path.join(out_dir, "good")
+    _synth_raw_write(good_dir, base)
+    shares, denom = f1_load_raw_dir(good_dir)
+    z = f1_normalize(shares)
+    scen = f1_build_scenarios(z)
+    results["eligible_count"] = dict(expected=6, got=len(z),
+                                     ok=len(z) == 6)
+    results["partial_excluded"] = dict(
+        expected=True, got=("F", "Partial") not in z,
+        ok=("F", "Partial") not in z)
+    results["denominator_includes_partial"] = dict(
+        expected=True,
+        got=denom[(1949, "F")] > sum(c for n, s, c in base[1949]
+                                     if s == "F" and n != "Partial") - 1
+            and any(n == "Partial" for n, s, c in base[1949]),
+        ok=True)
+    results["z_qc_pass"] = dict(expected=True,
+                                got=all(f1_post_z_qc(v, "t") for v in z.values()),
+                                ok=True)
+    # gate: correct table passes; a wrong hash ends with RAW_FILE_HASH_MISMATCH
+    table = [("yob%d.txt" % y,
+              hashlib.sha256(open(os.path.join(good_dir, "yob%d.txt" % y),
+                                  "rb").read()).hexdigest()) for y in years]
+    results["gate_pass"] = dict(expected=True,
+                                got=f1_verify_raw_files(good_dir, table),
+                                ok=True)
+    bad_table = [(table[0][0], "0" * 64)] + table[1:]
+    # QC failure branches -- each expected exception token written here first
+    def _drop_year(b):
+        b = dict(b); b.pop(1950); return b
+    def _dup(b):
+        b = dict(b); b[1880] = b[1880] + [b[1880][0]]; return b
+    def _zero_denom(_b):
+        # Unreachable from well-formed files (see _f1_share); the PRODUCT
+        # guard is exercised directly, with the expected token pre-written.
+        _f1_share(5, 0, 2000, "M")
+    def _zero_var(b):
+        b = dict(b)
+        for y in b:
+            fb = [r for r in b[y] if r[1] == "F"]
+            tot = sum(c for _, _, c in fb)
+            b[y] = ([("Cons", "F", tot)]                 # share == 0.5 every year
+                    + [(n, s, c) for n, s, c in b[y] if s != "F"]
+                    + fb)
+        return b
+    def _bad_floor(b):
+        b = dict(b); b[1890] = b[1890] + [("Low", "F", 4)]; return b
+    def _bad_fmt(b):
+        b = dict(b); b[1900] = b[1900] + [("Bad,Extra", "F", 7)]; return b
+    expect("MISSING_YEAR", _drop_year, "MISSING_YEAR")
+    expect("DUPLICATE_KEY", _dup, "DUPLICATE_KEY")
+    expect("ZERO_DENOMINATOR", _zero_denom, "ZERO_DENOMINATOR")
+    expect("ZERO_VARIANCE", _zero_var, "ZERO_VARIANCE")
+    expect("COUNT_BELOW_PUBLICATION_FLOOR", _bad_floor, "COUNT_BELOW_PUBLICATION_FLOOR")
+    expect("BAD_FORMAT", _bad_fmt, "BAD_FORMAT")
+    for label, build, token in cases:
+        d = os.path.join(out_dir, label.lower())
+        try:
+            built = build(base)
+            if built is not None:
+                _synth_raw_write(d, built)
+                s2, _ = f1_load_raw_dir(d)
+                f1_normalize(s2)
+            got = "NO_FAILURE"
+        except F1QCFailure as e:
+            got = str(e).split()[0]
+        results[label] = dict(expected=token, got=got, ok=got == token)
+    # gate failure branch
+    try:
+        f1_verify_raw_files(good_dir, bad_table)
+        got = "NO_FAILURE"
+    except F1QCFailure as e:
+        got = str(e).split()[0]
+    results["RAW_FILE_HASH_MISMATCH"] = dict(
+        expected="RAW_FILE_HASH_MISMATCH", got=got,
+        ok=got == "RAW_FILE_HASH_MISMATCH")
+    # tolerance breach: the step-11 literal, called directly with a z the
+    # branch can see (cannot arise from integer counts without a defect)
+    zbad = np.asarray(z[sorted(z)[0]]) + 1e-6
+    try:
+        f1_post_z_qc(zbad, "tolerance_breach")
+        got = "NO_FAILURE"
+    except F1QCFailure as e:
+        got = str(e).split()[0]
+    results["TOLERANCE_BREACH"] = dict(expected="Z_MEAN_QC", got=got,
+                                       ok=got == "Z_MEAN_QC")
+    results["pass_"] = all(v["ok"] for k, v in results.items()
+                           if isinstance(v, dict))
+    return results, scen
+
+
+def t_context_id_unique(scenarios):
+    """T-CONTEXT-ID-UNIQUE (rp1 C-4) -- MANDATORY: dry construction of the
+    real-mode context identity list on the T-F1-LOADER-SYNTH output; every
+    (fixture_id, mask_id, family) occurs exactly once."""
+    rows = f1_context_id_table(scenarios)
+    unique = len(rows) == len(set(rows))
+    per_traj = 3 * 8                    # 3 families x (full + 5 folds + 2 probes)
+    n_traj = sum(len(sc["strata"][sx]) for sc in scenarios for sx in SEXES)
+    expected_rows = n_traj * per_traj
+    return dict(rows=len(rows), expected_rows=expected_rows,
+                all_unique=unique,
+                pass_=bool(unique and len(rows) == expected_rows))
+
+
+# ================= C-5 (rp1): PI-2 (iii) observability ======================
+# D-8 PI-2 (iii)/(iv). FINDING (the full statement is deliverable G):
+# a refit that COMPLETES NUMERICALLY but is INADMISSIBLE under the frozen
+# taxonomy IS observable from fields the harness already receives.
+#   family side (frozen F2 engine 01714752..., classify_endpoint L256-L320):
+#     numerical completion and admissibility are SEPARATE fields of the
+#     per-start classification the engine returns -- theta_finite (L261-263),
+#     numerically_feasible (L268), no OPTIMIZER_NONCONVERGENCE (L293-294),
+#     objective finite (L296-297) versus scientific_domain_pass (L276-277),
+#     kural_t/kural_s (L277, L286-288) and the MORPHOLOGY_INADMISSIBLE
+#     predicate (L289-291); eligible (L299-305) conjoins them. The event is
+#     cls.eligible == False with predicates == ["MORPHOLOGY_INADMISSIBLE"]
+#     and numerically_feasible == True.
+#   spline side (frozen harness b31e5a6b..., stage drivers L340-L405): the
+#     frozen taxonomy for a spline mode IS the acceptance rule (status in
+#     {1,2} + finite endpoint/objective + constraint residual <= 1e-8;
+#     L137/L142/L157, accept L300-L312). The nearest event -- a clean
+#     optimizer return not accepted by the rule -- is observable from the
+#     tel fields the harness already receives (primary_status,
+#     stage1_accept, stage2_accept, fallback_invoked/fallback_status).
+# The counters below are REPORT-ONLY: they read only those existing fields,
+# change no frozen code, introduce no new classification, and enter no
+# scientific object (results get them in a report-only block). Any such
+# event on real data goes to the PI (D-8 PI-2 (iv)).
+INADMISSIBLE_COMPLETED = {"family_starts": 0, "spline_modes": 0}
+
+
+def family_start_inadmissible_completed(cls):
+    """True iff this per-start classification is 'numerically completed but
+    inadmissible under the frozen taxonomy' -- read ONLY from the fields the
+    frozen engine already returns."""
+    return bool(cls.get("eligible") is False
+                and list(cls.get("predicates", [])) == ["MORPHOLOGY_INADMISSIBLE"]
+                and cls.get("numerically_feasible") is True
+                and cls.get("theta_finite") is True)
+
+
+def spline_mode_completed_not_accepted(tel):
+    """True iff the mode's optimizer returned cleanly (primary_status True)
+    but no stage of the frozen acceptance rule accepted it -- read ONLY from
+    the tel fields the frozen stage drivers already emit."""
+    if not isinstance(tel, dict) or tel.get("primary_status") != "True":
+        return False
+    s1 = tel.get("stage1_accept")
+    s2 = tel.get("stage2_accept")
+    fb = tel.get("fallback_status")
+    accepted = (s1 == "True" or s2 == "True"
+                or tel.get("final_endpoint_source") == "PRIMARY"
+                or fb == "True")
+    return not accepted
+
+
+def t_inadmissible_observable(f2m, grids):
+    """T-INADMISSIBLE-OBSERVABLE (rp1 C-5) -- MANDATORY.
+
+    (a) family: a WITNESS endpoint is sought on the frozen P-01/P-02 start
+        lattices by calling the frozen classify_endpoint directly (no frozen
+        code changed; no optimizer run); the counting predicate must fire on
+        the witness and must NOT fire on an eligible record or on a
+        nonconverged one. If no lattice point classifies as morphology-only-
+        inadmissible, that is reported (not failed) and the predicate cases
+        still bind.
+    (b) spline: the counting predicate on synthetic tel dicts built from the
+        frozen drivers' own vocabulary -- clean-return-not-accepted True;
+        accepted or dirty-return False. Expected outcomes written before the
+        calls.
+    """
+    witness = None
+    for fam in ("P-01", "P-02"):
+        for theta in grids[fam]:
+            cls = f2m.classify_endpoint(theta, fam)
+            if family_start_inadmissible_completed(cls):
+                witness = dict(family=fam,
+                               theta=[float(v) for v in theta],
+                               predicates=cls["predicates"])
+                break
+        if witness:
+            break
+    fam_cases = dict(
+        witness_found=witness is not None,
+        witness=witness,
+        eligible_not_counted=not family_start_inadmissible_completed(
+            dict(eligible=True, predicates=[], numerically_feasible=True,
+                 theta_finite=True)),
+        nonconverged_not_counted=not family_start_inadmissible_completed(
+            dict(eligible=False,
+                 predicates=["MORPHOLOGY_INADMISSIBLE",
+                             "OPTIMIZER_NONCONVERGENCE"],
+                 numerically_feasible=True, theta_finite=True)),
+        infeasible_not_counted=not family_start_inadmissible_completed(
+            dict(eligible=False, predicates=["MORPHOLOGY_INADMISSIBLE"],
+                 numerically_feasible=False, theta_finite=True)),
+    )
+    spl_cases = dict(
+        clean_not_accepted_counted=spline_mode_completed_not_accepted(
+            dict(primary_status="True", stage1_accept="False",
+                 expansion_triggered="True", stage2_accept="False",
+                 fallback_invoked="True", fallback_status="False",
+                 final_endpoint_source="NONE")),
+        accepted_stage1_not_counted=not spline_mode_completed_not_accepted(
+            dict(primary_status="True", stage1_accept="True",
+                 final_endpoint_source="POLISH")),
+        accepted_primary_not_counted=not spline_mode_completed_not_accepted(
+            dict(primary_status="True", final_endpoint_source="PRIMARY")),
+        dirty_return_not_counted=not spline_mode_completed_not_accepted(
+            dict(primary_status="False", stage1_accept="False")),
+    )
+    pass_ = bool(all(v for k, v in fam_cases.items()
+                     if k not in ("witness_found", "witness"))
+                 and all(spl_cases.values()))
+    return dict(family=fam_cases, spline=spl_cases,
+                witness_on_frozen_lattice=fam_cases["witness_found"],
+                pass_=pass_)
+
+
+# ---------------- C-1 (rp1): T-STORE-READ-ACCOUNTING -----------------------
+def t_store_read_accounting(spl):
+    """T-STORE-READ-ACCOUNTING (rp1 C-1) -- MANDATORY.
+
+    Inside the unit-test phase, ONE TEST_ONLY spline context is fitted TWICE
+    with IDENTICAL keys under the active restart layer, in this test's own
+    key namespace ("tstoreread__"). The invariant checked -- robust to BOTH
+    a cold attempt (fit1 computes all T=len(FULL_O) modes fresh) and a
+    resumed attempt (fit1 itself is served from a store an EARLIER process
+    of this same attempt already populated, so fit1 reads instead of
+    writes): fit2 is served EVERY mode from the store, none recomputed --
+    served_to_fit2 == T, every served-row scoped/attributed correctly, and
+    fit2's result identical to fit1's. Whether fit1 itself was a cache hit
+    or a fresh compute (fit1_reads) is reported but not required to be zero,
+    since a resume legitimately makes it nonzero (R3A-06/C-1 provenance
+    still distinguishes the two: writer_pid in each row names whichever
+    process actually computed that mode). The declared re-read of the SAME
+    computation is what C-1 counts; it is legal ONLY inside this namespace
+    (T-KEY-NAMESPACE rule). The test's units stay in the store and in the
+    store manifest.
+    """
+    T_modes = len(FULL_O)
+    gen = sys.modules[GEN_MODULE_NAME]
+    x = gen.make_step("left")           # TEST_CONSTANT input, as INJ-EXC uses
+    _saved = KEY_SCOPE[0]
+    tel = []
+    try:
+        KEY_SCOPE[0] = "tstoreread__"
+        reads_before_fit1 = len(STORE_READ_LOG)
+        fit1 = fit_spline(spl, "T-STORE-READ", x, FULL_O, tel, "tsr:full")
+        fit1_reads = len(STORE_READ_LOG) - reads_before_fit1
+        reads_before_fit2 = len(STORE_READ_LOG)
+        fit2 = fit_spline(spl, "T-STORE-READ", x, FULL_O, tel, "tsr:full")
+        new_rows = STORE_READ_LOG[reads_before_fit2:]
+        served = len(new_rows)
+        rows_ok = all(r["scope_or_phase"] == "tstoreread__"
+                      and r["key_family"] == "splmode"
+                      and r["reader_pid"] == PID
+                      and r["writer_pid"] is not None
+                      for r in new_rows)
+        fine = READS_FINE.get(("tstoreread__", "splmode", PID), 0)
+        same_result = (fit1.get("valid") == fit2.get("valid")
+                       and fit1.get("mode") == fit2.get("mode")
+                       and fit1.get("rss") == fit2.get("rss"))
+    finally:
+        KEY_SCOPE[0] = _saved
+    pass_ = bool(served == T_modes and fine >= served
+                 and rows_ok and same_result)
+    return dict(modes=T_modes, fit1_reads=fit1_reads,
+                resumed_warm_start=(fit1_reads > 0),
+                served_to_fit2=served, fine_counter=fine,
+                per_read_rows_wellformed=rows_ok,
+                fit2_equals_fit1=same_result, pass_=pass_)
+
+
 # ------------------------- Y-04 exception-injection fixtures ---------------
 def run_exc_injection_fixtures(spl):
     """R3A-03, r4: the manifest declares run_scope = both for the INJ-EXC-*
@@ -2575,12 +3207,34 @@
     provides for the real scenarios). Each pass arms and clears its own
     injection state; wrappers are restored by direct reassignment per pass
     (never by stacking another install)."""
-    p1 = _exc_injection_pass(spl)
-    p2 = _exc_injection_pass(spl)
+    # C-2 (i), rp1: each pass runs under its OWN key namespace, so pass 2 is
+    # a SECOND EXECUTION in the same process (under the active layer it can
+    # never be served pass 1's cached mode units) and passes_identical
+    # compares two executions -- in a resumed process too, not only in a
+    # fresh one (A-5 R42A-03, second half).
+    _saved_scope = KEY_SCOPE[0]
+    try:
+        KEY_SCOPE[0] = "excpass1__"
+        p1 = _exc_injection_pass(spl)
+        KEY_SCOPE[0] = "excpass2__"
+        p2 = _exc_injection_pass(spl)
+    finally:
+        KEY_SCOPE[0] = _saved_scope
+    pass_keys_disjoint = not (WRITES_BY_SCOPE.get("excpass1__", set())
+                              & WRITES_BY_SCOPE.get("excpass2__", set()))
     identical = (p1[0] == p2[0])
     out = dict(p1[0])
     out["passes_identical"] = identical
+    out["pass_key_namespaces_disjoint"] = pass_keys_disjoint
     out["pass2"] = p2[0]
+    # T-KEY-NAMESPACE (rp1 C-2(ii), MANDATORY): the rule -- two different
+    # computations never share a key -- checked here on the two INJ-EXC
+    # passes, the one case in this harness where two DIFFERENT executions
+    # of the SAME fixture ids run in one process. The deliverable table
+    # (register row) is built separately from WRITES_BY_SCOPE; this is the
+    # test record for the id itself.
+    record_test("T-KEY-NAMESPACE", pass_keys_disjoint)
+    assert pass_keys_disjoint, "C-2: INJ-EXC pass namespaces overlap"
     assert identical, ("INJ-EXC-* pass1 != pass2: %r vs %r" % (p1[0], p2[0]))
     return out, p1[1] + p2[1]
 
@@ -3000,10 +3654,18 @@
     # R41A-02(c): a run REQUIRES its launch number from the environment; the
     # caller sets F3_R42_LAUNCH and redirects to the matching log pair.
     assert LAUNCH_NUMBER >= 1, (
-        "R41A-02(c) STOP: set F3_R42_LAUNCH to this launch's number (>= 1) "
+        "R41A-02(c) STOP: set F3_RP1_LAUNCH to this launch's number (>= 1) "
         "and redirect stdout/stderr to the matching launch-numbered log pair")
     print("LAUNCH_NUMBER = %d ; logs = %s / %s"
           % (LAUNCH_NUMBER, LAUNCH_STDOUT_PATH, LAUNCH_STDERR_PATH))
+    # C-3 (rp1 instruction §0/§4): the real-data switch MUST be False in
+    # every rp1 launch; rp1 never reads, opens or hash-checks a real SSA/F1
+    # file. Asserted at the very top so a code defect that flips the switch
+    # stops the cycle before any other work.
+    assert REAL_DATA_MODE is False, (
+        "C-3 STOP: REAL_DATA_MODE must stay False in rp1 (S-e = "
+        "SYNTHETIC_ONLY_IN_RP1); real_data_access stays false")
+    print("REAL_DATA_MODE = " + str(REAL_DATA_MODE))
     sys.path.insert(0, "p_konum_plus/calibration")
     genspec = importlib.util.spec_from_file_location(GEN_MODULE_NAME, GEN_PATH)
     gen = importlib.util.module_from_spec(genspec)
@@ -3109,14 +3771,26 @@
             (MANIFEST_REUSED_PATH, MANIFEST_HASH_REUSED, "manifest (reused r4-1)"),
             (R4_1_RESULTS_PATH, R4_1_RESULTS_HASH, "r4-1 results (baseline)"),
             (AUDIT_A2_PATH, AUDIT_A2_HASH, "A-2 (input)"),
-            (AUDIT_A3_PATH, AUDIT_A3_HASH, "A-3 (input)")):
+            (AUDIT_A3_PATH, AUDIT_A3_HASH, "A-3 (input)"),
+            # rp1's own dispatched pin set (rp1 instruction §1 / D-10 §1)
+            (RP1_INSTRUCTION_PATH, RP1_INSTRUCTION_HASH, "rp1 instruction"),
+            (D10_DISPATCH_RECORD_PATH, D10_DISPATCH_RECORD_HASH, "D-10"),
+            (D9_PATH, D9_HASH, "D-9 (QUALIFIED)"),
+            (D8_PATH, D8_HASH, "D-8"),
+            (AUDIT_A5_PATH, AUDIT_A5_HASH, "A-5 (input)"),
+            (R4_2_RESULTS_PATH, R4_2_RESULTS_HASH, "r4-2 results (non-regression baseline)"),
+            (R4_2_TELEMETRY_PATH, R4_2_TELEMETRY_HASH, "r4-2 telemetry"),
+            (R4_2_TEST_EVIDENCE_PATH, R4_2_TEST_EVIDENCE_HASH, "r4-2 test evidence"),
+            (F1_FREEZE_RECORD_PATH, F1_FREEZE_RECORD_HASH, "F1 freeze record")):
         obs_h = sha256_of(ipath)
         assert obs_h == ihash, (
             "P-1..P-4 STOP: %s observed %s != pinned %s" % (iname, obs_h, ihash))
     print("DISPATCH_PRECONDITIONS_P1_P4 = ALL PASS (observed hashes equal pins; "
-          "15 verified: D-3, r4 instruction, D-5, A-1, D-2, r4-1 instruction, "
+          "25 verified: D-3, r4 instruction, D-5, A-1, D-2, r4-1 instruction, "
           "D-6, A-2, A-3, r4-2 instruction, D-7, A-4, reused generator, "
-          "reused manifest, r4-1 results baseline)")
+          "reused manifest, r4-1 results baseline, rp1 instruction, D-10, "
+          "D-9, D-8, A-5, r4-2 results/telemetry/test-evidence baseline, "
+          "F1 freeze record)")
 
     CURRENT_PHASE[0] = "nr_gates"
     gates_cached = ckpt_load("nrgates_all")
@@ -3152,6 +3826,40 @@
     tmfe = t_mask_full_ext(f2m, grids)
     print("T_MASK_FULL_EXT = " + json.dumps(tmfe))
     assert record_test("T-MASK-FULL-EXT", tmfe["pass_"])
+
+    # ---- rp1 C-items: the new mandatory unit tests (before the fixtures) --
+    # C-3 REAL_DATA_MODE is asserted at main() start; S-e: the F1 pipeline is
+    # exercised ONLY on generated raw-format files, written as deliverable F1
+    # with a mini-manifest (RNG seed 20261002 declared there).
+    f1_synth_dir = f"p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_{DATE_TAG}"
+    f1_synth_results, f1_scen = t_f1_loader_synth(f1_synth_dir)
+    print("T_F1_LOADER_SYNTH = " + json.dumps(f1_synth_results, default=str))
+    assert record_test("T-F1-LOADER-SYNTH", f1_synth_results["pass_"]), \
+        "T-F1-LOADER-SYNTH FAIL -> STOP"
+    with open(os.path.join(f1_synth_dir, "SYNTH_FIXTURE_MANIFEST.json"), "w",
+              encoding="ascii", newline="\n") as _f:
+        json.dump(dict(rng="PCG64", seed=20261002,
+                       layout="SSA national yob<year>.txt (name,sex,count)",
+                       note="small synthetic files, not resembling or "
+                            "calibrated to any F1 trajectory (v6 L936); "
+                            "deliverable F1 of the rp1 instruction",
+                       files=sorted(
+                           os.path.relpath(os.path.join(dp, fn), f1_synth_dir).replace("\\", "/")
+                           for dp, dn, fns in os.walk(f1_synth_dir) for fn in fns
+                           if fn != "SYNTH_FIXTURE_MANIFEST.json")),
+                  _f, indent=1, sort_keys=True)
+    ctx_unique = t_context_id_unique(f1_scen)
+    print("T_CONTEXT_ID_UNIQUE = " + json.dumps(ctx_unique))
+    assert record_test("T-CONTEXT-ID-UNIQUE", ctx_unique["pass_"]), \
+        "T-CONTEXT-ID-UNIQUE FAIL -> STOP"
+    inad_obs = t_inadmissible_observable(f2m, grids)
+    print("T_INADMISSIBLE_OBSERVABLE = " + json.dumps(inad_obs, default=str))
+    assert record_test("T-INADMISSIBLE-OBSERVABLE", inad_obs["pass_"]), \
+        "T-INADMISSIBLE-OBSERVABLE FAIL -> STOP"
+    store_read_acct = t_store_read_accounting(spl)
+    print("T_STORE_READ_ACCOUNTING = " + json.dumps(store_read_acct))
+    assert record_test("T-STORE-READ-ACCOUNTING", store_read_acct["pass_"]), \
+        "T-STORE-READ-ACCOUNTING FAIL -> STOP"
 
     # R41A-01(c), r4-2: the real-path routing test. Runs BEFORE the fixtures
     # and before RUN1 so a routing defect stops the cycle early; it restores
@@ -3909,6 +4617,30 @@
     print("STORE_MANIFEST_WRITTEN = %s sha256=%s rows=%d"
           % (STORE_MANIFEST_PATH, store_manifest_hash, len(store_rows)))
 
+    # C-1 (rp1 instruction §4): "a new deliverable lists every read (key
+    # family, key, writer pid, reader pid)" -- the B' deliverable. STORE_READ_LOG
+    # was accumulated by every ckpt_load HIT; this writes it out verbatim.
+    with open(STORE_READ_LOG_PATH, "w", newline="", encoding="ascii") as f:
+        w = csv.writer(f, lineterminator="\n")
+        w.writerow(["scope_or_phase", "key_family", "key", "writer_pid",
+                    "writer_start", "reader_pid", "reader_start"])
+        for row in STORE_READ_LOG:
+            w.writerow([row["scope_or_phase"], row["key_family"], row["key"],
+                        row["writer_pid"], row["writer_start"],
+                        row["reader_pid"], row["reader_start"]])
+    with open(STORE_READ_LOG_PATH, encoding="ascii") as f:
+        store_read_log_csv_rows = sum(1 for _ in f) - 1
+    store_read_log_fine_sum = sum(READS_FINE.values())
+    assert (store_read_log_csv_rows == len(STORE_READ_LOG)
+            == store_read_log_fine_sum), (
+        "T-STORE-READ-LOG STOP: csv rows=%d, STORE_READ_LOG len=%d, "
+        "fine_counts sum=%d -- all three must agree"
+        % (store_read_log_csv_rows, len(STORE_READ_LOG), store_read_log_fine_sum))
+    store_read_log_hash = sha256_of(STORE_READ_LOG_PATH)
+    OPENED_FILES.append(STORE_READ_LOG_PATH)
+    print("STORE_READ_LOG_WRITTEN = %s sha256=%s rows=%d"
+          % (STORE_READ_LOG_PATH, store_read_log_hash, store_read_log_csv_rows))
+
     env = dict(python=platform.python_version(), numpy=np.__version__,
                scipy=scipy.__version__, platform=platform.platform(),
                OMP=os.environ["OMP_NUM_THREADS"],
@@ -4034,15 +4766,18 @@
     print("COVERAGE_DERIVED = %d rows ; downgraded_to_UNCOVERED = %s"
           % (len(coverage_final), json.dumps(derived_downgrades)))
 
-    # R41A-03 (r4-2): the end state must name THIS revision's dispatch record
-    # (D-7), by its OBSERVED hash. Re-read it here rather than reusing the
-    # precondition result, and assert the value written equals the observed
-    # one -- the instruction asks for the check, not just the value.
-    _d7_observed = sha256_of(D7_DISPATCH_RECORD_PATH)
-    assert _d7_observed == D7_DISPATCH_RECORD_HASH, (
-        "R41A-03 STOP: D-7 observed %s != pinned %s"
-        % (_d7_observed, D7_DISPATCH_RECORD_HASH))
-    print("PI_DISPATCH_RECORD (D-7) observed = " + _d7_observed
+    # rp1 instruction §9 (carrying forward R41A-03's rule): the end state
+    # must name THIS cycle's OWN dispatch record -- D-10, by its OBSERVED
+    # hash, not D-7 (r4-2's own record, still checked as a precondition
+    # above since it is historical and read-only). Re-read it here rather
+    # than reusing the precondition result; assert the value written equals
+    # the observed one -- the instruction asks for the check, not just the
+    # value.
+    _d10_observed = sha256_of(D10_DISPATCH_RECORD_PATH)
+    assert _d10_observed == D10_DISPATCH_RECORD_HASH, (
+        "rp1 STOP: D-10 observed %s != pinned %s"
+        % (_d10_observed, D10_DISPATCH_RECORD_HASH))
+    print("PI_DISPATCH_RECORD (D-10) observed = " + _d10_observed
           + " ; S-R2-1 source (D-5) = " + DISPATCH_RECORD_HASH)
 
     results = dict(
@@ -4103,15 +4838,31 @@
                               or "none"),
             detail=expect_result["fails"]),
         tests_run=dict(TESTS_RUN),
+        # rp1 C-items (instruction §4/§8): report-only/diagnostic blocks.
+        store_read_accounting=dict(
+            fine_counts={"%s|%s|%s" % k: v for k, v in READS_FINE.items()},
+            total_rows=len(STORE_READ_LOG),
+            store_read_log_path=STORE_READ_LOG_PATH,
+            store_read_log_sha256=store_read_log_hash,
+            store_read_log_rows=store_read_log_csv_rows),
+        key_namespace_table=sorted(
+            (dict(scope=scope, n_keys=len(keys),
+                 key_families=sorted({_key_family(k) for k in keys}))
+             for scope, keys in WRITES_BY_SCOPE.items()),
+            key=lambda r: r["scope"]),
+        f1_loader_synth=dict(pass_=f1_synth_results["pass_"],
+                             cases={k: v for k, v in f1_synth_results.items()
+                                    if k != "pass_"}),
+        context_id_unique=ctx_unique,
+        inadmissible_observable=inad_obs,
+        inadmissible_completed_counts=dict(INADMISSIBLE_COMPLETED),
         end_state=dict(
-            # R41A-03 (r4-2): the end state names ITS OWN dispatch record.
-            # r4-1 wrote D-5's hash here (the S-R2-1 source), which A-4 found
-            # is not what the instruction asks for. The value below is D-7 as
-            # OBSERVED on disk this run -- not the pinned literal -- and the
-            # assertion just above main()'s end-state block proves the two are
-            # equal. The S-R2-1 source keeps its own field.
-            PI_dispatch_record_hash=_d7_observed,
-            PI_dispatch_record_path=D7_DISPATCH_RECORD_PATH,
+            # rp1 instruction §9: the end state names ITS OWN dispatch record
+            # -- D-10, by its OBSERVED hash (carrying forward R41A-03's rule,
+            # which r4-2 applied to D-7). The S-R2-1 source (D-5) keeps its
+            # own field, as every cycle since r4-1 has kept it.
+            PI_dispatch_record_hash=_d10_observed,
+            PI_dispatch_record_path=D10_DISPATCH_RECORD_PATH,
             S_R2_1_source_dispatch_record_hash=DISPATCH_RECORD_HASH,
             S_R2_1_source_dispatch_record_path=DISPATCH_RECORD_PATH,
             # R3A-11, r4: BOTH fields computed from the test registry --
@@ -4127,7 +4878,13 @@
             mandatory_tests_missing=[t for t in MANDATORY_TESTS
                                      if not TESTS_RUN.get(t, {}).get("ran")],
             deferred_decisions=(["S-R2-1"] if S_R2_1 == "DEFERRED_THIS_CYCLE" else []),
-            narrowed_evidence=(["T-R2-2"] if T_R2_2 == "AUTHORIZE_RESTART" else []),
+            # rp1 instruction C-6: T-RP-1 enters narrowed_evidence BY VALUE,
+            # exactly as T-R2-2 does -- both are simple presence-of-the-PI-
+            # value checks (D-3 S5/S8.3), not a check of whether the layer
+            # was actually exercised this attempt.
+            narrowed_evidence=(
+                (["T-R2-2"] if T_R2_2 == "AUTHORIZE_RESTART" else [])
+                + (["T-RP-1"] if T_RP_1 == "ACTIVE_FROM_START" else [])),
             uncovered_coverage_rows=[r[0] for r in coverage_final
                                      if str(r[3]).startswith("UNCOVERED")],
             # S-R2-1 = PI_RULE (r4): EXACT-03 closed (D-5 S4(d)); open
@@ -4143,17 +4900,251 @@
                               or not six["mandatory_tests_all_run"])
                           else "CORRECTED_PENDING_INDEPENDENT_AUDIT")
     results["end_state"]["F3_STEP2_r4_status"] = f3_step2_r4_status
-    # R41A-03: the value actually written must be the observed D-7 hash, and
+    # rp1 §9: the value actually written must be the observed D-10 hash, and
     # the S-R2-1 source must stand in its own field, never in this one.
-    assert six["PI_dispatch_record_hash"] == sha256_of(D7_DISPATCH_RECORD_PATH), (
-        "R41A-03 STOP: end_state.PI_dispatch_record_hash = %s but D-7 observes %s"
-        % (six["PI_dispatch_record_hash"], sha256_of(D7_DISPATCH_RECORD_PATH)))
+    assert six["PI_dispatch_record_hash"] == sha256_of(D10_DISPATCH_RECORD_PATH), (
+        "rp1 STOP: end_state.PI_dispatch_record_hash = %s but D-10 observes %s"
+        % (six["PI_dispatch_record_hash"], sha256_of(D10_DISPATCH_RECORD_PATH)))
     assert six["S_R2_1_source_dispatch_record_hash"] == DISPATCH_RECORD_HASH
     assert six["PI_dispatch_record_hash"] != six["S_R2_1_source_dispatch_record_hash"], (
-        "R41A-03 STOP: the dispatch record and the S-R2-1 source must be "
-        "distinct records this revision (D-7 vs D-5)")
+        "rp1 STOP: the dispatch record and the S-R2-1 source must be "
+        "distinct records this cycle (D-10 vs D-5)")
     print("END_STATE = " + json.dumps(six, default=str))
     print("F3_STEP2_r4_status = " + f3_step2_r4_status)
+
+    # ================= §5 (rp1): T-NONREG-R4-2 (classes S / E / U) =========
+    # D-9 §2(a) binds the rp1 bytes through non-regression against r4-2,
+    # NO WHITELIST for the SCIENTIFIC fields. Every other field is compared
+    # too and classified: S (must be identical) / E (declared before the
+    # run, in the table below, with its reason) / U (anything else that
+    # differs -- an open finding). EXPECTATIONS_E is a SOURCE CONSTANT, so
+    # it exists before any run reads it -- "declared before the run" is
+    # true by construction, not by file timestamp.
+    CURRENT_PHASE[0] = "nonregression_r4_2"
+    _r42_obs = sha256_of(R4_2_RESULTS_PATH)
+    assert _r42_obs == R4_2_RESULTS_HASH, (
+        "rp1 STOP: r4-2 results observed %s != pinned %s"
+        % (_r42_obs, R4_2_RESULTS_HASH))
+    with open(R4_2_RESULTS_PATH, encoding="utf-8") as _f:
+        _r42_doc = json.load(_f)
+
+    EXPECTATIONS_E = {
+        # top-level or dotted-path prefixes expected to differ, with reasons.
+        # A real diff under one of these prefixes is EXPECTED, not a finding;
+        # a diff found ANYWHERE ELSE is UNEXPECTED (class U).
+        "process": "this process's own identity, timing, paths and "
+                   "C-1/C-6 counters (rp1 instruction S5)",
+        "environment": "recorded as in v6 S8; stated field by field if it "
+                       "differs (D-9 S2(a) binds code AND environment)",
+        "opened_files_declared": "rp1's own file paths",
+        "opened_files_audit_derived": "rp1's own file paths",
+        "tests_run": "rp1 adds T-STORE-READ-ACCOUNTING, T-KEY-NAMESPACE, "
+                    "T-F1-LOADER-SYNTH, T-CONTEXT-ID-UNIQUE, "
+                    "T-INADMISSIBLE-OBSERVABLE, T-NONREG-R4-2 (C-1..C-6 "
+                    "ADDITIONS, rp1 instruction S4)",
+        "store_read_accounting": "C-1 ADDITION (not in r4-2)",
+        "key_namespace_table": "C-2 ADDITION (not in r4-2)",
+        "f1_loader_synth": "C-3 ADDITION (not in r4-2)",
+        "context_id_unique": "C-4 ADDITION (not in r4-2)",
+        "inadmissible_observable": "C-5 ADDITION (not in r4-2)",
+        "inadmissible_completed_counts": "C-5 ADDITION (not in r4-2)",
+        "exc_injection_fixtures.pass_key_namespaces_disjoint": "C-2(i) ADDITION (not in r4-2)",
+        "end_state.PI_dispatch_record_hash": "rp1's own dispatch record is "
+            "D-10, not D-7 (rp1 instruction S9)",
+        "end_state.PI_dispatch_record_path": "rp1's own dispatch record path",
+        "end_state.F3_STEP2_r4_status": "computed fresh from THIS run's test "
+            "registry; expected equal unless a flag changed",
+        "end_state.narrowed_evidence": "rp1 instruction C-6: T-RP-1 enters "
+            "narrowed_evidence by value, exactly as T-R2-2 does; r4-2 (one "
+            "value) vs rp1 (two values) is the expected addition, not a "
+            "scientific change",
+        # these three are computed from TESTS_RUN BEFORE T-NONREG-R4-2
+        # itself is recorded (this very check), so they read stale/false
+        # AT COMPARISON TIME by construction; main() refreshes them
+        # immediately after this test is recorded (before the results file
+        # is written), so the DELIVERED results.json carries the correct,
+        # refreshed values -- only the live comparison here sees the stale
+        # snapshot. Declaring them E here does not change what gets
+        # delivered, only what this check is allowed to treat as expected.
+        "end_state.corrections_complete": "stale at comparison time -- "
+            "T-NONREG-R4-2 (this check) is not yet recorded in TESTS_RUN; "
+            "refreshed immediately after, before the results file is written",
+        "end_state.mandatory_tests_all_run": "stale at comparison time, same reason",
+        "end_state.mandatory_tests_missing": "stale at comparison time, same reason",
+    }
+
+    def _solver_exceptions_content_equal(a_list, b_list):
+        """solver_exceptions: a natural COVERED event reproduces identically
+        under unchanged frozen code+data, but its OWN provenance (pid,
+        start_iso, the traceback's file path -- which names the harness
+        file, different between r4-2 and rp1) legitimately differs every
+        run. Compare with those three fields stripped; a difference in
+        anything else is content, not provenance, and is a real finding."""
+        def strip(rec):
+            return {k: v for k, v in rec.items()
+                    if k not in ("pid", "start_iso", "traceback")}
+        sa = sorted(_cn(strip(r)) for r in (a_list or []))
+        sb = sorted(_cn(strip(r)) for r in (b_list or []))
+        return sa == sb
+
+    def _classify_e(path):
+        for prefix, reason in EXPECTATIONS_E.items():
+            if path == prefix or path.startswith(prefix + "."):
+                return reason
+        return None
+
+    def _diff_one_level(a, b, prefix=""):
+        """Top-level, then one level into dict values: every key present
+        in EITHER side, every leaf compared via canon(). Deliberately not
+        fully recursive beyond one level -- deep scientific content
+        (evaluations/stops) is covered by the S-class check below with its
+        own targeted, per-fixture comparison, which is more informative
+        than a generic deep diff would be."""
+        out = []
+        keys = sorted(set(a) | set(b)) if isinstance(a, dict) and isinstance(b, dict) \
+            else []
+        if not keys:
+            if _cn(a) != _cn(b):
+                out.append((prefix or "(root)", a, b))
+            return out
+        for k in keys:
+            p = "%s.%s" % (prefix, k) if prefix else k
+            av, bv = a.get(k, "<ABSENT>"), b.get(k, "<ABSENT>")
+            if av == "<ABSENT>" or bv == "<ABSENT>":
+                out.append((p, av, bv))
+                continue
+            if isinstance(av, dict) and isinstance(bv, dict) and not prefix:
+                # one level deeper, only from the top (process/environment/
+                # end_state need their sub-fields classified individually)
+                for k2 in sorted(set(av) | set(bv)):
+                    p2 = "%s.%s" % (p, k2)
+                    v2a, v2b = av.get(k2, "<ABSENT>"), bv.get(k2, "<ABSENT>")
+                    if _cn(v2a) != _cn(v2b):
+                        out.append((p2, v2a, v2b))
+            elif _cn(av) != _cn(bv):
+                out.append((p, av, bv))
+        return out
+
+    # S-class: the SCIENTIFIC objects, excluded from the generic diff above
+    # and checked here directly against r4-2, exactly as T-NONREG-R4-1
+    # checked them against r4-1 -- no whitelist, no absorption.
+    _S_KEYS = {"evaluations", "stops", "run1_canonical_sha256",
+              "run2_canonical_sha256", "determinism"}
+    _r42_ev = {e["fixture_id"]: e for e in _r42_doc["evaluations"]}
+    _rp1_ev = {e["fixture_id"]: e for e in evals1}
+    s_findings = []
+    for fid in sorted(set(_r42_ev) | set(_rp1_ev)):
+        a, b = _r42_ev.get(fid), _rp1_ev.get(fid)
+        if a is None or b is None:
+            s_findings.append(dict(path="evaluations.%s" % fid,
+                                   r4_2=_cn(a) if a else "<ABSENT>",
+                                   rp1=_cn(b) if b else "<ABSENT>"))
+            continue
+        changed = sorted(k for k in set(a) | set(b) if _cn(a.get(k)) != _cn(b.get(k)))
+        for k in changed:
+            s_findings.append(dict(path="evaluations.%s.%s" % (fid, k),
+                                   r4_2=_cn(a.get(k)), rp1=_cn(b.get(k))))
+    _r42_stops_cn = sorted(_cn(s) for s in _r42_doc.get("stops", []))
+    _rp1_stops_cn = sorted(_cn(s) for s in stops1)
+    if _r42_stops_cn != _rp1_stops_cn:
+        s_findings.append(dict(path="stops", r4_2=json.dumps(_r42_stops_cn),
+                               rp1=json.dumps(_rp1_stops_cn)))
+    for key, this_val in (("run1_canonical_sha256", h1),
+                          ("run2_canonical_sha256", h2),
+                          ("determinism", h1 == h2)):
+        if _cn(_r42_doc.get(key)) != _cn(this_val):
+            s_findings.append(dict(path=key, r4_2=_cn(_r42_doc.get(key)),
+                                   rp1=_cn(this_val)))
+
+    # E/U-class: generic diff of everything else in the results dict.
+    _results_minus_s = {k: v for k, v in results.items() if k not in _S_KEYS}
+    _r42_minus_s = {k: v for k, v in _r42_doc.items() if k not in _S_KEYS}
+    e_rows, u_findings = [], []
+    for path, a_val, b_val in _diff_one_level(_r42_minus_s, _results_minus_s):
+        if path == "solver_exceptions":
+            # provenance-stripped content check, not a blanket E (see
+            # _solver_exceptions_content_equal): a real content change
+            # still surfaces as a finding even though this path is listed.
+            if _solver_exceptions_content_equal(a_val, b_val):
+                e_rows.append(dict(
+                    path=path, classification="E",
+                    reason="a natural COVERED event's own provenance "
+                           "(pid/start_iso/traceback file path) differs per "
+                           "process; content (fixture/mode/exception/message) "
+                           "verified identical after stripping those fields",
+                    r4_2=_cn(a_val)[:500], rp1=_cn(b_val)[:500]))
+            else:
+                u_findings.append(dict(path=path, r4_2=_cn(a_val)[:500],
+                                       rp1=_cn(b_val)[:500]))
+            continue
+        reason = _classify_e(path)
+        if reason:
+            e_rows.append(dict(path=path, classification="E", reason=reason,
+                               r4_2=_cn(a_val)[:500], rp1=_cn(b_val)[:500]))
+        else:
+            u_findings.append(dict(path=path, r4_2=_cn(a_val)[:500],
+                                   rp1=_cn(b_val)[:500]))
+
+    nonreg42_rows = (
+        [dict(path="evaluations/stops/canonical/determinism (S)",
+             classification="S", reason="scientific, no whitelist",
+             r4_2="", rp1="")] if not s_findings else
+        [dict(path=f["path"], classification="S_FINDING", reason="",
+             r4_2=f["r4_2"][:500], rp1=f["rp1"][:500]) for f in s_findings]
+    ) + e_rows + [dict(path=f["path"], classification="U_FINDING", reason="",
+                       r4_2=f["r4_2"], rp1=f["rp1"]) for f in u_findings]
+
+    nonreg42_ok = bool(not s_findings and not u_findings)
+    print("NONREGRESSION_VS_R4_2 s_findings=%d e_declared=%d u_findings=%d"
+          % (len(s_findings), len(e_rows), len(u_findings)))
+    if s_findings:
+        print("NONREGRESSION_R4_2_S_FINDINGS = " + json.dumps(s_findings, default=str)[:4000])
+    if u_findings:
+        print("NONREGRESSION_R4_2_U_FINDINGS = " + json.dumps(u_findings, default=str)[:4000])
+    with open(NONREG_R42_PATH, "w", encoding="utf-8", newline="") as _f:
+        _w = csv.DictWriter(_f, fieldnames=["path", "classification", "reason", "r4_2", "rp1"])
+        _w.writeheader()
+        for r in nonreg42_rows:
+            _w.writerow(r)
+    OPENED_FILES.append(NONREG_R42_PATH)
+    OPENED_FILES.append(R4_2_RESULTS_PATH)
+    print("NONREGRESSION_R4_2_WRITTEN = " + NONREG_R42_PATH
+          + " sha256=" + sha256_of(NONREG_R42_PATH))
+    results["nonregression_vs_r4_2"] = dict(
+        baseline=R4_2_RESULTS_PATH, baseline_sha256=_r42_obs,
+        s_findings=s_findings, e_declared=len(e_rows), u_findings=u_findings,
+        pass_=nonreg42_ok)
+    assert record_test("T-NONREG-R4-2", nonreg42_ok), (
+        "T-NONREG-R4-2 FAIL vs r4-2 (%s): S findings=%s ; U findings=%s"
+        % (R4_2_RESULTS_HASH, json.dumps(s_findings, default=str)[:2000],
+           json.dumps(u_findings, default=str)[:2000]))
+
+    # T-NONREG-R4-2 is itself on MANDATORY_TESTS, but `results["tests_run"]`
+    # and `end_state`'s mandatory-test fields were computed (inside the
+    # `results = dict(...)` literal above) BEFORE this test was recorded --
+    # refresh them now so the delivered results.json is not stale about its
+    # own non-regression test. Recomputed from TESTS_RUN exactly as they
+    # were the first time (R3A-11: no literal); `six` is the SAME dict
+    # object as results["end_state"], so mutating it updates results too.
+    results["tests_run"] = dict(TESTS_RUN)
+    six["mandatory_tests_all_run"] = all(
+        TESTS_RUN.get(t, {}).get("ran") for t in MANDATORY_TESTS)
+    six["mandatory_tests_missing"] = [
+        t for t in MANDATORY_TESTS if not TESTS_RUN.get(t, {}).get("ran")]
+    six["corrections_complete"] = (
+        all(TESTS_RUN.get(t, {}).get("passed") for t in MANDATORY_TESTS)
+        and len(expect_result["fails"]) == 0)
+    f3_step2_r4_status = ("PARTIAL_PENDING_PI"
+                          if (six["deferred_decisions"] or six["narrowed_evidence"]
+                              or six["uncovered_coverage_rows"] or six["open_findings"]
+                              or not six["corrections_complete"]
+                              or not six["mandatory_tests_all_run"])
+                          else "CORRECTED_PENDING_INDEPENDENT_AUDIT")
+    six["F3_STEP2_r4_status"] = f3_step2_r4_status
+    print("END_STATE (refreshed after T-NONREG-R4-2) = "
+          + json.dumps(six, default=str))
+    print("F3_STEP2_r4_status (refreshed) = " + f3_step2_r4_status)
+
     with open(RESULTS_PATH, "w", encoding="utf-8", newline="\n") as f:
         json.dump(canon(results), f, sort_keys=True, indent=1)
         f.write("\n")
```

## Ek E — attempt4 → final RP1 tam diff

```diff
--- f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py
+++ rp1
@@ -126,7 +126,7 @@
 # (not just a name), the store is one disclosed, empty-at-first directory,
 # and every stored unit carries the pid/start-time of the process that
 # computed it -- this is what Y-01 corrects relative to r2's layer.
-# rp1 attempt 4 (T-RP-1 = ACTIVE_FROM_START, D-10 §2; rp1 instruction C-6):
+# rp1 attempt 5 (T-RP-1 = ACTIVE_FROM_START, D-10 §2; rp1 instruction C-6):
 # the restart layer stays ACTIVE -- for rp1 only, this replaces D-3 §8.3's
 # "Attempt 1 runs without it"; every other §8.3 rule (keys, store,
 # provenance, separation, interruption, check, progress, wording) applies
@@ -137,31 +137,46 @@
 # Attempt 2 (pid 13328) RAN TO A CLEAN EXIT 0 but was missing "T-RP-1" from
 # end_state.narrowed_evidence (a delivered-field defect, fixed for attempt 3).
 # See quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md.
-# Attempt 3 (pid unlogged by executor error, then a resumed process) was hit
-# by TWO further defects, both the executor's: (a) the resume after a
-# genuine interruption at SPL ctx 20 reused launch number 3 instead of a new
-# one, so the interrupted process's console output was overwritten -- an
-# R41A-02(c) violation (disclosed, not hidden; computational provenance
-# survives via the store manifest); (b) the resumed process then STOPPED on
-# a genuine logic bug in T-STORE-READ-ACCOUNTING itself: it assumed fit1
-# always computes fresh, which fails on a resume where fit1's 146 modes were
-# themselves already cached by the interrupted process. Fixed for attempt 4:
-# the test's invariant no longer requires fit1 to write anything; it only
-# requires fit2 to be served ALL modes from the store, which holds whether
-# fit1 was a fresh compute or itself a cache hit. See
+# Attempt 3 (pid 23540, interrupted; resumed as pid 26784) was hit by TWO
+# further defects, both the executor's: (a) the resume reused launch number
+# 3 instead of a new one, so the interrupted process's console output was
+# overwritten -- an R41A-02(c) violation (disclosed, not hidden;
+# computational provenance survives via the store manifest; the
+# interruption itself landed at SPL ctx 22, SCEN-A run1:M0:fold0, mid-write
+# on the P-02 fitter variant -- corrected here from this comment's own
+# earlier "ctx 20", which the attempt-3 quarantine note also still carries
+# uncorrected; see the attempt log's erratum line for the forensic evidence);
+# (b) the resumed process then STOPPED on a genuine logic bug in
+# T-STORE-READ-ACCOUNTING itself: it assumed fit1 always computes fresh,
+# which fails on a resume where fit1's 146 modes were themselves already
+# cached by the interrupted process. Fixed for attempt 4: the test's
+# invariant no longer requires fit1 to write anything; it only requires fit2
+# to be served ALL modes from the store, which holds whether fit1 was a
+# fresh compute or itself a cache hit. See
 # quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md.
-# None of the three defects (attempts 1-3) touched any scientific content
+# Attempt 4 (pid 26524) RAN TO A CLEAN EXIT 0 -- T-NONREG-R4-2 passed
+# (s_findings=0, u_findings=0), T-STORE-READ-ACCOUNTING passed cold
+# (fit1_reads=0, served_to_fit2=146), narrowed_evidence correct. The
+# executor then found, by a deliverable-by-deliverable scan against rp1
+# instruction §8 ordered by the PI, that STORE_READ_LOG_PATH (the B'
+# deliverable C-1 names: "a new deliverable lists every read") was declared
+# as a path constant but never written to -- STORE_READ_LOG stayed an
+# in-process list, counted (total_rows) but never persisted as a CSV. A
+# delivered-file omission, same class as attempt 2's narrowed_evidence gap;
+# fixed for attempt 5 by writing the CSV with a row-count assert against
+# total_rows and the fine_counts sum.
+# None of the four defects (attempts 1-4) touched any scientific content
 # (evaluations/stops/canonical/residual/determinism).
-# The rp1 store is its own directory, EMPTY at attempt 4's first launch; the
+# The rp1 store is its own directory, EMPTY at attempt 5's first launch; the
 # r4-2/r4-1/r4 stores stay where they are, untouched and unread.
 RESTART_LAYER_ACTIVE = True
 
-# rp1 attempt 4 supersedes the attempt-3 harness (the T-STORE-READ-ACCOUNTING
-# resume-robustness fix).
-SUPERSEDES_HARNESS_SHA256 = "d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d"
-SUPERSEDES_CUSTODY_SHA256 = "239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a"
-SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md"
-ATTEMPT_NUMBER = 4
+# rp1 attempt 5 supersedes the attempt-4 harness (the STORE_READ_LOG B'
+# deliverable fix).
+SUPERSEDES_HARNESS_SHA256 = "47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561"
+SUPERSEDES_CUSTODY_SHA256 = "49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165"
+SUPERSEDES_NOTE_PATH = "p_konum_plus/quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md"
+ATTEMPT_NUMBER = 5
 # R41A-02(c): every launch writes its OWN stdout/stderr pair with a
 # launch-numbered name; no log file is ever overwritten. The launch number
 # comes from the ENVIRONMENT (F3_RP1_LAUNCH, set by the caller alongside the
@@ -4602,6 +4617,30 @@
     print("STORE_MANIFEST_WRITTEN = %s sha256=%s rows=%d"
           % (STORE_MANIFEST_PATH, store_manifest_hash, len(store_rows)))
 
+    # C-1 (rp1 instruction §4): "a new deliverable lists every read (key
+    # family, key, writer pid, reader pid)" -- the B' deliverable. STORE_READ_LOG
+    # was accumulated by every ckpt_load HIT; this writes it out verbatim.
+    with open(STORE_READ_LOG_PATH, "w", newline="", encoding="ascii") as f:
+        w = csv.writer(f, lineterminator="\n")
+        w.writerow(["scope_or_phase", "key_family", "key", "writer_pid",
+                    "writer_start", "reader_pid", "reader_start"])
+        for row in STORE_READ_LOG:
+            w.writerow([row["scope_or_phase"], row["key_family"], row["key"],
+                        row["writer_pid"], row["writer_start"],
+                        row["reader_pid"], row["reader_start"]])
+    with open(STORE_READ_LOG_PATH, encoding="ascii") as f:
+        store_read_log_csv_rows = sum(1 for _ in f) - 1
+    store_read_log_fine_sum = sum(READS_FINE.values())
+    assert (store_read_log_csv_rows == len(STORE_READ_LOG)
+            == store_read_log_fine_sum), (
+        "T-STORE-READ-LOG STOP: csv rows=%d, STORE_READ_LOG len=%d, "
+        "fine_counts sum=%d -- all three must agree"
+        % (store_read_log_csv_rows, len(STORE_READ_LOG), store_read_log_fine_sum))
+    store_read_log_hash = sha256_of(STORE_READ_LOG_PATH)
+    OPENED_FILES.append(STORE_READ_LOG_PATH)
+    print("STORE_READ_LOG_WRITTEN = %s sha256=%s rows=%d"
+          % (STORE_READ_LOG_PATH, store_read_log_hash, store_read_log_csv_rows))
+
     env = dict(python=platform.python_version(), numpy=np.__version__,
                scipy=scipy.__version__, platform=platform.platform(),
                OMP=os.environ["OMP_NUM_THREADS"],
@@ -4802,7 +4841,10 @@
         # rp1 C-items (instruction §4/§8): report-only/diagnostic blocks.
         store_read_accounting=dict(
             fine_counts={"%s|%s|%s" % k: v for k, v in READS_FINE.items()},
-            total_rows=len(STORE_READ_LOG)),
+            total_rows=len(STORE_READ_LOG),
+            store_read_log_path=STORE_READ_LOG_PATH,
+            store_read_log_sha256=store_read_log_hash,
+            store_read_log_rows=store_read_log_csv_rows),
         key_namespace_table=sorted(
             (dict(scope=scope, n_keys=len(keys),
                  key_families=sorted({_key_family(k) for k in keys}))
```

## Ek F — Inline EXPECTATIONS_E (19 prefix)

```json
{
  "process": "this process's own identity, timing, paths and C-1/C-6 counters (rp1 instruction S5)",
  "environment": "recorded as in v6 S8; stated field by field if it differs (D-9 S2(a) binds code AND environment)",
  "opened_files_declared": "rp1's own file paths",
  "opened_files_audit_derived": "rp1's own file paths",
  "tests_run": "rp1 adds T-STORE-READ-ACCOUNTING, T-KEY-NAMESPACE, T-F1-LOADER-SYNTH, T-CONTEXT-ID-UNIQUE, T-INADMISSIBLE-OBSERVABLE, T-NONREG-R4-2 (C-1..C-6 ADDITIONS, rp1 instruction S4)",
  "store_read_accounting": "C-1 ADDITION (not in r4-2)",
  "key_namespace_table": "C-2 ADDITION (not in r4-2)",
  "f1_loader_synth": "C-3 ADDITION (not in r4-2)",
  "context_id_unique": "C-4 ADDITION (not in r4-2)",
  "inadmissible_observable": "C-5 ADDITION (not in r4-2)",
  "inadmissible_completed_counts": "C-5 ADDITION (not in r4-2)",
  "exc_injection_fixtures.pass_key_namespaces_disjoint": "C-2(i) ADDITION (not in r4-2)",
  "end_state.PI_dispatch_record_hash": "rp1's own dispatch record is D-10, not D-7 (rp1 instruction S9)",
  "end_state.PI_dispatch_record_path": "rp1's own dispatch record path",
  "end_state.F3_STEP2_r4_status": "computed fresh from THIS run's test registry; expected equal unless a flag changed",
  "end_state.narrowed_evidence": "rp1 instruction C-6: T-RP-1 enters narrowed_evidence by value, exactly as T-R2-2 does; r4-2 (one value) vs rp1 (two values) is the expected addition, not a scientific change",
  "end_state.corrections_complete": "stale at comparison time -- T-NONREG-R4-2 (this check) is not yet recorded in TESTS_RUN; refreshed immediately after, before the results file is written",
  "end_state.mandatory_tests_all_run": "stale at comparison time, same reason",
  "end_state.mandatory_tests_missing": "stale at comparison time, same reason"
}
```

## Ek G — Tam girdi byte-hash çıktısı

`final_checks.py` SHA256 değerini her dosyanın `read_bytes()` değeri üzerinden yeniden hesaplamıştır. 1.212 satır: 1.211 indirilen girdi/sidecar ve yüklenen audit instruction. Sentetik dosyalar bu listede yer alır. Liste bu audit kaydını ve onun sidecar'ını içermez; self-hash yoktur.

## Ek G çıktı — SHA256 ve input path

```text
c646dddeb35d6d6edcbefeff0cd6672e5b5ac30e43889ab9adab2532491d2509  p_konum_plus/calibration/_w3_writer_rp1_tmp.py
5eceb198a04e31643cbf7aae02c381413ad820c5a706a5ca0d6ea31ef80088b0  p_konum_plus/calibration/f1_input_freeze_record_2026-08-28.md
c39fb5198f64a2723014a1f3cb34596fc68685f42a33feb8b3fd9c02d57ce666  p_konum_plus/calibration/f2_d_f2_09_proposed_start_grid_manifest_2026-08-30.csv
2f191f0b0b24d962dfb0356be0daf201810ae9cb85d46b4164907cc43cce91f6  p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_2026-09-02.md
ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43  p_konum_plus/calibration/f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md
01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077  p_konum_plus/calibration/f2_step2_feasibility_harness_r3_2026-09-01.py
b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d  p_konum_plus/calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py
bef216e3ae1769cf92a6406b6e3f3ab77f36116cd2f8fa5a9dec98076762175f  p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md
4a1ff40e9b50afa94661ea00a1565775ea70a28c8e910bc63389db21c2152188  p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_2026-09-05.md.sha256
7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460  p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md
63959f655c39b83776307de319f658bf368b8fd9408239d7fda3aac39d58ea5a  p_konum_plus/calibration/f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md.sha256
5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad  p_konum_plus/calibration/f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md
756fcf5b466903a812f408f2008676b3f8597acbc63ea2fccc1d30a9b3c1a85b  p_konum_plus/calibration/f3_step2_adequacy_harness_r3_2026-09-22.py.sha256
4e0dc8cfb81543eeb95a46c609c5519fe32536f23c0a1433ef76d252b279388f  p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py
87d6e8c8cad8d17f8903179493b207cef1293842cb6e4b0aa136eec56cd1d7d9  p_konum_plus/calibration/f3_step2_adequacy_harness_r4-1_2026-09-29.py.sha256
b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730  p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py
3a0b81f5f042a99830f3ad2bff620c06664c8b9cda9d6650666a8a1466ad4ab7  p_konum_plus/calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py.sha256
54274b4e1edfb13f5a9c2d251f4c5bdc18a99e84a65dee2a3441a44dc698d34c  p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py
e70cd58d63cd00119202ef7c17becfe989a2a1d7067f118c4a798af639bd31e3  p_konum_plus/calibration/f3_step2_adequacy_harness_r4_2026-09-24.py.sha256
39c733a38eb14031b1525d31718488536f75ec1f57a2695c5a2a88744c5d6f09  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py
bfc24bf82b9562b27299e733256d33c93b8c47623b03752d45acb0aa7e9cce3a  p_konum_plus/calibration/f3_step2_adequacy_harness_rp1_2026-10-02.py.sha256
45a10494eb8938a88648e2742602d3599f8da8b05a923f4e98bd9a9ded13c671  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md
318aeff6eb1b5270c5cd8b3719b397ab2cf42eebceabad2a6e0dcfa31ea05e86  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-1_2026-09-29.md.sha256
c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md
44a604bb89bd4b758dd84b4a1913f63df991d73a9f4609c8513a3a157d6d1263  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md.sha256
0eed314c04203c18c137763bde62fea3c559cba89fffcdd269fdcc9dd2effdf4  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md
c559334743875f4aa1d5222d509133c30a9355bbc97b787e5cca8158f417aaca  p_konum_plus/calibration/f3_step2_class_c_pin_register_r4_2026-09-27.md.sha256
dbf25669b464712cdc41e68f00593e4eb2d4a87c643b16e8121f8e584b08e066  p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1_2026-10-04.md
3e0619b2830668b5144c4c5cd358dfaf1630546be1cdeb839bd127d14dd44f7f  p_konum_plus/calibration/f3_step2_class_c_pin_register_rp1_2026-10-04.md.sha256
7761a2f4324384975f5e143c370951f817726cf40af38f3f88d4a34279a598d3  p_konum_plus/calibration/f3_step2_fixture_generator_r3_2026-09-22.py.sha256
68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830  p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py
556eabfafa0eb21187f2090540ed9353ee41368bd0815f9695204ae3052ff6f9  p_konum_plus/calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py.sha256
393917300d2c8929d438fc47fe156c248d1ebfa48c808faa399ad39c35fcaf1c  p_konum_plus/calibration/f3_step2_fixture_generator_r4_2026-09-24.py
cf655df0c60b7b88dfc532342cb0f6e5c536b558d40ec557b5f3e2cccbdec51d  p_konum_plus/calibration/f3_step2_fixture_generator_r4_2026-09-24.py.sha256
955f010c3c9c21db66e48dcd2ae19e2bcea2bf0409fbae6e963a36ff63e5b872  p_konum_plus/calibration/f3_step2_fixture_manifest_r3_2026-09-22.csv.sha256
5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe  p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv
5ac6eb59f9f98d0b21fd7067b8b0d74801ab0ef28fb283167da9f6cbd98df63b  p_konum_plus/calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv.sha256
c0b38cebcddfeded6423f0ca592c322272cf3e8ab0a16836c89a90eb1ffe11f8  p_konum_plus/calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv
fec2eadf0c3dbc590cf7691dca4750486fef1778ae2131ae9cbf4a85c5004ed1  p_konum_plus/calibration/f3_step2_fixture_manifest_r4_2026-09-24.csv.sha256
d5539e0064f5aa9ce190eec144c64e32e7b858f763358f65a42b8f86747065e9  p_konum_plus/calibration/f3_step2_r3_restart_store_manifest_2026-09-22.csv.sha256
41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a  p_konum_plus/calibration/f3_step2_r4-1_nonregression_vs_r4_2026-09-29.csv
cc59cf571ad4ed11930b60fbd9151990d7d927c8b3e245d9b97a0280c93f07d1  p_konum_plus/calibration/f3_step2_r4-1_restart_store_manifest_2026-09-29.csv
9b678df6d6be6c0b9b5d96d0c358da4ec24debd5a7114a02e60a2f26a4608aa1  p_konum_plus/calibration/f3_step2_r4-1_run_stderr_2026-09-29.log
77120f5be87da8dada1cdad47f7840427922ba212464499950b1263f0747ecf4  p_konum_plus/calibration/f3_step2_r4-1_run_stdout_2026-09-29.log
d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123  p_konum_plus/calibration/f3_step2_r4-2_launch1_stderr_2026-09-30.log
89e206d20ac27d08469f39d6092f04ac8074372f9ba6cbe9b5ce69dbb98a4f2f  p_konum_plus/calibration/f3_step2_r4-2_launch1_stderr_2026-09-30.log.sha256
5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083  p_konum_plus/calibration/f3_step2_r4-2_launch1_stdout_2026-09-30.log
07811b64a04315a179ef4af3d70979b0be2a711a80bd18d78bd59d81bd63b084  p_konum_plus/calibration/f3_step2_r4-2_launch1_stdout_2026-09-30.log.sha256
df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613  p_konum_plus/calibration/f3_step2_r4-2_launch2_stderr_2026-09-30.log
96d9f6e0f4c8840ba2f62ad4c3e387518807013c3e3d88ab9f98cf64e38ac385  p_konum_plus/calibration/f3_step2_r4-2_launch2_stderr_2026-09-30.log.sha256
3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7  p_konum_plus/calibration/f3_step2_r4-2_launch2_stdout_2026-09-30.log
11e41d2044d36a89df0420ecc0173b2da8c481b10f1ab5193e788be990b885d5  p_konum_plus/calibration/f3_step2_r4-2_launch2_stdout_2026-09-30.log.sha256
0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d  p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv
6f57e3601e42aea368b3235dcd3988b56314c99667e4e536afe65761ce3eb320  p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4-1_2026-09-30.csv.sha256
41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a  p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv
7692e839983373ebcdfc2a1954d96b5defaf05a0d5453ee595d18ce0952fbfce  p_konum_plus/calibration/f3_step2_r4-2_nonregression_vs_r4_2026-09-30.csv.sha256
1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95  p_konum_plus/calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv
870d207a217a4b46e05e86f3a211c352ed41ba13aa240a9b08038d8a1dcc4115  p_konum_plus/calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv.sha256
f3c923b11942c2605e6d4269918c92fc0384a870f2fc38829891803403d4f1f1  p_konum_plus/calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv
58458ee9d11d9417131dd66fb13dcb3c99d007c4b3058005ccfcd7420ebc12d0  p_konum_plus/calibration/f3_step2_r4_restart_store_manifest_2026-09-24.csv.sha256
91dd3b85ff1e4ad3a08e231cf32d0c38db1599da1d70847519508721da50d2ee  p_konum_plus/calibration/f3_step2_residual_series_r3_2026-09-22.json.sha256
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_r4-1_2026-09-29.json
f43e4a53e7931acb398eabb779f471556b02a468f74eadf8913989d9c1a65f68  p_konum_plus/calibration/f3_step2_residual_series_r4-1_2026-09-29.json.sha256
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_r4-2_2026-09-30.json
5899020be60fc82e3f9b493b925c89cf35da640d3e0d1aa4e301bad9d0c6bb80  p_konum_plus/calibration/f3_step2_residual_series_r4-2_2026-09-30.json.sha256
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_r4_2026-09-24.json
2de333210441f033375a8f63f7a2969f164c94b2ebbba7a7688d553907be16f7  p_konum_plus/calibration/f3_step2_residual_series_r4_2026-09-24.json.sha256
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/calibration/f3_step2_residual_series_rp1_2026-10-02.json
d6b45bada873c26e4a7de00a5a6471ce59bbd30f0a7898e3b749b517f9e072af  p_konum_plus/calibration/f3_step2_residual_series_rp1_2026-10-02.json.sha256
714b5072589bec65f32f2a76f5b49130f4064b73bfd9ce5e9eb68df95570ed35  p_konum_plus/calibration/f3_step2_results_r3_2026-09-22.json.sha256
6dd4185b895d0d26fda47ab3269527232f733ad89c065467c0caa85a125a4385  p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json
a45152e06227f432b672790f735b14fe03e06f6d773d14d39e99991191f39ea8  p_konum_plus/calibration/f3_step2_results_r4-1_2026-09-29.json.sha256
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json
b6ca39cca360a27442d9a70b3bd96aaeae9123420cfa17970a1f3f730e581ae7  p_konum_plus/calibration/f3_step2_results_r4-2_2026-09-30.json.sha256
a15b7efffd1be8f41757a4fe7c91d0e2ec4e31ea6627aae89591c97eaa2f2374  p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json
6d94e20735b065f9ccda216d3adcbb55daba209f04b5caf56bdc4dde4595e527  p_konum_plus/calibration/f3_step2_results_r4_2026-09-24.json.sha256
ce89fdb43a9894e192a2ec0c1e24058a5a40dbcf4ed6183c73bcdfdc396dc882  p_konum_plus/calibration/f3_step2_results_rp1_2026-10-02.json
070d2b7e3f62bdc1578852f125338d29d927d67a9e92d27320874e106ddc9d38  p_konum_plus/calibration/f3_step2_results_rp1_2026-10-02.json.sha256
63452ff4a8f2ad99820eac509e074fb3c3a2cfb10ea765dd0f310baa6ee387b4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/SYNTH_FIXTURE_MANIFEST.json
f19f22a0e117397552fa93dbc89acefe3daf8230aa1f1d485672be73a5675fbc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/SYNTH_FIXTURE_MANIFEST.json.sha256
cb7a3ce1f47026a74a6a3fe0f6946f76c87a7ed1e0e2a09c7e9c39e69b66b115  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1880.txt
2767b4e29cf44ad293ca911671fc8158994a3e0a8ab8adb3e933e9f48b03cc29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1881.txt
f36f3a09c8999ad64575185276335826dad428f0f49a559b57d5efc0527d22d8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1882.txt
7db51d621eb9ca446e4205cb2a766569a8bfce8ca26baefa1628c000a774c6cc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1883.txt
0e5e95a369ec3effbeaa607e07f13d4f5fdb63c05510edcff461ad15cded9146  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1884.txt
96f7074c4779a1faa6733a0c2a636921760304c29111ad85dc4b8a87779b3444  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1885.txt
3da49bab2714080e60ba89a06a8fff6a0364b0770a9786c20d59d845ad1ce44a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1886.txt
6f8e104c5efe1bdbb4f2ae9d5fc062d69b3d915a7ae3816312a4f018064542de  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1887.txt
5fc9e694c1b808dbd3ca0214cda2b0842ed65d5d8799886496fddb47790a952f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1888.txt
169f1f8ae7932043bc97de7d0f08dfe701964be88403e83ab5c83d5a07e62d63  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1889.txt
bcdefc3f00a43805c9805f22a8cac4d52ecb9480bc4491eec9a440ebd144ad25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1890.txt
4f09308d376fed8d7a0e01ba97c1cd60cf12424ed4b860aee255a7b174e64bdd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1891.txt
fb309347045402395cf434fb9c1c1f90f57e85a1fc59f8bbe0228a32a8070945  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1892.txt
18e6c2f649b2a9f25494363b05fae3269771a5b64e81b87927ea2d1837a947fa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1893.txt
9b0bd57c4464cf4c6848690824556d81d16b45c2354ec7d0a09f5966c3142eee  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1894.txt
258edd815fc1b68faf23f569caca14c0f802c8d496d7041bbd4cdfc3ec8ad267  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1895.txt
c81967a7dc39f7a80f4f6b9375a085f5b524ba20e8a7d04c2be484261899ecac  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1896.txt
bd3420605a200b63d8e5c4720d630f9676681409415c6c3ab83fb0cddba90926  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1897.txt
e25413432255b672e75df0ecb4327965c174fcbdfddffa56a4297ef73bd8a5ea  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1898.txt
c3b80523807059594447dbf9725c9bc53306638aa4006b0bf652a79fc657ac72  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1899.txt
11eba289e1abb61780881015e2bf821f5a74f64dbec46c3a2c7ce06bdc0e7aff  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1900.txt
379f0c8e3295649d021447392764b8aa6a7b92a81db6cbc4fc3145a2ef96167c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1901.txt
f1f86e6e4619d34ae4f68189d3adab3962ec9b152efc0ffbeb17c30add8478a7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1902.txt
a07cbe0dc9ffd0f687f17708b3db0072fdc9ae824cee5c9593e6533dd6f3d482  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1903.txt
25ee85082f920e4728f160c48d75ccef9a281d01451769cbe437e7ec0f8bf5b0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1904.txt
8396ca5cb678f82b35d5807ba8171bc2dae834b086121141f0696c2217944d83  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1905.txt
539851ec9f87ef100c88872c62075697ec5858845e0a332a263c4ab217708fd5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1906.txt
199b5dbb5ee00ff607e6ce6b9594b604a12a3464f821f4f4465b7726c0e2868b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1907.txt
5c42cc01139def67c99a05a3a1da8df2fe16f5b13782ae5345d862ae27feca7a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1908.txt
c58e7cb78d8303880b6559ec83b9373a5096234b5d4d4f8fca0947ca199130e3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1909.txt
592a55632eac50a140d6e0e23af9f42b9055fb18c8add95738cd46a040f86944  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1910.txt
68011b45e4a82e67545cffe4cf6fb28db4e9ada4b5ca6ffa83ddd7cb1d1adf1f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1911.txt
a80476a212cab8bedc1bdf393a02c3c92d99448dd027fe12816330f26e11507b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1912.txt
e80413a8185a900dd852321751faa464eac3acffbe0769f6e1d899f73886471a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1913.txt
b8590df4de8beec972036918168de572bcb185f23d34a54fef3e88f0d7a268a6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1914.txt
c993ca0e3e214d13f23b97a04a79f6b9c1466b25fa373e20c750ac6a6ed66ab4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1915.txt
85f7339db04aabe3bdf8632914033eb9e67fe7c58234b8915ee7279a40ac8fd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1916.txt
59dde7eec31676e946481632c9fd897f474f5b72ccb43262e1ea06a089649a06  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1917.txt
cedf9e54f3ce92a0a7c61c712d2aea7ae832bfac3a1be84b90f3568101efaeff  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1918.txt
f8c1aaf8e6b3e3378507e82bd88cb7e525b46202f9199debcd09d764dee5223f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1919.txt
e6feedcdaf6924572e982ff2fac3e23e0d8c6df7a0d44362986d7c03c303d0bf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1920.txt
651b9629b509c9f72815023c7e098df9985158ec8b443c9b0c6451a8d8622204  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1921.txt
6bd21cda71c1942c361c1e55a0422429022703c34bebe68dd9b982664dd3e4f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1922.txt
2c8a4066e97e397698a78fcad8405b27bde5e0e0dd6a54d8c7c81dfabb62b1c9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1923.txt
3b276b53330e14867e42c0ab1057fec5fe0bc353bc62f7a6a7b36061bf6caefa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1924.txt
15d8eed4f7bc1498057055d7148eebcada293a43656a92d05baedf41198645a1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1925.txt
59806c52a9e231c546c17e74074e8a3699f9b13d7dfe05663f92c4ba519608d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1926.txt
9b4b22b5df77f4905744ae9c50607021fc60e3de84b9641698dd2291bc2d5909  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1927.txt
1f5e4b51d44aa77c98906112d6fabd8929336ac4f375a231f839cb253008028e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1928.txt
90888b34197411d350d7b7674c3c11b736bd804e9591f0375298563db3fa47f5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1929.txt
43be7c84fd9d094b5bc7f6007ece10021e779e444435ebf84c3a03f8e149e81e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1930.txt
fe40b81329cb3c8dfc184fc24050781612b292fe147c3c0642cf8fa200474c25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1931.txt
77697ec1483e753c593726f1e014b23c80e14e27d8a1eca9c16ea0ab21595d6e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1932.txt
3be465a4f15414a64ccfa731fd7441531574ff9ba042083891429fdff9a00536  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1933.txt
c112b656c3b0bb7ca7abd3cfbdf31ab1b1592ef3e2a42986bbb980947026c522  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1934.txt
11630dc298ba066540a2533c6baa34ff8a13b532dbef6d83bf697a6e1f69a77e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1935.txt
e0a4a1fa63c68d55bb0073485df50ea7d4c05cf9367d3a9352c9cbc8f6ddb2b4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1936.txt
c6b4dcfbc4727a8c7090270216d236fb3a6e6b18d07c3591dc6508f0c5ef48bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1937.txt
088d968d9a902251f0bf97c52eba8ce8fed687490907e09848e7a25eb837029d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1938.txt
a96ae6bee42afb7f94c0bbe8dd2a60efeb0b7cc14a96bea19631891b4e6f589c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1939.txt
e2325866576528ac9d7ee8c241951e4a9e17625825780d3081e61b25c898288f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1940.txt
2b55348f6322b9f4217a074e9df28849077b45073fbc07466664226955006950  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1941.txt
f06a37c541cb4c983211f7c6b31d64d1670afbdabb23d71b890987b70c7cc8f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1942.txt
0bdecee171c9755340c2c44d625b51778df031c4644dc75b24bff181d5b9c0be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1943.txt
222ff999cd78f738b32fc14c42d03e619b9062360d5daa29e1e501652e8243d2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1944.txt
873743c7461b1166d9d51286bc2cab56ae913ca3f4f5392f34a718ac5a36705f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1945.txt
ce7d70109aa3717d8b8666baceead357d7724f126034cea1a38ddd09660e1b59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1946.txt
01382b8ea79d81e61967217f394fdc9e1f8f90a086ff5a3108ee3b1771ef42e4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1947.txt
3129980e40fef4abdd2102d43504d5510612be961e0ecbc8fc3de76a6ec39d8b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1948.txt
e7348aebd9d777c26e43f4db335482682b3544b831dca8bb9d106ec6c5f3cba8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1949.txt
83f41e6d750885749fc06c0be24608dfcab357ab4e650b3b58744f2dca85e9f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1950.txt
0314c972de4bbe426fff5fec598ae72e74d3c515570b43f62098e189122282e2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1951.txt
48ac50c973cd6f5ea980a1da3a9c425070dfa73295797c7876aa31e8d5244948  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1952.txt
8d10084b351da3b69c3323baf795b2b1f33bb737b7bbb1ce68e890c4850b330a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1953.txt
5d7e87904883fa7eece2159d45959413af0f25d22e181881dae99709e3249d2e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1954.txt
6ffbeac91ff340f1158678dd9b0879ef9edad9b69cdeff9f370f778183fe7715  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1955.txt
58e525fe9e5005c4059ef47dc6ce4206dba5e2284b3f66d864c34ed4b0af8e4b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1956.txt
99c4beab08cbf6e9d759dd32a4a924d2dda3a36f870fc86d31104c086ebdd95b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1957.txt
fef8b6bbe15685eb520099a20c5835ffdd41c21724ddfc7b787645975b53c5e6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1958.txt
ce6e48423941728b38771974a4dc319188a54c0a8c182c122fb284eb587f06f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1959.txt
5d798b8f8b831b05572cfb29665ff6622eda6334c65c1feac3e502460ab4a3d1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1960.txt
e13ba9227e5faad0cd8f6c6ea008acbd860b2f0ca0fde79458ba209afac31c6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1961.txt
588e243589063e33ae62e70345bdcce53f6080bfec557a7079435f4449f5df8d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1962.txt
a43cbf9d230bb14bc9c07cf31da9771d837f0f2e7740b692e754202138602292  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1963.txt
4d1ac0f733e486f0d9831bb5962f96bbc0dc0b2152beb0eebbbec6e5f621fc07  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1964.txt
2c080acdf262c86cadc1fca4e7f4bf283cda2fd5ac98ecfa7eb4e0570724f625  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1965.txt
221e083f18e0fc4458f04ddfca4356df2a1b615d43eeb7055b3825fb2e828532  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1966.txt
c01062053898c8607ff02cb6d1ca0f9f047f854682066da6c752a64186e0dde4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1967.txt
7de7e5143f13d11f43ce2edd247a1b2f4ac7940f664b2ef82a3a6393528f5398  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1968.txt
04c2f34e65a44612ea9115ca439c8102d570a4efa99f5204f31fcb327b51bcd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1969.txt
1203ba2af4849868f94097e7811b00d8ecbf1795d62ea1486c1875545d42fc1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1970.txt
23932d730a52b949fa2a99e8c890fd68a44df68e245afd70fb76a163c2905822  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1971.txt
3c032b417f47882876b7a7af8a2c82bd9c2ce017c461f3d6c53813644e1c8924  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1972.txt
30ba20505223fef751e07a04cd83a8af9b97c20bd7bb38a9b37e93a3f865360e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1973.txt
f670e0604f047964f9a841ed17ad12f7c0603d0ec787a6fddee8129c9e633775  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1974.txt
eeb82418e71e619d3c6b6273f48036e9c6ab331f16c34cdfae3d7aa390d78c5b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1975.txt
24de081630e23114460293e1902ec97005e834c7ad4ae18049c5d2053ce6bf6f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1976.txt
8dcd066b5b142da9c4622311b533f4de6d3caa25f718b6cccb72bb4eb9dbdfbe  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1977.txt
6dfd1173c3195781210dc36754efbd847df2a869a453061e4a19fca421371b69  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1978.txt
7c2767f7a7de9ee667a01c455448e15f72a95875635c2c30f000274cea94dfb5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1979.txt
4402235a2f5856ee17a87f9163e03e67fd39135e0599904daa4b430b76be4f7b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1980.txt
c5e147f58595ae89099072a603d951ed594acc750bd81259dec98857918e2226  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1981.txt
56f749aa66c05e2de0a1c3f6d3f326b1573ae201cd38e691bafa8227e6e1c569  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1982.txt
af1dbf3ba56f4498098dd646a7002ce3af1a55a1d39e6997f41d9777f021071f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1983.txt
67e4efd8599fbc057034d879f6e06501249089b68e41b6acd144062bed3c713f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1984.txt
39626600b28ac2255ea66d1aafed278cfad3cbefc8e59b65530f68c86a7e534a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1985.txt
f918e85cb6ed0d7b3b5e22b8c92577daddf4509b73d31edb94e9627ca5f63f1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1986.txt
f9dfe77978d0e450d6d41f3c1b5364a64f21747fbbf2bc91fab0f95ce2f8a682  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1987.txt
5a9bf4d9e292efa67ca32cd0d1726e44afd4fe34ba09d491c48a5cb6d7cb42d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1988.txt
fa9de45e5b48b665c70b06ba3ea60b1a8b61e0cb5c23cab07f6451a52e57ad6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1989.txt
7a0026591d9eece5a75fa44ff66dd59eab6b6450c691065a652220dfd2e64bbb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1990.txt
31b0507aeba51f2fccc14f653940c291c8cf25a063601cc75b763e630bb29d2a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1991.txt
b289ec613b3b6489e0ad8bbc20382142870f93da84d6e8f91caf0490d028d7a8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1992.txt
897fe71a1207b1ef4dc61a2776a0c1ba673b3fd1647a8a54e4dd000d00962571  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1993.txt
7de8d30d147b6da8e3d172468349d5ea7a0d1efbe91864398b4409f054fd3ed0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1994.txt
016ddc544a51b0ba501e2a095c92995baf24322d0743b5e08ee9451fb1917f24  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1995.txt
674686f6551d5c634d9e7e8663362fd1454a712f3648a330bf57e6592591ed29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1996.txt
880227b6f3f4f4c6571a459163ba2a62d99c27e4b0ce51b3eec1e2c0201feb1d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1997.txt
678b608eb118f94dce9a3ff21a599b3d062c677511de489c2fca312d9efa1df6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1998.txt
4e833b423c65795446280dbaf968e50e402089474d57bafd53b7f7fac5591a37  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob1999.txt
cb55e7524f97d6d8d904f96d02aa07d5d270ec86c26eb052e045f0e7e716e44e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2000.txt
67e6e70b68b434f45944e9e955da29fe7ad3a2951c79fe6d5d676f2af0152e7e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2001.txt
8c454ebdd41d3cf2fcec8995abd6bd2c90f7ad29790c3e7a52b65f914d18032a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2002.txt
f8efac19c208bdbb4b614a3811a04fdcf5d769894ea528682492db2de7b211a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2003.txt
7f63575f4122896b5847ec3311480e22d7e250a3926ede4aa710c7d9849266bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2004.txt
fec80e345a4d70a56dc391a3ce84b4010901d7d9cf44049c696d4cf3e5765dce  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2005.txt
9280d2cdcbdb57eb6b6b55a24c5f5baf8db45a1f3f4e16f5feb826fa46d1dedf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2006.txt
78b8dd1f9b9f5dd476921bb8b413e997d1f75062827e96cee1b23e2a3e1432aa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2007.txt
5a18ab8a52caccb661232439d01e1d4ba43db77d3b539bd60790a36f7aeaabbd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2008.txt
6a73ef384d30bc18611038e3c884d70d5dd6e14067111a4288715b7636611e5d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2009.txt
94c27249389f0f014b13a481bd5eea357f4d152fb184fffd3fafeb813ad4546f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2010.txt
8ce48e1bf90aa9c7a39e5eefcc9ef32dec5d63fdf858625036d5b0f76795a2eb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2011.txt
18c927510aad45770129f74dba7241f158be1572ad69848a3ebd6989d24c2aec  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2012.txt
363e608862b9509b774a3680fe23693a929bcec8b19b670692335686c600187e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2013.txt
a0f47598fdd1377b19025a6d70cd90ca2f0becf0335dc7d1e5bcf8b7a2a66a91  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2014.txt
d7d8dc754642dd25013051181aeb87ee87ad4f110689101c32c04556cc191bd1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2015.txt
04476e1860f28cd6c5956f1a3cf763402c91e818b98a6b969b3ce878e45b530a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2016.txt
c76d674b4800a93bcee4598ef8111a17b4a68d09260012bbfbc5c5a99f858653  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2017.txt
ec2bdadedaf23ae105cf1274b90288cc42f97c3959be7ae32550710e4d3eee74  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2018.txt
3e8c9f819ca782ce053252030479ad454faeff3679296d542827b66b38dac9f3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2019.txt
0cdb7f3199632d58e9e132706f044f2896deebf04c7fab9b8354334c9beced59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2020.txt
e6c581afaa821984152eaf82757483ca2dc0b6b1d8c091665d961b33a1e3dd92  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2021.txt
b961e6e6bde668f9fab0badc0fcdccc4afeaf4fb66725afb2e5840310e5b2c56  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2022.txt
5c1345ad246cb13a5521aced224d407a4ce704286d8b7af786ac48ab0fe13d00  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2023.txt
f25111d4bdf7fc6844ea54ec73a3dabb83d29310795429c8f9e936f7b35a0650  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2024.txt
7dcd38c9f6629b15a0f85213d24a949cee29b0fe64e90fc790924941655a97a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/bad_format/yob2025.txt
cb7a3ce1f47026a74a6a3fe0f6946f76c87a7ed1e0e2a09c7e9c39e69b66b115  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1880.txt
2767b4e29cf44ad293ca911671fc8158994a3e0a8ab8adb3e933e9f48b03cc29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1881.txt
f36f3a09c8999ad64575185276335826dad428f0f49a559b57d5efc0527d22d8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1882.txt
7db51d621eb9ca446e4205cb2a766569a8bfce8ca26baefa1628c000a774c6cc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1883.txt
0e5e95a369ec3effbeaa607e07f13d4f5fdb63c05510edcff461ad15cded9146  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1884.txt
96f7074c4779a1faa6733a0c2a636921760304c29111ad85dc4b8a87779b3444  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1885.txt
3da49bab2714080e60ba89a06a8fff6a0364b0770a9786c20d59d845ad1ce44a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1886.txt
6f8e104c5efe1bdbb4f2ae9d5fc062d69b3d915a7ae3816312a4f018064542de  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1887.txt
5fc9e694c1b808dbd3ca0214cda2b0842ed65d5d8799886496fddb47790a952f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1888.txt
169f1f8ae7932043bc97de7d0f08dfe701964be88403e83ab5c83d5a07e62d63  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1889.txt
06dcf4b1d9b249ab75e0b06acbd45588cace281c89370909d5255d729bcce87d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1890.txt
4f09308d376fed8d7a0e01ba97c1cd60cf12424ed4b860aee255a7b174e64bdd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1891.txt
fb309347045402395cf434fb9c1c1f90f57e85a1fc59f8bbe0228a32a8070945  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1892.txt
18e6c2f649b2a9f25494363b05fae3269771a5b64e81b87927ea2d1837a947fa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1893.txt
9b0bd57c4464cf4c6848690824556d81d16b45c2354ec7d0a09f5966c3142eee  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1894.txt
258edd815fc1b68faf23f569caca14c0f802c8d496d7041bbd4cdfc3ec8ad267  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1895.txt
c81967a7dc39f7a80f4f6b9375a085f5b524ba20e8a7d04c2be484261899ecac  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1896.txt
bd3420605a200b63d8e5c4720d630f9676681409415c6c3ab83fb0cddba90926  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1897.txt
e25413432255b672e75df0ecb4327965c174fcbdfddffa56a4297ef73bd8a5ea  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1898.txt
c3b80523807059594447dbf9725c9bc53306638aa4006b0bf652a79fc657ac72  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1899.txt
929148ecb75a8ca93237bcc734a9cb5a903f3a99baa17e81ce0103e48ddf14f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1900.txt
379f0c8e3295649d021447392764b8aa6a7b92a81db6cbc4fc3145a2ef96167c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1901.txt
f1f86e6e4619d34ae4f68189d3adab3962ec9b152efc0ffbeb17c30add8478a7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1902.txt
a07cbe0dc9ffd0f687f17708b3db0072fdc9ae824cee5c9593e6533dd6f3d482  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1903.txt
25ee85082f920e4728f160c48d75ccef9a281d01451769cbe437e7ec0f8bf5b0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1904.txt
8396ca5cb678f82b35d5807ba8171bc2dae834b086121141f0696c2217944d83  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1905.txt
539851ec9f87ef100c88872c62075697ec5858845e0a332a263c4ab217708fd5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1906.txt
199b5dbb5ee00ff607e6ce6b9594b604a12a3464f821f4f4465b7726c0e2868b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1907.txt
5c42cc01139def67c99a05a3a1da8df2fe16f5b13782ae5345d862ae27feca7a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1908.txt
c58e7cb78d8303880b6559ec83b9373a5096234b5d4d4f8fca0947ca199130e3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1909.txt
592a55632eac50a140d6e0e23af9f42b9055fb18c8add95738cd46a040f86944  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1910.txt
68011b45e4a82e67545cffe4cf6fb28db4e9ada4b5ca6ffa83ddd7cb1d1adf1f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1911.txt
a80476a212cab8bedc1bdf393a02c3c92d99448dd027fe12816330f26e11507b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1912.txt
e80413a8185a900dd852321751faa464eac3acffbe0769f6e1d899f73886471a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1913.txt
b8590df4de8beec972036918168de572bcb185f23d34a54fef3e88f0d7a268a6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1914.txt
c993ca0e3e214d13f23b97a04a79f6b9c1466b25fa373e20c750ac6a6ed66ab4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1915.txt
85f7339db04aabe3bdf8632914033eb9e67fe7c58234b8915ee7279a40ac8fd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1916.txt
59dde7eec31676e946481632c9fd897f474f5b72ccb43262e1ea06a089649a06  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1917.txt
cedf9e54f3ce92a0a7c61c712d2aea7ae832bfac3a1be84b90f3568101efaeff  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1918.txt
f8c1aaf8e6b3e3378507e82bd88cb7e525b46202f9199debcd09d764dee5223f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1919.txt
e6feedcdaf6924572e982ff2fac3e23e0d8c6df7a0d44362986d7c03c303d0bf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1920.txt
651b9629b509c9f72815023c7e098df9985158ec8b443c9b0c6451a8d8622204  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1921.txt
6bd21cda71c1942c361c1e55a0422429022703c34bebe68dd9b982664dd3e4f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1922.txt
2c8a4066e97e397698a78fcad8405b27bde5e0e0dd6a54d8c7c81dfabb62b1c9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1923.txt
3b276b53330e14867e42c0ab1057fec5fe0bc353bc62f7a6a7b36061bf6caefa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1924.txt
15d8eed4f7bc1498057055d7148eebcada293a43656a92d05baedf41198645a1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1925.txt
59806c52a9e231c546c17e74074e8a3699f9b13d7dfe05663f92c4ba519608d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1926.txt
9b4b22b5df77f4905744ae9c50607021fc60e3de84b9641698dd2291bc2d5909  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1927.txt
1f5e4b51d44aa77c98906112d6fabd8929336ac4f375a231f839cb253008028e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1928.txt
90888b34197411d350d7b7674c3c11b736bd804e9591f0375298563db3fa47f5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1929.txt
43be7c84fd9d094b5bc7f6007ece10021e779e444435ebf84c3a03f8e149e81e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1930.txt
fe40b81329cb3c8dfc184fc24050781612b292fe147c3c0642cf8fa200474c25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1931.txt
77697ec1483e753c593726f1e014b23c80e14e27d8a1eca9c16ea0ab21595d6e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1932.txt
3be465a4f15414a64ccfa731fd7441531574ff9ba042083891429fdff9a00536  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1933.txt
c112b656c3b0bb7ca7abd3cfbdf31ab1b1592ef3e2a42986bbb980947026c522  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1934.txt
11630dc298ba066540a2533c6baa34ff8a13b532dbef6d83bf697a6e1f69a77e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1935.txt
e0a4a1fa63c68d55bb0073485df50ea7d4c05cf9367d3a9352c9cbc8f6ddb2b4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1936.txt
c6b4dcfbc4727a8c7090270216d236fb3a6e6b18d07c3591dc6508f0c5ef48bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1937.txt
088d968d9a902251f0bf97c52eba8ce8fed687490907e09848e7a25eb837029d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1938.txt
a96ae6bee42afb7f94c0bbe8dd2a60efeb0b7cc14a96bea19631891b4e6f589c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1939.txt
e2325866576528ac9d7ee8c241951e4a9e17625825780d3081e61b25c898288f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1940.txt
2b55348f6322b9f4217a074e9df28849077b45073fbc07466664226955006950  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1941.txt
f06a37c541cb4c983211f7c6b31d64d1670afbdabb23d71b890987b70c7cc8f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1942.txt
0bdecee171c9755340c2c44d625b51778df031c4644dc75b24bff181d5b9c0be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1943.txt
222ff999cd78f738b32fc14c42d03e619b9062360d5daa29e1e501652e8243d2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1944.txt
873743c7461b1166d9d51286bc2cab56ae913ca3f4f5392f34a718ac5a36705f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1945.txt
ce7d70109aa3717d8b8666baceead357d7724f126034cea1a38ddd09660e1b59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1946.txt
01382b8ea79d81e61967217f394fdc9e1f8f90a086ff5a3108ee3b1771ef42e4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1947.txt
3129980e40fef4abdd2102d43504d5510612be961e0ecbc8fc3de76a6ec39d8b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1948.txt
e7348aebd9d777c26e43f4db335482682b3544b831dca8bb9d106ec6c5f3cba8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1949.txt
83f41e6d750885749fc06c0be24608dfcab357ab4e650b3b58744f2dca85e9f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1950.txt
0314c972de4bbe426fff5fec598ae72e74d3c515570b43f62098e189122282e2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1951.txt
48ac50c973cd6f5ea980a1da3a9c425070dfa73295797c7876aa31e8d5244948  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1952.txt
8d10084b351da3b69c3323baf795b2b1f33bb737b7bbb1ce68e890c4850b330a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1953.txt
5d7e87904883fa7eece2159d45959413af0f25d22e181881dae99709e3249d2e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1954.txt
6ffbeac91ff340f1158678dd9b0879ef9edad9b69cdeff9f370f778183fe7715  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1955.txt
58e525fe9e5005c4059ef47dc6ce4206dba5e2284b3f66d864c34ed4b0af8e4b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1956.txt
99c4beab08cbf6e9d759dd32a4a924d2dda3a36f870fc86d31104c086ebdd95b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1957.txt
fef8b6bbe15685eb520099a20c5835ffdd41c21724ddfc7b787645975b53c5e6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1958.txt
ce6e48423941728b38771974a4dc319188a54c0a8c182c122fb284eb587f06f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1959.txt
5d798b8f8b831b05572cfb29665ff6622eda6334c65c1feac3e502460ab4a3d1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1960.txt
e13ba9227e5faad0cd8f6c6ea008acbd860b2f0ca0fde79458ba209afac31c6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1961.txt
588e243589063e33ae62e70345bdcce53f6080bfec557a7079435f4449f5df8d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1962.txt
a43cbf9d230bb14bc9c07cf31da9771d837f0f2e7740b692e754202138602292  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1963.txt
4d1ac0f733e486f0d9831bb5962f96bbc0dc0b2152beb0eebbbec6e5f621fc07  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1964.txt
2c080acdf262c86cadc1fca4e7f4bf283cda2fd5ac98ecfa7eb4e0570724f625  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1965.txt
221e083f18e0fc4458f04ddfca4356df2a1b615d43eeb7055b3825fb2e828532  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1966.txt
c01062053898c8607ff02cb6d1ca0f9f047f854682066da6c752a64186e0dde4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1967.txt
7de7e5143f13d11f43ce2edd247a1b2f4ac7940f664b2ef82a3a6393528f5398  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1968.txt
04c2f34e65a44612ea9115ca439c8102d570a4efa99f5204f31fcb327b51bcd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1969.txt
1203ba2af4849868f94097e7811b00d8ecbf1795d62ea1486c1875545d42fc1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1970.txt
23932d730a52b949fa2a99e8c890fd68a44df68e245afd70fb76a163c2905822  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1971.txt
3c032b417f47882876b7a7af8a2c82bd9c2ce017c461f3d6c53813644e1c8924  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1972.txt
30ba20505223fef751e07a04cd83a8af9b97c20bd7bb38a9b37e93a3f865360e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1973.txt
f670e0604f047964f9a841ed17ad12f7c0603d0ec787a6fddee8129c9e633775  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1974.txt
eeb82418e71e619d3c6b6273f48036e9c6ab331f16c34cdfae3d7aa390d78c5b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1975.txt
24de081630e23114460293e1902ec97005e834c7ad4ae18049c5d2053ce6bf6f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1976.txt
8dcd066b5b142da9c4622311b533f4de6d3caa25f718b6cccb72bb4eb9dbdfbe  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1977.txt
6dfd1173c3195781210dc36754efbd847df2a869a453061e4a19fca421371b69  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1978.txt
7c2767f7a7de9ee667a01c455448e15f72a95875635c2c30f000274cea94dfb5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1979.txt
4402235a2f5856ee17a87f9163e03e67fd39135e0599904daa4b430b76be4f7b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1980.txt
c5e147f58595ae89099072a603d951ed594acc750bd81259dec98857918e2226  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1981.txt
56f749aa66c05e2de0a1c3f6d3f326b1573ae201cd38e691bafa8227e6e1c569  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1982.txt
af1dbf3ba56f4498098dd646a7002ce3af1a55a1d39e6997f41d9777f021071f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1983.txt
67e4efd8599fbc057034d879f6e06501249089b68e41b6acd144062bed3c713f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1984.txt
39626600b28ac2255ea66d1aafed278cfad3cbefc8e59b65530f68c86a7e534a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1985.txt
f918e85cb6ed0d7b3b5e22b8c92577daddf4509b73d31edb94e9627ca5f63f1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1986.txt
f9dfe77978d0e450d6d41f3c1b5364a64f21747fbbf2bc91fab0f95ce2f8a682  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1987.txt
5a9bf4d9e292efa67ca32cd0d1726e44afd4fe34ba09d491c48a5cb6d7cb42d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1988.txt
fa9de45e5b48b665c70b06ba3ea60b1a8b61e0cb5c23cab07f6451a52e57ad6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1989.txt
7a0026591d9eece5a75fa44ff66dd59eab6b6450c691065a652220dfd2e64bbb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1990.txt
31b0507aeba51f2fccc14f653940c291c8cf25a063601cc75b763e630bb29d2a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1991.txt
b289ec613b3b6489e0ad8bbc20382142870f93da84d6e8f91caf0490d028d7a8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1992.txt
897fe71a1207b1ef4dc61a2776a0c1ba673b3fd1647a8a54e4dd000d00962571  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1993.txt
7de8d30d147b6da8e3d172468349d5ea7a0d1efbe91864398b4409f054fd3ed0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1994.txt
016ddc544a51b0ba501e2a095c92995baf24322d0743b5e08ee9451fb1917f24  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1995.txt
674686f6551d5c634d9e7e8663362fd1454a712f3648a330bf57e6592591ed29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1996.txt
880227b6f3f4f4c6571a459163ba2a62d99c27e4b0ce51b3eec1e2c0201feb1d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1997.txt
678b608eb118f94dce9a3ff21a599b3d062c677511de489c2fca312d9efa1df6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1998.txt
4e833b423c65795446280dbaf968e50e402089474d57bafd53b7f7fac5591a37  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob1999.txt
cb55e7524f97d6d8d904f96d02aa07d5d270ec86c26eb052e045f0e7e716e44e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2000.txt
67e6e70b68b434f45944e9e955da29fe7ad3a2951c79fe6d5d676f2af0152e7e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2001.txt
8c454ebdd41d3cf2fcec8995abd6bd2c90f7ad29790c3e7a52b65f914d18032a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2002.txt
f8efac19c208bdbb4b614a3811a04fdcf5d769894ea528682492db2de7b211a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2003.txt
7f63575f4122896b5847ec3311480e22d7e250a3926ede4aa710c7d9849266bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2004.txt
fec80e345a4d70a56dc391a3ce84b4010901d7d9cf44049c696d4cf3e5765dce  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2005.txt
9280d2cdcbdb57eb6b6b55a24c5f5baf8db45a1f3f4e16f5feb826fa46d1dedf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2006.txt
78b8dd1f9b9f5dd476921bb8b413e997d1f75062827e96cee1b23e2a3e1432aa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2007.txt
5a18ab8a52caccb661232439d01e1d4ba43db77d3b539bd60790a36f7aeaabbd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2008.txt
6a73ef384d30bc18611038e3c884d70d5dd6e14067111a4288715b7636611e5d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2009.txt
94c27249389f0f014b13a481bd5eea357f4d152fb184fffd3fafeb813ad4546f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2010.txt
8ce48e1bf90aa9c7a39e5eefcc9ef32dec5d63fdf858625036d5b0f76795a2eb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2011.txt
18c927510aad45770129f74dba7241f158be1572ad69848a3ebd6989d24c2aec  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2012.txt
363e608862b9509b774a3680fe23693a929bcec8b19b670692335686c600187e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2013.txt
a0f47598fdd1377b19025a6d70cd90ca2f0becf0335dc7d1e5bcf8b7a2a66a91  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2014.txt
d7d8dc754642dd25013051181aeb87ee87ad4f110689101c32c04556cc191bd1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2015.txt
04476e1860f28cd6c5956f1a3cf763402c91e818b98a6b969b3ce878e45b530a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2016.txt
c76d674b4800a93bcee4598ef8111a17b4a68d09260012bbfbc5c5a99f858653  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2017.txt
ec2bdadedaf23ae105cf1274b90288cc42f97c3959be7ae32550710e4d3eee74  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2018.txt
3e8c9f819ca782ce053252030479ad454faeff3679296d542827b66b38dac9f3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2019.txt
0cdb7f3199632d58e9e132706f044f2896deebf04c7fab9b8354334c9beced59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2020.txt
e6c581afaa821984152eaf82757483ca2dc0b6b1d8c091665d961b33a1e3dd92  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2021.txt
b961e6e6bde668f9fab0badc0fcdccc4afeaf4fb66725afb2e5840310e5b2c56  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2022.txt
5c1345ad246cb13a5521aced224d407a4ce704286d8b7af786ac48ab0fe13d00  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2023.txt
f25111d4bdf7fc6844ea54ec73a3dabb83d29310795429c8f9e936f7b35a0650  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2024.txt
7dcd38c9f6629b15a0f85213d24a949cee29b0fe64e90fc790924941655a97a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/count_below_publication_floor/yob2025.txt
4d12f67fc993cc0191c9269a77e0b2854775f2f4f567ac9dd2c725e8a7375c24  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1880.txt
2767b4e29cf44ad293ca911671fc8158994a3e0a8ab8adb3e933e9f48b03cc29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1881.txt
f36f3a09c8999ad64575185276335826dad428f0f49a559b57d5efc0527d22d8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1882.txt
7db51d621eb9ca446e4205cb2a766569a8bfce8ca26baefa1628c000a774c6cc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1883.txt
0e5e95a369ec3effbeaa607e07f13d4f5fdb63c05510edcff461ad15cded9146  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1884.txt
96f7074c4779a1faa6733a0c2a636921760304c29111ad85dc4b8a87779b3444  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1885.txt
3da49bab2714080e60ba89a06a8fff6a0364b0770a9786c20d59d845ad1ce44a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1886.txt
6f8e104c5efe1bdbb4f2ae9d5fc062d69b3d915a7ae3816312a4f018064542de  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1887.txt
5fc9e694c1b808dbd3ca0214cda2b0842ed65d5d8799886496fddb47790a952f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1888.txt
169f1f8ae7932043bc97de7d0f08dfe701964be88403e83ab5c83d5a07e62d63  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1889.txt
bcdefc3f00a43805c9805f22a8cac4d52ecb9480bc4491eec9a440ebd144ad25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1890.txt
4f09308d376fed8d7a0e01ba97c1cd60cf12424ed4b860aee255a7b174e64bdd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1891.txt
fb309347045402395cf434fb9c1c1f90f57e85a1fc59f8bbe0228a32a8070945  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1892.txt
18e6c2f649b2a9f25494363b05fae3269771a5b64e81b87927ea2d1837a947fa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1893.txt
9b0bd57c4464cf4c6848690824556d81d16b45c2354ec7d0a09f5966c3142eee  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1894.txt
258edd815fc1b68faf23f569caca14c0f802c8d496d7041bbd4cdfc3ec8ad267  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1895.txt
c81967a7dc39f7a80f4f6b9375a085f5b524ba20e8a7d04c2be484261899ecac  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1896.txt
bd3420605a200b63d8e5c4720d630f9676681409415c6c3ab83fb0cddba90926  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1897.txt
e25413432255b672e75df0ecb4327965c174fcbdfddffa56a4297ef73bd8a5ea  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1898.txt
c3b80523807059594447dbf9725c9bc53306638aa4006b0bf652a79fc657ac72  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1899.txt
929148ecb75a8ca93237bcc734a9cb5a903f3a99baa17e81ce0103e48ddf14f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1900.txt
379f0c8e3295649d021447392764b8aa6a7b92a81db6cbc4fc3145a2ef96167c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1901.txt
f1f86e6e4619d34ae4f68189d3adab3962ec9b152efc0ffbeb17c30add8478a7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1902.txt
a07cbe0dc9ffd0f687f17708b3db0072fdc9ae824cee5c9593e6533dd6f3d482  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1903.txt
25ee85082f920e4728f160c48d75ccef9a281d01451769cbe437e7ec0f8bf5b0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1904.txt
8396ca5cb678f82b35d5807ba8171bc2dae834b086121141f0696c2217944d83  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1905.txt
539851ec9f87ef100c88872c62075697ec5858845e0a332a263c4ab217708fd5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1906.txt
199b5dbb5ee00ff607e6ce6b9594b604a12a3464f821f4f4465b7726c0e2868b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1907.txt
5c42cc01139def67c99a05a3a1da8df2fe16f5b13782ae5345d862ae27feca7a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1908.txt
c58e7cb78d8303880b6559ec83b9373a5096234b5d4d4f8fca0947ca199130e3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1909.txt
592a55632eac50a140d6e0e23af9f42b9055fb18c8add95738cd46a040f86944  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1910.txt
68011b45e4a82e67545cffe4cf6fb28db4e9ada4b5ca6ffa83ddd7cb1d1adf1f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1911.txt
a80476a212cab8bedc1bdf393a02c3c92d99448dd027fe12816330f26e11507b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1912.txt
e80413a8185a900dd852321751faa464eac3acffbe0769f6e1d899f73886471a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1913.txt
b8590df4de8beec972036918168de572bcb185f23d34a54fef3e88f0d7a268a6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1914.txt
c993ca0e3e214d13f23b97a04a79f6b9c1466b25fa373e20c750ac6a6ed66ab4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1915.txt
85f7339db04aabe3bdf8632914033eb9e67fe7c58234b8915ee7279a40ac8fd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1916.txt
59dde7eec31676e946481632c9fd897f474f5b72ccb43262e1ea06a089649a06  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1917.txt
cedf9e54f3ce92a0a7c61c712d2aea7ae832bfac3a1be84b90f3568101efaeff  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1918.txt
f8c1aaf8e6b3e3378507e82bd88cb7e525b46202f9199debcd09d764dee5223f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1919.txt
e6feedcdaf6924572e982ff2fac3e23e0d8c6df7a0d44362986d7c03c303d0bf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1920.txt
651b9629b509c9f72815023c7e098df9985158ec8b443c9b0c6451a8d8622204  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1921.txt
6bd21cda71c1942c361c1e55a0422429022703c34bebe68dd9b982664dd3e4f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1922.txt
2c8a4066e97e397698a78fcad8405b27bde5e0e0dd6a54d8c7c81dfabb62b1c9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1923.txt
3b276b53330e14867e42c0ab1057fec5fe0bc353bc62f7a6a7b36061bf6caefa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1924.txt
15d8eed4f7bc1498057055d7148eebcada293a43656a92d05baedf41198645a1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1925.txt
59806c52a9e231c546c17e74074e8a3699f9b13d7dfe05663f92c4ba519608d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1926.txt
9b4b22b5df77f4905744ae9c50607021fc60e3de84b9641698dd2291bc2d5909  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1927.txt
1f5e4b51d44aa77c98906112d6fabd8929336ac4f375a231f839cb253008028e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1928.txt
90888b34197411d350d7b7674c3c11b736bd804e9591f0375298563db3fa47f5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1929.txt
43be7c84fd9d094b5bc7f6007ece10021e779e444435ebf84c3a03f8e149e81e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1930.txt
fe40b81329cb3c8dfc184fc24050781612b292fe147c3c0642cf8fa200474c25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1931.txt
77697ec1483e753c593726f1e014b23c80e14e27d8a1eca9c16ea0ab21595d6e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1932.txt
3be465a4f15414a64ccfa731fd7441531574ff9ba042083891429fdff9a00536  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1933.txt
c112b656c3b0bb7ca7abd3cfbdf31ab1b1592ef3e2a42986bbb980947026c522  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1934.txt
11630dc298ba066540a2533c6baa34ff8a13b532dbef6d83bf697a6e1f69a77e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1935.txt
e0a4a1fa63c68d55bb0073485df50ea7d4c05cf9367d3a9352c9cbc8f6ddb2b4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1936.txt
c6b4dcfbc4727a8c7090270216d236fb3a6e6b18d07c3591dc6508f0c5ef48bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1937.txt
088d968d9a902251f0bf97c52eba8ce8fed687490907e09848e7a25eb837029d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1938.txt
a96ae6bee42afb7f94c0bbe8dd2a60efeb0b7cc14a96bea19631891b4e6f589c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1939.txt
e2325866576528ac9d7ee8c241951e4a9e17625825780d3081e61b25c898288f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1940.txt
2b55348f6322b9f4217a074e9df28849077b45073fbc07466664226955006950  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1941.txt
f06a37c541cb4c983211f7c6b31d64d1670afbdabb23d71b890987b70c7cc8f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1942.txt
0bdecee171c9755340c2c44d625b51778df031c4644dc75b24bff181d5b9c0be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1943.txt
222ff999cd78f738b32fc14c42d03e619b9062360d5daa29e1e501652e8243d2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1944.txt
873743c7461b1166d9d51286bc2cab56ae913ca3f4f5392f34a718ac5a36705f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1945.txt
ce7d70109aa3717d8b8666baceead357d7724f126034cea1a38ddd09660e1b59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1946.txt
01382b8ea79d81e61967217f394fdc9e1f8f90a086ff5a3108ee3b1771ef42e4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1947.txt
3129980e40fef4abdd2102d43504d5510612be961e0ecbc8fc3de76a6ec39d8b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1948.txt
e7348aebd9d777c26e43f4db335482682b3544b831dca8bb9d106ec6c5f3cba8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1949.txt
83f41e6d750885749fc06c0be24608dfcab357ab4e650b3b58744f2dca85e9f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1950.txt
0314c972de4bbe426fff5fec598ae72e74d3c515570b43f62098e189122282e2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1951.txt
48ac50c973cd6f5ea980a1da3a9c425070dfa73295797c7876aa31e8d5244948  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1952.txt
8d10084b351da3b69c3323baf795b2b1f33bb737b7bbb1ce68e890c4850b330a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1953.txt
5d7e87904883fa7eece2159d45959413af0f25d22e181881dae99709e3249d2e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1954.txt
6ffbeac91ff340f1158678dd9b0879ef9edad9b69cdeff9f370f778183fe7715  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1955.txt
58e525fe9e5005c4059ef47dc6ce4206dba5e2284b3f66d864c34ed4b0af8e4b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1956.txt
99c4beab08cbf6e9d759dd32a4a924d2dda3a36f870fc86d31104c086ebdd95b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1957.txt
fef8b6bbe15685eb520099a20c5835ffdd41c21724ddfc7b787645975b53c5e6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1958.txt
ce6e48423941728b38771974a4dc319188a54c0a8c182c122fb284eb587f06f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1959.txt
5d798b8f8b831b05572cfb29665ff6622eda6334c65c1feac3e502460ab4a3d1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1960.txt
e13ba9227e5faad0cd8f6c6ea008acbd860b2f0ca0fde79458ba209afac31c6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1961.txt
588e243589063e33ae62e70345bdcce53f6080bfec557a7079435f4449f5df8d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1962.txt
a43cbf9d230bb14bc9c07cf31da9771d837f0f2e7740b692e754202138602292  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1963.txt
4d1ac0f733e486f0d9831bb5962f96bbc0dc0b2152beb0eebbbec6e5f621fc07  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1964.txt
2c080acdf262c86cadc1fca4e7f4bf283cda2fd5ac98ecfa7eb4e0570724f625  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1965.txt
221e083f18e0fc4458f04ddfca4356df2a1b615d43eeb7055b3825fb2e828532  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1966.txt
c01062053898c8607ff02cb6d1ca0f9f047f854682066da6c752a64186e0dde4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1967.txt
7de7e5143f13d11f43ce2edd247a1b2f4ac7940f664b2ef82a3a6393528f5398  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1968.txt
04c2f34e65a44612ea9115ca439c8102d570a4efa99f5204f31fcb327b51bcd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1969.txt
1203ba2af4849868f94097e7811b00d8ecbf1795d62ea1486c1875545d42fc1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1970.txt
23932d730a52b949fa2a99e8c890fd68a44df68e245afd70fb76a163c2905822  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1971.txt
3c032b417f47882876b7a7af8a2c82bd9c2ce017c461f3d6c53813644e1c8924  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1972.txt
30ba20505223fef751e07a04cd83a8af9b97c20bd7bb38a9b37e93a3f865360e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1973.txt
f670e0604f047964f9a841ed17ad12f7c0603d0ec787a6fddee8129c9e633775  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1974.txt
eeb82418e71e619d3c6b6273f48036e9c6ab331f16c34cdfae3d7aa390d78c5b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1975.txt
24de081630e23114460293e1902ec97005e834c7ad4ae18049c5d2053ce6bf6f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1976.txt
8dcd066b5b142da9c4622311b533f4de6d3caa25f718b6cccb72bb4eb9dbdfbe  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1977.txt
6dfd1173c3195781210dc36754efbd847df2a869a453061e4a19fca421371b69  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1978.txt
7c2767f7a7de9ee667a01c455448e15f72a95875635c2c30f000274cea94dfb5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1979.txt
4402235a2f5856ee17a87f9163e03e67fd39135e0599904daa4b430b76be4f7b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1980.txt
c5e147f58595ae89099072a603d951ed594acc750bd81259dec98857918e2226  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1981.txt
56f749aa66c05e2de0a1c3f6d3f326b1573ae201cd38e691bafa8227e6e1c569  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1982.txt
af1dbf3ba56f4498098dd646a7002ce3af1a55a1d39e6997f41d9777f021071f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1983.txt
67e4efd8599fbc057034d879f6e06501249089b68e41b6acd144062bed3c713f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1984.txt
39626600b28ac2255ea66d1aafed278cfad3cbefc8e59b65530f68c86a7e534a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1985.txt
f918e85cb6ed0d7b3b5e22b8c92577daddf4509b73d31edb94e9627ca5f63f1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1986.txt
f9dfe77978d0e450d6d41f3c1b5364a64f21747fbbf2bc91fab0f95ce2f8a682  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1987.txt
5a9bf4d9e292efa67ca32cd0d1726e44afd4fe34ba09d491c48a5cb6d7cb42d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1988.txt
fa9de45e5b48b665c70b06ba3ea60b1a8b61e0cb5c23cab07f6451a52e57ad6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1989.txt
7a0026591d9eece5a75fa44ff66dd59eab6b6450c691065a652220dfd2e64bbb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1990.txt
31b0507aeba51f2fccc14f653940c291c8cf25a063601cc75b763e630bb29d2a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1991.txt
b289ec613b3b6489e0ad8bbc20382142870f93da84d6e8f91caf0490d028d7a8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1992.txt
897fe71a1207b1ef4dc61a2776a0c1ba673b3fd1647a8a54e4dd000d00962571  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1993.txt
7de8d30d147b6da8e3d172468349d5ea7a0d1efbe91864398b4409f054fd3ed0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1994.txt
016ddc544a51b0ba501e2a095c92995baf24322d0743b5e08ee9451fb1917f24  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1995.txt
674686f6551d5c634d9e7e8663362fd1454a712f3648a330bf57e6592591ed29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1996.txt
880227b6f3f4f4c6571a459163ba2a62d99c27e4b0ce51b3eec1e2c0201feb1d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1997.txt
678b608eb118f94dce9a3ff21a599b3d062c677511de489c2fca312d9efa1df6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1998.txt
4e833b423c65795446280dbaf968e50e402089474d57bafd53b7f7fac5591a37  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob1999.txt
cb55e7524f97d6d8d904f96d02aa07d5d270ec86c26eb052e045f0e7e716e44e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2000.txt
67e6e70b68b434f45944e9e955da29fe7ad3a2951c79fe6d5d676f2af0152e7e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2001.txt
8c454ebdd41d3cf2fcec8995abd6bd2c90f7ad29790c3e7a52b65f914d18032a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2002.txt
f8efac19c208bdbb4b614a3811a04fdcf5d769894ea528682492db2de7b211a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2003.txt
7f63575f4122896b5847ec3311480e22d7e250a3926ede4aa710c7d9849266bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2004.txt
fec80e345a4d70a56dc391a3ce84b4010901d7d9cf44049c696d4cf3e5765dce  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2005.txt
9280d2cdcbdb57eb6b6b55a24c5f5baf8db45a1f3f4e16f5feb826fa46d1dedf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2006.txt
78b8dd1f9b9f5dd476921bb8b413e997d1f75062827e96cee1b23e2a3e1432aa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2007.txt
5a18ab8a52caccb661232439d01e1d4ba43db77d3b539bd60790a36f7aeaabbd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2008.txt
6a73ef384d30bc18611038e3c884d70d5dd6e14067111a4288715b7636611e5d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2009.txt
94c27249389f0f014b13a481bd5eea357f4d152fb184fffd3fafeb813ad4546f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2010.txt
8ce48e1bf90aa9c7a39e5eefcc9ef32dec5d63fdf858625036d5b0f76795a2eb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2011.txt
18c927510aad45770129f74dba7241f158be1572ad69848a3ebd6989d24c2aec  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2012.txt
363e608862b9509b774a3680fe23693a929bcec8b19b670692335686c600187e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2013.txt
a0f47598fdd1377b19025a6d70cd90ca2f0becf0335dc7d1e5bcf8b7a2a66a91  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2014.txt
d7d8dc754642dd25013051181aeb87ee87ad4f110689101c32c04556cc191bd1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2015.txt
04476e1860f28cd6c5956f1a3cf763402c91e818b98a6b969b3ce878e45b530a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2016.txt
c76d674b4800a93bcee4598ef8111a17b4a68d09260012bbfbc5c5a99f858653  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2017.txt
ec2bdadedaf23ae105cf1274b90288cc42f97c3959be7ae32550710e4d3eee74  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2018.txt
3e8c9f819ca782ce053252030479ad454faeff3679296d542827b66b38dac9f3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2019.txt
0cdb7f3199632d58e9e132706f044f2896deebf04c7fab9b8354334c9beced59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2020.txt
e6c581afaa821984152eaf82757483ca2dc0b6b1d8c091665d961b33a1e3dd92  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2021.txt
b961e6e6bde668f9fab0badc0fcdccc4afeaf4fb66725afb2e5840310e5b2c56  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2022.txt
5c1345ad246cb13a5521aced224d407a4ce704286d8b7af786ac48ab0fe13d00  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2023.txt
f25111d4bdf7fc6844ea54ec73a3dabb83d29310795429c8f9e936f7b35a0650  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2024.txt
7dcd38c9f6629b15a0f85213d24a949cee29b0fe64e90fc790924941655a97a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/duplicate_key/yob2025.txt
cb7a3ce1f47026a74a6a3fe0f6946f76c87a7ed1e0e2a09c7e9c39e69b66b115  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1880.txt
2767b4e29cf44ad293ca911671fc8158994a3e0a8ab8adb3e933e9f48b03cc29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1881.txt
f36f3a09c8999ad64575185276335826dad428f0f49a559b57d5efc0527d22d8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1882.txt
7db51d621eb9ca446e4205cb2a766569a8bfce8ca26baefa1628c000a774c6cc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1883.txt
0e5e95a369ec3effbeaa607e07f13d4f5fdb63c05510edcff461ad15cded9146  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1884.txt
96f7074c4779a1faa6733a0c2a636921760304c29111ad85dc4b8a87779b3444  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1885.txt
3da49bab2714080e60ba89a06a8fff6a0364b0770a9786c20d59d845ad1ce44a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1886.txt
6f8e104c5efe1bdbb4f2ae9d5fc062d69b3d915a7ae3816312a4f018064542de  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1887.txt
5fc9e694c1b808dbd3ca0214cda2b0842ed65d5d8799886496fddb47790a952f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1888.txt
169f1f8ae7932043bc97de7d0f08dfe701964be88403e83ab5c83d5a07e62d63  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1889.txt
bcdefc3f00a43805c9805f22a8cac4d52ecb9480bc4491eec9a440ebd144ad25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1890.txt
4f09308d376fed8d7a0e01ba97c1cd60cf12424ed4b860aee255a7b174e64bdd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1891.txt
fb309347045402395cf434fb9c1c1f90f57e85a1fc59f8bbe0228a32a8070945  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1892.txt
18e6c2f649b2a9f25494363b05fae3269771a5b64e81b87927ea2d1837a947fa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1893.txt
9b0bd57c4464cf4c6848690824556d81d16b45c2354ec7d0a09f5966c3142eee  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1894.txt
258edd815fc1b68faf23f569caca14c0f802c8d496d7041bbd4cdfc3ec8ad267  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1895.txt
c81967a7dc39f7a80f4f6b9375a085f5b524ba20e8a7d04c2be484261899ecac  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1896.txt
bd3420605a200b63d8e5c4720d630f9676681409415c6c3ab83fb0cddba90926  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1897.txt
e25413432255b672e75df0ecb4327965c174fcbdfddffa56a4297ef73bd8a5ea  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1898.txt
c3b80523807059594447dbf9725c9bc53306638aa4006b0bf652a79fc657ac72  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1899.txt
929148ecb75a8ca93237bcc734a9cb5a903f3a99baa17e81ce0103e48ddf14f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1900.txt
379f0c8e3295649d021447392764b8aa6a7b92a81db6cbc4fc3145a2ef96167c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1901.txt
f1f86e6e4619d34ae4f68189d3adab3962ec9b152efc0ffbeb17c30add8478a7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1902.txt
a07cbe0dc9ffd0f687f17708b3db0072fdc9ae824cee5c9593e6533dd6f3d482  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1903.txt
25ee85082f920e4728f160c48d75ccef9a281d01451769cbe437e7ec0f8bf5b0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1904.txt
8396ca5cb678f82b35d5807ba8171bc2dae834b086121141f0696c2217944d83  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1905.txt
539851ec9f87ef100c88872c62075697ec5858845e0a332a263c4ab217708fd5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1906.txt
199b5dbb5ee00ff607e6ce6b9594b604a12a3464f821f4f4465b7726c0e2868b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1907.txt
5c42cc01139def67c99a05a3a1da8df2fe16f5b13782ae5345d862ae27feca7a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1908.txt
c58e7cb78d8303880b6559ec83b9373a5096234b5d4d4f8fca0947ca199130e3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1909.txt
592a55632eac50a140d6e0e23af9f42b9055fb18c8add95738cd46a040f86944  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1910.txt
68011b45e4a82e67545cffe4cf6fb28db4e9ada4b5ca6ffa83ddd7cb1d1adf1f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1911.txt
a80476a212cab8bedc1bdf393a02c3c92d99448dd027fe12816330f26e11507b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1912.txt
e80413a8185a900dd852321751faa464eac3acffbe0769f6e1d899f73886471a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1913.txt
b8590df4de8beec972036918168de572bcb185f23d34a54fef3e88f0d7a268a6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1914.txt
c993ca0e3e214d13f23b97a04a79f6b9c1466b25fa373e20c750ac6a6ed66ab4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1915.txt
85f7339db04aabe3bdf8632914033eb9e67fe7c58234b8915ee7279a40ac8fd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1916.txt
59dde7eec31676e946481632c9fd897f474f5b72ccb43262e1ea06a089649a06  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1917.txt
cedf9e54f3ce92a0a7c61c712d2aea7ae832bfac3a1be84b90f3568101efaeff  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1918.txt
f8c1aaf8e6b3e3378507e82bd88cb7e525b46202f9199debcd09d764dee5223f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1919.txt
e6feedcdaf6924572e982ff2fac3e23e0d8c6df7a0d44362986d7c03c303d0bf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1920.txt
651b9629b509c9f72815023c7e098df9985158ec8b443c9b0c6451a8d8622204  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1921.txt
6bd21cda71c1942c361c1e55a0422429022703c34bebe68dd9b982664dd3e4f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1922.txt
2c8a4066e97e397698a78fcad8405b27bde5e0e0dd6a54d8c7c81dfabb62b1c9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1923.txt
3b276b53330e14867e42c0ab1057fec5fe0bc353bc62f7a6a7b36061bf6caefa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1924.txt
15d8eed4f7bc1498057055d7148eebcada293a43656a92d05baedf41198645a1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1925.txt
59806c52a9e231c546c17e74074e8a3699f9b13d7dfe05663f92c4ba519608d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1926.txt
9b4b22b5df77f4905744ae9c50607021fc60e3de84b9641698dd2291bc2d5909  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1927.txt
1f5e4b51d44aa77c98906112d6fabd8929336ac4f375a231f839cb253008028e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1928.txt
90888b34197411d350d7b7674c3c11b736bd804e9591f0375298563db3fa47f5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1929.txt
43be7c84fd9d094b5bc7f6007ece10021e779e444435ebf84c3a03f8e149e81e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1930.txt
fe40b81329cb3c8dfc184fc24050781612b292fe147c3c0642cf8fa200474c25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1931.txt
77697ec1483e753c593726f1e014b23c80e14e27d8a1eca9c16ea0ab21595d6e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1932.txt
3be465a4f15414a64ccfa731fd7441531574ff9ba042083891429fdff9a00536  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1933.txt
c112b656c3b0bb7ca7abd3cfbdf31ab1b1592ef3e2a42986bbb980947026c522  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1934.txt
11630dc298ba066540a2533c6baa34ff8a13b532dbef6d83bf697a6e1f69a77e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1935.txt
e0a4a1fa63c68d55bb0073485df50ea7d4c05cf9367d3a9352c9cbc8f6ddb2b4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1936.txt
c6b4dcfbc4727a8c7090270216d236fb3a6e6b18d07c3591dc6508f0c5ef48bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1937.txt
088d968d9a902251f0bf97c52eba8ce8fed687490907e09848e7a25eb837029d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1938.txt
a96ae6bee42afb7f94c0bbe8dd2a60efeb0b7cc14a96bea19631891b4e6f589c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1939.txt
e2325866576528ac9d7ee8c241951e4a9e17625825780d3081e61b25c898288f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1940.txt
2b55348f6322b9f4217a074e9df28849077b45073fbc07466664226955006950  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1941.txt
f06a37c541cb4c983211f7c6b31d64d1670afbdabb23d71b890987b70c7cc8f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1942.txt
0bdecee171c9755340c2c44d625b51778df031c4644dc75b24bff181d5b9c0be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1943.txt
222ff999cd78f738b32fc14c42d03e619b9062360d5daa29e1e501652e8243d2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1944.txt
873743c7461b1166d9d51286bc2cab56ae913ca3f4f5392f34a718ac5a36705f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1945.txt
ce7d70109aa3717d8b8666baceead357d7724f126034cea1a38ddd09660e1b59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1946.txt
01382b8ea79d81e61967217f394fdc9e1f8f90a086ff5a3108ee3b1771ef42e4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1947.txt
3129980e40fef4abdd2102d43504d5510612be961e0ecbc8fc3de76a6ec39d8b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1948.txt
e7348aebd9d777c26e43f4db335482682b3544b831dca8bb9d106ec6c5f3cba8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1949.txt
83f41e6d750885749fc06c0be24608dfcab357ab4e650b3b58744f2dca85e9f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1950.txt
0314c972de4bbe426fff5fec598ae72e74d3c515570b43f62098e189122282e2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1951.txt
48ac50c973cd6f5ea980a1da3a9c425070dfa73295797c7876aa31e8d5244948  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1952.txt
8d10084b351da3b69c3323baf795b2b1f33bb737b7bbb1ce68e890c4850b330a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1953.txt
5d7e87904883fa7eece2159d45959413af0f25d22e181881dae99709e3249d2e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1954.txt
6ffbeac91ff340f1158678dd9b0879ef9edad9b69cdeff9f370f778183fe7715  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1955.txt
58e525fe9e5005c4059ef47dc6ce4206dba5e2284b3f66d864c34ed4b0af8e4b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1956.txt
99c4beab08cbf6e9d759dd32a4a924d2dda3a36f870fc86d31104c086ebdd95b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1957.txt
fef8b6bbe15685eb520099a20c5835ffdd41c21724ddfc7b787645975b53c5e6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1958.txt
ce6e48423941728b38771974a4dc319188a54c0a8c182c122fb284eb587f06f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1959.txt
5d798b8f8b831b05572cfb29665ff6622eda6334c65c1feac3e502460ab4a3d1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1960.txt
e13ba9227e5faad0cd8f6c6ea008acbd860b2f0ca0fde79458ba209afac31c6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1961.txt
588e243589063e33ae62e70345bdcce53f6080bfec557a7079435f4449f5df8d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1962.txt
a43cbf9d230bb14bc9c07cf31da9771d837f0f2e7740b692e754202138602292  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1963.txt
4d1ac0f733e486f0d9831bb5962f96bbc0dc0b2152beb0eebbbec6e5f621fc07  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1964.txt
2c080acdf262c86cadc1fca4e7f4bf283cda2fd5ac98ecfa7eb4e0570724f625  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1965.txt
221e083f18e0fc4458f04ddfca4356df2a1b615d43eeb7055b3825fb2e828532  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1966.txt
c01062053898c8607ff02cb6d1ca0f9f047f854682066da6c752a64186e0dde4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1967.txt
7de7e5143f13d11f43ce2edd247a1b2f4ac7940f664b2ef82a3a6393528f5398  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1968.txt
04c2f34e65a44612ea9115ca439c8102d570a4efa99f5204f31fcb327b51bcd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1969.txt
1203ba2af4849868f94097e7811b00d8ecbf1795d62ea1486c1875545d42fc1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1970.txt
23932d730a52b949fa2a99e8c890fd68a44df68e245afd70fb76a163c2905822  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1971.txt
3c032b417f47882876b7a7af8a2c82bd9c2ce017c461f3d6c53813644e1c8924  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1972.txt
30ba20505223fef751e07a04cd83a8af9b97c20bd7bb38a9b37e93a3f865360e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1973.txt
f670e0604f047964f9a841ed17ad12f7c0603d0ec787a6fddee8129c9e633775  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1974.txt
eeb82418e71e619d3c6b6273f48036e9c6ab331f16c34cdfae3d7aa390d78c5b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1975.txt
24de081630e23114460293e1902ec97005e834c7ad4ae18049c5d2053ce6bf6f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1976.txt
8dcd066b5b142da9c4622311b533f4de6d3caa25f718b6cccb72bb4eb9dbdfbe  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1977.txt
6dfd1173c3195781210dc36754efbd847df2a869a453061e4a19fca421371b69  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1978.txt
7c2767f7a7de9ee667a01c455448e15f72a95875635c2c30f000274cea94dfb5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1979.txt
4402235a2f5856ee17a87f9163e03e67fd39135e0599904daa4b430b76be4f7b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1980.txt
c5e147f58595ae89099072a603d951ed594acc750bd81259dec98857918e2226  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1981.txt
56f749aa66c05e2de0a1c3f6d3f326b1573ae201cd38e691bafa8227e6e1c569  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1982.txt
af1dbf3ba56f4498098dd646a7002ce3af1a55a1d39e6997f41d9777f021071f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1983.txt
67e4efd8599fbc057034d879f6e06501249089b68e41b6acd144062bed3c713f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1984.txt
39626600b28ac2255ea66d1aafed278cfad3cbefc8e59b65530f68c86a7e534a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1985.txt
f918e85cb6ed0d7b3b5e22b8c92577daddf4509b73d31edb94e9627ca5f63f1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1986.txt
f9dfe77978d0e450d6d41f3c1b5364a64f21747fbbf2bc91fab0f95ce2f8a682  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1987.txt
5a9bf4d9e292efa67ca32cd0d1726e44afd4fe34ba09d491c48a5cb6d7cb42d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1988.txt
fa9de45e5b48b665c70b06ba3ea60b1a8b61e0cb5c23cab07f6451a52e57ad6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1989.txt
7a0026591d9eece5a75fa44ff66dd59eab6b6450c691065a652220dfd2e64bbb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1990.txt
31b0507aeba51f2fccc14f653940c291c8cf25a063601cc75b763e630bb29d2a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1991.txt
b289ec613b3b6489e0ad8bbc20382142870f93da84d6e8f91caf0490d028d7a8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1992.txt
897fe71a1207b1ef4dc61a2776a0c1ba673b3fd1647a8a54e4dd000d00962571  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1993.txt
7de8d30d147b6da8e3d172468349d5ea7a0d1efbe91864398b4409f054fd3ed0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1994.txt
016ddc544a51b0ba501e2a095c92995baf24322d0743b5e08ee9451fb1917f24  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1995.txt
674686f6551d5c634d9e7e8663362fd1454a712f3648a330bf57e6592591ed29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1996.txt
880227b6f3f4f4c6571a459163ba2a62d99c27e4b0ce51b3eec1e2c0201feb1d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1997.txt
678b608eb118f94dce9a3ff21a599b3d062c677511de489c2fca312d9efa1df6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1998.txt
4e833b423c65795446280dbaf968e50e402089474d57bafd53b7f7fac5591a37  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob1999.txt
cb55e7524f97d6d8d904f96d02aa07d5d270ec86c26eb052e045f0e7e716e44e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2000.txt
67e6e70b68b434f45944e9e955da29fe7ad3a2951c79fe6d5d676f2af0152e7e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2001.txt
8c454ebdd41d3cf2fcec8995abd6bd2c90f7ad29790c3e7a52b65f914d18032a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2002.txt
f8efac19c208bdbb4b614a3811a04fdcf5d769894ea528682492db2de7b211a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2003.txt
7f63575f4122896b5847ec3311480e22d7e250a3926ede4aa710c7d9849266bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2004.txt
fec80e345a4d70a56dc391a3ce84b4010901d7d9cf44049c696d4cf3e5765dce  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2005.txt
9280d2cdcbdb57eb6b6b55a24c5f5baf8db45a1f3f4e16f5feb826fa46d1dedf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2006.txt
78b8dd1f9b9f5dd476921bb8b413e997d1f75062827e96cee1b23e2a3e1432aa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2007.txt
5a18ab8a52caccb661232439d01e1d4ba43db77d3b539bd60790a36f7aeaabbd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2008.txt
6a73ef384d30bc18611038e3c884d70d5dd6e14067111a4288715b7636611e5d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2009.txt
94c27249389f0f014b13a481bd5eea357f4d152fb184fffd3fafeb813ad4546f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2010.txt
8ce48e1bf90aa9c7a39e5eefcc9ef32dec5d63fdf858625036d5b0f76795a2eb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2011.txt
18c927510aad45770129f74dba7241f158be1572ad69848a3ebd6989d24c2aec  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2012.txt
363e608862b9509b774a3680fe23693a929bcec8b19b670692335686c600187e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2013.txt
a0f47598fdd1377b19025a6d70cd90ca2f0becf0335dc7d1e5bcf8b7a2a66a91  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2014.txt
d7d8dc754642dd25013051181aeb87ee87ad4f110689101c32c04556cc191bd1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2015.txt
04476e1860f28cd6c5956f1a3cf763402c91e818b98a6b969b3ce878e45b530a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2016.txt
c76d674b4800a93bcee4598ef8111a17b4a68d09260012bbfbc5c5a99f858653  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2017.txt
ec2bdadedaf23ae105cf1274b90288cc42f97c3959be7ae32550710e4d3eee74  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2018.txt
3e8c9f819ca782ce053252030479ad454faeff3679296d542827b66b38dac9f3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2019.txt
0cdb7f3199632d58e9e132706f044f2896deebf04c7fab9b8354334c9beced59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2020.txt
e6c581afaa821984152eaf82757483ca2dc0b6b1d8c091665d961b33a1e3dd92  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2021.txt
b961e6e6bde668f9fab0badc0fcdccc4afeaf4fb66725afb2e5840310e5b2c56  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2022.txt
5c1345ad246cb13a5521aced224d407a4ce704286d8b7af786ac48ab0fe13d00  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2023.txt
f25111d4bdf7fc6844ea54ec73a3dabb83d29310795429c8f9e936f7b35a0650  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2024.txt
7dcd38c9f6629b15a0f85213d24a949cee29b0fe64e90fc790924941655a97a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/good/yob2025.txt
cb7a3ce1f47026a74a6a3fe0f6946f76c87a7ed1e0e2a09c7e9c39e69b66b115  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1880.txt
2767b4e29cf44ad293ca911671fc8158994a3e0a8ab8adb3e933e9f48b03cc29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1881.txt
f36f3a09c8999ad64575185276335826dad428f0f49a559b57d5efc0527d22d8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1882.txt
7db51d621eb9ca446e4205cb2a766569a8bfce8ca26baefa1628c000a774c6cc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1883.txt
0e5e95a369ec3effbeaa607e07f13d4f5fdb63c05510edcff461ad15cded9146  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1884.txt
96f7074c4779a1faa6733a0c2a636921760304c29111ad85dc4b8a87779b3444  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1885.txt
3da49bab2714080e60ba89a06a8fff6a0364b0770a9786c20d59d845ad1ce44a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1886.txt
6f8e104c5efe1bdbb4f2ae9d5fc062d69b3d915a7ae3816312a4f018064542de  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1887.txt
5fc9e694c1b808dbd3ca0214cda2b0842ed65d5d8799886496fddb47790a952f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1888.txt
169f1f8ae7932043bc97de7d0f08dfe701964be88403e83ab5c83d5a07e62d63  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1889.txt
bcdefc3f00a43805c9805f22a8cac4d52ecb9480bc4491eec9a440ebd144ad25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1890.txt
4f09308d376fed8d7a0e01ba97c1cd60cf12424ed4b860aee255a7b174e64bdd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1891.txt
fb309347045402395cf434fb9c1c1f90f57e85a1fc59f8bbe0228a32a8070945  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1892.txt
18e6c2f649b2a9f25494363b05fae3269771a5b64e81b87927ea2d1837a947fa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1893.txt
9b0bd57c4464cf4c6848690824556d81d16b45c2354ec7d0a09f5966c3142eee  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1894.txt
258edd815fc1b68faf23f569caca14c0f802c8d496d7041bbd4cdfc3ec8ad267  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1895.txt
c81967a7dc39f7a80f4f6b9375a085f5b524ba20e8a7d04c2be484261899ecac  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1896.txt
bd3420605a200b63d8e5c4720d630f9676681409415c6c3ab83fb0cddba90926  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1897.txt
e25413432255b672e75df0ecb4327965c174fcbdfddffa56a4297ef73bd8a5ea  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1898.txt
c3b80523807059594447dbf9725c9bc53306638aa4006b0bf652a79fc657ac72  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1899.txt
929148ecb75a8ca93237bcc734a9cb5a903f3a99baa17e81ce0103e48ddf14f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1900.txt
379f0c8e3295649d021447392764b8aa6a7b92a81db6cbc4fc3145a2ef96167c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1901.txt
f1f86e6e4619d34ae4f68189d3adab3962ec9b152efc0ffbeb17c30add8478a7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1902.txt
a07cbe0dc9ffd0f687f17708b3db0072fdc9ae824cee5c9593e6533dd6f3d482  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1903.txt
25ee85082f920e4728f160c48d75ccef9a281d01451769cbe437e7ec0f8bf5b0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1904.txt
8396ca5cb678f82b35d5807ba8171bc2dae834b086121141f0696c2217944d83  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1905.txt
539851ec9f87ef100c88872c62075697ec5858845e0a332a263c4ab217708fd5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1906.txt
199b5dbb5ee00ff607e6ce6b9594b604a12a3464f821f4f4465b7726c0e2868b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1907.txt
5c42cc01139def67c99a05a3a1da8df2fe16f5b13782ae5345d862ae27feca7a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1908.txt
c58e7cb78d8303880b6559ec83b9373a5096234b5d4d4f8fca0947ca199130e3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1909.txt
592a55632eac50a140d6e0e23af9f42b9055fb18c8add95738cd46a040f86944  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1910.txt
68011b45e4a82e67545cffe4cf6fb28db4e9ada4b5ca6ffa83ddd7cb1d1adf1f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1911.txt
a80476a212cab8bedc1bdf393a02c3c92d99448dd027fe12816330f26e11507b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1912.txt
e80413a8185a900dd852321751faa464eac3acffbe0769f6e1d899f73886471a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1913.txt
b8590df4de8beec972036918168de572bcb185f23d34a54fef3e88f0d7a268a6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1914.txt
c993ca0e3e214d13f23b97a04a79f6b9c1466b25fa373e20c750ac6a6ed66ab4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1915.txt
85f7339db04aabe3bdf8632914033eb9e67fe7c58234b8915ee7279a40ac8fd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1916.txt
59dde7eec31676e946481632c9fd897f474f5b72ccb43262e1ea06a089649a06  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1917.txt
cedf9e54f3ce92a0a7c61c712d2aea7ae832bfac3a1be84b90f3568101efaeff  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1918.txt
f8c1aaf8e6b3e3378507e82bd88cb7e525b46202f9199debcd09d764dee5223f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1919.txt
e6feedcdaf6924572e982ff2fac3e23e0d8c6df7a0d44362986d7c03c303d0bf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1920.txt
651b9629b509c9f72815023c7e098df9985158ec8b443c9b0c6451a8d8622204  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1921.txt
6bd21cda71c1942c361c1e55a0422429022703c34bebe68dd9b982664dd3e4f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1922.txt
2c8a4066e97e397698a78fcad8405b27bde5e0e0dd6a54d8c7c81dfabb62b1c9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1923.txt
3b276b53330e14867e42c0ab1057fec5fe0bc353bc62f7a6a7b36061bf6caefa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1924.txt
15d8eed4f7bc1498057055d7148eebcada293a43656a92d05baedf41198645a1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1925.txt
59806c52a9e231c546c17e74074e8a3699f9b13d7dfe05663f92c4ba519608d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1926.txt
9b4b22b5df77f4905744ae9c50607021fc60e3de84b9641698dd2291bc2d5909  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1927.txt
1f5e4b51d44aa77c98906112d6fabd8929336ac4f375a231f839cb253008028e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1928.txt
90888b34197411d350d7b7674c3c11b736bd804e9591f0375298563db3fa47f5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1929.txt
43be7c84fd9d094b5bc7f6007ece10021e779e444435ebf84c3a03f8e149e81e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1930.txt
fe40b81329cb3c8dfc184fc24050781612b292fe147c3c0642cf8fa200474c25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1931.txt
77697ec1483e753c593726f1e014b23c80e14e27d8a1eca9c16ea0ab21595d6e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1932.txt
3be465a4f15414a64ccfa731fd7441531574ff9ba042083891429fdff9a00536  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1933.txt
c112b656c3b0bb7ca7abd3cfbdf31ab1b1592ef3e2a42986bbb980947026c522  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1934.txt
11630dc298ba066540a2533c6baa34ff8a13b532dbef6d83bf697a6e1f69a77e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1935.txt
e0a4a1fa63c68d55bb0073485df50ea7d4c05cf9367d3a9352c9cbc8f6ddb2b4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1936.txt
c6b4dcfbc4727a8c7090270216d236fb3a6e6b18d07c3591dc6508f0c5ef48bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1937.txt
088d968d9a902251f0bf97c52eba8ce8fed687490907e09848e7a25eb837029d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1938.txt
a96ae6bee42afb7f94c0bbe8dd2a60efeb0b7cc14a96bea19631891b4e6f589c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1939.txt
e2325866576528ac9d7ee8c241951e4a9e17625825780d3081e61b25c898288f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1940.txt
2b55348f6322b9f4217a074e9df28849077b45073fbc07466664226955006950  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1941.txt
f06a37c541cb4c983211f7c6b31d64d1670afbdabb23d71b890987b70c7cc8f6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1942.txt
0bdecee171c9755340c2c44d625b51778df031c4644dc75b24bff181d5b9c0be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1943.txt
222ff999cd78f738b32fc14c42d03e619b9062360d5daa29e1e501652e8243d2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1944.txt
873743c7461b1166d9d51286bc2cab56ae913ca3f4f5392f34a718ac5a36705f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1945.txt
ce7d70109aa3717d8b8666baceead357d7724f126034cea1a38ddd09660e1b59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1946.txt
01382b8ea79d81e61967217f394fdc9e1f8f90a086ff5a3108ee3b1771ef42e4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1947.txt
3129980e40fef4abdd2102d43504d5510612be961e0ecbc8fc3de76a6ec39d8b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1948.txt
e7348aebd9d777c26e43f4db335482682b3544b831dca8bb9d106ec6c5f3cba8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1949.txt
0314c972de4bbe426fff5fec598ae72e74d3c515570b43f62098e189122282e2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1951.txt
48ac50c973cd6f5ea980a1da3a9c425070dfa73295797c7876aa31e8d5244948  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1952.txt
8d10084b351da3b69c3323baf795b2b1f33bb737b7bbb1ce68e890c4850b330a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1953.txt
5d7e87904883fa7eece2159d45959413af0f25d22e181881dae99709e3249d2e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1954.txt
6ffbeac91ff340f1158678dd9b0879ef9edad9b69cdeff9f370f778183fe7715  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1955.txt
58e525fe9e5005c4059ef47dc6ce4206dba5e2284b3f66d864c34ed4b0af8e4b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1956.txt
99c4beab08cbf6e9d759dd32a4a924d2dda3a36f870fc86d31104c086ebdd95b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1957.txt
fef8b6bbe15685eb520099a20c5835ffdd41c21724ddfc7b787645975b53c5e6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1958.txt
ce6e48423941728b38771974a4dc319188a54c0a8c182c122fb284eb587f06f2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1959.txt
5d798b8f8b831b05572cfb29665ff6622eda6334c65c1feac3e502460ab4a3d1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1960.txt
e13ba9227e5faad0cd8f6c6ea008acbd860b2f0ca0fde79458ba209afac31c6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1961.txt
588e243589063e33ae62e70345bdcce53f6080bfec557a7079435f4449f5df8d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1962.txt
a43cbf9d230bb14bc9c07cf31da9771d837f0f2e7740b692e754202138602292  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1963.txt
4d1ac0f733e486f0d9831bb5962f96bbc0dc0b2152beb0eebbbec6e5f621fc07  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1964.txt
2c080acdf262c86cadc1fca4e7f4bf283cda2fd5ac98ecfa7eb4e0570724f625  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1965.txt
221e083f18e0fc4458f04ddfca4356df2a1b615d43eeb7055b3825fb2e828532  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1966.txt
c01062053898c8607ff02cb6d1ca0f9f047f854682066da6c752a64186e0dde4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1967.txt
7de7e5143f13d11f43ce2edd247a1b2f4ac7940f664b2ef82a3a6393528f5398  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1968.txt
04c2f34e65a44612ea9115ca439c8102d570a4efa99f5204f31fcb327b51bcd3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1969.txt
1203ba2af4849868f94097e7811b00d8ecbf1795d62ea1486c1875545d42fc1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1970.txt
23932d730a52b949fa2a99e8c890fd68a44df68e245afd70fb76a163c2905822  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1971.txt
3c032b417f47882876b7a7af8a2c82bd9c2ce017c461f3d6c53813644e1c8924  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1972.txt
30ba20505223fef751e07a04cd83a8af9b97c20bd7bb38a9b37e93a3f865360e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1973.txt
f670e0604f047964f9a841ed17ad12f7c0603d0ec787a6fddee8129c9e633775  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1974.txt
eeb82418e71e619d3c6b6273f48036e9c6ab331f16c34cdfae3d7aa390d78c5b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1975.txt
24de081630e23114460293e1902ec97005e834c7ad4ae18049c5d2053ce6bf6f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1976.txt
8dcd066b5b142da9c4622311b533f4de6d3caa25f718b6cccb72bb4eb9dbdfbe  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1977.txt
6dfd1173c3195781210dc36754efbd847df2a869a453061e4a19fca421371b69  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1978.txt
7c2767f7a7de9ee667a01c455448e15f72a95875635c2c30f000274cea94dfb5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1979.txt
4402235a2f5856ee17a87f9163e03e67fd39135e0599904daa4b430b76be4f7b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1980.txt
c5e147f58595ae89099072a603d951ed594acc750bd81259dec98857918e2226  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1981.txt
56f749aa66c05e2de0a1c3f6d3f326b1573ae201cd38e691bafa8227e6e1c569  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1982.txt
af1dbf3ba56f4498098dd646a7002ce3af1a55a1d39e6997f41d9777f021071f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1983.txt
67e4efd8599fbc057034d879f6e06501249089b68e41b6acd144062bed3c713f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1984.txt
39626600b28ac2255ea66d1aafed278cfad3cbefc8e59b65530f68c86a7e534a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1985.txt
f918e85cb6ed0d7b3b5e22b8c92577daddf4509b73d31edb94e9627ca5f63f1e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1986.txt
f9dfe77978d0e450d6d41f3c1b5364a64f21747fbbf2bc91fab0f95ce2f8a682  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1987.txt
5a9bf4d9e292efa67ca32cd0d1726e44afd4fe34ba09d491c48a5cb6d7cb42d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1988.txt
fa9de45e5b48b665c70b06ba3ea60b1a8b61e0cb5c23cab07f6451a52e57ad6c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1989.txt
7a0026591d9eece5a75fa44ff66dd59eab6b6450c691065a652220dfd2e64bbb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1990.txt
31b0507aeba51f2fccc14f653940c291c8cf25a063601cc75b763e630bb29d2a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1991.txt
b289ec613b3b6489e0ad8bbc20382142870f93da84d6e8f91caf0490d028d7a8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1992.txt
897fe71a1207b1ef4dc61a2776a0c1ba673b3fd1647a8a54e4dd000d00962571  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1993.txt
7de8d30d147b6da8e3d172468349d5ea7a0d1efbe91864398b4409f054fd3ed0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1994.txt
016ddc544a51b0ba501e2a095c92995baf24322d0743b5e08ee9451fb1917f24  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1995.txt
674686f6551d5c634d9e7e8663362fd1454a712f3648a330bf57e6592591ed29  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1996.txt
880227b6f3f4f4c6571a459163ba2a62d99c27e4b0ce51b3eec1e2c0201feb1d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1997.txt
678b608eb118f94dce9a3ff21a599b3d062c677511de489c2fca312d9efa1df6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1998.txt
4e833b423c65795446280dbaf968e50e402089474d57bafd53b7f7fac5591a37  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob1999.txt
cb55e7524f97d6d8d904f96d02aa07d5d270ec86c26eb052e045f0e7e716e44e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2000.txt
67e6e70b68b434f45944e9e955da29fe7ad3a2951c79fe6d5d676f2af0152e7e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2001.txt
8c454ebdd41d3cf2fcec8995abd6bd2c90f7ad29790c3e7a52b65f914d18032a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2002.txt
f8efac19c208bdbb4b614a3811a04fdcf5d769894ea528682492db2de7b211a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2003.txt
7f63575f4122896b5847ec3311480e22d7e250a3926ede4aa710c7d9849266bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2004.txt
fec80e345a4d70a56dc391a3ce84b4010901d7d9cf44049c696d4cf3e5765dce  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2005.txt
9280d2cdcbdb57eb6b6b55a24c5f5baf8db45a1f3f4e16f5feb826fa46d1dedf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2006.txt
78b8dd1f9b9f5dd476921bb8b413e997d1f75062827e96cee1b23e2a3e1432aa  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2007.txt
5a18ab8a52caccb661232439d01e1d4ba43db77d3b539bd60790a36f7aeaabbd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2008.txt
6a73ef384d30bc18611038e3c884d70d5dd6e14067111a4288715b7636611e5d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2009.txt
94c27249389f0f014b13a481bd5eea357f4d152fb184fffd3fafeb813ad4546f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2010.txt
8ce48e1bf90aa9c7a39e5eefcc9ef32dec5d63fdf858625036d5b0f76795a2eb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2011.txt
18c927510aad45770129f74dba7241f158be1572ad69848a3ebd6989d24c2aec  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2012.txt
363e608862b9509b774a3680fe23693a929bcec8b19b670692335686c600187e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2013.txt
a0f47598fdd1377b19025a6d70cd90ca2f0becf0335dc7d1e5bcf8b7a2a66a91  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2014.txt
d7d8dc754642dd25013051181aeb87ee87ad4f110689101c32c04556cc191bd1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2015.txt
04476e1860f28cd6c5956f1a3cf763402c91e818b98a6b969b3ce878e45b530a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2016.txt
c76d674b4800a93bcee4598ef8111a17b4a68d09260012bbfbc5c5a99f858653  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2017.txt
ec2bdadedaf23ae105cf1274b90288cc42f97c3959be7ae32550710e4d3eee74  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2018.txt
3e8c9f819ca782ce053252030479ad454faeff3679296d542827b66b38dac9f3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2019.txt
0cdb7f3199632d58e9e132706f044f2896deebf04c7fab9b8354334c9beced59  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2020.txt
e6c581afaa821984152eaf82757483ca2dc0b6b1d8c091665d961b33a1e3dd92  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2021.txt
b961e6e6bde668f9fab0badc0fcdccc4afeaf4fb66725afb2e5840310e5b2c56  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2022.txt
5c1345ad246cb13a5521aced224d407a4ce704286d8b7af786ac48ab0fe13d00  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2023.txt
f25111d4bdf7fc6844ea54ec73a3dabb83d29310795429c8f9e936f7b35a0650  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2024.txt
7dcd38c9f6629b15a0f85213d24a949cee29b0fe64e90fc790924941655a97a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/missing_year/yob2025.txt
e3a16e083702d792a6291abe3020ea109c365882060b91776b7394ded22e8d3d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1880.txt
19427aff61cffe41c9040b4339614d7a2633441e3a7082951b42600805bb0d9a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1881.txt
e23edba61aec9bb1aee1405aedd721c2693e6f84145b27370a6a7807c1f5755a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1882.txt
ff8f2a49595fac7a179d629c709d889f5892215d939178f37a17c471be3fb767  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1883.txt
12f07df8be9c8c44de2fc64f84b24735d1e0a4f5ce26ee9221fbe8f7227bc512  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1884.txt
e4b756131eed0f4794dca53a09c37b1592fde241fc98fd8d6c6a4a1fbebc5678  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1885.txt
78eb17effec28f0aabee306927fb495739575236f937f5de8a17faf159eadc02  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1886.txt
b066a61d818af8be1e4e4a0e8668980af1b608a80f4448e34a404466e08c2e02  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1887.txt
7852dd2275b13d7394a9e2c732feb0adc0937c1ebacc23516786cbffb15ff94f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1888.txt
6123d3022fa11b0e3c2964a0314c0846cb77238513129dc462f250b6a0761752  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1889.txt
f060f2b2760d62d53ede95faea6acde45f86b6518b04f6371a3206a13a3b1dcd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1890.txt
3bc2098ac512ed0a4824312f77d8c2e2863dff47401a7be3dc8f1be8b7747fed  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1891.txt
f7afd6c1b8a8695c303301bf10e47551ee202a811395cf5e6350fc3d612da4f7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1892.txt
a9299b0853442f4e3bfd0fdf10a50610a0808e0016517c51fb5cc8860ca3df6f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1893.txt
b993514fc97ad7067c59d96c6427860485516c553f4f6a3aaae9e1a5b544de89  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1894.txt
e7ba8f1039730fc01f05ea29ba11db9e080dbd6e4f9723cefe8f2182e8f7b526  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1895.txt
877ad69f3ce8f83216be62d96e4f1744cf6f7588cbed4b3227e03738ebcb42a9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1896.txt
0ad305e8b77aeb2a93758cf5e7d871a27f66daf76b9ccae1b5ae760a461e361f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1897.txt
91a835d34e5a65533e41b0f7f8fae06945b64e184ad90b9fff39afa0116435bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1898.txt
a56ae6a8dc9f7198ea7f5daecb17f4df4749677cc6af02422d16454e99a4c859  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1899.txt
e06a508a9c3c433c20bec9a7e6ce9ee95b1487667b0b9faa4a367bcd2e840369  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1900.txt
ed468a8facabbe80ce7ddcb9f536da9a4dcf6b89a07954d4b6a8f3a3cafeaa63  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1901.txt
22d69195bfeb7aaa9abaf62144c9e440e96b97c840cb6f1b3999d97fcf2cdc8e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1902.txt
4e13e83f582a81cbb6f5f56aa18d65409d8755a026bde5951307d56912433488  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1903.txt
4c5c1ae50910bbada3ff48c62860b839d6e877ba31f3d30f24e3352078cae51c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1904.txt
f86c3c3b1423fc9f42d45f88746ae268ab0b3234f147d5c9fb920682e3d02737  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1905.txt
e12e14e3860ec11c2c001215e2eb2fb5306f8e83b4e172c45395fc94db0e5877  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1906.txt
df2b4bac40bb4e24a912ba43a0967eb2f65d12c7e8944df30379465b1fd30c1d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1907.txt
32062e577b3601317d84a5f201bd04275924ba08f4b3684c7e97b3a4a8869928  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1908.txt
4ea9564cc8485f8f25a99bb7170b838c1815aab2c18e57f7b45d1f041b91fd8a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1909.txt
d9698e773f59890ba22bbb8e17d3874fb9a4b9c3ff2486e23d1452caac6aab0f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1910.txt
f2ac728e2128f18f212cf709ace9499b9daadccf94333f9b64ac7b3a357c7874  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1911.txt
f0c54741cc23d6511754c5c02ec8d95ab958bc97bcf6800c066f9973270173bc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1912.txt
4f6c8f2e007a7318903a63bedf0803c0172b306ce556bebb16acb5ef5f1e47bb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1913.txt
9a57cd9e7c80bd9f0db2b7658e98bf593a16f5dd6cdf05f15c9d2e1dbe91a105  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1914.txt
a4587d5ebcd17a288509a37fdfa691f7dc78fe74422d00018b80e38b518585a6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1915.txt
613ccb7be7650d910b16f8cbd1e9d59f8935ee1161a3c80447b7bf047e303f9c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1916.txt
56dd45af6b0f0c1ad1213ae1d76e1c9cde56c93cc0fa4c8c096de9d9a1cb2b87  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1917.txt
ec870c20d3f8d45f3d643a4ca0d3cc91ff43f5613a20dc0a29130485bb4dff65  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1918.txt
7eccc670bb76b47e93eb5bc8bcd845e63b9adab7daa1844b46799e81faca1a5e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1919.txt
bfaa3df28175ef51a557bdfdfd26db003abd76e1760e6c114316a4d5ffe07690  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1920.txt
4d7c48fef5e8b8ad6e58a110594316c7631d56a3f2c8d17d5cfb7efd1d652f25  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1921.txt
1cfabcc6e1254e49318fe8e67fccd7579142e749b9bd1e364f7943fcb05c6c11  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1922.txt
bf21131d4f813e7bc72888ac94f35edafff0d6139aff2e1797fc86f7e1c6f7db  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1923.txt
fc6e7ea86d4de462b55ac1a957bde759cfcd84f019df6cbbc9ef676c5fbd3789  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1924.txt
2246a42a100817e70968c0424cec6038d5bb9c2bef9599297ef514de74763312  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1925.txt
c0ed98d01086929e9bab2776d5bde42c53ad0f123011125bfc3432c78da7a2a5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1926.txt
71522e0d9489250a6bd249c6c2f5e82492561d7516961c5ee09416e1b1dcf315  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1927.txt
9d604ab4a403992e79f39aa492f3479e72d6806625311b1ee59f9d180058f0e8  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1928.txt
b832f522ab8e625cf6d55f0be5f860722eac877defba13b2f9c463ad37092700  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1929.txt
928f199618313da25f3014b3e60d21fa094e357e480ab0c49bcd0d0557029f3e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1930.txt
c2f3d2420f7dce9b311d4d44d8ca6c66e6a35ad9c262b4a37d04833c99c273b2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1931.txt
2a095f5aebd2940612a97184a82fb4bb4b95cb8f9e58643ab29486ff0a09a58b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1932.txt
ba01915171bcb7c37ee618816584d397b05cecad230767c6902edbfe380bbd80  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1933.txt
9b1da0b211126618572cf3a24c299e828b1eec2c619d70f47438bcc374cc77d6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1934.txt
0f0643bc80fe5691924d49d417aaf12a5fcb0d4e7bc8388a17a4075bb8b04278  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1935.txt
2f1b99d93e521c255013a6cad8370fa05746de8ae470210ebe711c3034aa771a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1936.txt
311e591dc5f80b07ae00ccf1bd88ba515562bf58824fb716512030a13e73856a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1937.txt
4a05f421ceef5147b8e21d428b330cf51f16ca959485087dc94b9a0e6fb6c469  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1938.txt
5014cb07c5a0b5a11a6525253ae57f5da547eeb5c2f71f52042f8d794206d4da  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1939.txt
2316884941ede37e74947a1cd48de6f43016bf5ed8208e71efe3c27111093819  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1940.txt
496cf0ed56e0165026f747df708757ebcf71b154fd23e25afd1d88bccc1b9dbc  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1941.txt
6d922dacc5e296924c6a2d20ae5ed2e0863c5f0e5a9155102c4f87cf448f37e5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1942.txt
a615b3708213ceacd52e7010e268256c61cc870d9fc15f4999f60743cb0fa41b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1943.txt
bdaf1e56d997b4976fd94fe6df3bf1e7b8082a0975cc5f0e3acc2071a29f966c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1944.txt
464576f960d31890d02b795c3af8a13694ac05e1254c4136b55a11265eb94f6d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1945.txt
ae83c402c8b4df67f15e28554f4b0d39377637e599df69071136554ae20b5934  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1946.txt
e01fe4469f3f4300ce4acd48b10cf2d4771fd92c359bb314946543589503b841  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1947.txt
3081e2c7eeb0f3159d5a3df0586ef8384ca40084145648044053f79f8ee2b7f4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1948.txt
a1076708622b971b044167bbd27ba05c337550c65c8ea6ee857c81858456bf8a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1949.txt
347b2c88e453ff45adcff9a6b00e30dd252ffd620c8da322f7b366a752122310  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1950.txt
b7024da43e69f97d7abd017199a12de845e984bb89f80d90eea9e1618bad53bb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1951.txt
830908389645bc30309002532a65cc8a2841cf73ed51a5d0173215e9099eedd6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1952.txt
a2343dd6bc6b49d7a2cbc01e42a9ea8f1d2fe6c9b7cd12e7280bc1b031ec2280  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1953.txt
7ec20ca4cd6404b367ffc235bb6da0f22a9448773e7838ad61522e7a7818cc2c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1954.txt
0e0c14c327e3696dd79a1d780383edd9bef3b08fd64707214c0d00b29f66bbb2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1955.txt
96caf0a37837e4e14682e67af0a1710e912b11198e865a17e1fb80599bea80a2  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1956.txt
53ec62128474804b42c9502812ff3128a3dca4199d5980ff37eeef0df70753bb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1957.txt
19318ef72a74045dc5eaf634a20628ddbdae062dffafc5ad68004f70390fc741  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1958.txt
25777886c0374006c4dc0767d4cb837d9d0dfb9b7b0427a35008cd815aae55e9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1959.txt
47b8ce86321c2d5a0a7357bff5c82ca1d2a56a28fa55e20e95ee4a158be5c18c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1960.txt
a2d651447cdc116f6381db2acf8be38a6b901000153ba0391e086e5a0e27dc13  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1961.txt
df5debcc64fe12291155a22cd4bfc4025281c4a96085f747d2ecabe6e80efe1a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1962.txt
70de783f6bcb22ce7544c5d1f1cc7855c6e03d62ca40b3a3cff53d138944ff1a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1963.txt
545ac6d4264f745fd5601c5cd2e3794e7c57e381e7aec88683d2ebc5fc182592  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1964.txt
4353c2ba928d70223e08ba09dd5d3fc0a9e1f67aa32b4cfb109c10754c6297d7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1965.txt
2b7e76bafd46af3a2a1a568cd410381c57a0a91fdce11842accd177aa8d0c39e  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1966.txt
9a84d185b9a6f65657f499c6869b0ab79f51d161938d611fbe5e05041e5f4d12  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1967.txt
739607db0eacf45edb5e6078dbd8afb697c827bf1f29fca08f1f3c1998afd7b6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1968.txt
a1de77408ab96e55dd0105c9bf2515d823d0aa1e3b9fa57f78cc69cff691fa45  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1969.txt
dc6efc0edf4b274fbf0ec0790892244f473815bf86a8f3e5c87300344927576d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1970.txt
0ba24673d52fca6ef2713e9d2fa4be8a7a6db6cdc353e062a8c60d1b5f576185  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1971.txt
1dd799eb925479bf94396e4169cf624c7e4a9a039d5006a541fe50edd7c6066c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1972.txt
73f0dc42de7aea9cad24e8d948844084c5d546db1c4c091fe63254d10122a899  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1973.txt
cb910f61b9658a6c39207a40c808c6e66878befaeb51bddd93baa9713c33cc76  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1974.txt
7ba05842eaec77af83409ca2e3fe0aa6396011e61a819c9ff42b6daf8326eeca  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1975.txt
e0b4f3bb3189c6f1c72be564fd171a88c7a1a226e73efb87ef8270fb34dc5d73  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1976.txt
29582ccaee7614b5dae8acb38e23963af16dbb63fc5d3586a98f0ec4f6ff1833  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1977.txt
8236b9c9a78a8bfcb744959920bdd37659263e619df7f4f9869d1be3989687f1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1978.txt
7d11ec0345da65f90036f86c478a6794feafaefffe1d2e88cf1320694a5d9cfe  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1979.txt
98a4dbe6366a49394951de3e16bd2355876e5a307741ed4f88960da9edd33e4f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1980.txt
ecd16b8768b390128f036dce2f568904ac9d51018af5aa3d4286cdd1cdad4b10  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1981.txt
6b926f1f3ba3a5a027ae72d9fd273cc511ca4bb5f849be8fd030fe3548287dcf  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1982.txt
85b70d74b2cc423188da9e0d7ae93e7abef18779c2e670881539c684a080dfe6  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1983.txt
d141612c4747e2f7380432d7b2549031e933c6c32139bede1f6f74fe02a2a8bb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1984.txt
96c654c8a7f0cdc27d7c9e511c76ffb093a8f45f7e65d9b82e911dd4f46b3de1  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1985.txt
156fd2474cea419bb556b82bfd5b97370370bd565fb5dd03e20670de68c80b23  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1986.txt
94b565fa1f3f13b060969be1866f2f81799d17ad84d16c8623ba38ce43643f33  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1987.txt
a27b33bc2c0647933e4e8c90e54dda703dd4fdd975a26fa6393d19921cbfde92  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1988.txt
707c25999f9b52d7ac8ecca58d5b135a7eb73dfbc13efeb56337c0944cec62cd  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1989.txt
401f8a1cc230289e567a89b7fea42e9c8f1493a19c9d5f6ec40d898a69a76d10  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1990.txt
ca244fb994269efd7041f4bbe1b7ff16b5803eabb38da643b821f9cbb6529dcb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1991.txt
2ae7895bd826a4148050da9b5afa1141087500966ccedbbb3ed2c052be289139  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1992.txt
dbb979d7a507c9b21a957b1e42abb5f1a253a75afc56777d4ae86239e1154be0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1993.txt
08777d2c6f26a61c8331a2bcbdaadde027c3825d8787205f3bb201d8817113cb  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1994.txt
ab35408028692eda5e5a00fccf8f3060ab8d8f66a86da30a8f288fb1422244be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1995.txt
491ff4f348de46d5468bdf6943eff684a62c6bd7e75a3d80e272fca95f5b068c  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1996.txt
ffa851f95086b779ff9cb7578671945fe3484e8af53cb999fd433bddcc5dad48  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1997.txt
10e4803107228283aa78ad6095eec1e9fcd65b0f65e67b0ea8bb619602d84725  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1998.txt
7ad75c19cf0c08c350498ebc189fc0118bdc0d21acc4499c5fa46b065ee6e313  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob1999.txt
6c688a23fa0839ce8c1aeee62b019700f1fa78bb2b998c004aeb979c2259fe9a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2000.txt
87c696900540866b25dbb7a6b5bfeb05ece2c814be4dd4494458b79f3c84a435  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2001.txt
c76ce3b4256063708ac09f4d4a8f5bbca8fe68bd74238fe25e49dabd9515ad5b  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2002.txt
e9ef9d6b24c54f4dcb7fe23ae9b54b807e78dd515d300fbd58b655015660cfa3  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2003.txt
a6eae174d72fff1cf5b61a944f03172ec3927dfe86862ad589293de566483c47  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2004.txt
31397e35a89a25d4de4f90c353dac341c2fdaf07900ec0518a7c3a18c65d5df4  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2005.txt
64bcbf69fa953659d5d5f8751de25083051da58ab3002e4516f92053277ee6e9  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2006.txt
a0b11547338440eff89803910e7a4c11c65cb37df4e02430dd9fa99dd654e74f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2007.txt
f708abe149bbba996143a146dfaa3d2bbe74dd25cd4f1ee25ce5b2536485458a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2008.txt
7fb9620d12d37de0c006f2e1c6a1a7405fff9605027ec53cb61f5e2b3af44375  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2009.txt
beca845bed18d9312935e2b9dd91c6974ad465a4436ee476256439d35b238065  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2010.txt
613ec867d2e27308e8ab71fd7948d0f48c3cb6b5f03f95381c8ff1417dc8090a  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2011.txt
2ee353b0964f8b5c24913fd0929e417c21c75ff197d590941b0d865cb05b86d7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2012.txt
91c375c47b0211b518fcb4911c215bb712398867d26ee8d03eae943a8b16b0b5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2013.txt
162edd518fd88632e067b0c3fdadf5238555e1178ed2c0204ca3b863cdac77ee  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2014.txt
084a9d1eb2181f7855a50338cb5b6e7dc14a3259addc5722f3dabfd0e77a2cef  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2015.txt
502b5a2b48a96dfc4981ae867394034b0c0c0d9a86e56dabb1f2690ed67de1c7  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2016.txt
bcfdbfeaad1fc0353a3bed1c5358eba7d3f5c6a6357b645c87e6eef2205a3d03  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2017.txt
4338ba53f885a326863551f0e1a29b63c7a0f211b32e6327ba4cbd76a6eef14d  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2018.txt
3eebee5ed65b67c87d0b4997c023f1b3ef2057cf69cd04e781ca0aeeb4b8c1be  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2019.txt
664ba815a928bba42080d26dc726adaa7d876c12ab16d7f9223e476477feacda  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2020.txt
ef8277077817eefd2445bbb7b376a3b568cfc4c15d99d8e16119df9fe480417f  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2021.txt
3f24e2ba7430ecf7079c4a497e1b5c6fa522be7d2cc1f4f7a7384b585fcfcf06  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2022.txt
e43ca522c84730cce7309cd5e687503c1a8fc5c679750c419c19d8b9f4cf9dae  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2023.txt
a6f35d34640ea0db7b81617727157e8f8095e20cab5dbca610462f6adb85f7d5  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2024.txt
f43021fe485fdc5ecc9a914e0dfe2a1d14c91f0536dd54910320f710f8ff4bd0  p_konum_plus/calibration/f3_step2_rp1_f1_synth_fixtures_2026-10-02/zero_variance/yob2025.txt
c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b  p_konum_plus/calibration/f3_step2_rp1_launch1_stderr_2026-10-02.log
445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f  p_konum_plus/calibration/f3_step2_rp1_launch1_stdout_2026-10-02.log
df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613  p_konum_plus/calibration/f3_step2_rp1_launch2_stderr_2026-10-02.log
d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7  p_konum_plus/calibration/f3_step2_rp1_launch2_stdout_2026-10-02.log
915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45  p_konum_plus/calibration/f3_step2_rp1_launch3_stderr_2026-10-02.log
7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d  p_konum_plus/calibration/f3_step2_rp1_launch3_stdout_2026-10-02.log
df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613  p_konum_plus/calibration/f3_step2_rp1_launch5_stderr_2026-10-02.log
06b1c9b4874e26a6ffdc4eb9bfb5bfb95a4cb1675c22e4ed50a0b18142c12034  p_konum_plus/calibration/f3_step2_rp1_launch5_stderr_2026-10-02.log.sha256
cbd2281e5719911a997ddf9103707d50adc74e7857616aaf443f9b0dd815f715  p_konum_plus/calibration/f3_step2_rp1_launch5_stdout_2026-10-02.log
86da51d5e818413ce36fcdaea593cdbe995229684af32fe55d655b89ed09d3c8  p_konum_plus/calibration/f3_step2_rp1_launch5_stdout_2026-10-02.log.sha256
0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d  p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv
3cc9e168d2de91f83fba807cd658e05aca14d8bc85f618d69e4fee052b9c44d6  p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv.sha256
6b98e427a819f0464adf1ca100183905ae51f24de140cc4bd4c1a9bda42d5739  p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv
09c48c90d1f69328fdf2eb9d5ab4cd2063fef237d7a6d1f9098e973eadc17ad4  p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv.sha256
41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a  p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv
fce594636a3d2315092d4d9809658dfee61624ff2e7eb4014ba75e768fd5d80d  p_konum_plus/calibration/f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv.sha256
ca355af467f66a05b19e82fa3e2f515ce41a253718b0120e30fae6338d96a733  p_konum_plus/calibration/f3_step2_rp1_restart_store_manifest_2026-10-02.csv
423ba75c05d4909668670612f49098902f5fd0f82f746868583ae20b0500ea11  p_konum_plus/calibration/f3_step2_rp1_restart_store_manifest_2026-10-02.csv.sha256
6ae8ea008adf77c2af4e24de646d8c280aad5fbf330e0e6b9cb2f3137a7fafb1  p_konum_plus/calibration/f3_step2_rp1_store_read_log_2026-10-02.csv
23e29d378ee19e8a60ef10c07f6fbe9e17b251b3ecc63a5fc12e4f8cee8f8f1a  p_konum_plus/calibration/f3_step2_rp1_store_read_log_2026-10-02.csv.sha256
790cf31adb25b33bd8feb82c3cc00046f61470ecf02a499c581b92a4cc7373fe  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r3_2026-09-22.csv.sha256
22a5ae8f9cdcdc2e715cf7374603d1a9899a52fce812b1fd125713eb6f987c88  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-1_2026-09-29.csv
7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv
d7f689fe5e9fdac3b6084e28b4e9d7e433a0d04d1768a72f9315d3acc91c80b5  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv
ea9e877f5663d45915832dfc9c91231d06ab631ae083bacbadfde1d67a8d1395  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_r4_2026-09-24.csv.sha256
2648cb7feeba22f54c1cb27432d23c885ff3fb0d939ef28a596779b8a5390084  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv
05fd3cd7d42053e01f686c575e93284d2512e028205a92f47bc2978ff5bec42d  p_konum_plus/calibration/f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv.sha256
8a801fde61fa5e13fc0ec268f39d6d1ff120a9094302d273a92032bf534cff65  p_konum_plus/calibration/f3_step2_telemetry_r3_2026-09-22.csv.sha256
85cf7620b360a0f5d999f121d12ded79fd5f805ecd55d4103ae73aba267c7167  p_konum_plus/calibration/f3_step2_telemetry_r4-1_2026-09-29.csv
3fe3acda8e6d1ea53ca2b137f25f5277dc97628c33119c90f81211263feccfb9  p_konum_plus/calibration/f3_step2_telemetry_r4-1_2026-09-29.csv.sha256
ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d  p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv
acc9e0ccee5085df92f5bd9fc2bfc99e8c5394e9409e0d64bf66a6135194c427  p_konum_plus/calibration/f3_step2_telemetry_r4-2_2026-09-30.csv.sha256
11e1e721595cb74ce458a018d88dcd11efbc9448822d716a1c11e4864f3a3910  p_konum_plus/calibration/f3_step2_telemetry_r4_2026-09-24.csv
61cc185d764c6a4386652f724f94a324b14e735a8fc3dad5cc12ddd04e113b8b  p_konum_plus/calibration/f3_step2_telemetry_r4_2026-09-24.csv.sha256
836076827ae8b30d712191f5d3507dec6b721824acaa81bae491401d2e8f468f  p_konum_plus/calibration/f3_step2_telemetry_rp1_2026-10-02.csv
9d48382757e25537f176409283d7f12fffbc504d35ab1e50d9485e94c6f38d33  p_konum_plus/calibration/f3_step2_telemetry_rp1_2026-10-02.csv.sha256
5e99371a02ef30024ca32c90c6c254df49578ac01a714797d334669bee0ceb12  p_konum_plus/calibration/f3_step2_test_evidence_r3_2026-09-22.json.sha256
f74dccf0dfaa650a40a2bb790d36c465f7106ed5030354d6677bb84e9b9fd2cd  p_konum_plus/calibration/f3_step2_test_evidence_r4-1_2026-09-29.json
15911bee3a6f181e9674541362fee1d60de01017fd552d7235afa4cdb4410e33  p_konum_plus/calibration/f3_step2_test_evidence_r4-1_2026-09-29.json.sha256
c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf  p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json
ba78b6d41d9e507bc002c697d0e75264d3727e51f47ad32a696b9a5c6a92eeb6  p_konum_plus/calibration/f3_step2_test_evidence_r4-2_2026-09-30.json.sha256
118c35076263ca040692d2a77188cc8dd6503cb8489babd1377febe2a4d44ee2  p_konum_plus/calibration/f3_step2_test_evidence_r4_2026-09-24.json
8a86e0637b6aa250d728ce5cc537642042757f99c54cf6d2300fe31b80e169e5  p_konum_plus/calibration/f3_step2_test_evidence_r4_2026-09-24.json.sha256
809e9d043d136371fafcd158d5955853f61e67490db370d1d56761b7f8e6578d  p_konum_plus/calibration/f3_step2_test_evidence_rp1_2026-10-02.json
f7f2cd1c5d206b1842f8351a8d4bc0263ee0377490a555351eb4fdeae7e5db43  p_konum_plus/calibration/f3_step2_test_evidence_rp1_2026-10-02.json.sha256
aa86f1ea635780a9d50348a02e280340dcb461914045e4015b6da1c7043be9ac  p_konum_plus/manifests/f1_input_hash_table_2026-08-28.csv
7e5a0e41630344b95885380a659023a292dcb259b866c70b289e4e48d26becd1  p_konum_plus/notes/f3_step2_r4-2_karar_kaydi_taslak_incelemesi_2026-10-01.md
721243ff7fce42f539db0bc3fa895059e427120538772d72aa05e9f5789995cd  p_konum_plus/prompts/Claude_Chat_F3_STEP2_v5_section16_feedback.md
a57b6fca304deb82d2f48ef4b1b30ef545d250bd5a21009bd2390bf72effcbd5  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md
aee40b3df003b6184810fde221a75363a1066d6e322a14248c2d2f9de13dae4e  p_konum_plus/prompts/Claude_Code_F3_REALDATA_PREP_RP1_INSTRUCTION_2026-10-02.md.sha256
adb59f60e7c1a72b6e901b86d1958a874f09c1301003b32c4884816fe43ab792  p_konum_plus/prompts/Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v1_2026-09-05.md
09df38443346229fc2dac0afb795e6c5cd6b621fe1e4e6756316c43416e96f65  p_konum_plus/prompts/Claude_Code_F3_STEP1_CUSTODY_IMPORT_PROMPT_v2_2026-09-05.md
da5a0a137296954ae737db4c3678ea0d8b806eece48ca448b87712178b4eb6b7  p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v1_2026-09-05.md
2860fade8d34e74b8ea77d22d469fa0c9b29e05eaf27310b407a45031a626243  p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v2_2026-09-05.md
4f2b6492f74b0dea7f4ff09eeff24b01d785158238983015ea0c600f5fe134a7  p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v3_2026-09-05.md
bfa9b7d8114169712cf9efaa57bfde0e69356a2f6e9c6facaab22147f72ee458  p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v4_2026-09-05.md
679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09  p_konum_plus/prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
b5ce12c368628ade92ff96e5132eafbc18ff57093d8e6b47a3a775458f00ee00  p_konum_plus/prompts/Claude_Code_F3_STEP1_r3_to_r4_UPDATED_FINAL_EXACTNESS_CORRECTION_PROMPT_v4_2026-09-05.md
17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376  p_konum_plus/prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5  p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
a5399a0967885a7a5c25df2f0e0390dfae750892b7b54ee2a2eee1b77ea78abe  p_konum_plus/prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md.sha256
283ac4e29b6a42faddb3565adfdec41ec6b9ca949395de7041de622b2b704330  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md
36f7a8d5d94d6a07d0e398a463731eebb215d11b4d32e4daec4fa05a68ee3f49  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-1_CORRECTION_INSTRUCTION_2026-09-29.md.sha256
d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
7c296528442c0cf749e1dfaed8842ee7938c611b2faf46d2fd68a8a5c8ed10ad  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md.sha256
e12839587153cd9ee461d0697f431d5ddf740e8eec5b82741fe478333e6dd387  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md
65c102177fa53eb63047abfb521e3291063429d0cc3acf00a8273e298984127b  p_konum_plus/prompts/Claude_Code_F3_STEP2_R4_CORRECTION_INSTRUCTION_2026-09-24.md.sha256
4c89577bed6820da3ad50d9651f742c4de33d3441027182b2696e30712847f34  p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md
d07b10bee34d5c962e514618f67f4cefbeeb78e7ab569c47d8b5271064c836d6  p_konum_plus/prompts/f3_realdata_prep_rp1_pi_dispatch_record_2026-10-02.md.sha256
da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498  p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md
c2acbf840f4a15c7b3b68b0b53db8994c4415c538520cce9655ccf1dacf52795  p_konum_plus/prompts/f3_step2_pi_ratified_content_2026-09-07.md.sha256
1ab17e44fd16d6c7f69a5563030ad854809e8569c3469275deda5c6f0aa304d3  p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md
a440e41ef5b38a26d7957e56ad35f43548dc9123d9cf36c4d154e64b41016e60  p_konum_plus/prompts/f3_step2_qualification_pi_decision_record_2026-10-02.md.sha256
11cfa591cee0a3dbb1eab0a14083484049a10aa7c9cfd65b9df43847bbcd31c6  p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md
8573ae450366759164d9f806e12379fe1ce5feedcef56ae812e4164907888deb  p_konum_plus/prompts/f3_step2_r3_independent_audit_claude-fable-5-1_DRAFT_r1_2026-09-24.md.sha256
4e62353630db3b7f681c0183bfdf4f0bc25a8961f04824fdcec6808c8b09e865  p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md
9de7a3ac49add24707a92912504686fa0622e78f8dcd25b9069eb56f8bffe9ee  p_konum_plus/prompts/f3_step2_r3_pi_dispatch_record_2026-09-22.md.sha256
ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82  p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md
ba79f6526d8e48f0338b49617033c8a80cfbbbe02a72c4233cfa9743ac08550a  p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md.sha256
a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0  p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
ca543912d1028400af18d209f55fd77f519597090dddbc887b00add5b538d9ec  p_konum_plus/prompts/f3_step2_r4-1_pi_dispatch_record_2026-09-29.md.sha256
9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575  p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
8ad88af482276b4a99a5fbc4d5b73e0788f99b12870c6d0b2b305a315d2e4a1a  p_konum_plus/prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md.sha256
aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae  p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md
60d9674eab99ec4303a9fcc4b0b61d5a8dc2c13ff2c438f1dc53ef9156dd258e  p_konum_plus/prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md.sha256
a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb  p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md
bb81fe6aed3aba75d5f47d91a24de7f2d0bb0852cd77f30372a377f6e80d4459  p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md.sha256
b721702785d0eca6de3a07793b2ec9adfc7144617b9726ac0a731d71be74219a  p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md
d6bbe533fb7e55888709d0ba11a66ee53db2073a01ae395aba7ffadbbf8c828e  p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-28.md.sha256
9c16abb5beb112cd014d4318049de167b45feaf358f7ad31ec990136543543f9  p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md
fc742ede2b76336f61c8045ddbf09be0ba5a174c8e6d821e3130e19aaee534c5  p_konum_plus/prompts/f3_step2_r4_independent_audit_claude-opus-5-5_DRAFT_r2_2026-09-28.md.sha256
0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851  p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md
cf5da5a5c84fd5f8309d6844716fe1b610fc4cf9e0b6c53b2041c59eb9545848  p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md.sha256
0b177ee4b1a9efc409c5f47ef3ada102e7795229e0b5761af45a64a33c607639  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md
6867f59ce1c6c19ff1554329e525bd2b2d445b5917e78daac01fea2882aa9a41  p_konum_plus/prompts/p_konum_plus_lightweight_review_policy_r1_2026-10-04.md.sha256
d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3  p_konum_plus/protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
d015c3cdc505cdf816764633e885605ce2b8c305fabaf4ebe9cf1406e24a458c  p_konum_plus/provenance/f3_realdata_prep_rp1_attempt_log_2026-10-04.md
502198d947549400dde84d065a86ce6ef7a8dbe3f2883791f760fb22139df01e  p_konum_plus/provenance/f3_realdata_prep_rp1_attempt_log_2026-10-04.md.sha256
5d36806b1036c4169870622e73a0f2c78b4c9c943c29c8902e4e83c6cd6a4d3d  p_konum_plus/provenance/f3_realdata_prep_rp1_c5_observability_statement_2026-10-04.md
ba4a60fb5642f10c2a7d01541d545b154c087711e77f34f9639ce10f3e6d2c36  p_konum_plus/provenance/f3_realdata_prep_rp1_c5_observability_statement_2026-10-04.md.sha256
6d8dbe067d54c50e213779e70b30c260def5ac75e516b4bfc5436cca5e9bd541  p_konum_plus/provenance/f3_realdata_prep_rp1_size_estimate_2026-10-04.md
a4acc679893341e1cd55194d4d52925e4b1a5181665bf82354c831680584c964  p_konum_plus/provenance/f3_realdata_prep_rp1_size_estimate_2026-10-04.md.sha256
a3ddcf1f2d5c5ce2fdce19b9efeb24ca0d461bfd7381c7f3505773363e37149d  p_konum_plus/provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md
d3b9424c7de0c56747616955ad0806765b65bd0fe0d08627efd60f2ad2da0ef0  p_konum_plus/provenance/f3_realdata_prep_rp1_start_state_inventory_2026-10-02.md.sha256
858091d68e09d8431864fda86b0d1399386d156b07bb2e37dd920d6f937a44c9  p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md
1d666c2dbf955654cecabae60afe95d59d4c700d3a6a22ae03482571425fa26f  p_konum_plus/provenance/f3_realdata_prep_rp1_transmission_list_2026-10-04.md.sha256
99b615d2c3ee0c94815af7793e1d8be669a29ef5d070891224d457305864a4dc  p_konum_plus/provenance/f3_step1_freeze_record_independent_audit_2026-09-05.md
a10c32c4170575748dcfe1a332a995b405f4f3cf888d5bde1e1301597de940d6  p_konum_plus/provenance/f3_step1_freeze_record_r1_endoftask_report_2026-09-05.md
5470d1eccc8b80627c7032a940e0dac99a50be57ab3392aeb442b5ccf09cd4b8  p_konum_plus/provenance/f3_step1_freeze_record_r1_narrow_reaudit_2026-09-05.md
a48c516b7976cd4559f3825f124cf91e266f7107dfd1c5962c7a8249d43a08d2  p_konum_plus/provenance/f3_step1_freeze_record_r1_report_2026-09-05.md
57c92d2df6f2b923fedbb1cef3671238ca3020f8ac02cc16eb553eaa9026e969  p_konum_plus/provenance/f3_step1_freeze_record_task_stop_report_2026-09-05.md
5955e86590d1c4706000e4e43e6d5cf692dd000ba867a3b26170d1c5548de877  p_konum_plus/provenance/f3_step1_r3_to_r4_exactness_correction_report_2026-09-05.md
9b070d4b1302ca5acbe19a8c69b2a67e17f823d5936f187ff47ff69405de2273  p_konum_plus/provenance/f3_step1_r3_to_r4_independent_regenerated_diff_2026-09-05.txt
a8ba561e6ff61f0d2d401c9b58598205a7c3a9282786e5892527d48e26c6a043  p_konum_plus/provenance/f3_step1_r3_to_r4_semantic_diff_2026-09-05.txt
84c2416560e4b103335d70db660e05995361da63b35070c72880d87319dd8eea  p_konum_plus/provenance/f3_step1_r4_independent_audit_2026-09-05.md
152db9556126c54e67c8cfbc3a144468f7bad5ca7111e15b8550b1d1f8111893  p_konum_plus/provenance/f3_step2_correction_report_r3_2026-09-24.md.sha256
e7939a220b26d61a53f2b025ca2b3fa3a94cd1d01a3b41ef93caafd013afcf3e  p_konum_plus/provenance/f3_step2_correction_report_r4-1_2026-09-29.md
7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6  p_konum_plus/provenance/f3_step2_correction_report_r4-2_2026-09-30.md
7d58a50f1e9548512fb14a317a54b981319128383fa4258e9b1084738cd09541  p_konum_plus/provenance/f3_step2_correction_report_r4-2_2026-09-30.md.sha256
5c9dea88e45d1dbbf990a8aa1b706948e27df5dfa8243f17d3fca331d2b42848  p_konum_plus/provenance/f3_step2_correction_report_r4_2026-09-27.md
572ddd0bc6abbc5f739d72c2282313c741b9d76d410f455df48e61b39da0b1b9  p_konum_plus/provenance/f3_step2_correction_report_r4_2026-09-27.md.sha256
bf72d3e5284639972d33cb21ee87e026015fda1dc3e4eb91e85a3a038455159c  p_konum_plus/provenance/f3_step2_correction_report_rp1_2026-10-04.md
ece4c126e9f55e4f6fe8d9211a955ad28676394dce765d5c56bc31f2bca2aa07  p_konum_plus/provenance/f3_step2_correction_report_rp1_2026-10-04.md.sha256
ffc90aabe0de6fb8bb2ac7de3c855032b979ad80122a94927d158e0c292166f1  p_konum_plus/provenance/f3_step2_r3_attempt_log_2026-09-22.md.sha256
feace2bed9cef15ecc34e164c1c8e56bc704f77a490db85090bcaa2f1518b5f8  p_konum_plus/provenance/f3_step2_r3_preexecution_custody_2026-09-22.md.sha256
ce2cbe70a5112531a35c673b0f5eacfd35b627b701f291be2990d72267b4e5ea  p_konum_plus/provenance/f3_step2_r3_start_state_inventory_2026-09-22.md.sha256
ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739  p_konum_plus/provenance/f3_step2_r4-1_attempt_log_2026-09-29.md
3bc4e5784b7d602427790619eafde5458fcfb63be507bf3801d99be3bc5fe78d  p_konum_plus/provenance/f3_step2_r4-1_preexecution_custody_2026-09-29.md
fedd964a95dad3a7c9027218c70616f65be8dd7e7ee4e7d128a89812344b61f2  p_konum_plus/provenance/f3_step2_r4-1_start_state_inventory_2026-09-29.md
b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65  p_konum_plus/provenance/f3_step2_r4-2_attempt_log_2026-09-30.md
b8d8b798b01ac32c914eabe2edadcf22a2b8671c89aba2e17ca6af8568925808  p_konum_plus/provenance/f3_step2_r4-2_attempt_log_2026-09-30.md.sha256
ae0f0768d90fa7ace69746ce28e79fa25cddac6f0478edb5aa835b3e442d019e  p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md
ae10b8c3dfd6fff438a2f14e754ffc70b7a810ec76761d06c47bc3a6eeca9fe9  p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt1_2026-09-30.md.sha256
766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1  p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md
287f38dbe85fd06145ddb984aa1c296a658c8f0eb00958e69052e7ec20813935  p_konum_plus/provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md.sha256
66b08a96ca25175beede8de711a348eea25dd034d9d996d78114844de7de74d5  p_konum_plus/provenance/f3_step2_r4-2_start_state_inventory_2026-09-30.md
52975b592ddbe24df9235e413e039e71d2b778f64e81e57740ddfb88fbe2f572  p_konum_plus/provenance/f3_step2_r4-2_start_state_inventory_2026-09-30.md.sha256
711e728d5dc16baed07badf09f6f89bfa0328eea2d3e9b934a1bbbeab87d2606  p_konum_plus/provenance/f3_step2_r4-2_transmission_list_2026-09-30.md
08b22a042f72cf1d9bbae78a7e3bbf07e38ae60f9041396b709bd235ba6d6bdd  p_konum_plus/provenance/f3_step2_r4-2_transmission_list_2026-09-30.md.sha256
8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69  p_konum_plus/provenance/f3_step2_r4_attempt_log_2026-09-24.md
d82c3fdc80f069293845e28b43cfeaa2531c90ca3c740fce4967bf588ab54bf3  p_konum_plus/provenance/f3_step2_r4_attempt_log_2026-09-24.md.sha256
0f1724ab8b8d9daeb28d8277b414022ac46823011e35ad87df6cf228c7c41c8f  p_konum_plus/provenance/f3_step2_r4_preexecution_custody_2026-09-24.md
8af35f8226f13400184974282d9d10d0904398390c0d7a7f8541650137f68076  p_konum_plus/provenance/f3_step2_r4_preexecution_custody_2026-09-24.md.sha256
f78966d063c9991c590ed29d14f5671d998184aa6515b8f658c0f956998183eb  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt1_2026-10-02.md
79751849125202bd9eedd391107d8f57c9ebf38fc686df404512333e704c218b  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt1_2026-10-02.md.sha256
f2d33d169c161d6d004570d7aa92c8241d136bf0bb9822e76c774adce6ec1aa4  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt2_2026-10-02.md
c6f686ea1ab7b1de5472d35d4dcdccdc4a117b4a73e4037f634afb55fb2fd7c2  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt2_2026-10-02.md.sha256
239adb3a69aaaf6feb070e03336d963cbae3dba98c41619427f5fcd79604154a  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt3_2026-10-02.md
ea5aef2d95ff8ec559a1d038b431385636dfad8f15e15404fd6b2a8bdec0b3f2  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt3_2026-10-02.md.sha256
49cc92c9f05fdc903479ceefc94011ade198d0eedc03f411c4c062c68bffa165  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt4_2026-10-02.md
e8a5b3518d6934dd5997238fb8e812e515bcad6a2c5ce304507571e6872c011a  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt4_2026-10-02.md.sha256
7e2ee506a2819dc1a0f579751dbfa552d2a472d50309fef2a2e0d1731a853ae9  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt5_2026-10-02.md
cb129755b8be76b65aa950a7b8777e72f0c7c89f60b27eb073acbdbab25fe71c  p_konum_plus/provenance/f3_step2_rp1_preexecution_custody_attempt5_2026-10-02.md.sha256
3bd9e7cfdbdfe9358f91792db12447594d86956cd1c1b185552cb2da4d94b787  p_konum_plus/provenance/nonnormative/ssa_application_calibrated_benchmark_v11_final_sentez_2026-08-26.md
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_residual_series_rp1_2026-10-02.json
bdcfa38a9b92e56b67db1b2695d46d20d107d3c9e865d154865ec8dea0d2234f  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_results_rp1_2026-10-02.json
0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv
57c37a59263270f35e74886df776f936931fdbafdb038d906b1cd5a2a72ffb08  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv
41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv
80598c6594fe6716e79031cc33ebc7a675d987807cfd953695ae0f63df25743e  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_rp1_restart_store_manifest_2026-10-02.csv
664cb224c0213a3c444bb18ca676c934e622be71caa6a3c438cb820806ba50d2  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv
8dc73655e7742428110ea78959d612de7b0c0bf987491f63e6b9808c7679aa2c  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_telemetry_rp1_2026-10-02.csv
433245a940950c0a741beb8334c232925096f5282a99eff325891412da08bc9d  p_konum_plus/quarantine/ATTEMPT2_NARROWED_EVIDENCE_MISSING_f3_step2_test_evidence_rp1_2026-10-02.json
3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_residual_series_rp1_2026-10-02.json
19e06629cc54a28fb86242e3972bc51d2eb5119436b754f64fc3d958a6bd293d  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_results_rp1_2026-10-02.json
0192f7dd92431adba0afb59fe86fbf18c458b96d3c19938081eecd34227c161d  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_rp1_nonregression_vs_r4-1_2026-10-02.csv
be53990e6371b6345e301d93262c6ed9fa7a3c8e25423f55975db94f7da16da9  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_rp1_nonregression_vs_r4-2_2026-10-02.csv
41dca0ba7fab7a40c289ca8140643f818164721e80be25eceec72cd5234b542a  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_rp1_nonregression_vs_r4_2026-10-02.csv
7ab600e4dd509a912dab89090093d47a22de074284c6dc72e5d69542fb1b9117  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_rp1_restart_store_manifest_2026-10-02.csv
540f879220cf43d1c56e8dde56fc7a8e0bd930b51048b073714c62e03e6b57fd  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_spline_percall_telemetry_rp1_2026-10-02.csv
1a72aa76e293eef412ab869dea1ac57732c79ff934a10cdf8ddf18c9d4d87081  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_telemetry_rp1_2026-10-02.csv
dd741a1b13ad888e0b7e6b6b2cb5d9c597f086b612155c418d901308f5b70ca3  p_konum_plus/quarantine/ATTEMPT4_STORE_READ_LOG_MISSING_f3_step2_test_evidence_rp1_2026-10-02.json
6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31  p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT1_SUPERSEDED.py
891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd  p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.py
f882b9226d1981dc8fa30daf5a24ad6087f975f10d58f10e55a25b17f0ebb3a5  p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.py
99f895c10ab63caecde17a2f56dd1c03e892edbc582eda27255df6f212251e7a  p_konum_plus/quarantine/f3_step2_adequacy_harness_r3_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.py
b22708d2fd7e1a68c5c471285d58d5398992bcde36690e5b04dc94321f6d9841  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py
16df26d84b59f956b716d95996fef5d091c04d9e54e2265d966f76f7e5b9a5f4  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT1_RESTART_LAYER_OFF.py.sha256
280869892d8a07bc4752fc08770e010533649218c7bdcd10301216893f5f93f2  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py
3548ad62451dad5571662385aed5fca0111affab02ac65b7614ebc062fb311d7  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-1_2026-09-29_ATTEMPT2_NONREG_CANON_BUG.py.sha256
9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py
e84361e2ae973aaa19b2ae3a1b1ce820cfa539e7875905c724258cc0e3fa70bd  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py.sha256
f137299c02a2cd1dee775cd5afa16ba59b379940c58b9be8dab67b3ed72e1418  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.py
20d830e0002fb7ee66c3feca20ed2778b44e99745962729b0396258737e56306  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT2_INTERRUPTED.py
814e395a24aa0dcdac2e9c89481a69595bf30e6859977080c03e678619b0786f  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.py
90ea0ff39550e6e15539a0b60d93c3c2f880453ef12476081c35bd53e8a30805  p_konum_plus/quarantine/f3_step2_adequacy_harness_r4_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.py
08d9bcc8c2c65091ef6f456ded7ac44460e18ee6e92c8c737a0fe9424e45f8f2  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py
7103b136f1ba7fc497fd149ece659366d10f0a7d2c60cb525ed623dbcb6f7948  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT1_NONREG_STALE_ENDSTATE_BUG.py.sha256
0d6894c27ebd6f21e875218ac2c473b6d6c3a58c59fdf80ae632eee95fa335b5  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py
e91d7750b2b8d1b940215714b2ae224c82d32e715449cac7260ec18ff62acba1  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT2_NARROWED_EVIDENCE_MISSING.py.sha256
d57003f9a826596e7c1393a41f3ea2c7dc86f47d52ee02c2bf0daec00dceaf2d  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py
0d1f3b28ba80dba0a682bf5c50585a8b0d4cd8ae6f698009bc960d78bdedd4e8  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT3_STORE_READ_RESUME_BUG.py.sha256
47b42533fb99be264ca68c9936f0954054f55d1fbb40d6fa50a638e897b26561  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py
3c7d0e62cee84c27bf0133ed729614b79d6c0c883b9f222041e3f5f9422966fa  p_konum_plus/quarantine/f3_step2_adequacy_harness_rp1_2026-10-02_ATTEMPT4_STORE_READ_LOG_MISSING.py.sha256
78e6627d94bae3bc7b20f5b6d998b7ff733ea3f37e18fab3b1d58826430a93c9  p_konum_plus/quarantine/f3_step2_r3_attempt1_supersession_note_2026-09-22.md
3a1ad5aa694f52dd15f8e50b689df992f5688715d9f183c706e65b6112dc3470  p_konum_plus/quarantine/f3_step2_r3_attempt8_telemetry_replay_bug_note_2026-09-24.md
683108f3e6960fc1a4e18bd0f80679624e255dd4520a9b6f7bd2f71a3435fcad  p_konum_plus/quarantine/f3_step2_r3_auditor_transmittal_note_corruption_incident_2026-09-23.md
88558b260227aa0830a7bc65be9301f8e70965c6cfcc8901c09985cb02de661c  p_konum_plus/quarantine/f3_step2_r3_exc_classification_bug_note_2026-09-22.md
9db9079f3fe05944fc25188a423b44ce0a2020baa87a0876465beb505ced985f  p_konum_plus/quarantine/f3_step2_r3_independent_audit_corrections_note_2026-09-23.md
c8d47629ea56e8228a3ac7358ca4c4cd10d339403a32e6a54ed314966f6688bd  p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT1_SUPERSEDED.md
a4c7d65c8d778277b92e83e14a31a90a51b6e5e1df18f2c8da815d7ce00de0c0  p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT2-3_SUSPECT_CLASSIFICATION_BUG.md
e67bd9d79eed56f78092b460a54a586195ab72703ed937489872935c815d5905  p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT5_PRE_AUDIT_P1-P7_CORRECTIONS.md
2e55e150c4b256c073a74b758094f9d95e6147e881d75bbed36c721b2cc1d657  p_konum_plus/quarantine/f3_step2_r3_preexecution_custody_2026-09-22_ATTEMPT8_CRASHED_TELEMETRY_REPLAY_BUG.md
7ff79add1a72219a64a64f73cb5f14160148a120582715e400435ba4434dcab4  p_konum_plus/quarantine/f3_step2_r4-1_attempt1_interruption_note_2026-09-29.md
8fa1cab46ecfc0f92cb2df6301c4cab9a8e4b2079ce1a7fed4e1fb323e171b94  p_konum_plus/quarantine/f3_step2_r4-1_attempt1_stderr_2026-09-29.log
f0398c8e7350e5eb7a5d6f7168decdeea88da5bdf12be06c9654bb4813c8d546  p_konum_plus/quarantine/f3_step2_r4-1_attempt1_stdout_2026-09-29.log
e27b29b2ae8746aa7dce2700aa11d942b8ed1f1db429a482845623fee7e9f6e2  p_konum_plus/quarantine/f3_step2_r4-1_attempt2_nonreg_canon_bug_note_2026-09-29.md
83c1e4a49778cdd973fa40838a7997317cea45e687afeadebba89d22a1a9b253  p_konum_plus/quarantine/f3_step2_r4-1_attempt2_stderr_2026-09-29.log
9381d124f61d1435e6d107320e127246798ae23f34d5b01dabadcb48c34fd7cf  p_konum_plus/quarantine/f3_step2_r4-1_attempt2_stdout_2026-09-29.log
3adbd089c03c8212e56f9c275b5785562a3289e2bf2b4977b71ee1b34473e2aa  p_konum_plus/quarantine/f3_step2_r4-1_quarantine_label_annotation_note_2026-09-29.md
a4b5e176de9be9e8caa1b2145ce99e9c2539fcbea254df0a23ba2bfada470bbe  p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md
e2f27007f1abc229962807182a6879d66e2e877bf81074f7b60c9bbf8082c956  p_konum_plus/quarantine/f3_step2_r4-2_attempt1_interruption_note_2026-09-30.md.sha256
d688ac98f0617f2b65979bc7ac4b320d179f18ba312332070bc26bc22ec39123  p_konum_plus/quarantine/f3_step2_r4-2_launch1_stderr_2026-09-30.log
89e206d20ac27d08469f39d6092f04ac8074372f9ba6cbe9b5ce69dbb98a4f2f  p_konum_plus/quarantine/f3_step2_r4-2_launch1_stderr_2026-09-30.log.sha256
5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083  p_konum_plus/quarantine/f3_step2_r4-2_launch1_stdout_2026-09-30.log
07811b64a04315a179ef4af3d70979b0be2a711a80bd18d78bd59d81bd63b084  p_konum_plus/quarantine/f3_step2_r4-2_launch1_stdout_2026-09-30.log.sha256
40b3a53d2a4628ce3736585d17ea63aeea93f19a16f0c0e67b7c3e6262fca006  p_konum_plus/quarantine/f3_step2_r4_attempt1_stdout_2026-09-24.log
0ebaaaeb15afff233758ccb073e71df3840ea0edc7b5fa2df9ae066c8608c4a4  p_konum_plus/quarantine/f3_step2_r4_attempt1_supersession_note_2026-09-24.md
1f1e0e080930be80311ff7a1ff08f75984991a0fb3e05c905ce0b2e5889bf818  p_konum_plus/quarantine/f3_step2_r4_attempt2_interruption_note_2026-09-26.md
71a0bfd2c1914ff93edd4aec3d3efdec95c318cc7e04ddc8b41ea169ef201dd1  p_konum_plus/quarantine/f3_step2_r4_attempt2_stdout_2026-09-26.log
e467d95ffa8995738b2cba45b18322c95c03c1c09a138fce44c8c49843136815  p_konum_plus/quarantine/f3_step2_r4_attempt34_k05_nondeterminism_note_2026-09-26.md
fbbcc5e6c7d8c627d6109a3dd93466fc8a229cdd5f0cd33849cc0ef57a7cccef  p_konum_plus/quarantine/f3_step2_r4_attempt3_stdout_2026-09-26.log
3b87122312f6d4908fa540d989f728a41ede07b37506a7c0b980b9fe45000328  p_konum_plus/quarantine/f3_step2_r4_attempt4_stdout_2026-09-26.log
3ba2075f986300486f69f3958a4ed28edce06ac9b13e326b879a03c582d7f831  p_konum_plus/quarantine/f3_step2_r4_attempt56_mutation_leak_note_2026-09-27.md
ca429b22c2920fd91ae86abafd552de0f5f6c7706d7fd37d42c05e337814467e  p_konum_plus/quarantine/f3_step2_r4_attempt5_stdout_2026-09-26.log
3130cb5f14e0f44abb216c2515a098ddd220c8b16c928b2b1411d79863561d2f  p_konum_plus/quarantine/f3_step2_r4_attempt6_stdout_2026-09-27.log
307809c55cc969b747b8748e560a8837a24638582066ddd5a914ba0b5a26e441  p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT1_ANY_MODE_UNRELATED_BUG.md
856201af365a2c1b696136e42598513a6410774e8a4dff341cc5ba336605eb78  p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT2_INTERRUPTED.md
51499dc4fd86933de986c1ca30e76b177ea6854ecb903ebc7208ebea5b8f3c4f  p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT3-4_K05_COUNTER_NONDETERMINISM.md
cb2204b1aa1a07db7f3a00748c1e47025d3800e4c7eaa598d088967a67f62273  p_konum_plus/quarantine/f3_step2_r4_preexecution_custody_2026-09-24_ATTEMPT5-6_MUTATION_LEAK.md
2357898e6d7314a5b950fc356def73a4e78ce7d27a6e67b863b6041d7784be1b  p_konum_plus/quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md
d2180862369bd75f5c557777f5676f7b816e2b3ae0c39bc6e9aa54bbb3ad504e  p_konum_plus/quarantine/f3_step2_rp1_attempt1_nonreg_bug_note_2026-10-02.md.sha256
029fcc980513e74c142250cb9ccc51051a541af71a9dd9a85364aa705d20ca0c  p_konum_plus/quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md
4b8e1359dc1ad149d31514ef84dd6fcd15db183b39e8e816f86d61e4402431c2  p_konum_plus/quarantine/f3_step2_rp1_attempt2_narrowed_evidence_note_2026-10-02.md.sha256
527fd2495bd4642b956ea18b760beca5a1168449cd55214bc7f6b7bb9a49a1d3  p_konum_plus/quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md
4366e29974e15e110a220d5b0b6f9c49048592e5364d4393e1123a121c31bcce  p_konum_plus/quarantine/f3_step2_rp1_attempt3_store_read_resume_bug_note_2026-10-02.md.sha256
73d9040bb3ed4aaf5d72dda0fd04a6189b11c38e843429e009b4641f3a79e530  p_konum_plus/quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md
6b6b15ebae3624f3533d4e64ad9bae5a1c2acf68e9fb166c61fc32cf7fc85b38  p_konum_plus/quarantine/f3_step2_rp1_attempt4_store_read_log_missing_note_2026-10-03.md.sha256
c39f1cbda77c769e146d8dc08c36c940687e747b9c572cd0ba6fcd75688c354b  p_konum_plus/quarantine/f3_step2_rp1_launch1_stderr_2026-10-02.log
e3361aab463b55407bbd705a93e26ee08fe7ffa1a401ef4a6eaba5f3fc53bed0  p_konum_plus/quarantine/f3_step2_rp1_launch1_stderr_2026-10-02.log.sha256
445fe0635a6d1420e4436657b101a28e07f22fbd5345e40e82fd26cdf810ec1f  p_konum_plus/quarantine/f3_step2_rp1_launch1_stdout_2026-10-02.log
6d88a49897d302c758f148a5cc2bc102438d3cc7b1619826cb01c84b108a5c79  p_konum_plus/quarantine/f3_step2_rp1_launch1_stdout_2026-10-02.log.sha256
df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613  p_konum_plus/quarantine/f3_step2_rp1_launch2_stderr_2026-10-02.log
13ec898e0523d332bc065d2a2a5b174e93208ba86d5dcb6af395feeedc7fcd38  p_konum_plus/quarantine/f3_step2_rp1_launch2_stderr_2026-10-02.log.sha256
d3a1751f4df56fcdec92579c086e48f2230789f09a18d189dda064b5a007d9c7  p_konum_plus/quarantine/f3_step2_rp1_launch2_stdout_2026-10-02.log
b219204d3213848c5d277f697cecfc2d69e0c2cb03ab53039306092281166e3a  p_konum_plus/quarantine/f3_step2_rp1_launch2_stdout_2026-10-02.log.sha256
915a7197f7f44d11befd973ea095596099eb839fa008e9e4d769a5d1e229bb45  p_konum_plus/quarantine/f3_step2_rp1_launch3_stderr_2026-10-02.log
77c45ec039ce148af660b635e12d639f7cbfb0d7af3762620f1f17ff2126cffc  p_konum_plus/quarantine/f3_step2_rp1_launch3_stderr_2026-10-02.log.sha256
7aaed93846bb688a6c5e7a0ea697606edcd9a53f2d9ae552a4306bcb4bce2d4d  p_konum_plus/quarantine/f3_step2_rp1_launch3_stdout_2026-10-02.log
44707ab67c7ae7d9bf0eab37bbcc7de43a86e898fc2fce521302f8d4d5468848  p_konum_plus/quarantine/f3_step2_rp1_launch3_stdout_2026-10-02.log.sha256
df257d124c1240ec97feba2f382eb4dc26150ebce619ceed9ea819eb56874613  p_konum_plus/quarantine/f3_step2_rp1_launch4_stderr_2026-10-02.log
fa7ccf61f6063136c607e210265c2327a4e368507a8e4c8b70fe856d17df6c5a  p_konum_plus/quarantine/f3_step2_rp1_launch4_stderr_2026-10-02.log.sha256
c1b286fa378def03c91035199750f6243cb501768f10852996dfdc8b4d71f698  p_konum_plus/quarantine/f3_step2_rp1_launch4_stdout_2026-10-02.log
3cdbafdf32664e0ada96e4fe190996b42b554b22e063da34568ec64f2fef6923  p_konum_plus/quarantine/f3_step2_rp1_launch4_stdout_2026-10-02.log.sha256
7a77da84978577de2483efbe8baa0f98cce6a7d6ca616153e21980ca67b127b1  p_konum_plus/quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv
9fe259d5d96a05b8e8e6ae3abbda648d23fb3f4b01d07db9ce4fbddd94858896  p_konum_plus/quarantine/r3_restart_store_548ae790_foreign_entries_listing_2026-09-27.csv.sha256
1f411fb2de44493971a6c4a425a71a5fb14441e3f567b8e087e015c4f37f738a  upload/F3_RP1_INDEPENDENT_AUDIT_INSTRUCTION_2026-10-04.md
```

---

NON-NORMATIVE — no PI acceptance implied. End of independent audit record.
