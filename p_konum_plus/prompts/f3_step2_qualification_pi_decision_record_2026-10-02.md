# p_konum_plus — F3 STEP-2 — PI nitelendirme kararı (F3_STEP2 sonuç kaydı, D-9) — 2026-10-02

> Bu kayıt D-8'in (`f3_step2_r4-2_pi_decision_record_2026-10-01.md`, `aadf2840…`) child'ıdır ve zincirde D-9 adını
> alır. D-8 §2 madde 3'ün "PI'nın F3_STEP2 sonucunu yazacağı kendi kaydı" dediği kayıt budur: PI-1 … PI-4 ve PI-2 (ii)
> cümlesi buraya taşınır (§3). **Bu kayıt PI'nın 2026-10-02 tarihli onayıyla imzalıdır** (§8). İçine kendi hash'i
> yazılmaz; hash'i ayrı bir `.sha256` dosyasında durur. Metin DRAFT r2'den (`2766f7b4…`) türetildi; r2, r1
> (`3fb6fbe8…`) ve ilk taslak (`6a664e74…`) yeniden yazılmaz. Değişiklikler §11'de (11.0: r2 → imzalı sürüm).

```text
record                = f3_step2_qualification_pi_decision_record_2026-10-02.md   (D-9; ad imza tarihini taşır)
drafts                = f3_step2_qualification_pi_decision_record_DRAFT_r2_2026-10-02.md
                        2766f7b476c3e883546c938a533b1e0db48a973724f946e5fc288d7f1a487640 (imzalanan metnin taslağı)
                        f3_step2_qualification_pi_decision_record_DRAFT_r1_2026-10-02.md
                        3fb6fbe8d1c05d9b40515b0c8b7f4897fc453814bd61d7ee3862e90ef5443ed4
                        f3_step2_qualification_pi_decision_record_DRAFT_2026-10-01.md
                        6a664e74fee6a4424b9b30a1985da183bd2ceb5063332288147d2d40c5bb64b2 (üçü de değişmez)
record_class          = PI-owned F3_STEP2 sonuç kaydı (D-8 §2 madde 3); child of D-8
                        aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae
PI                    = Öner
date_time_local       = 2026-10-02, UTC+3 (imza; §8)
prepared_by           = Claude (Claude Code, bulut oturumu), PI'nın 2026-10-01 tarihli talimatıyla: "QUALIFIED karar
                        kaydı taslağı. F3 STEP-1'in ratify edilmiş içeriğini ve v11'in ilgili bölümlerini oku,
                        F3_EXECUTION_READY'nin ne gerektirdiğini doğrula, sonra taslağı yaz." r1, PI'nın 2026-10-02
                        tarihli onayıyla ("Onay veriyorum, hazırla") hazırlandı: taslağı 922f02d'ye göre güncelle;
                        diğer denetçi taslağı yeniden yazmaz, denetler. r2, o denetçinin r1 incelemesinin sekiz
                        bulgusunu işler (PI'nın 2026-10-02 iletisi; §11.1). İmzalı sürüm, PI'nın 2026-10-02 tarihli
                        talimatıyla §8'deki seçimler, gerekçe ve imza cümlesi doldurularak hazırlandı (§8, §11.0).
                        Model tanımlayıcısı bu kayda yazılmadı
prior_exposure        = bu oturum D-1 … D-8'i, A-1 … A-5'i ve r3 … r4-2 talimatlarını yazmadı; önceki oturumlara dair
                        belleği yoktur, bu yüzden D-8'in üst taslağını hazırlayan "Claude, cloud oturumu" ile ilişkisini
                        bilemez. Yürütücü, denetçi ve bu taslakçı aynı model ailesindendir (§4 AÇ-1)
inputs                = origin/p_konum_plus, baş 922f02d (2026-10-01 19:52 +0300), git archive ile çıkarıldı.
                        2e51d11'den sonraki üç commit yalnız dosya ekler: iki NON-NORMATIVE not (notes/) ile D-8, A-5
                        ve sidecar'ları (prompts/); paket dosyası değişmedi. D-8 ve A-5'in commit'li baytları PI'nın
                        daha önce yüklediği kopyalarla aynıdır (§10, 8.2)
status                = SIGNED (PI onayı, 2026-10-02; §8)
what_this_record_is   = PI'nın F3_STEP2 = QUALIFIED kararının yazılı hali: neyi kapsadığı (§2), hangi kayıtlı
                        sınırlılıklarla verildiği (§3), F3_EXECUTION_READY için nelerin kaldığı (§5)
what_this_record_is_not = F3_EXECUTION_READY = true değil; real_data_access değişimi değil; gerçek-veri yürütmesinin
                        yetkilendirilmesi değil; 6B spesifikasyonu değil; D-8'in, A-5'in ya da dondurulmuş veya
                        onaylanmış herhangi bir metnin değişimi değil; F4–F12 (V11 L1025–1033) hakkında hüküm
                        değil; yürütücüye kod, koşu ya da teslim talimatı değil
```

Kanıt etiketleri: [A] bu oturumun teslim edilen baytlar üzerinde kendi komutuyla gördüğü (komut ve çıktı §10;
A-5'teki [A] denetçinindir); [A-S] A-5 denetçisinin ortamında yürütme (A-5'ten aktarılır); [X] yürütücünün ya da
PI'nın beyanı. D-8 ve A-5'ten aktarılan olgular kendi kaynaklarındaki etiketi taşır. Satır numaraları
§10'daki dosya anahtarlarıyla verilir (S1REC = STEP-1 freeze record r1, S1NRA = dar yeniden denetim, D1 = v6, D3,
D8, A5, RES = r4-2 sonuç JSON'u, H = r4-2 harness …).

## 0. Geçerlilik koşulları (üçü birden)

```text
Q-1  PI bu kaydı imzalar (§8).
Q-2  D-8 yürürlüktedir: V-1 ve V-2 sağlanmıştır (D8 L51–52) ve C-1' tetiklenmemiştir. C-1' (D8 L115–116): PI-1,
     A-5 olguları (1)–(5) üzerine verildi; bu olgulardan birini değiştiren bir denetim kaydı (A-5'in bir child'ı
     dahil) gelirse PI-1 düşer. PI-1 düşerse bu kayıttaki QUALIFIED da YÜRÜRLÜKTEN KALKAR ve karar PI'ya döner.
Q-3  §10 8.1'deki depo dosyaları (§2'nin bayt bağı, D-8 ve A-5 dahil; DR0, DR1 ve DR2 hariç — onlar bu kaydın
     depoda olmayan taslaklarıdır; DR2 de), imzalı kayıt depoya konduğu anda orada yazan hash'lere eşittir. Eşit
     değilse kayıt hüküm doğurmaz ve PI'ya döner.

durum (imza anında, 2026-10-02)
     Q-1 = sağlandı: PI'nın 2026-10-02 tarihli onay mesajı (§8)
     Q-2 = D-8 metni V-1 ve V-2'yi "sağlandı" yazıyor [A]; C-1''i tetikleyen bir kayıt bu oturumun taradığı dosyalarda
           yok [A, sınırlı: yalnız origin/p_konum_plus 922f02d tarandı]. İmzadan hemen önce git ls-remote ile
           uzak dal yeniden sorgulandı: p_konum_plus = 922f02d, 922f02d'den sonra commit sayısı 0 (§10 8.9) [A]
     Q-3 = 922f02d'de tuttu [A]: 8.1'deki 30 depo dosyasının her birinin arşiv baytı 922f02d'deki git blob'una
           eşit; sidecar'ı olan 20'sinde sidecar da eşit (§10 8.1b, 8.2). Yürütücünün çalışma ağacı bu oturumca
           görülmedi
```

## 1. Karar

```text
F3_STEP2              = QUALIFIED   (PI, 2026-10-02; §8; bayt-bağı kuralı (a) ile birlikte, §2)
nitelik               = kayıtlı sınırlılıklarla nitelendirme: L-1 (T-R2-2 daraltılmış kanıt; PI-1) ve L-2
                        (A.5 (iii) kapsanmadı; PI-2). QUALIFIED bu iki sınırlılıktan ayrı alıntılanmaz (§3)
hesaplanan durum      = F3_STEP2_r4_status = PARTIAL_PENDING_PI (RES end_state; A5 L447 [A]). Bu kayıt onu
                        değiştirmez ve yeniden hesaplamaz. v6 §13'e göre hiçbir hesaplanan durum QUALIFIED değildir
                        ve tek başına F3_EXECUTION_READY doğurmaz (D1 L1103); QUALIFIED, bağımsız denetimden sonra
                        PI'nın ayrı eylemidir: "F3_STEP2 = QUALIFIED can be declared only by the PI after that audit."
                        (D1 L1186; D3 L1077–1078; D8 L290)
dayanak               = (1) bağımsız denetim tamamlandı: A-5 audit_verdict = PASSED; global blocker 0; kapıya özgü
                            blocker 0 (A5 L40, L43, L44). D-8 V-2 bu verdict'e dayanır (D8 L52, L297)
                        (2) PARTIAL_PENDING_PI'yı tutan her liste bir PI kararıyla karşılandı:
                              narrowed_evidence       = [T-R2-2]                         → D-8 PI-1 KABUL
                              uncovered_coverage_rows = ["A.5 (iii) inadmissible refit"] → D-8 PI-2 KABUL
                              deferred_decisions      = [] ; open_findings = []          (RES end_state) [A]
                        (3) RES'te yazan değerler [A]: corrections_complete = true ; mandatory_tests_all_run = true,
                            eksik [] ; determinism = true ; run1 = run2 = 556106e7… ; real_data_access = false.
                            Şerhler kaynaktaki gibi: RUN1 == RUN2 ölçümünün kendisi [X], teslim edilen RUN1 içeriği
                            556106e7…'ye eşit [A] (D8 L106–107; A5 L200, C-06: "[X], within one process");
                            corrections_complete "true by its test-based definition [A]; in the auditor's view the
                            records (R42A-01) and the store-read reporting (R42A-03) are incomplete — cleanup, not
                            blocking" (A5 L440–441)
                        (4) A-5'in üç cleanup maddesinin akışı D-8 PI-3 ile belirlendi. Taslakçının okuması:
                            hiçbiri QUALIFIED'ı koşullamaz, çünkü PI-3'ün istisnası gerçek-veri uyumunun başlamasını
                            koşullar (D8 L172–176): R42A-01 yalnız kayıt maddesidir (sonraki döngünün ilk kaydı;
                            D8 L205); R42A-02 PI-4 ile kapandı; R42A-03 (b) gerçek-veri uyumu başlamadan kapanır
                            (D8 L211; §5 G-1). PI bu okumayı benimsedi (§8)
                        (5) AÇIK FAIL SATIRI — karar verilirken bilinmeli. A-5'in kontrol listesinde C-31 FAIL'dır:
                            "units read from the store reported (D-3 §8.3 provenance) | none read | FAIL — the second
                            INJ-EXC pass read the 438 INJ-EXC mode units the first pass stored; they are not counted —
                            R42A-03 (b)" (A5 L225) [A-5'in [A]'sı]. D-3 §11'in QUALIFIED'dan önce istediği denetim
                            bu §8.3 okumasını içerir ("under §8.3, read the store manifest and the unit provenance
                            against the attempt log. F3_STEP2 = QUALIFIED can be declared only by the PI after that
                            audit.", D3 L1077–1078). Denetim yapıldı ve bu satırı FAIL buldu; A-5 bulguyu cleanup
                            sınıflandırdı, blocker saymadı (verdict PASSED), D-8 onu R42A-03 (b) olarak gerçek-veri
                            uyumundan önceye bağladı. Sonuç: sonuç JSON'u, rapor ve deneme günlüğü depodan birim
                            okunmadığını yazar, oysa birim-test fazında 438 mod birimi okundu; sayaç kabadır
                            (D8 L108–112). Etkilenmeyenler: değerlendirme nesneleri, stop kayıtları, artık serileri ve
                            RUN1 == RUN2 (D8 L215–217). Etkilenen: INJ-EXC iki-geçiş testinin son süreçteki kanıtı;
                            passes_identical = true orada gerçek bir ikinci yürütmeye değil tekrar oynatmaya dayanır
                            (D8 L108–110); bunu kısmen deneme 1 karşılar (iki geçiş taze, aynı sonuç; son süreç
                            değil; D8 L113–114). QUALIFIED bu FAIL satırı açıkken, bilerek verildi (§8)
```

