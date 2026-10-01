# p_konum_plus — F3 STEP-2 r4-2 — PI karar kaydı (D-8) — 2026-10-01

> Bu kayıt D-7'nin (`f3_step2_r4-2_pi_dispatch_record_2026-09-30.md`, `a3e70509…`) çocuğudur ve zincirde D-8 adını
> alır. Metni, PI'nın 2026-10-01'de yüklediği taslaktan (`f3_step2_r4-2_pi_decision_record_DRAFT_2026-10-01.md`,
> `1581f3be…`) ve onun revize child taslağından (`f3_step2_r4-2_pi_decision_record_DRAFT_r1_2026-10-01.md`,
> `eb10db1b…`) türetildi; iki taslak da yeniden yazılmaz. D-7 §5 iki kararı `not_decided_here` olarak açık
> bırakmıştı: T-R2-2'nin daraltılmış kanıtının kabulü ve "A.5 (iii) inadmissible refit" satırının kayıtlı
> sınırlılık olarak kabulü. Bu kayıt o iki kararı, r4-2 denetiminin (A-5) açık bıraktığı temizlik maddelerinin
> akıbetini ve A-5'in R42A-02 için istediği PI kaydını yazıya döker. **Bu kayıt PI'nın 2026-10-01 tarihli onayıyla
> imzalıdır** (§5). İçine kendi hash'i yazılmaz; hash'i ayrı bir `.sha256` dosyasında durur.

```text
record                = f3_step2_r4-2_pi_decision_record_2026-10-01.md   (D-8)
record_class          = PI-owned decision record for the open PI decisions of the r4-2 revision (inside the r4 cycle)
                        (child of D-7 a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb)
drafts                = f3_step2_r4-2_pi_decision_record_DRAFT_2026-10-01.md
                        1581f3be22f1f8556d1570f19c489ee67264186dc31d9bdae2a98c10b0d376d7 (PI'nın yüklediği taslak)
                        f3_step2_r4-2_pi_decision_record_DRAFT_r1_2026-10-01.md
                        eb10db1b8de640c6103318614ad826661295f3be058b220ebfa44807d2075f63 (revize child taslak)
                        (ikisi de değişmez)
PI                    = Öner
date_time_local       = 2026-10-01, UTC+3
prepared_by           = Claude (Cowork oturumu; yapılandırılmış model tanımlayıcısı claude-opus-5-5, hizmet veren
                        model farklı olabilir), PI'nın 2026-10-01 tarihli onay mesajıyla (§5): DRAFT r1'in seçim
                        alanları PI'nın onayladığı önerilere göre dolduruldu, §2 PI'nın onayıyla daraltıldı (§6.1).
                        Önceki maruziyet: bu oturum D-3'ü ve r4, r4-1, r4-2 talimatlarını taslakladı, D-4 … D-7'yi
                        PI'nın yazılı talimatıyla doldurdu (PI-4'ün konusu olan D-7 §3 (2) dahil), A-1 … A-5'i yazdı,
                        2026-09-30'da PI kabul etmeden önce PI-4'ün konusu olan okumanın talimatın amacıyla tutarlı
                        olduğunu PI'ya söyledi (D-7 §3 (2)'nin yerine geçen bir kayıt gerekeceğini belirtmeden; A-5
                        başlığı) ve 2026-10-01'de bu kayıttaki seçimler için önerileri verdi. Üst taslağın
                        hazırlayanı: kendi prepared_by satırındaki gibi (Claude, cloud oturumu)
status                = SIGNED (PI onayı, 2026-10-01; §5)
what_this_record_is   = PI'nın dört kararının (PI-1 … PI-4) ve PI-1 ile PI-3'teki seçimlerin yazılı hali;
                        yürütücüye giden talimatın sınırı
what_this_record_is_not = QUALIFIED ilanı değil; r4-2 paketinin kabulü değil; A-5'in kabulü ya da yeniden
                        değerlendirmesi değil; bilimsel onay değil; dondurulmuş veya onaylanmış hiçbir metnin,
                        S-R2-1'in ya da D-2'nin değişimi değil; r3, r4, r4-1 veya r4-2 paketlerinde ya da herhangi
                        bir denetim veya dispatch kaydında geriye dönük değişiklik değil (PI-4, D-7 §3 (2)'nin
                        yerine geçer; D-7'nin metni yeniden yazılmaz)
```

## 0. Geçerlilik koşulları (ikisi birden)

```text
V-1  PI bu kaydı imzalar (§5).
V-2  r4-2 paketinin bağımsız denetimi (A-5) tamamlanmış ve verdict'i "blocker yok" (A-4'teki PASSED sözlüğü)
     olmuştur. A-5 bir global ya da kapıya özgü blocker bulursa, bu kayıttaki PI-1 … PI-4 hükümleri YÜRÜRLÜĞE
     GİRMEZ ve PI yeniden karar verir.

durum
     V-1 = sağlandı: PI'nın 2026-10-01 tarihli onay mesajı (§5)
     V-2 = sağlandı: A-5 = f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md (9111bc71…),
           2026-10-01: audit_verdict = PASSED ; global blocker 0 ; kapıya özgü blocker 0 ; cleanup 3
           (R42A-01 … R42A-03) ; informational 7 (R42A-04 … R42A-10) (A-5 §0)
```

Gerekçe: D-7 §5 bu iki kararı açık bıraktı; A-4 §7 ve A-5 §7 onları ve temizlik maddelerinin akıbetini PI'ya
bırakır. Bu kayıt, PI'nın onayıyla ve A-5 sonucuyla yürürlüğe giren karar metnidir.

## 1. Kararlar

Durum iki PI kararı yüzünden PARTIAL_PENDING_PI'daydı (D-7 §5; A-5 §7): PI-1 ve PI-2. İkisi bu kayıtla KABUL
edildi; F3_STEP2 = QUALIFIED ilanı ayrı bir PI eylemidir (§3). PI-3 temizlik maddelerinin akışını belirler; PI-4,
A-5'in R42A-02 için istediği PI kaydıdır.

### PI-1 — T-R2-2: daraltılmış kanıtın (narrowed_evidence) kabulü