## 2. QUALIFIED'ın kapsamı

```text
nitelenen             = F3 STEP-1 freeze record r1 §10 madde 2'deki STEP-2 implementation-pin görevi (CLASS_C):
                        ACF uygulaması, SOLVER-B spline çözücü pinleri, prob maskesi (E = 15, LEFT/RIGHT) ve fold
                        şeması (K = 5) uygulama kesinliği; ve bunları yükleyip kullanan yeterlilik-değerlendirme
                        harness'ı (yükleyiciler, sarmalayıcılar, S-1/S-2 uygulamaları, karar katmanı; D-2'nin S-1 …
                        T-5 değerleriyle) — "synthetic qualification only; no real SSA fit until its own gate"
                        (S1REC L510–518)
bayt bağı             = harness b988e962… (r4-2, deneme 2) ; generator 68d126cf… ve manifest 5c09c4f0… (r4-1'den
                        değişmeden) ; results f2a0a4d5… ; register c281e713… ; report 7754ba02… ; residual
                        3ee624f3… ; test evidence c156b9e0… ; telemetry ac70eaf5… ; per-call telemetry 7e44fdf9… ;
                        store manifest 1082e0eb… ; RUN1 = RUN2 kanonik 556106e7…
                        yüklenen dondurulmuş kod: spline harness r2 b31e5a6b… ; F2 engine 01714752…
                        PI içeriği: D-2 da0c4064… (S-1 … T-5) ; S-R2-1 = PI_RULE (D-5 0cd87ad5…) ;
                        T-R2-2 = AUTHORIZE_RESTART (tam hash'ler §10 8.1)
yürütücü ortamı       = Windows-10-10.0.19045-SP0 ; Python 3.11.7 ; numpy 1.26.4 ; scipy 1.14.1 ;
                        MKL = OMP = OPENBLAS = 1 (RES environment: değerler JSON'dan okundu [A]; ortamın kendisi [X])
denetçi ortamı        = Linux ; Python 3.11.15 ; numpy 2.4.4 ; scipy 1.17.1 (A-5 başlığı) ; karar katmanının 35/35
                        yeniden üretimi orada yapıldı [A-S]
```

Bayt-bağı kuralı — PI'nın seçimi (§8):

```text
[x] (a) QUALIFIED, yukarıdaki baytlar ve yürütücü ortamı için verilir. Gerçek-veri yolunda koşacak kod ya da ortam
        bunlardan farklıysa (R42A-03 (b) kapanışı, RESTART_LAYER_ACTIVE sabiti (H L141), gerçek-veri yükleyicisi,
        paket sürümleri dahil), fark gerçek-veri hazırlık talimatının tanımlayacağı bir non-regression kanıtıyla
        — r4-2'ye karşı, whitelist'siz, RUN1 kanonik 556106e7… ve artık serisi 3ee624f3… adlandırılmış
        değerlerinde — ve bağımsız denetimle bağlanmadan nitelenmiş sayılmaz          [SEÇİLDİ — PI, 2026-10-02]
[ ] (b) QUALIFIED, harness'ın sözleşme düzeyindeki davranışı için verilir; kod ya da ortam farkının nasıl
        bağlanacağını gerçek-veri hazırlık talimatı kendi başına belirler

(a)'nın gerekçesi (bilgi)
  - D-8, gerçek-veri uyumundan önce bir kod değişikliği istiyor: R42A-03 (b) (D8 L211–214). Değişiklik harness'a
    düşerse nitelenen baytlar gerçek-veride koşan baytlar olmaz
  - r4-2 harness'ında gerçek-veri giriş yolu yok: 4172 satırda F1/manifest/okuma referansı yok, real_data_access
    False'a sabit (H L4087, L4167; §10 8.7) [A]. Gerçek-veri koşusu her durumda yeni kod içerecek
  - (a) yeni bilimsel literal getirmez; r4-1 → r4-2'de uygulanan T-NONREG yöntemini ve D-3 §3'ün mantığını
    (harness değişirse W-3 tekrarlanır; D-8 PI-1 bilgi bloğunda da anılır) gerçek-veri yoluna taşır
  - (b) seçilirse QUALIFIED, denetlenmemiş bayt farklarını sessizce kapsar
```

QUALIFIED şunları nitelemez:

```text
- gerçek SSA verisinde herhangi bir sonucu, eşiği (P03_threshold_values = NOT_COMPUTED), yeterlilik ölçümünü ya da
  jeneratör seçimini (D2 L207: "No real SSA/F1 fit, empirical threshold computation, generator selection, F4 or
  algorithm×CVI execution is authorized by this file alone.")
- A.5 (iii) satırını (L-2)
- v6 §8'in tam aynı-süreç determinizm sözleşmesini (L-1: T-R2-2 daraltılmış kanıt)
- C4a/C4b karar katmanının ve D-P04 4a/4b çözümünün gerçek fitler üzerinden sınanmış olmasını: bu iki kapsam satırı
  yalnız karar-katmanı enjeksiyonuyla kapsandı (status covered_injection_only; RES coverage, §10 8.4) [A]. Kapsam
  kuralı onları kapsanmış sayar (A5 L222, C-28 PASS); burada açıklama olarak yazılır, sınırlılık kararı değildir
- 6B eşlikçisini (STEP-2 kapsamı dışında; S1REC L518 "contains NO 6B content")
```

## 3. D-8'den taşınanlar: PI-1 … PI-4 ve PI-2 (ii) cümlesi

D-8 §2 madde 3 gereği (D8 L278). Bu bölüm D-8'in hükümlerini yeniden yazmaz, özetler ve yerini gösterir; çelişki
halinde D-8 geçerlidir.

PI-2 (ii) cümlesi, aynen:

> A.5 (iii), mevcut sentetik test paketinde sınanmamıştır; bu kapsam eksikliği kayıtlı sınırlılık olarak kabul edilmiştir.