```text
karar                 = KABUL (PI, 2026-10-01; §5)
                        not: üst taslakta da KABUL'dü, C-1 koşuluyla. C-1'in üç parçasından ikisi A-5'te doğrulandı
                        (final koşu baştan tek süreçti; T-SINGLE-PROCESS tutuyor); biri A-5 olgularıyla çelişiyordu
                        ("yeniden başlatma katmanı kapalıydı": katman final süreçte açıktı, olgu (2)); C-1'in atıf
                        yaptığı (b)'deki gerekçe de D-3 kuralıyla uyuşmuyordu (dayanak (b)). Üst taslağın kendi
                        kuralıyla ("Doğrulanmazsa PI-1 düşer ve PI'ya döner") karar PI'ya döndü; PI bu kayıtla,
                        aşağıdaki A-5 olguları ve C-1' ile yeniden verdi
konu                  = T-R2-2 = AUTHORIZE_RESTART, daraltılmış bir kanıt sözleşmesine izin verir (v6 §8 aynı-süreç
                        determinizmi ister) ve D-3 §5'e göre narrowed_evidence listesinde değeri yüzünden yer alır:
                        "listed in narrowed_evidence by value, whether or not a restart layer comes to be used";
                        D-3 §8.3: "T-R2-2 stays in narrowed_evidence whether or not the layer was introduced".
                        Karar: bu daraltılmış kanıt, r4-2'de gerçekte kullanıldığı biçimiyle (aşağıdaki A-5
                        olguları) kabul edilir ve kayıtlı sınırlılık olarak taşınır
dayanak (bilgi için)  = (a) T-R2-2 = AUTHORIZE_RESTART, PI'nın 2026-09-21 tarihli değeridir ("PI tercihim: T-R2-2 =
                            AUTHORIZE_RESTART", D-5 §3) ve D-4 → D-5 → D-6 → D-7 (§2) üzerinden değişmeden taşınıyor
                        (b) yürütücünün beyanı [X] (r4-2 raporu §7): "narrowed_evidence = [T-R2-2] (single-process
                            THIS revision, but the narrowing concerns the r4 cycle's history; a PI decision, not
                            this revision's)". Üst taslak bunu "narrowed_evidence yalnız r4 döngüsünün geçmişinde
                            yeniden başlatma katmanı kullanıldığı için duruyor" diye aktarmıştı. Kuralın gerekçesi
                            bu değildir: T-R2-2 listede değeri yüzünden durur (D-3 §5, §8.3; A-5 §7). Ayrıca r4-2'de
                            katman final süreçte de okuma yaptı (olgu (4))
                        (c) A-4 [A-S]: r4-1 karar katmanı denetçinin ortamında iki kez bayt bayt yeniden üretildi
                            (35 karar-katmanı nesnesi). A-5 [A-S]: r4-2 harness'ıyla aynı yeniden üretim (35 / 35);
                            yürütücünün gerçek-yol testi teslim edilen kayda alan alan eşit; denetçinin 12 vakalık
                            probu önceden yazılan beklentilere eşit (A-5 §5)
A-5 olguları          = (üst taslağın C-1'inin yerine geçer)
                        (1) final koşu (deneme 2, harness b988e962…) baştan tek süreçti: pid 10412, başlangıç
                            2026-09-30T20:38:58.140644, bitiş 21:36:01.300416 (sonuç JSON'unun process bloğu);
                            store manifest'indeki 11.869 birimin hepsi bu sürecin; launch 2 RUN_COMPLETE 10412 ile
                            biter; T-SINGLE-PROCESS tutuyor [A] (A-5 §2, C-24)
                        (2) yeniden başlatma katmanı bu süreçte AÇIKTI (harness L141 RESTART_LAYER_ACTIVE = True;
                            launch 2 stdout L6; deneme-2 custody kaydı L93) [A]. Katmanın kapalı olduğu deneme 1
                            (pid 14804, harness 9e4d2803…) SPL ctx 13'te durdu (launch 1 stdout'un son satırı, L40)
                            ve depoya birim yazmadı (store manifest'teki birimlerin hepsi deneme 2'nin) [A];
                            durmanın dış kesinti olduğu yürütücünün beyanıdır [X]
                        (3) RUN1, RUN2 ve her değerlendirme nesnesi depodan okunmadan hesaplandı [A]; v6 §8'in
                            determinizm ifadesi RUN1 == RUN2 için geçerlidir: tek süreç, koşuların arasında ve
                            içinde depo okuması yok. RUN1 == RUN2 ölçümünün kendisi [X]; teslim edilen RUN1 içeriği
                            iddia edilen 556106e7… değerine eşit [A] (A-5 §2)
                        (4) katman, birim-test fazında üç INJ-EXC-* fikstürünün ikinci geçişini, birinci geçişin
                            aynı süreçte depoya yazdığı 438 mod biriminden servis etti: bu geçiş ikinci bir yürütme
                            değil tekrar oynatmadır ve passes_identical yapı gereği true'dur. Sonuç JSON'u, rapor
                            (L68) ve deneme günlüğü (L67) depodan birim okunmadığını yazar; sayaç kabadır (A-5
                            R42A-03, cleanup) [A]
                        (5) katmanın kapalı olduğu deneme 1 (bu fonksiyonlarda aynı kod) iki geçişi de taze yürüttü
                            ve aynı sonuçları verdi [A] (A-5 R42A-03 (a))
C-1' (yeni koşul)     = PI-1, (1)–(5)'teki olgular üzerine verilmiştir. Bu olgulardan birini değiştiren bir denetim
                        kaydı (A-5'in bir child'ı dahil) gelirse PI-1 düşer ve PI'ya döner (PI korudu, 2026-10-01)
ek tek-süreç koşusu   = GEREKMİYOR (PI, 2026-10-01; üst taslaktaki değerle aynı): katmanı baştan kapalı bir koşu
                        (üst taslak: "kemer-pantolon askısı") istenmez. İkinci geçişin final süreçte gerçekten
                        yürütülmesi istenirse yol, R42A-03'ün kapanışıdır: ikinci geçişe kendi anahtar alanı (PI-3)
  bilgi (karar anında)  ne gösterirdi: INJ-EXC-* ikinci geçişi final süreçte gerçekten yürütülürdü; olgu (4)'teki
                        tekrar oynatma ortadan kalkardı. Ne göstermezdi: T-R2-2'nin narrowed_evidence'tan çıkması;
                        D-3 §5 ve §8.3'e göre değeri yüzünden listede kalır. Olgu (5), aynı iki geçişin katmansız
                        bir süreçte aynı sonucu verdiğini zaten gösteriyor (deneme 1; final süreç değil)
                        yol: deneme-2 baytlarıyla (b988e962…) yapılamazdı, katman sabiti True'dur (L141) [A].
                        Katmanı kapalı tek teslim baytları deneme 1'inkilerdir (9e4d2803…, L137), ama orada launch
                        numarası 1'e sabittir (L152) ve launch-1 log çifti zaten vardır [A]. Her iki yol da ayrı
                        bir talimat isterdi; harness değişirse D-3 §3 gereği W-3 tekrarlanır. D-3 §8.3: "Attempt 1
                        runs without it (§8.1)" (L937). D-3 §8.2: AUTHORIZE_RESTART altında katmansız koşu
                        kesilirse yürütücü katmanı ekleyebilir (L930–931)
                        süre ve kesintiler [X, yürütücünün deneme günlükleri; süre sonuç JSON'undan, A]: deneme 2
                        yaklaşık 57 dakika sürdü (olgu (1)). r3 … r4-2'de katmanı kapalı başlayan koşuların hiçbiri
                        sona ulaşmadı: r3 #1 (ctx 41), r4 #2 (ctx 34), r4-1 #1 (ctx 41) ve r4-2 #1 (ctx 13) dış
                        kesintiyle durdu, r4 #1 bir kusurla. Katman açık koşular da dış kesintiyle durdu (r3 #2,
                        #4, #6, #9; r4 #3, #5, #7; r4-1 #3). Boş depodan başlayıp hesabın tamamını tek süreçte
                        bitiren iki koşu var, ikisi de katman açık: r4-1 #2 (yaklaşık 51 dakika, sonra bir kontrol
                        kusuruyla durdu) ve r4-2 #2
```

### PI-2 — "A.5 (iii) inadmissible refit" satırı: kayıtlı sınırlılık

```text
karar                 = KABUL (kalıcı kayıtlı sınırlılık, F3_STEP2 için)
konu                  = "A.5 (iii) inadmissible refit" satırı UNCOVERED kalır: sayısal olarak tamamlanan ama
                        dondurulmuş taksonomiye göre kabul edilemez bir yeniden uyum, dondurulmuş koda
                        dokunmadan yapay olarak kurulamıyor
dayanak (bilgi için)  = r3 (§5), r4-1 (§6) düzeltme raporları ve D-5 §7 bunu önceden öngörmüş; A-4 bunu
                        engelleyici saymadı (açık satır: yalnızca bu). A-5 C-28 [A]: kapsam 64 satır, r4-1'inkiyle
                        aynı; kapsanmayan satır yalnız A.5 (iii); A-5 de engelleyici saymadı
hükümler              = (i)   Bu satırı kapatmak için dondurulmuş koda dokunulmaz (F2 donuk; F3 STEP-1 donuk)
                        (ii)  F3_STEP2 sonuç kaydına şu cümle aynen taşınır: "A.5 (iii), mevcut sentetik test
                              paketinde sınanmamıştır; bu kapsam eksikliği kayıtlı sınırlılık olarak kabul
                              edilmiştir."
                        (iii) F3 gerçek-veri yürütmesinde yürütücü, mevcut dondurulmuş çıktı/telemetriden
                              GÖZLENEBİLİYORSA, "sayısal olarak tamamlandı ama kabul edilemez" sınıfına düşen
                              yeniden uyumların sayısını raporlar. Gözlenemiyorsa bunu söyler. Bu sayıyı elde etmek
                              için dondurulmuş kod DEĞİŞTİRİLMEZ
                        (iv)  Böyle bir olay gerçek veride görülürse yürütücü bunu PI'ya bildirir ve bilimsel
                              işlemini kendisi belirlemez (zincirin kuralı: yürütücü metodolojik çözüm önermez,
                              belirsizlikte durur)
onay                  = PI, 2026-10-01 (§5); karar, konu ve hükümler üst taslaktan değişmeden. (ii)'deki F3_STEP2
                        sonuç kaydı, PI'nın kendi kaydıdır (§2 madde 3)
```

### PI-3 — Temizlik maddeleri: akış ve sınır

Üç alan üst taslaktan aynen alındı:

```text
karar                 = r4-2'nin temizlik maddeleri (R41A-01…R41A-06) ve A-5'in ek olarak çıkarabileceği
                        temizlik maddeleri yeni bir düzeltme turu açmadan SONRAKİ DÖNGÜYLE BİRLİKTE
                        ilerleyebilir; AMA şu istisnayla:
istisna               = Gerçek-veri uyumunun gerçekten çalışacağı yola dokunan her kod maddesi (R41A-01 dahil)
                        gerçek-veri uyumu BAŞLAMADAN kapatılmış olmalıdır. R41A-01, r4-2 kapsamındadır ve
                        yürütücüye göre kapatıldı; A-5 bunu doğrular. A-5 R41A-01'i tam kapalı bulmazsa,
                        gerçek-veri erişimi (real_data_access) false kalır ve madde kapanana kadar F3
                        gerçek-veri yürütmesi başlamaz
yalnız belge/kayıt    = Yalnızca belge veya kayıt niteliğindeki maddeler (özet blokları, erratum, tanım
                        düzeltmeleri) sonraki döngüyle birlikte taşınabilir
```

A-5'e göre durum ve PI'nın seçimleri:

```text
R41A-01 (istisnanın    (a) ve (c) KAPALI [A] [A-S]; (d) KAPALI [A]; (b) KAPALI [A-S], PI'nın 2026-09-30 mesajıyla
 koşulu için)           kabul ettiği kriter bazındaki okumaya göre (kabulün kendisi [X]); A-5'in açık saydığı PI
                        kaydı bu kayıttır (PI-4, KABUL)
R41A-02, -03, -06      KAPALI [A]; R41A-02'de kopyalama zamanı [X]
R41A-05                KAPALI [A]; bilgi düzeyinde üç kusur, R42A-05
R41A-04                KISMEN KAPALI; kalan kısmı R42A-01 (a)
R42A-01 (cleanup;      kayıtlar eksik: rapor hash bloğu (register, deneme günlüğü, kesinti notu, dört launch log'u
 yetki X)               ve deneme-1 kopyası tam hash'le basılmamış); iletim listesi kesinti notunu (a4b5e176…)
                        yalnız sidecar'ıyla veriyor; parents_unchanged re-hash değerleri basılmamış. Yalnız kayıt
                        maddesi
R42A-02 (cleanup;      PI-4 ile kapanır (bu kaydın imzasıyla)
 yetki T, PI)
R42A-03 (cleanup;      aşağıda
 yetki X)
R42A-09 (informational, fit_spline'da, gerçek yoldaki kodda: bir bağlamın etiketi, süreçte aynı fikstür ve maske
 latent)                kimliğiyle daha önce kaydedilmiş yakalamalardan da türetilir; kriterler her durumda tutulur,
                        yalnız etiket ve yalnız doğal yöne değişebilir; A-5: "none in this cycle", yetki X (if
                        ever addressed)
R42A-04 … R42A-10      diğerleri informational; A-5'e göre eylem gerekmez (R42A-05 (i), R42A-01 ile aynı kayıt
                        child'ında düzeltilebilir)

R42A-01 yolu          = İLK YOL (PI, 2026-10-01): bir sonraki döngünün ilk kaydında (başlangıç envanteri) r4-2
                        paketinin her dosyası tam hash'iyle, r4-1 ve r4 paketleri yeniden hash'leriyle listelenir ve
                        R41A-04 yanıt satırı için bir erratum satırı yazılır (yanıt satırı bloğun gösterdiğine göre).
                        Bu, o döngünün talimatına girer (yalnız kayıt maddesi). İkinci yol seçilmedi: A-5 §1 r4
                        paketinin yeniden hash'ini içermez, R42A-01 (c)'yi karşılamaz ve bir denetim kaydını custody
                        defterine çevirirdi
R42A-03 sınıfı        = (b) gerçek-veri yoluna dokunabilecek kod maddesi (PI, 2026-10-01): istisna uygulanır,
                        gerçek-veri uyumu başlamadan kapatılır. Kapanış gerçek-veri hazırlık talimatına girer
                        (A-5'in kapanış eylemi, aşağıda (iv)). PI gerçek-veri koşusunun katmansız olacağına ayrıca
                        karar verirse bu sınıf yeni bir PI kaydıyla (a)'ya çevrilebilir
  olgular (bilgi)       (i)   tekrar oynatma yalnız birim-test fazındaki üç INJ-EXC-* fikstürünü etkiler (yalnız
                              TEST_ONLY enjeksiyonlu); değerlendirme nesneleri, stop kayıtları, artık serileri ve
                              RUN1 == RUN2 etkilenmez [A]
                        (ii)  units_read_from_store sayacı yalnız kaba birimleri sayar (harness L3135, L3237,
                              L3327); fit_spline içinde depodan okunan mod birimlerini (L1104–1105) saymaz [A].
                              D-3 §8.3 şunu ister: "the results JSON reports, per run label, the units computed by
                              the final process and the units read from the store, with their pids". Bu yüzden mod
                              birimi okunan bir koşuda okuma kaydı eksik kalır (r4-2'de olduğu gibi). Bu karar
                              kaydı, gerçek-veri yürütmesinin bu katmanı kullanıp kullanmayacağını belirlemez
                        (iii) aynı örüntü r4 ve r4-1 telemetrisinde de var; A-2 … A-4 görmedi (A-5 R42A-03)
                        (iv)  A-5'in kapanış eylemi (yetki X): "report fine-grained store reads, or state that the
                              counter is coarse and list the replayed units; if the second pass is meant as
                              determinism evidence, give it its own key namespace as RUN1/RUN2 have"
```

### PI-4 — R41A-01 (b) karışık-etiket kuralı: kriter bazında okuma (R42A-02)