(D-8 L150–152'deki cümle satır kırılmaları boşluğa indirgenince bu satıra eşittir: §10 8.5, equal = True [A].)

```text
L-1 / PI-1  T-R2-2 daraltılmış kanıt: KABUL (D8 L66–137). Olgular (1)–(5), D-8'deki etiketleriyle (D8 L94–114):
            (1) final koşu (deneme 2, harness b988e962…) baştan tek süreçti, pid 10412; T-SINGLE-PROCESS tutuyor [A]
            (2) yeniden başlatma katmanı bu süreçte AÇIKTI [A]; katmanın kapalı olduğu deneme 1 depoya birim yazmadı
                [A]; durmanın dış kesinti olduğu yürütücünün beyanıdır [X]
            (3) RUN1, RUN2 ve her değerlendirme nesnesi depodan okunmadan hesaplandı [A]; RUN1 == RUN2 ölçümünün
                kendisi [X]; teslim edilen RUN1 içeriği 556106e7…'ye eşit [A]
            (4) katman, birim-test fazında üç INJ-EXC-* fikstürünün ikinci geçişini birinci geçişin aynı süreçte
                depoya yazdığı 438 mod biriminden servis etti: bu geçiş tekrar oynatmadır, passes_identical yapı
                gereği true'dur. Sonuç JSON'u, rapor (L68) ve deneme günlüğü (L67) depodan birim okunmadığını yazar;
                sayaç kabadır (A-5 R42A-03, cleanup; A-5 C-31 FAIL) [A]
            (5) katmanın kapalı olduğu deneme 1 (bu fonksiyonlarda aynı kod) iki geçişi de taze yürüttü ve aynı
                sonuçları verdi [A]
            ([A] ve [X] burada D-8'in etiketleridir: A-5 denetçisinin doğrulaması / yürütücünün beyanı.)
            C-1' bu kayda Q-2 olarak taşındı. Ek tek-süreç koşusu: GEREKMİYOR (D8 L117). T-R2-2, D-3 §5 ve §8.3
            gereği narrowed_evidence'ta değeri yüzünden kalır
L-2 / PI-2  "A.5 (iii) inadmissible refit": kalıcı kayıtlı sınırlılık, KABUL (D8 L139–162). Hükümler: (i) satırı
            kapatmak için dondurulmuş koda dokunulmaz; (ii) yukarıdaki cümle; (iii) gerçek-veri yürütmesinde
            yürütücü, dondurulmuş çıktı/telemetriden gözlenebiliyorsa "sayısal olarak tamamlandı ama kabul edilemez"
            yeniden uyumların sayısını raporlar, gözlenemiyorsa söyler, dondurulmuş kodu değiştirmez; (iv) böyle bir
            olay görülürse yürütücü PI'ya bildirir, bilimsel işlemini kendisi belirlemez. (iii) ve (iv) gerçek-veri
            talimatına girer (§5 G-3)
PI-3        temizlik akışı (D8 L164–228): R41A-01 A-5'e göre KAPALI (D8 L184–186); R42A-01 İLK YOL — sonraki döngünün
            ilk kaydında (başlangıç envanteri) r4-2 paketinin her dosyası tam hash'iyle, r4-1 ve r4 paketleri yeniden
            hash'leriyle ve R41A-04 yanıt satırı için bir erratum satırı (D8 L205–210); R42A-03 sınıfı (b) — gerçek-
            veri uyumu başlamadan kapanır, gerçek-veri koşusu katmansız olacaksa yeni bir PI kaydıyla (a)'ya
            çevrilebilir (D8 L211–214)
PI-4        R41A-01 (b) karışık-etiket kuralı: kriter bazında okuma KABUL; iki tür farklı kritere ulaştığında D-7 §3
            (2)'nin cinsiyet bazındaki ifadesinin yerine geçer; aynı kritere ulaştıklarında sonuç aynıdır
            (D8 L230–268). Teslim edilen hiçbir çıktıyı değiştirmez
```

## 4. Açıklamalar (sınırlılık kararı değil; QUALIFIED'ın neye dayandığını söyler)

```text
AÇ-1 bağımsızlık. A-1 … A-5 aynı Cowork oturumu tarafından yazıldı; o oturum D-3'ü ve r4, r4-1, r4-2 talimatlarını
     taslakladı, D-4 … D-7'yi doldurdu ve D-8'i hazırladı (A5 L10; D8 L23–31). A-5 bunu kendisi söyler: "agreement
     with them is not an independent derivation" (A5 L15). STEP-1 kayıt denetimleri de bir Claude oturumunundur
     (S1AUD, S1NRA başlıkları). Yürütücü (Claude Code), denetçiler ve bu taslakçı aynı model ailesindendir.
     QUALIFIED, bu nitelikteki bir denetime dayanır
AÇ-2 A-5'in dosya adı "DRAFT r1" taşır. D-8 A-5'i kabul etmez, değiştirmez, yeniden değerlendirmez; V-2 onun
     verdict'ine dayanır (D8 L52, L297). Bu kayıt da A-5'in verdict'ine aynı biçimde dayanır
AÇ-3 D-8 ve A-5, 922f02d ile p_konum_plus/prompts/ altında commit'lidir; commit'li sidecar'larla eşit ve PI'nın
     daha önce yüklediği kopyalarla bayt bayt aynıdır (§10 8.2) [A]
```

## 5. F3_EXECUTION_READY: ne gerektirir, nerede duruyor

Bu bölüm bilgi amaçlıdır ve F3_EXECUTION_READY = false'u değiştirmez. Koşullar kayıtlardan okunmuştur; yeni koşul
eklenmez.

```text
Kural (S1REC L525–526): "F3_EXECUTION_READY remains false until all required pre-execution governance closures
(1, 2 and 3 above) have independently passed." Dar yeniden denetim aynı şeyi iki görev için yineler (S1NRA L66–70).

E-1  STEP-1 freeze record + provenans raporu bağımsız denetimi (S1REC §10 madde 1)
     durum = GEÇTİ. Kayıt denetimi 99b615d2… kaydı (bef216e3…) ve provenans raporunu (2c746625…) kapsar,
             F3_STEP1_FREEZE_RECORD_AUDIT = PASS; r1 dar yeniden denetimi 5470d1ec… audit_result = PASS (S1NRA L17);
             F3_STEP1_status = FROZEN (S1NRA L54) [A: kayıtlar okundu; denetimler yeniden yapılmadı]
E-2  STEP-2 implementation-pin görevi, CLASS_C, sentetik nitelendirme (S1REC §10 madde 2, L510)
     durum = KAPANDI: bu kayıtla, F3_STEP2 = QUALIFIED (PI, 2026-10-02; §1, §8)
E-3  R-REV 6B eşlikçi spesifikasyonu: ayrı artefakt, ayrı provenans, ayrı bağımsız denetim; yalnız spesifikasyon,
     yürütme yok (S1REC §10 madde 3, L520; S1NRA L69–70). Zamanlama: "specification frozen before
     F3_EXECUTION_READY" (S1REC L416). Kökeni F3-STEP1-6B-GOV-01, "reviewer class gate-specific blocker" (S1P5 L31)
     durum = AÇIK. Son kayıtlı durum 6B_companion = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED (S1REC L498;
             S1NRA L58). origin/p_konum_plus (922f02d) dahil depodaki hiçbir ref'te ve tarihçede adında 6b, companion
             ya da r-rev geçen dosya yok (§10 8.6) [A]. Yerel klasörde bir 6B spesifikasyonu varsa bu oturum görmedi

sonuç: E-3 kapanmadan F3_EXECUTION_READY true olamaz. Bu kayıt imzalansa da F3_EXECUTION_READY = false kalır.
```

Gerçek-veri uyumunun başlaması için ayrıca (D-8):

```text
G-1  R42A-03 (b) kapanışı: gerçek-veri yoluna dokunabilecek kod maddesi, gerçek-veri uyumu başlamadan kapanır
     (D8 L172–176, L211–214). Gerçek-veri hazırlık talimatına girer. A-5'in kapanış eylemi: ince taneli depo
     okumalarını raporla ya da sayacın kaba olduğunu söyleyip tekrar oynatılan birimleri listele; ikinci geçiş
     determinizm kanıtı sayılacaksa ona RUN1/RUN2'deki gibi kendi anahtar alanını ver (D8 L225–227)
G-2  gerçek-veri yürütmesi için ayrı PI yetkilendirmesi ve dispatch kaydı (D8 L294–295; D2 L207;
     S1REC L517 "no real SSA fit until its own gate")
G-3  PI-2 (iii) ve (iv) gerçek-veri talimatına girer (D8 L153–159)
G-4  R41A-01 kapalı: A-5'e göre KAPALI (D8 L184–186) → sağlandı
yalnız kayıt maddesi, koşul değil: R42A-01 (D8 L177–178, L205–210)
```

Kim true yapar: bu oturumun taradığı 383 metin dosyasının hiçbiri F3_EXECUTION_READY'yi true yapacak kaydı ya da
kişiyi adlandırmıyor; tek eşleşme v6'daki olumsuzlama ("neither yields F3_EXECUTION_READY = true"; §10 8.8) [A].
Taslakçı önerisi: E-1 … E-3 kapandığında ayrı, imzalı bir PI kaydı; G-1 … G-3 o kayıtla ya da gerçek-veri dispatch
kaydıyla bağlanır.

## 6. Bu kayıt ne yapmaz

```text
F3_EXECUTION_READY    = false (değişmez; §5 E-3 açık)
real_data_access      = false (değişmez)
gerçek-veri yürütmesi = yetkilendirilmez (§5 G-2)
6B eşlikçisi          = oluşturulmaz, kapsanmaz; yalnız E-3'ün açık olduğu yazılır
D-8, A-5              = değiştirilmez, yeniden değerlendirilmez; D-8 hükümleri §3'te özetlenir, çelişkide D-8 geçerlidir
R42A-01, R42A-03      = kapatılmaz; akışları D-8 PI-3'teki gibidir
F4–F12                = hüküm yok (V11 L1025–1033; D-8 aynı ifadeyi F4–F8 için kurar, D8 L296)
commit                = false (bu kayıt commit talimatı içermez)
```

## 7. Yürütücüye (Claude Code) talimatın sınırı — yalnız imzalı sürüm için

```text
Bu kayıt imzalı olarak (Q-1) elinize ulaştığında:
  1. Kaydı ayrı .sha256 sidecar'ıyla, adını değiştirmeden D-8'in durduğu dizine koyun: p_konum_plus/prompts/.
     Kendi hash'ini içine yazmayın
  2. Q-3'ü uygulayın: §10 8.1'deki dosyaları (DR0 hariç; o bu taslağın üst taslağıdır ve depoda değildir)
     depodaki kopyalara karşı yeniden hash'leyin; biri eşit değilse durun ve PI'ya bildirin
  3. Başka hiçbir dosya yazmayın; hiçbir dosyayı değiştirmeyin, taşımayın, yeniden adlandırmayın ya da silmeyin.
     Başka hiçbir kayıtta durum alanı güncellemeyin
  4. F3_EXECUTION_READY'ye ve real_data_access'e dokunmayın; gerçek veri okumayın
  5. Commit yapmayın
Q-1 sağlanmamışsa bu kayıttan hiçbir iş çıkarılmaz.
```

## 8. İmza

```text
Bu kaydı okudum. F3_STEP2 için aşağıda işaretlediğim kararın, §2'deki kapsamla (bayt-bağı kuralında işaretlediğim
seçenekle), §3'teki kayıtlı sınırlılıklarla ve §0'daki geçerlilik koşullarıyla birlikte kayda geçmesini istiyorum.

PI                    = Öner
karar                 = [x] QUALIFIED   [ ] QUALIFIED verilmez   [ ] ertelenir
bayt-bağı kuralı      = [x] (a)   [ ] (b)
D-8 / C-1'            = [x] C-1' tetiklenmedi (922f02d itibarıyla A-5'in bir child'ı ya da r4-2'yi yeniden
                            inceleyen başka bir denetim kaydı yok; imzadan hemen önce uzak dal yeniden sorgulandı,
                            922f02d'den sonra commit yok — §10 8.9)
                        [ ] tetiklendi

gerekçe (PI)
  karar   (1) Önkoşul sağlandı: v6 ve D-3 QUALIFIED'ı bağımsız denetimden sonra ister (D1 L1186; D3 L1077–1078);
              A-5 o denetimi yaptı, global ve kapıya özgü blocker 0 (A5 L40, L43, L44). PARTIAL_PENDING_PI'yı tutan
              iki liste D-8 PI-1 ve PI-2 ile karşılandı.
          (2) C-31 FAIL (A5 L225) değerlendirme nesnelerini, stop kayıtlarını, artık serisini ve RUN1 == RUN2'yi
              etkilemez (D8 L215–217). INJ-EXC iki-geçiş testinin son süreçteki kanıtı ise bir tekrar
              oynatmadır; bunu kısmen deneme 1 karşılar (iki geçiş taze, aynı sonuç; son süreç değil).
          (3) C-31'in kapanışı planlıdır: D-8, R42A-03 (b)'yi gerçek-veri uyumundan önce kapanacak biçimde bağladı
              (D8 L211–214). FAIL karar alanına açıkça yazılıdır (§1 (5)); karar bilerek verildi.
          (4) Ertelemenin kazancı yok: QUALIFIED hiçbir kapıyı açmaz (F3_EXECUTION_READY = false, E-3 açık;
              real_data_access = false). R42A-03'ün kapanışı harness'ı değiştirecek ve (a) altında o baytlar
              non-regression kanıtı ve bağımsız denetim olmadan nitelenmiş sayılmaz. Ertelemek QUALIFIED'ı fiilen
              hazırlık döngüsünün sonuna kaydırırdı; aynı kontrolü (a) zaten sağlar.
  bayt    (1) Gerçek-veri koşusu yeni kod içerecek: r4-2 harness'ında gerçek-veri giriş yolu yok (H L4087, L4167;
              §10 8.7) ve R42A-03 (b)'nin kapanışı kodu değiştirir.
          (2) (b), denetlenmemiş bayt farklarını kapsayan sessiz bir kapsam yaratırdı.
          (3) (a) yeni yöntem getirmez: r4-1 → r4-2'deki T-NONREG yöntemini ve D-3 §3'ün "harness değişirse W-3
              tekrarlanır" mantığını gerçek-veri yoluna uygular; yeni bilimsel literal yok.
          (4) Bedeli: gerçek-veri hazırlık talimatına bir non-regression maddesi (r4-2'ye karşı, whitelist'siz,
              RUN1 kanonik 556106e7… ve artık serisi 3ee624f3…) ve ardından bir bağımsız denetim girer.
  C-1'    922f02d itibarıyla D-8 olgularından (1)–(5) birini değiştiren denetim kaydı yok. Diğer denetçinin r1
          incelemesi r4-2'yi değil taslağı inceledi; getirdiği C-31 FAIL yeni bir olgu değil, D-8 olgu (4)'tedir.

imza / onay           = ONAYLANDI. PI'nın 2026-10-02 tarihli mesajı, aynen:
                        «bu üç seçimi ve 1. noktadaki daraltılmış ifadeyi gerekçe olarak §8'e yazıp imzaya hazır sürümü
                        hazırlarım. İmza cümlemi e tarihini de sen ekle»
                        Seçimler ve gerekçe, PI'nın 2026-10-02 tarihli kararlar mesajından ve onun üzerine yapılan
                        karşılaştırmadan (1. noktadaki daraltılmış ifade dahil) alındı. Kaydın bu son metni PI'ya
                        teslim edildi; PI'nın onu yürütücüye iletmesi, metni ve yukarıdaki beyanı benimsemesidir
date_time_local       = 2026-10-02, UTC+3
F3_EXECUTION_READY    = false (değişmez; §5 E-3 açık) ; real_data_access = false ; commit = false
```

## 9. Taslakçı seçimleri ve PI'ya açık sorular (imza anında; seçimler §8'de verildi)

| # | yer | seçim | neden |
|---|---|---|---|
| 1 | başlık | ad `f3_step2_qualification_pi_decision_record_…`, zincir numarası D-9 | D-8'in ad örüntüsü; D-8'in child'ı |
| 2 | §1 | karar değeri QUALIFIED olarak yazıldı; imza kutusunda üç seçenek | PI'nın talebi QUALIFIED kaydıydı; karar PI'nın |
| 3 | §1 | "kayıtlı sınırlılıklarla nitelendirme" ifadesi; yeni bir durum adı (ör. QUALIFIED_WITH_LIMITATIONS) icat edilmedi | v6 ve D-3 sözlüğünde yalnız QUALIFIED var; sınırlılıklar ayrı alanda |
| 4 | §2 | bayt-bağı kuralı, (a) önerisiyle | R42A-03 (b) kodu değiştirecek; harness'ın gerçek-veri yolu yok (§10 8.7) |
| 5 | §2 | covered_injection_only iki satır açıklama olarak | RES coverage; A-5 C-28 onları kapsanmış sayar |
| 6 | §4 | bağımsızlık açıklaması (AÇ-1) | A5 L10, L15; PI'nın "bağımsızlık sınırlı" notu |
| 7 | §5 | E-1 … E-3 ve G-1 … G-4 tablosu; "kim true yapar" önerisi | S1REC §10; D-8 §3, PI-3; hiçbir kayıt adlandırmıyor (§10 8.8) |
| 8 | başlık | model tanımlayıcısı yazılmadı | bu oturumun depo içeriği kuralı; PI isterse ekler |
| 9 | §0 Q-2 | C-1' tetiklenip PI-1 düşerse QUALIFIED da düşer. Bu kural D-8'de yoktur; taslakçının eklemesidir | QUALIFIED, PARTIAL_PENDING_PI'yı tutan iki listeden birinin PI kabulüne (PI-1) dayanır; o kabul düşerse dayanak kalmaz. Tetiklenmesi ancak r4-2'yi yeniden inceleyen bir kayıt D-8 olgularından birini değiştirirse olur |
| 10 | §1 (5) | açık FAIL satırı (A-5 C-31) karar alanına yazıldı | PI, açık bir FAIL satırı varken QUALIFIED'ı bilerek vermeli ya da ertelemeli (diğer denetçinin 1. bulgusu) |

PI'ya açık sorular (bu kayıtta karara bağlanmaz):

```text
S-a  6B eşlikçi spesifikasyonu (E-3) hangi sırayla açılacak: gerçek-veri hazırlık talimatından önce, paralel, sonra?
     E-3 kapanmadan F3_EXECUTION_READY true olamaz; hazırlık işini (gerçek veri okumadan) engellemez
S-b  Gerçek-veri koşusunda yeniden başlatma katmanı kullanılacak mı? Hayırsa R42A-03 yeni bir PI kaydıyla (a)'ya
     çevrilebilir (D8 L213–214); evetse G-1 kod kapanışı ve §2 (a) altındaki non-regression gerekir
S-c  Gerçek-veri koşusunun kod biçimi: nitelenmiş harness'a bir gerçek-veri giriş modu eklemek mi, nitelenmiş
     fonksiyonları bayt-eşit içe aktaran ayrı bir koşturucu mu? §2 bayt-bağı seçimi bunu koşullar
S-d  A-5 R42A-09 (latent; fit_spline etiketi aynı fikstür ve maske kimliğindeki önceki yakalamalardan türetilir;
     D8 L198–201): gerçek-veri bağlam kimlikleri benzersiz olacak mı? A-5'e göre kriterler her durumda tutulur,
     yalnız etiket değişebilir
```

## 10. Hash'ler ve satır olguları: komut ve çıktı

10.0 Girdilerin hazırlanması (bu oturum, 2026-10-02):

```text
$ git ls-remote origin
592bc7aaa4ec299efb554d14236264c2661755c7	HEAD
592bc7aaa4ec299efb554d14236264c2661755c7	refs/heads/main
922f02d39b2b01ddfe783402f4310fc68a04edce	refs/heads/p_konum_plus
$ git log --oneline -4 origin/p_konum_plus
922f02d p_konum_plus: register D-8 (signed PI decision record) and A-5 (r4-2 audit)
4aa2abf p_konum_plus: add the second note the previous commit's message promised
82a7464 p_konum_plus: archive two informational executor notes
2e51d11 p_konum_plus: r4-2 correction revision package
$ git diff --stat 2e51d11 origin/p_konum_plus
 ...4-2_karar_kaydi_taslak_incelemesi_2026-10-01.md |   86 +
 .../notes/pkp_proje_durum_raporu_2026-09-30.md     |   84 +
 ...nt_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md | 1816 ++++++++++++++++++++
 ...t_claude-opus-5-5_DRAFT_r1_2026-10-01.md.sha256 |    1 +
 .../f3_step2_r4-2_pi_decision_record_2026-10-01.md |  579 +++++++
 ...p2_r4-2_pi_decision_record_2026-10-01.md.sha256 |    1 +
 6 files changed, 2567 insertions(+)
$ git diff --name-status 2e51d11 origin/p_konum_plus | grep -v '^A'
(boş: değişen ya da silinen dosya yok)
$ git archive origin/p_konum_plus p_konum_plus | tar -x -C <scratchpad>/pkp2
$ ok=0; bad=0; for s in $(find . -name '*.sha256' | sort); do d=$(dirname $s); exp=$(awk '{print $1}' $s);
    fn=$(awk '{print $2}' $s | sed 's/^\*//'); if [ -f "$d/$fn" ]; then act=$(sha256sum "$d/$fn" | awk '{print $1}');
    if [ "$exp" = "$act" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "MISMATCH $s"; fi;
    else echo "MISSING target for $s -> $fn"; fi; done; echo "ok=$ok bad=$bad"      (cwd: pkp2/p_konum_plus)
MISSING target for ./quarantine/STRAY_MALFORMED_root_f3_step2_correction_report_r3_2026-09-24.md.sha256 ->
ok=117 bad=0
(not: hedefsiz tek sidecar, adının söylediği gibi karantinadaki bozuk kopyadır)
```

10.1 Komut: `python3 -B qualified_record_facts_signed.py` (Python 3.11.15, Linux). Betik çıktısını UTF-8 olarak
`qualified_record_facts_signed_output.txt` dosyasına yazar ve konsola tek bir ASCII özet satırı basar:

```text
wrote 171 lines to qualified_record_facts_signed_output.txt ; sha256 a6462893d03bf2019d4ab5be83a90f5b36bef12ebfe1e0cb1a04bb5086eb3504
```

10.2 Çıktı dosyası (aynen):

```text
== 8.1 sha256 (file key, sha256, file name)
V11   d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3  ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
CALP  b6b4ed8363791e0232b7b2436ac26db91eee73a85dff0aab552e4fb76fa88280  yeni_proje_empirik_kalibrasyon_protokolu_v0.md
F2FR  ee2cb99d43de2c01ce80125548a88f0b555103263e8ee512b5b6ade7cd163e43  f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md
S1R4  5e594136d6c27adcf6cade9c52c1fb83e5183312899fb46bb96b8cc2c695f4ad  f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md
S1REC 7055f186fd3a067ac147239be9fff739da52c6410a093afdcbbadb915cdcb460  f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md
S1AUD 99b615d2c3ee0c94815af7793e1d8be669a29ef5d070891224d457305864a4dc  f3_step1_freeze_record_independent_audit_2026-09-05.md
S1NRA 5470d1eccc8b80627c7032a940e0dac99a50be57ab3392aeb442b5ccf09cd4b8  f3_step1_freeze_record_r1_narrow_reaudit_2026-09-05.md
S1P5  679b5e3285cbe6968b57d1ef006f9e5d2d4d323bf7648b5876040e9b9f3cae09  Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md
D1    17187d31f772a91872240c299872ebbd1100ed06cdf204099d603340e9046376  Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md
D2    da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498  f3_step2_pi_ratified_content_2026-09-07.md
D3    5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5  Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
D7    a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb  f3_step2_r4-2_pi_dispatch_record_2026-09-30.md
D8    aadf2840d7063dd2c13e829c23128f821115fd9839a63b748afc6ac28764e9ae  f3_step2_r4-2_pi_decision_record_2026-10-01.md
A5    9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575  f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
DR0   6a664e74fee6a4424b9b30a1985da183bd2ceb5063332288147d2d40c5bb64b2  f3_step2_qualification_pi_decision_record_DRAFT_2026-10-01.md
DR1   3fb6fbe8d1c05d9b40515b0c8b7f4897fc453814bd61d7ee3862e90ef5443ed4  f3_step2_qualification_pi_decision_record_DRAFT_r1_2026-10-02.md
DR2   2766f7b476c3e883546c938a533b1e0db48a973724f946e5fc288d7f1a487640  f3_step2_qualification_pi_decision_record_DRAFT_r2_2026-10-02.md
INS   d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
H     b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730  f3_step2_adequacy_harness_r4-2_2026-09-30.py
GEN   68d126cf07b11b844cec0d43a607f0e340ec2ea195870f9b4e27f812b29f9830  f3_step2_fixture_generator_r4-1_2026-09-29.py
MAN   5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe  f3_step2_fixture_manifest_r4-1_2026-09-29.csv
RES   f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  f3_step2_results_r4-2_2026-09-30.json
RSD   3ee624f3a3e0ddb9acef9e0f23988417a308e8b003d756823b8a5c521afd9d4f  f3_step2_residual_series_r4-2_2026-09-30.json
TEV   c156b9e0ef70f72f751d32e7b2826f4db2fc2a3b78308f54d96ab57a924082bf  f3_step2_test_evidence_r4-2_2026-09-30.json
TEL   ac70eaf580ba4fddf3de63f6ef41ac1eb739483cc88d6cc0fbcec767965ddd5d  f3_step2_telemetry_r4-2_2026-09-30.csv
PCT   7e44fdf95d376813b06593d330707b058f18ff23f3fc22be142b68b04149e51c  f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv
STM   1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95  f3_step2_r4-2_restart_store_manifest_2026-09-30.csv
REG   c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c  f3_step2_class_c_pin_register_r4-2_2026-09-30.md
REP   7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6  f3_step2_correction_report_r4-2_2026-09-30.md
LOG   b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65  f3_step2_r4-2_attempt_log_2026-09-30.md
C2    766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1  f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md
SPL   b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d  f3_spline_solver_qualification_harness_r2_2026-09-03.py
F2E   01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077  f2_step2_feasibility_harness_r3_2026-09-01.py

== 8.1b every 8.1 file in the repository: archive bytes == git blob at 922f02d? own sidecar?
V11   blob_equal=True ; no sidecar
CALP  blob_equal=True ; no sidecar
F2FR  blob_equal=True ; no sidecar
S1R4  blob_equal=True ; no sidecar
S1REC blob_equal=True ; sidecar_equal=True
S1AUD blob_equal=True ; no sidecar
S1NRA blob_equal=True ; no sidecar
S1P5  blob_equal=True ; no sidecar
D1    blob_equal=True ; no sidecar
D2    blob_equal=True ; sidecar_equal=True
D3    blob_equal=True ; sidecar_equal=True
D7    blob_equal=True ; sidecar_equal=True
D8    blob_equal=True ; sidecar_equal=True
A5    blob_equal=True ; sidecar_equal=True
DR0   not in the repository (scratchpad draft; excluded from Q-3)
DR1   not in the repository (scratchpad draft; excluded from Q-3)
DR2   not in the repository (scratchpad draft; excluded from Q-3)
INS   blob_equal=True ; sidecar_equal=True
H     blob_equal=True ; sidecar_equal=True
GEN   blob_equal=True ; sidecar_equal=True
MAN   blob_equal=True ; sidecar_equal=True
RES   blob_equal=True ; sidecar_equal=True
RSD   blob_equal=True ; sidecar_equal=True
TEV   blob_equal=True ; sidecar_equal=True
TEL   blob_equal=True ; sidecar_equal=True
PCT   blob_equal=True ; sidecar_equal=True
STM   blob_equal=True ; sidecar_equal=True
REG   blob_equal=True ; sidecar_equal=True
REP   blob_equal=True ; sidecar_equal=True
LOG   blob_equal=True ; sidecar_equal=True
C2    blob_equal=True ; sidecar_equal=True
SPL   blob_equal=True ; no sidecar
F2E   blob_equal=True ; no sidecar

== 8.2 D-8 and A-5: committed sidecar == computed? committed bytes == earlier upload?
D8  sidecar aadf2840d7063dd2... computed aadf2840d7063dd2... equal=True ; identical_to_upload=True
A5  sidecar 9111bc71933f0fcc... computed 9111bc71933f0fcc... equal=True ; identical_to_upload=True

== 8.3 line facts (key, line numbers, first matching line, stripped, max 100 chars)
V11   L5          **Statü:** FINAL NORMATIVE METHODOLOGY CONTRACT — henüz PI imzasıyla `frozen` durumuna geçirilmedi
V11   L1024       | **F3** | cross-fit adequacy thresholds + generator tie-break | both primary candidates fail → STOP
V11   L278        - F3'te pinlenir.
CALP  L259        | procedure | (1) freeze cross-fit scheme; (2) freeze the adequacy-threshold **derivation rule** (ow
S1REC L107        v11_wins            = true
S1REC L416        timing          = specification frozen before F3_EXECUTION_READY; executed
S1REC L498        6B_companion               = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED
S1REC L510        2. F3 STEP-2 implementation-pin task — CLASS_C only:
S1REC L520        3. Separately governed R-REV 6B companion specification task:
S1REC L525        F3_EXECUTION_READY remains false until all required pre-execution governance
S1AUD L191        F3_EXECUTION_READY remains false until 2 and 3 (and r1, if opened) have independently passed.
S1NRA L17         audit_result:  PASS
S1NRA L54         F3_STEP1_status         = FROZEN   (r4 5e594136… as ratified; record r1 precedence over r4
S1NRA L69         B. R-REV 6B companion specification task (specification only; no execution)
S1NRA L70         F3_EXECUTION_READY remains false until both have independently passed.
S1P5  L31         (reviewer id F3-STEP1-6B-GOV-01; reviewer class gate-specific blocker)
D1    L1103       neither yields F3_EXECUTION_READY = true.
D1    L1186       option. F3_STEP2 = QUALIFIED can be declared only by the PI after that audit.
D2    L201        F3_EXECUTION_READY = false
D2    L207        All remaining execution-prompt custody and dispatch conditions still apply. Nothing here asserts tha
D3    L1013       `deferred_decisions` contains S-R2-1 if its value is DEFERRED_THIS_CYCLE; `narrowed_evidence` contai
D3    L1077       under §8.3, read the store manifest and the unit provenance against the attempt log. F3_STEP2 = QUAL
D3    L1078       declared only by the PI after that audit.
D7    L106        expected status            = PARTIAL_PENDING_PI (T-R2-2 in narrowed_evidence; the coverage row
D8    L52         V-2 = sağlandı: A-5 = f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md (9111bc
D8    L51         V-1 = sağlandı: PI'nın 2026-10-01 tarihli onay mesajı (§5)
D8    L115        C-1' (yeni koşul)     = PI-1, (1)–(5)'teki olgular üzerine verilmiştir. Bu olgulardan birini değişti
D8    L117        ek tek-süreç koşusu   = GEREKMİYOR (PI, 2026-10-01; üst taslaktaki değerle aynı): katmanı baştan kap
D8    L139        ### PI-2 — "A.5 (iii) inadmissible refit" satırı: kayıtlı sınırlılık
D8    L150        (ii)  F3_STEP2 sonuç kaydına şu cümle aynen taşınır: "A.5 (iii), mevcut sentetik test
D8    L153        (iii) F3 gerçek-veri yürütmesinde yürütücü, mevcut dondurulmuş çıktı/telemetriden
D8    L157        (iv)  Böyle bir olay gerçek veride görülürse yürütücü bunu PI'ya bildirir ve bilimsel
D8    L172        istisna               = Gerçek-veri uyumunun gerçekten çalışacağı yola dokunan her kod maddesi (R41A
D8    L205        R42A-01 yolu          = İLK YOL (PI, 2026-10-01): bir sonraki döngünün ilk kaydında (başlangıç envan
D8    L211        R42A-03 sınıfı        = (b) gerçek-veri yoluna dokunabilecek kod maddesi (PI, 2026-10-01): istisna u
D8    L230        ### PI-4 — R41A-01 (b) karışık-etiket kuralı: kriter bazında okuma (R42A-02)
D8    L278        PI-1 … PI-4 ve PI-2 (ii)'deki cümle, PI'nın F3_STEP2 sonucunu yazacağı kendi kaydına (örneğin QUALIF
D8    L290        F3_STEP2 = QUALIFIED        = bu kayıtla İLAN EDİLMEZ. PI-1 ve PI-2 kabul edilir ve A-5 temiz çıkars
D8    L294        gerçek-veri yürütmesi       = bu kayıt gerçek veri yürütmesini yetkilendirmez; mevcut yürütmeye geçi
D8    L23         prepared_by           = Claude (Cowork oturumu; yapılandırılmış model tanımlayıcısı claude-opus-5-5,
A5    L10         reviewer_prior_exposure = true — this session drafted D-3 and the r4, r4-1 and r4-2 instructions, fi
A5    L15         checked here are this session's own; agreement with them is not an independent derivation
A5    L40         audit_verdict                 = PASSED — no global and no gate-specific blocker is open on the deliv
A5    L43         global blockers               = 0
A5    L44         gate-specific blockers        = 0
A5    L447        F3_STEP2_r4_status        = PARTIAL_PENDING_PI (agrees with the executor)
A5    L222        | C-28 | coverage 64 rows; only A.5 (iii) uncovered | 64, 0 downgraded | PASS [A] (identical to r4-1
A5    L242        | R42A-09 | informational (latent) | fit_spline derives a context's tag from every UNRELATED capture
A5    L200        | C-06 | RUN1 == RUN2 | true | [X], within one process (C-24) |
A5    L225        | C-31 | units read from the store reported (D-3 §8.3 provenance) | none read | FAIL — the second IN
A5    L440        corrections_complete      = true by its test-based definition [A]; in the auditor's view the records
D8    L106        içinde depo okuması yok. RUN1 == RUN2 ölçümünün kendisi [X]; teslim edilen RUN1 içeriği
D8    L111        (L68) ve deneme günlüğü (L67) depodan birim okunmadığını yazar; sayaç kabadır (A-5
D8    L114        ve aynı sonuçları verdi [A] (A-5 R42A-03 (a))
D8    L296        F4–F8                       = v11 §22 dondurma sırasındaki bu kapıların hiçbirini açmaz, onlar hakkı
D8    L297        A-5                         = bu kayıt A-5'i kabul etmez, değiştirmez, yeniden değerlendirmez; bulgu
V11   L1025       | **F4** | final-refit rule, parameter banks, source IDs, descriptors, label_fuzz | unstable/unsuppo
V11   L1033       | **F12** | **ratification only:** final analysis/reporting contract, full-text consistency review,
H     L141        RESTART_LAYER_ACTIVE = True
REP   L141        COVERAGE_DERIVED = 64 rows, downgraded = []; the only UNCOVERED row remains the authored

== 8.4 results JSON (RES): end_state, process subset, environment, determinism, coverage
end_state = {"F3_STEP2_r4_status": "PARTIAL_PENDING_PI", "PI_dispatch_record_hash": "a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb", "PI_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md", "S_R2_1_source_dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851", "S_R2_1_source_dispatch_record_path": "p_konum_plus/prompts/f3_step2_r4_pi_dispatch_record_2026-09-24.md", "corrections_complete": true, "deferred_decisions": [], "mandatory_tests_all_run": true, "mandatory_tests_missing": [], "narrowed_evidence": ["T-R2-2"], "open_findings": [], "uncovered_coverage_rows": ["A.5 (iii) inadmissible refit"]}
process   = {"attempt_number": 2, "end": "2026-09-30T21:36:01.300416", "launch_number": 2, "pid": 10412, "restart_layer_active": true, "start": "2026-09-30T20:38:58.140644", "store_manifest_sha256": "1082e0eb6caa9eaab2f779802b2023967716f424bd4278f674bc92130ae87f95", "store_rows": 11869, "units_read_from_store": {"nr_gates": 0, "residual_export": 0, "run1": 0, "run2": 0, "unit_tests": 0}}
environment = {"MKL": "1", "OMP": "1", "OPENBLAS": "1", "numpy": "1.26.4", "platform": "Windows-10-10.0.19045-SP0", "python": "3.11.7", "scipy": "1.14.1"}
real_data_access = False ; determinism = True ; run1 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77 ; run2 = 556106e7c4609ade0f43990f7572f19a8c60e2babec25028115d003ae1254c77
f2_engine_sha256 = 01714752eacda37a21fbcc0946c96be4f6b25d2a74b7bbe3da6fe0887df10077 ; spline_solver_sha256 = b31e5a6b69e5bbd96bce07a8634fb9474672ec5d6538d929287193d83ecdc64d ; fixture_manifest_sha256 = 5c09c4f0811fa51bc3b9c7b4744875c439888a654ef970a9718a82eeec69dcfe
pi_ratified = {"S1": "(a)", "S2": "alpha", "S_R2_1": "PI_RULE", "T1": "AUTHORIZE", "T2": "T-2a", "T3": "AUTHORIZE", "T4": "T-4a", "T5": "CONFIRM_WITHIN_SCOPE", "T_R2_2": "AUTHORIZE_RESTART", "content_hash": "da0c4064615263b1aef8884bc1a7fef64d319a40ff48e313c0bb19a522d1c498", "dispatch_record_hash": "0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851"}
coverage rows = 64 ; by status = {"UNCOVERED(no construction possible without touching frozen code)": 1, "covered": 61, "covered_injection_only": 2}
  non-plain row: C4a/C4b decision layer | decision_layer_injection | covered_injection_only
  non-plain row: A.5 (iii) inadmissible refit | n/a | UNCOVERED(no construction possible without touching frozen code)
  non-plain row: D-P04 resolve at 4a / 4b (decision layer) | decision_layer_injection | covered_injection_only

== 8.5 PI-2 (ii) sentence: whitespace-normalised equality with D-8
found_in_D8 = True ; equal = True ; sentence_sha256 = 64f173f6d0dfb76cec75eea049c83bf37bb8cb8f2ce75997a6f04688fbac0bb6

== 8.6 6B companion specification: paths in every fetched ref whose name matches 6b|companion|r_rev|r-rev
claude/laughing-bohr-yyda2h 592bc7a           files=995   matches=none
main 592bc7a                                  files=995   matches=none
origin/claude/laughing-bohr-yyda2h 592bc7a    files=995   matches=none
origin/main 592bc7a                           files=995   matches=none
origin/p_konum_plus 922f02d                   files=1387  matches=none
all-history path matches = none

== 8.7 r4-2 harness (H): references to a real-data input path
lines = 4172 ; matches = 2
  L4087 real_data_access=False,
  L4167 print("REAL_DATA_ACCESS = false")

== 8.8 archive: any text that sets F3_EXECUTION_READY to true or names who sets it
  prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md L1103 neither yields F3_EXECUTION_READY = true.
text files scanned = 383 (matches listed above; a 'neither yields ... = true' line is a negation)

== 8.9 C-1' check: commits on origin/p_konum_plus after 922f02d (remote queried with git ls-remote)
remote p_konum_plus = 922f02d39b2b01ddfe783402f4310fc68a04edce
commits after 922f02d = 0
```

10.3 Betik `qualified_record_facts_signed.py` (aynen):

```python
"""Facts for the signed F3_STEP2 QUALIFIED PI decision record (D-9, 2026-10-02). Read-only.

Inputs: ARCH = `git archive origin/p_konum_plus p_konum_plus` (head 922f02d) extracted to
pkp2/p_konum_plus (D-8 and A-5 are committed there); UP = the PI's earlier uploads of D-8 and A-5,
used only for a byte comparison; DR0, DR1, DR2 = the parent DRAFTs (r0, r1, r2) in this scratchpad. Collects hashes, line facts (file key, line
numbers, first matching line), the results-JSON end state and coverage counts, the PI-2 (ii)
sentence check and the 6B-spec search, writes them UTF-8 to qualified_record_facts_signed_output.txt and
prints one ASCII summary line (repository rule: no non-ASCII in print()).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ARCH = os.path.join(HERE, "pkp2", "p_konum_plus")
UP = "/root/.claude/uploads/2b0b16b1-8f48-5e55-9c15-49689e46562d"
REPO = "/home/user/tartan-names"


LINES: list[str] = []


def out(s: str) -> None:
    LINES.append(s)


def sha(p: str) -> str:
    with open(p, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


A = lambda rel: os.path.join(ARCH, rel)  # noqa: E731
F = {
    "V11": A("protocol/ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md"),
    "CALP": A("calibration/yeni_proje_empirik_kalibrasyon_protokolu_v0.md"),
    "F2FR": A("calibration/f2_generator_specification_record_FINAL_FREEZE_r1_2026-09-02.md"),
    "S1R4": A("calibration/f3_step1_r1_corrected_ratification_candidate_r4_2026-09-05.md"),
    "S1REC": A("calibration/f3_step1_pi_ratification_freeze_record_r1_2026-09-05.md"),
    "S1AUD": A("provenance/f3_step1_freeze_record_independent_audit_2026-09-05.md"),
    "S1NRA": A("provenance/f3_step1_freeze_record_r1_narrow_reaudit_2026-09-05.md"),
    "S1P5": A("prompts/Claude_Code_F3_STEP1_PI_RATIFICATION_FREEZE_RECORD_PROMPT_v5_2026-09-05.md"),
    "D1": A("prompts/Claude_Code_F3_STEP2_CORRECTION_EXECUTION_PROMPT_DRAFT_v6.md"),
    "D2": A("prompts/f3_step2_pi_ratified_content_2026-09-07.md"),
    "D3": A("prompts/Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md"),
    "D7": A("prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md"),
    "D8": A("prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md"),
    "A5": A("prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md"),
    "DR0": os.path.join(HERE, "f3_step2_qualification_pi_decision_record_DRAFT_2026-10-01.md"),
    "DR1": os.path.join(HERE, "f3_step2_qualification_pi_decision_record_DRAFT_r1_2026-10-02.md"),
    "DR2": os.path.join(HERE, "f3_step2_qualification_pi_decision_record_DRAFT_r2_2026-10-02.md"),
    "INS": A("prompts/Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md"),
    "H": A("calibration/f3_step2_adequacy_harness_r4-2_2026-09-30.py"),
    "GEN": A("calibration/f3_step2_fixture_generator_r4-1_2026-09-29.py"),
    "MAN": A("calibration/f3_step2_fixture_manifest_r4-1_2026-09-29.csv"),
    "RES": A("calibration/f3_step2_results_r4-2_2026-09-30.json"),
    "RSD": A("calibration/f3_step2_residual_series_r4-2_2026-09-30.json"),
    "TEV": A("calibration/f3_step2_test_evidence_r4-2_2026-09-30.json"),
    "TEL": A("calibration/f3_step2_telemetry_r4-2_2026-09-30.csv"),
    "PCT": A("calibration/f3_step2_spline_percall_telemetry_r4-2_2026-09-30.csv"),
    "STM": A("calibration/f3_step2_r4-2_restart_store_manifest_2026-09-30.csv"),
    "REG": A("calibration/f3_step2_class_c_pin_register_r4-2_2026-09-30.md"),
    "REP": A("provenance/f3_step2_correction_report_r4-2_2026-09-30.md"),
    "LOG": A("provenance/f3_step2_r4-2_attempt_log_2026-09-30.md"),
    "C2": A("provenance/f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md"),
    "SPL": A("calibration/f3_spline_solver_qualification_harness_r2_2026-09-03.py"),
    "F2E": A("calibration/f2_step2_feasibility_harness_r3_2026-09-01.py"),
}

out("== 8.1 sha256 (file key, sha256, file name)")
for k, p in F.items():
    out("%-5s %s  %s" % (k, sha(p), os.path.basename(p)))

out("")
out("== 8.1b every 8.1 file in the repository: archive bytes == git blob at 922f02d? own sidecar?")
for k, p in F.items():
    if not p.startswith(ARCH):
        out("%-5s not in the repository (scratchpad draft; excluded from Q-3)" % k)
        continue
    rel = os.path.relpath(p, os.path.dirname(ARCH)).replace(os.sep, "/")
    blob = subprocess.run(["git", "-C", REPO, "show", "922f02d:" + rel], capture_output=True, check=True).stdout
    sc = p + ".sha256"
    if os.path.exists(sc):
        rec = open(sc, encoding="ascii").read().split()[0]
        side = "sidecar_equal=%s" % (rec == sha(p))
    else:
        side = "no sidecar"
    out("%-5s blob_equal=%s ; %s" % (k, hashlib.sha256(blob).hexdigest() == sha(p), side))

out("")
out("== 8.2 D-8 and A-5: committed sidecar == computed? committed bytes == earlier upload?")
for k, sc, up in (("D8", "prompts/f3_step2_r4-2_pi_decision_record_2026-10-01.md.sha256",
                   "680fc77c-f3_step2_r4-2_pi_decision_record_2026-10-01.md"),
                  ("A5", "prompts/f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md.sha256",
                   "f4253511-f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md")):
    rec = open(A(sc), encoding="ascii").read().split()[0]
    same = open(F[k], "rb").read() == open(os.path.join(UP, up), "rb").read()
    out("%-3s sidecar %s... computed %s... equal=%s ; identical_to_upload=%s" % (
        k, rec[:16], sha(F[k])[:16], rec == sha(F[k]), same))
out("")
out("== 8.3 line facts (key, line numbers, first matching line, stripped, max 100 chars)")
PAT = [
    ("V11", "**Statü:**"), ("V11", "| **F3** |"), ("V11", "F3'te pinlenir"),
    ("CALP", "| procedure | (1) freeze cross-fit scheme"),
    ("S1REC", "v11_wins            = true"),
    ("S1REC", "timing          = specification frozen before F3_EXECUTION_READY"),
    ("S1REC", "6B_companion               = ADOPTED_SPEC_ONLY_NOT_CREATED_NOT_EXECUTED"),
    ("S1REC", "2. F3 STEP-2 implementation-pin task"), ("S1REC", "3. Separately governed R-REV 6B companion"),
    ("S1REC", "F3_EXECUTION_READY remains false until all required pre-execution governance"),
    ("S1AUD", "F3_EXECUTION_READY remains false until 2 and 3"),
    ("S1NRA", "audit_result:  PASS"), ("S1NRA", "F3_STEP1_status         = FROZEN"),
    ("S1NRA", "B. R-REV 6B companion specification task"),
    ("S1NRA", "F3_EXECUTION_READY remains false until both have independently passed."),
    ("S1P5", "F3-STEP1-6B-GOV-01"),
    ("D1", "neither yields F3_EXECUTION_READY = true."),
    ("D1", "F3_STEP2 = QUALIFIED can be declared only by the PI after that audit."),
    ("D2", "F3_EXECUTION_READY = false"), ("D2", "No real SSA/F1 fit, empirical threshold computation"),
    ("D3", "`narrowed_evidence` contains T-R2-2 if"),
    ("D3", "under §8.3, read the store manifest and the unit provenance"),
    ("D3", "declared only by the PI after that audit."),
    ("D7", "expected status            = PARTIAL_PENDING_PI"),
    ("D8", "V-2 = sağlandı"), ("D8", "V-1 = sağlandı"), ("D8", "C-1' (yeni koşul)"),
    ("D8", "ek tek-süreç koşusu   = GEREKMİYOR"),
    ("D8", "### PI-2"), ("D8", "(ii)  F3_STEP2 sonuç kaydına"), ("D8", "(iii) F3 gerçek-veri yürütmesinde"),
    ("D8", "(iv)  Böyle bir olay gerçek veride"),
    ("D8", "istisna               = Gerçek-veri uyumunun"), ("D8", "R42A-01 yolu          = İLK YOL"),
    ("D8", "R42A-03 sınıfı        = (b)"), ("D8", "### PI-4"),
    ("D8", "PI-1 … PI-4 ve PI-2 (ii)'deki cümle, PI'nın F3_STEP2 sonucunu"),
    ("D8", "F3_STEP2 = QUALIFIED        = bu kayıtla İLAN EDİLMEZ"),
    ("D8", "gerçek-veri yürütmesi       = bu kayıt gerçek veri yürütmesini yetkilendirmez"),
    ("D8", "prepared_by           = Claude (Cowork"),
    ("A5", "reviewer_prior_exposure = true"), ("A5", "agreement with them is not an independent derivation"), ("A5", "audit_verdict                 = PASSED"),
    ("A5", "global blockers               = 0"), ("A5", "gate-specific blockers        = 0"),
    ("A5", "F3_STEP2_r4_status        = PARTIAL_PENDING_PI (agrees with the executor)"),
    ("A5", "| C-28 |"), ("A5", "| R42A-09 |"), ("A5", "| C-06 |"), ("A5", "| C-31 |"),
    ("A5", "corrections_complete      = true by its test-based definition"),
    ("D8", "RUN1 == RUN2 ölçümünün kendisi [X]"), ("D8", "(L68) ve deneme günlüğü (L67)"),
    ("D8", "ve aynı sonuçları verdi [A]"), ("D8", "F4–F8                       ="),
    ("D8", "bu kayıt A-5'i kabul etmez"), ("V11", "| **F4** |"), ("V11", "| **F12** |"),
    ("H", "RESTART_LAYER_ACTIVE = True"),
    ("REP", "COVERAGE_DERIVED = 64 rows"),
]
for key, pat in PAT:
    lines = open(F[key], encoding="utf-8").read().splitlines()
    hits = [i + 1 for i, l in enumerate(lines) if pat in l]
    first = lines[hits[0] - 1].strip()[:100].rstrip() if hits else ""
    out(("%-5s L%-10s %s" % (key, ",".join(map(str, hits)) or "NOT_FOUND", first)).rstrip())

out("")
out("== 8.4 results JSON (RES): end_state, process subset, environment, determinism, coverage")
r = json.load(open(F["RES"], encoding="utf-8"))
out("end_state = " + json.dumps(r["end_state"], sort_keys=True))
p = r["process"]
out("process   = " + json.dumps({k: p[k] for k in ("pid", "start", "end", "attempt_number", "launch_number",
                                                   "restart_layer_active", "store_rows", "store_manifest_sha256",
                                                   "units_read_from_store")}, sort_keys=True))
out("environment = " + json.dumps(r["environment"], sort_keys=True))
out("real_data_access = %s ; determinism = %s ; run1 = %s ; run2 = %s" % (
    r["real_data_access"], r["determinism"], r["run1_canonical_sha256"], r["run2_canonical_sha256"]))
out("f2_engine_sha256 = %s ; spline_solver_sha256 = %s ; fixture_manifest_sha256 = %s" % (
    r["f2_engine_sha256"], r["spline_solver_sha256"], r["fixture_manifest_sha256"]))
out("pi_ratified = " + json.dumps(r["pi_ratified"], sort_keys=True))
cov = r["coverage"]
out("coverage rows = %d ; by status = %s" % (len(cov), json.dumps(dict(Counter(row[3] for row in cov)), sort_keys=True)))
for row in cov:
    if row[3] != "covered":
        out("  non-plain row: %s | %s | %s" % (row[0], row[2], row[3]))

out("")
out("== 8.5 PI-2 (ii) sentence: whitespace-normalised equality with D-8")
SENT = ("A.5 (iii), mevcut sentetik test paketinde sınanmamıştır; bu kapsam eksikliği kayıtlı "
        "sınırlılık olarak kabul edilmiştir.")
d8 = re.sub(r"\s+", " ", open(F["D8"], encoding="utf-8").read())
m = re.search(r'şu cümle aynen taşınır: "(.*?)"', d8)
out("found_in_D8 = %s ; equal = %s ; sentence_sha256 = %s" % (
    bool(m), bool(m) and m.group(1) == SENT, hashlib.sha256(SENT.encode("utf-8")).hexdigest()))

out("")
out("== 8.6 6B companion specification: paths in every fetched ref whose name matches 6b|companion|r_rev|r-rev")
refs = subprocess.run(["git", "-C", REPO, "for-each-ref", "--format=%(refname:short) %(objectname:short)"],
                      capture_output=True, text=True, check=True).stdout.split("\n")
for ref in [x for x in refs if x.strip()]:
    name = ref.split()[0]
    paths = subprocess.run(["git", "-C", REPO, "ls-tree", "-r", "--name-only", name],
                           capture_output=True, text=True, check=True).stdout.splitlines()
    hits = [q for q in paths if re.search(r"6b|companion|r_rev|r-rev", q, re.I)]
    out("%-45s files=%-5d matches=%s" % (ref, len(paths), hits or "none"))
hist = subprocess.run(["git", "-C", REPO, "log", "--all", "--name-only", "--format="],
                      capture_output=True, text=True, check=True).stdout.splitlines()
out("all-history path matches = %s" % (sorted({q for q in hist if re.search(r"6b|companion|r_rev|r-rev", q, re.I)}) or "none"))

out("")
out("== 8.7 r4-2 harness (H): references to a real-data input path")
hl = open(F["H"], encoding="utf-8").read().splitlines()
pat = re.compile(r"f1_|manifests/|eligible_trajectory|data/preprocessed|read_csv|real_data", re.I)
hits = [(i + 1, l.strip()[:80]) for i, l in enumerate(hl) if pat.search(l)]
out("lines = %d ; matches = %d" % (len(hl), len(hits)))
for n, t in hits:
    out("  L%d %s" % (n, t))

out("")
out("== 8.8 archive: any text that sets F3_EXECUTION_READY to true or names who sets it")
pat2 = re.compile(r"EXECUTION_READY\s*=\s*true|EXECUTION_READY becomes|set F3_EXECUTION_READY|declare[s]? F3_EXECUTION_READY", re.I)
n_files = 0
for root, _dirs, files in os.walk(ARCH):
    for fn in sorted(files):
        fp = os.path.join(root, fn)
        try:
            txt = open(fp, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError):
            continue
        n_files += 1
        for i, l in enumerate(txt.splitlines(), 1):
            if pat2.search(l):
                out("  %s L%d %s" % (os.path.relpath(fp, ARCH), i, l.strip()[:90]))
out("text files scanned = %d (matches listed above; a 'neither yields ... = true' line is a negation)" % n_files)

out("")
out("== 8.9 C-1' check: commits on origin/p_konum_plus after 922f02d (remote queried with git ls-remote)")
ls = subprocess.run(["git", "-C", REPO, "ls-remote", "origin", "refs/heads/p_konum_plus"],
                    capture_output=True, text=True, check=True).stdout.split()
out("remote p_konum_plus = %s" % (ls[0] if ls else "?"))
cnt = subprocess.run(["git", "-C", REPO, "rev-list", "--count", "922f02d.." + (ls[0] if ls else "origin/p_konum_plus")],
                     capture_output=True, text=True, check=True).stdout.strip()
out("commits after 922f02d = %s" % cnt)

OUT = os.path.join(HERE, "qualified_record_facts_signed_output.txt")
with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
    fh.write("\n".join(LINES) + "\n")
print("wrote %d lines to %s ; sha256 %s" % (len(LINES), os.path.basename(OUT), sha(OUT)))
```

## 11. Değişiklikler

### 11.0 DRAFT r2 → imzalı sürüm (PI'nın 2026-10-02 talimatı)

| # | yer | değişiklik | neden |
|---|---|---|---|
| 1 | başlık, üst not | ad imza tarihiyle (`…_2026-10-02.md`, D-9); status SIGNED; drafts satırı üç taslağı hash'leriyle verir | PI onayı |
| 2 | §0 | Q-1 sağlandı; Q-2'ye imza öncesi uzak dal sorgusu; Q-3'ten DR2 de hariç | §8; §10 8.9 |
| 3 | §1 | karar QUALIFIED (bayt bağı (a) ile); (4)'te "PI bu okumayı benimsedi"; (5)'te etkilenen kanıt (INJ-EXC iki-geçiş testinin tekrar oynatması, deneme 1 ile kısmi karşılık) ve "bilerek verildi" | PI kararı; karşılaştırmanın 1. noktası |
| 4 | §2, §5 | bayt-bağı (a) işaretlendi; E-2 durumu KAPANDI | PI kararı |
| 5 | §8 | üç seçim, PI gerekçesi, imza/onay (PI mesajı aynen), tarih | PI talimatı |
| 6 | §10 | betik `qualified_record_facts_signed.py`: DR2 hash'i ve 8.9 (C-1' için uzak dal sorgusu) eklendi | dürüstlük kuralı |