```text
karar                 = KABUL (PI, 2026-10-01; §5)
                        PI'nın 2026-09-30 mesajı okumayı kabul etmiş ve register ile raporda yazılmasını istemişti
                        (dayanak); D-7 §3 (2)'nin yerine geçme kararı bu kayıtla verildi
konu                  = Bir cinsiyette hem doğal hem enjekte bekleyen (pending) olay varsa etiket KRİTER BAZINDA
                        belirlenir: her yönlendirilen kriter yalnız okuduğu bağlamlardan gelen etiketi taşır (full →
                        C3, C4b; fold → C2; probe → C4b; C4a yönlendirilmez); iki tür AYNI kritere ulaşırsa
                        F3-STEP2-EXACT-04 kullanılır (bir kriterin bağlamları içinde doğal etiket kazanır).
                        Rapordaki örnek (aynı cinsiyette enjekte full + doğal probeL): C3 = TEST_ONLY_INJECTED,
                        C4b = F3-STEP2-EXACT-04; rapor: "The natural event is never masked — it surfaces in C4b
                        and in the mechanism outcome." (r4-2 raporu §4, L84–87)
hüküm                 = İki türün FARKLI kriterlere ulaştığı bir cinsiyet için bu okuma, D-7 §3 (2)'nin cinsiyet
                        bazındaki ifadesinin yerine geçer: "(2) when a sex has both a natural and an injected
                        pending event, F3-STEP2-EXACT-04 is used;" (D-7 L77–78; D-7 ile kabul edildi, L83). İki tür
                        aynı kritere ulaştığında sonuç D-7 §3 (2) ile aynıdır. D-7'nin metni yeniden yazılmaz; bu
                        kayıt onun child'ıdır
kapsam (bilgi)        = r4-2, PI'nın 2026-09-30 mesajından sonra bu okumayla yürütüldü; bu kayıtla r4-2'nin bu
                        okumayla yürütülmüş olması yazılı bir PI kaydına dayanır
nitelik               = D-7 §3'ün drafter choices listesindeki bir mühendislik seçiminin değişimidir ("none a
                        scientific value", D-7 L75); yeni bilimsel literal yok; dondurulmuş hiçbir metne dokunmaz
etki                  = teslim edilen hiçbir çıktıyı değiştirmez: hiçbir fikstürde iki tür birlikte yok (A-5 R42A-02).
                        Okuma, T-SPL-PENDING-REALPATH'in "natural and injected, same sex" vakasında sınandı (C3 =
                        TEST_ONLY_INJECTED, C4b = F3-STEP2-EXACT-04), denetçinin ortamında yeniden üretildi [A-S];
                        denetçi probunda P6, P7 (aynı kriter) ve P8 (iki cinsiyet) beklendiği gibi [A-S] (A-5 §5)
ilgili (bilgi; PI-4'ün  (1) r4-2 talimatının kural cümlesi "if a sex has both kinds for the criteria it routes" der
 hükmüne dahil değil)       (L80–81) ve yürütücü onu kriter bazında okudu; talimatın vaka satırı cinsiyet bazında
                            yazılmıştır (L91–92) (A-5 R42A-02). Talimat yeniden yazılmaz
                        (2) iki tür birlikte varsa mekanizma sonucu doğal etiketi taşır (harness L1639); r4-1
                            etiketleri birleştiriyordu (A-5 R42A-04, informational; teslim edilen hiçbir çıktı
                            değişmedi)
dayanak (bilgi için)  = PI mesajı, 2026-09-30, yürütücünün aktarımıyla (r4-2 raporu §1, L32) [X]: "R41A-01 (b)
                        için kriter bazındaki okuman kabul; register satırında ve raporda açıkça yaz. Devam et."
                        Okumanın yazılı hali: r4-2 raporu §4 (L76–91); register satırı PIN-SPLINE-PENDING-TAG-SCOPE
                        (L49). A-5'in kapanış eylemi (yetki T, PI): "a PI-owned record (child of D-7) stating that
                        the per-criterion reading supersedes D-7 §3 (2) for a sex whose two kinds reach different
                        criteria"
```

## 2. Yürütücüye (Claude Code) talimatın sınırı

```text
Bu kayıt imzalı ve V-2 sağlanmış olarak elinize ulaştığında:
  1. Kaydı (D-8) ayrı .sha256 sidecar'ıyla, adını değiştirmeden, D-7 ve A-4'ün durduğu dizine koyun:
     p_konum_plus/prompts/ (r4-2 harness L374, L377). Kendi hash'ini içine yazmayın
  2. A-5'i (9111bc71…) sidecar'ıyla aynı dizine koyun: girdi, direktif değil; V-2 onun verdict'ine dayanır
  3. Başka hiçbir dosya yazmayın; hiçbir dosyayı değiştirmeyin, taşımayın, yeniden adlandırmayın ya da silmeyin.
     PI-1 … PI-4 ve PI-2 (ii)'deki cümle, PI'nın F3_STEP2 sonucunu yazacağı kendi kaydına (örneğin QUALIFIED
     kararını verdiği kayda) PI tarafından taşınır; o kaydı yürütücü oluşturmaz
  4. Dondurulmuş ya da onaylanmış hiçbir metni, hash'i veya parametreyi DEĞİŞTİRMEYİN
  5. F3_STEP2 = QUALIFIED ilan ETMEYİN: bu PI'nın ayrı bir eylemidir (§3)
  6. Bu kayıt kod değişikliği, yeniden koşu ya da yeni teslim talimatı içermez (R42A-01 ve R42A-03 dahil); bunlar
     ancak ayrı bir talimat ve PI dispatch kaydıyla verilir
V-1 veya V-2 sağlanmamışsa bu kayıttan hiçbir iş çıkarılmaz.
```

## 3. Bu kayıt ne yapmaz

```text
F3_STEP2 = QUALIFIED        = bu kayıtla İLAN EDİLMEZ. PI-1 ve PI-2 kabul edilir ve A-5 temiz çıkarsa
                              QUALIFIED ilanı PI'nın ayrı, imzalı bir eylemidir
F3_EXECUTION_READY          = bu kayıtla değişmez
real_data_access            = bu kayıtla değişmez (false kalır)
gerçek-veri yürütmesi       = bu kayıt gerçek veri yürütmesini yetkilendirmez; mevcut yürütmeye geçiş koşulları ve
                              PI yetkilendirmesi ayrıca sağlanmalıdır
F4–F8                       = v11 §22 dondurma sırasındaki bu kapıların hiçbirini açmaz, onlar hakkında hüküm içermez
A-5                         = bu kayıt A-5'i kabul etmez, değiştirmez, yeniden değerlendirmez; bulgularını aktarır
                              (V-2 onun verdict'ine dayanır)
commit                      = false (bu kayıt commit talimatı içermez)
```

## 4. Atıf yapılan kayıtlar (hash'ler bu oturumun elindeki kopyalar üzerinde hesaplandı; komut ve çıktı §7)

| Kayıt | Dosya | SHA256 |
|---|---|---|
| üst taslak | `f3_step2_r4-2_pi_decision_record_DRAFT_2026-10-01.md` | `1581f3be22f1f8556d1570f19c489ee67264186dc31d9bdae2a98c10b0d376d7` |
| revize child taslak (DRAFT r1) | `f3_step2_r4-2_pi_decision_record_DRAFT_r1_2026-10-01.md` | `eb10db1b8de640c6103318614ad826661295f3be058b220ebfa44807d2075f63` |
| D-7 (r4-2 PI dispatch) | `f3_step2_r4-2_pi_dispatch_record_2026-09-30.md` | `a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb` |
| D-6 (r4-1 PI dispatch) | `f3_step2_r4-1_pi_dispatch_record_2026-09-29.md` | `a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0` |
| D-5 (r4 PI dispatch) | `f3_step2_r4_pi_dispatch_record_2026-09-24.md` | `0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851` |
| D-3 | `Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md` | `5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5` |
| r4-2 talimatı | `Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md` | `d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe` |
| A-4 (r4-1 denetimi) | `f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md` | `ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82` |
| A-5 (r4-2 denetimi) | `f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md` | `9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575` |
| A-5 kanıt zip'i | `f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_auditor_evidence.zip` | `7990ee33a1f60a6062e4f48c1cd672fc2308d5eff9fcbe3bb19667ccd0fa4a3c` |
| r4-2 teslim zip'i | `f3_step2_r4-2_delivery_2026-09-30.zip` | `3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad` |
| r4-2 düzeltme raporu | `f3_step2_correction_report_r4-2_2026-09-30.md` | `7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6` |
| r4-2 register | `f3_step2_class_c_pin_register_r4-2_2026-09-30.md` | `c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c` |
| r4-2 sonuç JSON'u | `f3_step2_results_r4-2_2026-09-30.json` | `f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba` |
| r4-2 harness (deneme 2) | `f3_step2_adequacy_harness_r4-2_2026-09-30.py` | `b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730` |
| r4-2 harness (deneme 1, karantina kopyası) | `f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py` | `9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74` |
| r4-2 custody, deneme 2 | `f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md` | `766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1` |
| r4-2 deneme günlüğü | `f3_step2_r4-2_attempt_log_2026-09-30.md` | `b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65` |
| r4-2 launch 1 stdout | `f3_step2_r4-2_launch1_stdout_2026-09-30.log` | `5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083` |
| r4-2 launch 2 stdout | `f3_step2_r4-2_launch2_stdout_2026-09-30.log` | `3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7` |
| r3 deneme günlüğü | `f3_step2_r3_attempt_log_2026-09-22.md` | `253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5` |
| r4 deneme günlüğü | `f3_step2_r4_attempt_log_2026-09-24.md` | `8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69` |
| r4-1 deneme günlüğü | `f3_step2_r4-1_attempt_log_2026-09-29.md` | `ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739` |
| v11 | `ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md` | `d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3` |

Not: r4-2'nin denetçiye giden zip'i (`3a93e558…`) A-5 §1'de bu oturumca hesaplandı ve içindeki 27 dosya kendi
sidecar'larıyla doğrulandı [A]; üst taslaktaki "bu oturum onu doğrulamadı" notu üst taslağı hazırlayan oturum
içindir. Bu tablo bir doğrulama talimatı değildir; yürütücünün doğrulayacağı dosyalar §2'dekilerdir.

## 5. İmza

```text
Bu kaydı okudum. PI-1 … PI-4 kararlarımın ve PI-1 ile PI-3'te işaretlediğim seçimlerin, §0'daki geçerlilik
koşullarıyla (V-1, V-2) birlikte kayda geçmesini istiyorum.

PI                    = Öner
imza / onay           = ONAYLANDI. PI'nın 2026-10-01 tarihli Cowork mesajı, aynen:
                        «tamam önerilerini onaylıyorum (§2'deki tanımsız "sonuç/durum kaydı": daraltın. önerisi
                        dahil) onaylanmış halde imzalı sürümü, yeni sidecar'ı ve iletme mesajını hazırla»
                        Kaydın bu son metni PI'ya teslim edildi; PI'nın onu yürütücüye iletmesi, metni ve yukarıdaki
                        beyanı benimsemesidir
date_time_local       = 2026-10-01, UTC+3
A-5 verdict (V-2)     = PASSED (A-5 §0: global blocker 0, kapıya özgü blocker 0)
onaylanan seçimler    = PI-1 KABUL ; ek tek-süreç koşusu GEREKMİYOR ; C-1' korunur ; PI-2 KABUL (değişmeden) ;
                        R42A-01 ilk yol ; R42A-03 (b) ; PI-4 KABUL ; §2 daraltıldı. Kaynak: Claude'un 2026-10-01
                        tarihli önerileri ve PI'nın yukarıdaki onayı
```

## 6. Değişiklikler

### 6.1 DRAFT r1'e göre (imzalı sürüm)

| # | yer | değişiklik | neden |
|---|---|---|---|
| 1 | başlık ve üst not | ad D-8; status SIGNED; date_time_local dolduruldu; drafts satırı iki taslağı hash'leriyle veriyor; prepared_by imzalı sürüme ve 2026-10-01 önerilerine göre güncellendi; taslak uyarısı yerine imza cümlesi | PI onayı |
| 2 | §0 | V-1 ve V-2 durumu: sağlandı; gerekçe cümlesi imzalı sürüme göre | §5; A-5 §0 |
| 3 | §1 giriş | PI-1 ve PI-2'nin KABUL edildiği ve QUALIFIED'ın ayrı bir eylem olduğu yazıldı | PI onayı |
| 4 | PI-1 | karar KABUL; soru cümlesi karar cümlesi oldu; C-1' korundu; ek tek-süreç koşusu GEREKMİYOR; bilgi bloğu karar anındaki bilgi olarak bırakıldı, GEREKLİ seçeneğine ait cümleler ve taslakçı notu çıkarıldı; ikinci geçiş için R42A-03 yolu notu eklendi | PI onayı |
| 5 | PI-2 | onay satırı eklendi; karar, konu ve hükümler değişmedi | PI onayı; §2 madde 3 |
| 6 | PI-3 | üç alan aynen; R42A-01 ilk yol (sonraki döngünün ilk kaydı, erratum satırı dahil); R42A-03 (b) ve (a)'ya dönüş koşulu; R41A-01 ve R42A-02 satırları PI-4'e göre güncellendi | PI onayı |
| 7 | PI-4 | karar KABUL; karar notu ve kapsam cümlesi kararın verilmiş olmasına göre yazıldı | PI onayı |
| 8 | §2 | daraltıldı: yürütücü yalnız D-8 ve A-5'i sidecar'larıyla p_konum_plus/prompts/ dizinine koyar; başka dosya yazmaz; PI-1 … PI-4 ve PI-2 (ii) cümlesini PI kendi F3_STEP2 sonuç kaydına taşır | PI'nın onayladığı öneri (tanımsız sonuç/durum kaydı); dizin D-7 ve A-4'ünkü (r4-2 harness L374, L377) |
| 9 | §3 | A-5 satırındaki A-5 §1 hash listesi notu yerine V-2 notu | R42A-01'de ikinci yol seçilmedi |
| 10 | §4 | DRAFT r1 satırı; tablonun doğrulama talimatı olmadığı notu | soy; yürütücünün gereksiz yere durmaması |
| 11 | §5 | imza/onay (PI mesajı aynen), tarih, A-5 verdict ve onaylanan seçimler dolduruldu; benimseme notu | PI onayı |
| 12 | §7 | 24 dosyalık hash bloğu ve satır olguları yeniden üretildi | dürüstlük kuralı |

### 6.2 Üst taslaktan DRAFT r1'e (DRAFT r1 §6, aynen)