### 11.1 r1 → r2 (diğer denetçinin r1 incelemesi, PI'nın 2026-10-02 iletisi)

Her bulgu bu oturumda kaynak dosyada yeniden kontrol edildi; sekizi de tuttu (§10 8.3 satırları).

| # | sınıf (inceleme) | bulgu | r2'deki düzeltme |
|---|---|---|---|
| 1 | önemli | A-5 C-31 FAIL (A5 L225) taslakta hiç geçmiyor; §3 PI-1 özeti D-8 olgu (4)'ün raporlama yarısını (D8 L110–112) düşürüyor | §1 dayanağına (5) eklendi: C-31 FAIL, D-3 L1077–1078 ile ilişkisi, A-5 sınıflandırması, D-8 akışı ve "ertelenir" seçeneği; §3 olgu (4) tam haliyle; §9 satır 10 |
| 2 | cleanup | RUN1 = RUN2 [A] etiketiyle verilmiş, kaynakta ölçüm [X]; corrections_complete A5 L440 şerhi olmadan; §3 olguları etiketsiz; olgu (5)'te "aynı sonuçları verdi" düşmüş | §1 (3) RES değerleri [A], ölçüm [X], A5 L440–441 şerhi aynen; §3 olgu (1)–(5) D-8 etiketleriyle ve (5) tam |
| 3 | cleanup | Q-3 DR0'ı da koşul yapıyor; "922f02d'de tuttu [A]" iddiası 8.1 için gösterilmemiş | Q-3'ten DR0 ve DR1 çıkarıldı; betiğe 8.1b eklendi: 8.1'deki her depo dosyası için arşiv baytı == 922f02d git blob'u ve kendi sidecar'ı; Q-3 durumu buna dayanıyor |
| 4 | cleanup | imzalı sürüm için önerilen adda tarih 2026-10-01 kalmış (ve satır r1'de parent_draft altına düşmüştü) | ad `…_<imza tarihi>.md`, record alanının altına taşındı |
| 5 | cleanup | "F4 … F12" için kaynak yok; D-8 "F4–F8" der | v11 §22 satırları (V11 L1025–1033) kaynak gösterildi; D-8'in F4–F8 ifadesine atıf (D8 L296) |
| 6 | cleanup | §4 A-2 "D-8 A-5'i kabul etti" diyor; D8 L297 "kabul etmez … V-2 onun verdict'ine dayanır" | AÇ-2 ve §1 (1) "dayanır" olarak düzeltildi |
| 7 | cleanup | §4 A-1 … A-3 etiketleri denetim kimlikleri A-1 … A-5 ile çakışıyor | önek AÇ- (açıklama) |
| 8 | bilgi | Q-2'deki "QUALIFIED da düşer" kuralı taslakçının eklemesi, §9'da yok | §9 satır 9 |

İncelemenin NOT PERFORMED dediği kontroller (S1REC, S1AUD, S1NRA, S1P5, D-1, D-2, D-3, D-7, v11, CALP, RES, harness
atıfları; §10.0; 6B araması; §5 E-1 … E-3) bu dosyaların hepsi 922f02d'de commit'li olduğundan, o denetçi tarafından
depodan yapılabilir. E-3 için okunacak yer: S1REC L416, L498, L510–526; S1NRA L58, L66–70; S1P5 L31.

### 11.2 r0 → r1 (ilk taslağa, 6a664e74…, göre; r1 §11, aynen)

| # | yer | değişiklik | neden |
|---|---|---|---|
| 1 | başlık, üst not | TASLAK r1, 2026-10-02; parent_draft satırı; ilk taslağın değişmediği notu | soy |
| 2 | prepared_by | PI'nın 2026-10-02 onayı; diğer denetçinin taslağı yeniden yazmayıp denetleyeceği | PI onayı |
| 3 | inputs | baş 4aa2abf → 922f02d; D-8 ve A-5 artık commit'li ve yüklemelerle bayt bayt aynı | 922f02d commit'i |
| 4 | §0 Q-2, Q-3 durumu | taranan kaynak 922f02d; "PyCharm kopyaları görülmedi" yerine "yürütücünün çalışma ağacı görülmedi" | D-8 ve A-5 depoda |
| 5 | §4 A-3 | "origin'de yoktur" → 922f02d'de commit'li, sidecar ve yükleme eşitliği | 922f02d commit'i |
| 6 | §5 | 4aa2abf → 922f02d; 379 → 383 metin dosyası | yeni dört dosya |
| 7 | §7 madde 2 | yükleme adı notu çıkarıldı; DR0'ın depoda olmadığı notu | 8.1 artık kanonik adlar |
| 8 | §10 | 10.0 komutları ve çıktıları 922f02d'ye göre; betik r1 (ARCH = pkp2; D-8 ve A-5 depodan; 8.2 yükleme karşılaştırması; DR0 hash'i) | dürüstlük kuralı |

Karar, kapsam, sınırlılıklar, bayt-bağı seçenekleri, F3_EXECUTION_READY analizi (E-1 … E-3, G-1 … G-4) ve açık
sorular (S-a … S-d) ilk taslaktaki gibidir; satır olgularının hepsi 922f02d'de aynı satır numaralarında bulundu (§10 8.3).