| # | yer | değişiklik | neden |
|---|---|---|---|
| 1 | başlık | parent_draft satırı; bu child için prepared_by ve önceki maruziyet (D-7 §3 (2) için belirtilmeyen nokta dahil); what_this_record_is dört karar ve seçimlere genişledi; what_this_record_is_not'a A-5 ve PI-4/D-7 ilişkisi eklendi | child kaydının soyu; hazırlayanın A-5, D-7 ve PI-4'ün konusu üzerindeki maruziyeti; yeni alanlar |
| 2 | üst not | D-7 §5'in Türkçe tırnaklı ifadesi yerine D-7'deki alan adı (`not_decided_here`); A-4 §7 yerine A-5; revizyonun nedeni cümlesi | alıntı gibi görünen bir çevirinin yerine kaynaktaki ad; açık maddeleri artık A-5 sayıyor |
| 3 | §0 | V-2 hükmü PI-1 … PI-4'ü kapsar; V-2 durumu (A-5 PASSED, blocker 0) bilgi olarak eklendi; gerekçe cümlesi D-7 §5, A-4 §7 ve A-5 §7'ye bağlandı | A-5 artık var; gerekçe kaynakta okunan ifadeye indirildi |
| 4 | §1 giriş | PI-1 … PI-4'ün rolünü söyleyen iki cümle | PI-4 yeni |
| 5 | PI-1 karar | KABUL seçim kutusuna çevrildi; üst taslaktaki değer yanında | üst C-1'in bir parçası A-5 olgularıyla çelişiyor; üst taslağın kendi kuralıyla PI-1 PI'ya döndü |
| 6 | PI-1 konu | iki süreç arası kanıt tanımı çıkarıldı; D-3 §5 ve §8.3'ün değer bazlı kuralı yazıldı | o tanım A-4 §7'nin r4-1 için yazdığı durumdu; r4-2'de tek süreç vardır (A-5 §2) |
| 7 | PI-1 dayanak (a) | D-5'teki PI ifadesi ve D-4 halkası eklendi | değerin kaynağı |
| 8 | PI-1 dayanak (b) | yürütücünün beyanı aynen alıntılandı; gerekçesi D-3 kuralıyla düzeltildi | listede kalış nedeni geçmiş değil değerdir (D-3 §5, §8.3; A-5 §7) |
| 9 | PI-1 dayanak (c) | A-4 kanıt katmanı [A] yerine [A-S]; A-5 [A-S] eklendi | A-4'te yeniden üretim §5 Auditor execution [A-S] altındadır |
| 10 | PI-1 C-1 | yerine A-5 olguları (1)–(5) ve C-1' (taslakçı metni) | PI'nın 2026-10-01 seçimi; C-1'in katmanın kapalı olduğu varsayımı r4-2'de doğru değil (olgu (2)) |
| 11 | PI-1 ek tek-süreç koşusu | GEREKMİYOR seçim kutusuna çevrildi; alan adı korundu; ne gösterir, ne göstermez, yol, süre ve kesintiler bilgisi eklendi; yaklaşık bir saat yerine ölçülen süre | PI-1 bütünüyle PI'ya döndüğü için alt değeri de PI'nındır; süre sonuç JSON'unda okunur |
| 12 | PI-2 | karar, konu ve hükümler değişmedi; dayanağa A-5 C-28 eklendi; D-5 S7 yazımı D-5 §7 oldu | A-5 kapsam durumunu doğruladı; yazım |
| 13 | PI-3 | karar, istisna ve yalnız belge/kayıt üst taslaktan aynen; A-5'e göre durum (istisnanın R41A-01 koşuluna A-5'in cevabı dahil); R42A-09 ayrıca anıldı; R42A-01 yolu ve R42A-03 sınıfı için PI alanları | A-5 artık var; R42A-01 … R42A-03 yeni maddeler (A-5 §7); R42A-09 gerçek yoldaki kodda |
| 14 | PI-4 | eklendi, seçim kutusuyla | A-5 R42A-02 kapanış eylemi (yetki T, PI); PI'nın 2026-09-30 mesajı okumayı kabul etti, D-7 hakkında hüküm içermez |
| 15 | §2 | PI-1 … PI-4; madde 6 (kod, koşu veya teslim talimatı yok) | yeni alanların yürütücüye etkisi sınırlandı |
| 16 | §3 | F4–F8 ve A-5 satırları | bu kaydın kapsam sınırı |
| 17 | §4 | üst taslak, A-5, A-5 kanıt zip'i, teslim zip'i ve dayanak dosyaları eklendi; D-5'in dosya adı yazıldı; hash'ler bu oturumda hesaplandı; zip notu düzeltildi | atıfların her biri hesaplanmış hash'le |
| 18 | §5 | PI-1 … PI-4 ve seçim kutuları; cümle düzeltildi | yeni alanlar; dil |
| 19 | §7 | hash ve satır olgularının komut çıktısı | dürüstlük kuralı: kullanılan komut ve çıktı gösterilir |

## 7. Hash'ler ve satır olguları: komut ve çıktı

Hash'ler bu oturumun elindeki kopyalar üzerinde hesaplandı; kopyalar `cited_d8/` klasörüne kanonik adlarıyla kondu.
Bu kaydın kendi hash'i burada yoktur; ayrı `.sha256` dosyasındadır.

7.1 Komut: `sha256sum <24 dosya, §4 sırasıyla>` (sha256sum (GNU coreutils) 9.4). Çıktı:

```text
1581f3be22f1f8556d1570f19c489ee67264186dc31d9bdae2a98c10b0d376d7  f3_step2_r4-2_pi_decision_record_DRAFT_2026-10-01.md
eb10db1b8de640c6103318614ad826661295f3be058b220ebfa44807d2075f63  f3_step2_r4-2_pi_decision_record_DRAFT_r1_2026-10-01.md
a3e705093577135f9992685a483b2f0de343326da6c3aecbb278e7672e1ec1fb  f3_step2_r4-2_pi_dispatch_record_2026-09-30.md
a92a0518dd053a54b5baab63f0057b8304d5581afbb497da137f593d6c3fe3b0  f3_step2_r4-1_pi_dispatch_record_2026-09-29.md
0cd87ad5b95264f65e862bf6f6c84b0f2cbe9c5eb234b1cd85ed7cc4af36a851  f3_step2_r4_pi_dispatch_record_2026-09-24.md
5b0e19ea58ddd6557ee3bcf8f5bd3c314c52f32b9692ac377a90252b4bfba8f5  Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md
d668033867913f728050b1944178d2eb56c3a0a9e43299cc84b391409f354ffe  Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md
ad22293661393f84dfa0fe9dee5f64be17737b56f060fe42dac3e3d685a29c82  f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2026-09-30.md
9111bc71933f0fccfab213f785bea1d3b0f27e3b34a5da00dae0f83a78b57575  f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_2026-10-01.md
7990ee33a1f60a6062e4f48c1cd672fc2308d5eff9fcbe3bb19667ccd0fa4a3c  f3_step2_r4-2_independent_audit_claude-opus-5-5_DRAFT_r1_auditor_evidence.zip
3a93e558c78b37e32228498fe3ba634e6f80394ee06d6d64ea7fb33eb8855cad  f3_step2_r4-2_delivery_2026-09-30.zip
7754ba029724231dfaec7a8845f68cebfa18a4da090ad4c2b845fb6a54da8de6  f3_step2_correction_report_r4-2_2026-09-30.md
c281e713eac753ea5b39ca671fd2f3cf2b448b8c4280a12f408facb50b39fd1c  f3_step2_class_c_pin_register_r4-2_2026-09-30.md
f2a0a4d5a94de0e902d8403243f4fc92faa315468ec21213a64860f3efa1e1ba  f3_step2_results_r4-2_2026-09-30.json
b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730  f3_step2_adequacy_harness_r4-2_2026-09-30.py
9e4d2803101de6b48b69965882772c2f5a65d71ddce95269b4616dceb6731d74  f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py
766ad7b6c5b2d6c3703a889b2a4bfc56563ff134c97afe779be1498d3d839fe1  f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md
b69a591587867e431e6a4afc2522b3780511fc5056d8d4ee345c525cc1e8fd65  f3_step2_r4-2_attempt_log_2026-09-30.md
5d58afbbe845894bc27c294661eca143810b8903bf4de4a5207498b6bdedf083  f3_step2_r4-2_launch1_stdout_2026-09-30.log
3af46762c1339312b9a5c1182275a1970545c83b9c1978567605af05225c27a7  f3_step2_r4-2_launch2_stdout_2026-09-30.log
253163891bab5d2e2d457e08c853359082277f6d990014f454bcd4078996d6a5  f3_step2_r3_attempt_log_2026-09-22.md
8409014748679248cc65c25bb35c9003ae674724ea63184433bdcb419bf66f69  f3_step2_r4_attempt_log_2026-09-24.md
ee5b48623a842b2ed0c9e85e73d7127364646aaf478b254b0dc02727a87b1739  f3_step2_r4-1_attempt_log_2026-09-29.md
d136502f41b35810d5dfb8b958dff7d9d7b66afb27c90e0c3be641d53546b9e3  ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md
```

7.2 Komut: `python3 -B line_facts_d8.py` (betik 7.3'te). Çıktı — her satır: dosya anahtarı, satır numaraları, ilk
eşleşen satırın başı:

```text
PARENT L55        koşul C-1             = A-5, (b)'deki beyanı doğrular: r4-2'nin final koşusu baştan tek süreçti,
PARENT L56        başlatma katmanı kapalıydı ve T-SINGLE-PROCESS geçti. Doğrulanmazsa PI-1 düşer ve PI'ya
D7     L77        engines (T-SPL-PENDING-REALPATH), not a manifest fixture; (2) when a sex has both a natural
D7     L83        accepted_with_this_record = YES
D7     L103       not_decided_here           = whether the narrowed evidence of T-R2-2 is acceptable ; whether the
D7     L75        drafter choices       = the r4-2 instruction adds engineering choices of its drafter, none a sci
D5     L140       basis (informational): the PI's value of 2026-09-21 ("PI tercihim: T-R2-2 = AUTHORIZE_RESTART"),
D3     L391       conditions of §8.3. The value permits a narrower evidence contract (v6 §8 asks for
D3     L393       value, whether or not a restart layer comes to be used; the report says which (§10)
D3     L954       counters and telemetry rows (Y-01 T-CALLCOUNT); the results JSON reports, per run label, the
D3     L970       status      T-R2-2 stays in narrowed_evidence whether or not the layer was introduced (§5, §10)
D3     L939       interruption as the reason. Introducing it changes the harness, so the rule of §3 applies: the f
D3     L308       the manifest changes after W-3 for any reason — a defect found in a run included — then, before
D3     L311       repeated with a new record, and the report names every superseded record and file with its hash
D3     L930       under AUTHORIZE_RESTART: after the first interruption the executor may introduce a restart layer
D3     L937       The authorization permits a restart layer; it does not require one. Attempt 1 runs without it (§
INS    L80        natural event, TEST_ONLY_INJECTED for an injected one; if a sex has both kinds for the criteria
INS    L91        injection → an ordinary failure, no pending cell; a natural and an injected event in the same
REP    L32        R41A-01 (b) için kriter bazındaki okuman kabul; register satırında ve raporda açıkça yaz. Devam
REP    L68        pid; per-call split entirely pid 10412; units_read_from_store all 0).
REP    L76        ## 4. The R41A-01(b) reading — stated, as the PI directed
REP    L84        wins (`merge_pending_tags`). Concretely: an injected event in `full` and a natural one in
REP    L86        **C4b = F3-STEP2-EXACT-04** (natural wins where both arrive). The natural event is never
REP    L143       narrowed_evidence = [T-R2-2] (single-process THIS revision, but the narrowing concerns the
REG    L49        | **PIN-SPLINE-PENDING-TAG-SCOPE (NEW — the R41A-01(b) reading, stated for the auditor)** | r4-2
H      L374       D7_DISPATCH_RECORD_PATH = "p_konum_plus/prompts/f3_step2_r4-2_pi_dispatch_record_2026-09-30.md"
H      L377       AUDIT_A4_PATH = "p_konum_plus/prompts/f3_step2_r4-1_independent_audit_claude-opus-5-5_DRAFT_r1_2
H      L141       RESTART_LAYER_ACTIVE = True
H1     L61,137    beginning with RESTART_LAYER_ACTIVE = False; a restart layer only after a
H1     L152       LAUNCH_NUMBER = 1
H      L1104      mkey = "splmode_%s_%s_%s_%s" % (fixture_id, mask_id, m, xhash)
H      L1105      cached_mode = ckpt_load(mkey)
H      L3135      UNITS_READ_FROM_STORE["nr_gates"] += 1
H      L3237      UNITS_READ_FROM_STORE["unit_tests"] += 1
H      L3327      UNITS_READ_FROM_STORE[run_label] += 1
H      L1639      tag = merge_pending_tags(sorted(spl_tags))
C2     L93        restart_layer_active_at_this_W3 = True (r4-2 attempt 1 is ONE process from the
LOG    L67        zero units from the store (`units_read_from_store` all 0). **T-SINGLE-PROCESS therefore
L1     L40        PROGRESS SPL ctx 13 SCEN-A run1:F0:fold1
L2     L6         RESTART_LAYER_ACTIVE = True
L2     L146       RUN_COMPLETE 10412
V11    L1017      # 22. FINAL freeze sequence
V11    L1025      | **F4** | final-refit rule, parameter banks, source IDs, descriptors, label_fuzz | unstable/uns
V11    L1029      | **F8** | H*, empirical dependence representation, canonical response, robustness/transfer law
LG3    L21        | 1 | 1 (`6ddcc26d67df35c1e736f4031d9d17ba0f5fc46f6d1a08b486e071c6bd8b3c31`, `RESTART_LAYER_ACTI
LG3    L22        | 2 | 2 (`891574fca8a5dbb7a0e181c7cf92fd21c22ea1e2492ee266f052ca44f64a52bd`, restart layer intro
LG4    L26        | 2 | 29296 | 2026-09-26T13:25:59 | 13:59:38 (ctx 34) | **interrupted** externally (no error; ho
LG41   L21        | 1 | 19528 | 2026-09-29T20:24:03 | ~20:35 (ctx 41) | **interrupted** externally (no error; host
LOG    L42        ## Attempt 2 — harness b988e9628731f6d0736ea3eaa4e9b4b5816ef5b15caf560a99c15e53933d0730 (restart
LOG    L40        | 1 | launch1_stdout / launch1_stderr (5d58afbb… / d688ac98…) | 14804 | 2026-09-30 (evening) | (
r3    L21  #1  pid 4220  2026-09-22T12:22:28.806647 | stopped at RUN2 SCEN-A:F0:fold0 (ctx 41)   | interrupted
r3    L22  #2  pid 5232  2026-09-22T14:43:48.833968 | stopped at RUN2 SCEN-A:F0:fold4 (ctx 45)   | interrupted
r3    L23  #3  pid 8740  2026-09-23T13:37:05.516474 | `RUN_COMPLETE 8740`, exit 0                | completed
r3    L24  #4  pid 21380 2026-09-23T13:56:21.156411 | stopped at RUN2 SCEN-A:F0:fold1 (ctx 42)   | interrupted
r3    L25  #5  pid 24220 2026-09-23T19:32:32.616091 | end 2026-09-23T19:50:36.580655, exit 0     | completed
r3    L26  #6  pid 18036 2026-09-23T21:51:13.308056 | stopped at RUN2 SCEN-A:F0:full (ctx 40)    | interrupted
r3    L27  #7  pid — (never started) 2026-09-24                 | Python never opened the script             | operator error, not a harness or e
r3    L28  #8  pid 15252 2026-09-24T11:37:01.875876 | reached results-writing, then `AssertionEr | crashed on its own new assertion
r3    L29  #9  pid 10920 2026-09-24T12:02:04.573394 | stopped at RUN1 SCEN-A:M0:probeR (ctx 23)  | interrupted
r3    L30  #10 pid 1240  2026-09-24T14:27:44.558016 | end 2026-09-24T14:51:59.765920, exit 0     | completed, verified
r4    L21  #1  pid 30160 2026-09-26T13:04:38        | 13:23:21 (ctx 10)                          | crashed on its own new assertion
r4    L26  #2  pid 29296 2026-09-26T13:25:59        | 13:59:38 (ctx 34)                          | interrupted
r4    L31  #3  pid 27308 2026-09-26T14:55:16        | 15:29:43 (ctx 43)                          | interrupted
r4    L32  #4  pid 24680 2026-09-26T18:23:36        | 18:41:21 (exit 1)                          | stopped by T-CANON
r4    L37  #5  pid 25924 2026-09-26T18:43:34        | 19:30:00 (ctx 70)                          | interrupted
r4    L38  #6  pid 35860 2026-09-27T15:59:08        | 16:03:19 (exit 1)                          | stopped by T-CANON again
r4    L43  #7  pid 31388 2026-09-27T16:05:40        | 16:36:33 (ctx 33)                          | interrupted
r4    L44  #8  pid 29564 2026-09-27T17:44:22        | 18:06:15, **exit 0**                       | COMPLETED, VERIFIED
r4-1  L21  #1  pid 19528 2026-09-29T20:24:03        | ~20:35 (ctx 41)                            | interrupted
r4-1  L26  #2  pid 3348  2026-09-29T21:15:37        | ~22:06 (exit 1)                            | ran the ENTIRE computation
r4-1  L31  #3  pid 22616 2026-09-29T22:14:16        | (ctx 42)                                   | interrupted
r4-1  L32  #4  pid 7972  2026-09-30T12:44:02        | 13:03:07, **exit 0**                       | COMPLETED, VERIFIED
r4-2  L40  #1  pid 14804 2026-09-30 (evening)       | (ctx 13)                                   | interrupted
r4-2  L58  #2  pid 10412 2026-09-30T20:38:58        | 21:36:01, **exit 0**                       | COMPLETED, VERIFIED
```

7.3 Betik `line_facts_d8.py`:

```python
"""Line facts for the PI decision record D-8 (r4-2; signed 2026-10-01). Read-only: for every line number the record
cites, search the cited file (staged copies, hashes in section 7) for a fixed text and print file:line: text."""
import os
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cited_d8")
F = {"PARENT": "f3_step2_r4-2_pi_decision_record_DRAFT_2026-10-01.md",
     "D7": "f3_step2_r4-2_pi_dispatch_record_2026-09-30.md",
     "D5": "f3_step2_r4_pi_dispatch_record_2026-09-24.md",
     "D3": "Claude_Code_F3_STEP2_R3_CORRECTION_EXECUTION_PROMPT_DRAFT_v2.md",
     "INS": "Claude_Code_F3_STEP2_R4-2_CORRECTION_INSTRUCTION_2026-09-30.md",
     "REP": "f3_step2_correction_report_r4-2_2026-09-30.md",
     "REG": "f3_step2_class_c_pin_register_r4-2_2026-09-30.md",
     "H": "f3_step2_adequacy_harness_r4-2_2026-09-30.py",
     "H1": "f3_step2_adequacy_harness_r4-2_2026-09-30_ATTEMPT1_INTERRUPTED.py",
     "C2": "f3_step2_r4-2_preexecution_custody_attempt2_2026-09-30.md",
     "LOG": "f3_step2_r4-2_attempt_log_2026-09-30.md",
     "L1": "f3_step2_r4-2_launch1_stdout_2026-09-30.log",
     "L2": "f3_step2_r4-2_launch2_stdout_2026-09-30.log",
     "V11": "ssa_application_calibrated_benchmark_v11_FINAL_NORMATIVE_2026-08-27.md",
     "LG3": "f3_step2_r3_attempt_log_2026-09-22.md", "LG4": "f3_step2_r4_attempt_log_2026-09-24.md",
     "LG41": "f3_step2_r4-1_attempt_log_2026-09-29.md"}
PAT = [("PARENT", "koşul C-1"), ("PARENT", "Doğrulanmazsa PI-1 düşer"),
       ("D7", "(2) when a sex has both a natural"), ("D7", "accepted_with_this_record = YES"),
       ("D7", "not_decided_here"), ("D7", "none a scientific value"),
       ("D5", "PI tercihim: T-R2-2 = AUTHORIZE_RESTART"),
       ("D3", "The value permits a narrower evidence contract"), ("D3", "value, whether or not a restart layer comes to be used"),
       ("D3", "the results JSON reports, per run label"), ("D3", "T-R2-2 stays in narrowed_evidence"),
       ("D3", "Introducing it changes the harness, so the rule of §3 applies"),
       ("D3", "the manifest changes after W-3 for any reason"), ("D3", "repeated with a new record"),
       ("D3", "under AUTHORIZE_RESTART: after the first interruption"), ("D3", "Attempt 1 runs without it (§8.1)"),
       ("INS", "if a sex has both kinds for the criteria"), ("INS", "a natural and an injected event in the same"),
       ("REP", "R41A-01 (b) için kriter bazındaki okuman kabul"), ("REP", "units_read_from_store all 0"),
       ("REP", "## 4. The R41A-01(b) reading"), ("REP", "Concretely: an injected event in `full` and a natural one in"),
       ("REP", "The natural event is never"),
       ("REP", "narrowed_evidence = [T-R2-2] (single-process THIS revision"),
       ("REG", "| **PIN-SPLINE-PENDING-TAG-SCOPE"),
       ("H", "D7_DISPATCH_RECORD_PATH = "), ("H", "AUDIT_A4_PATH = "),
       ("H", "RESTART_LAYER_ACTIVE = True"), ("H1", "RESTART_LAYER_ACTIVE = False"), ("H1", "LAUNCH_NUMBER = 1"), ("H", 'mkey = "splmode_%s_%s_%s_%s"'), ("H", "cached_mode = ckpt_load(mkey)"),
       ("H", 'UNITS_READ_FROM_STORE["nr_gates"] += 1'), ("H", 'UNITS_READ_FROM_STORE["unit_tests"] += 1'),
       ("H", "UNITS_READ_FROM_STORE[run_label] += 1"), ("H", "tag = merge_pending_tags(sorted(spl_tags))"),
       ("C2", "restart_layer_active_at_this_W3 = True"), ("LOG", "zero units from the store"),
       ("L1", "PROGRESS SPL ctx 13"), ("L2", "RESTART_LAYER_ACTIVE = True"), ("L2", "RUN_COMPLETE 10412"),
       ("V11", "# 22. FINAL freeze sequence"), ("V11", "| **F4** |"), ("V11", "| **F8** |"),
       ("LG3", "RESTART_LAYER_ACTIVE=False"), ("LG3", "restart layer introduced"),
       ("LG4", "the restart layer is introduced next"), ("LG41", "the restart layer is introduced next"),
       ("LOG", "(restart layer ON, store empty)"), ("LOG", "NO store unit (layer off")]
for key, pat in PAT:
    lines = open(os.path.join(C, F[key]), encoding="utf-8").read().splitlines()
    hits = [i + 1 for i, l in enumerate(lines) if pat in l]
    first = lines[hits[0] - 1].strip()[:96].rstrip() if hits else ""
    print(("%-6s L%-9s %s" % (key, ",".join(map(str, hits)) or "NOT_FOUND", first)).rstrip())

# attempt logs: every table row as  log, attempt, pid, start, end/stop, first bold phrase of the outcome
import re
LOGS = (("r3", "f3_step2_r3_attempt_log_2026-09-22.md"), ("r4", "f3_step2_r4_attempt_log_2026-09-24.md"),
        ("r4-1", "f3_step2_r4-1_attempt_log_2026-09-29.md"), ("r4-2", "f3_step2_r4-2_attempt_log_2026-09-30.md"))
for lab, fn in LOGS:
    for i, l in enumerate(open(os.path.join(C, fn), encoding="utf-8").read().splitlines(), 1):
        m = re.match(r"^\| (\d+) \|", l)
        if not m:
            continue
        cells = [c.strip() for c in l.strip().strip("|").split(" | ")]
        bold = re.search(r"\*\*(.+?)\*\*", cells[-1])
        pid = next((c for c in cells[1:4] if re.fullmatch(r"\d{3,6}|— \(never started\)", c)), "?")
        print(("%-5s L%-3d #%-2s pid %-5s %-26s | %-42s | %s" % (lab, i, m.group(1), pid, cells[-3][:26] if len(cells) > 3 else "",
               cells[-2][:42], (bold.group(1) if bold else "")[:34])).rstrip())
```
