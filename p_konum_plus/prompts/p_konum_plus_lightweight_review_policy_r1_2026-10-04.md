# p_konum_plus — Talimat ve denetim döngüsü kuralı — PI yönetişim kaydı (D-11 r1) — 2026-10-04

> D-11'in (`p_konum_plus_lightweight_review_policy_2026-10-03.md`, `e42a9caf…`) r1'idir ve onun yerine geçer; D-11
> hiçbir yere yerleştirilmedi, metni yeniden yazılmaz. D-10 ve D-9'un child'ıdır. **PI'nın 2026-10-04 tarihli
> talimatıyla hazırlanmış imzalı son metindir (§11).** İçine kendi hash'i yazılmaz; hash'i ayrı bir `.sha256`
> dosyasında durur. D-11'e göre değişiklikler §13'te.

```text
record              = p_konum_plus_lightweight_review_policy_r1_2026-10-04.md   (D-11 r1)
record_class        = PI-owned yönetişim kaydı: F3'ün kalanı ve F4 … F12 için talimat ve denetim döngüsünün kuralı
status              = SIGNED (PI talimatı, 2026-10-04; §11)
supersedes          = p_konum_plus_lightweight_review_policy_2026-10-03.md
                      e42a9cafa3ea4161dba3b9e11fe31b7ada8c07cb6a7101f58f1e9e6d0d057e0d (D-11; yerleştirilmedi)
base_content        = review_policy_v4.md 971813d80905ea92e1131b32ed9423bb80de01ad795ac6eeaf8c51119b29e7e2
                      (§0 … §9 bu metinden; dört değişiklik §13'te)
supersedes_draft    = p_konum_plus_lightweight_review_policy_DRAFT_2026-10-02.md
                      b4ea295d72b3675b430341fe6ffb6005154b4c61618c8c9e179cb26a8dbd6415 (imzalanmadı; hükümsüz)
basis               = PI'nın 2026-10-02 talimatı («Projenin kalanında aşağıdaki öneriyi izle: …»); iki dış eleştiri;
                      iki tur bağımsız eleştirmen kontrolü (4 + 2 eleştirmen)
prepared_by         = Claude (Claude Code bulut oturumu); D-9, rp1 talimatı, D-10 ve D-11'i de bu oturum hazırladı
timing              = F4 açılmadan ve hiçbir gerçek-veri sonucu görülmeden (repo başı fadf771; real_data_access = false)
what_this_record_is_not = v11'in, F1/F2/F3 STEP-1 dondurma kayıtlarının, D-2'nin, D-9'un ya da D-10'un değişimi değil;
                      hiçbir bilimsel kararı, eşiği ya da literal'i değiştirmez; rp1'e geriye uygulanmaz
```

## 0. Yer ve zaman
- Tek seferlik, numaralı, imzalı bir PI kaydı (D-11). F4 açılmadan ve hiçbir gerçek-veri sonucu görülmeden
  imzalanır (ön-kayıt). Kapı talimatları ona atıf yapar ve yalnız §8 bloğunu doldurur.
- Geriye uygulanmaz: rp1, D-10 ve rp1 §10 ile olduğu gibi yürür.
- v11 kapı başına denetim derinliği sabitlemez. Ama zorunlu inceleme ve onaylar vardır; D-11 bunların hiçbirini
  kaldırmaz, üstlerine bir sınıflandırma ekler:
  - F11 applicability audit ve QC (v11 L1032, L1225)
  - §24 zorunlu QC (L1202)
  - F12 tutarlılık incelemesi ve imza (L1033, L1248–1249)
  - protokol v0'da her kapının PI onay adımları (owner_or_authority satırları)
  - STEP-1 r1'in bağımsız geçiş kuralı (L525–526)
  - D-9 §2 (a)
- Döngü sınırlarının dayanağı v11 §25.29–30'dur: LLM uzlaşısı bağımsız kanıt değildir; yalnız ifade uzlaştırması
  için yeni tur açılmaz.

## 1. Değişmeyenler
- Bilimsel karar, eşik, literal, kapı geçişi ve QUALIFIED/READY ilanı yalnız PI'nındır.
- Outcome firewall: F12'den önce Claude Code hiçbir algorithm × CVI sonucu üretmez ve okumaz (v11 §28.6;
  protokol A-50).
- Gerçek-veri erişimi yalnız PI yetkisiyle olur.
- STOP davranışı korunur (v11 §28.8). Protokol v0 §9'daki STOP koşulları (L747 vd.) yazılı davranışlarıyla
  uygulanır.
- Dondurulmuş metin, hash ve parametre değişmez. Her teslimat yeni bir dosyadır, hash'li ve sidecar'lıdır;
  hiçbir dosyanın üzerine yazılmaz.
- Yürütücü kendi çıktısını denetlemez ve metodolojik çözüm önermez.
- D-9 §2 (a): gerçek-veri yolunda koşacak kodda ya da ortamda her fark için whitelist'siz non-regression,
  bağımsız denetim ve PI bağlaması gerekir. 6B kodu da bunun kapsamındadır.
- Protokol v0'da owner_or_authority'si PI içeren her pin ya da donma nesnesi, sınıfı ne olursa olsun ancak PI
  onayıyla kapanır.

## 2. Sınıf — DEĞİŞİKLİK başına
| Sınıf | Ne zaman | Kontrol |
|---|---|---|
| BİLİMSEL-a | henüz donmamış bir kural, tanım, literal, eşik türetme kuralı, seçim kuralı ya da sonuç yorumu donduruluyor/değişiyor; fit-failure, nonfinite ya da tie politikası; outcome firewall'u etkileyen her şey | TAM-a: imzadan önce yöntem incelemesi (§6'daki tek tur) + PI onayı |
| BİLİMSEL-b | bu paketin bir koşusu gerçek veriyi açıyor (real_data_access = true) ya da ondan yeni değer hesaplıyor; daha önce dondurulmuş bir kural uygulanarak değer hesaplanıyor | TAM-b: bağımsız uygulama doğrulaması (kurala madde madde eşleme, firewall) + PI onayı; kural yeniden incelenmez (v11 §28.3) |
| HESAPLAMA | veri okuma kodu, hesaplama, sınıflamayı değiştirmeyen hata yönetimi, yeniden üretilebilirlik — bu pakette yalnız sentetik ya da donmuş girdide koşan | TEKNİK: bağımsız oturum; değişen kısım + adı konmuş sonuç karşılaştırmaları (bilimsel nesnelerde whitelist yok) |
| KAYIT | açıklama, biçim; sonucu ve yeniden üretilebilirliği etkilemeyen kayıt | sonraki paketin başlangıç envanterinde kapanır; tur ya da koşu açmaz |
| YERLEŞTİRME | imzalı bir kaydın yerleştirilmesi ya da commit'i | yürütücü yerleştirmede hash'leri yeniden hesaplar (D-9 §7 gibi); §4 madde 1–2 ve commit durumu bir sonraki paketin başlangıç envanterinde ve onun denetiminde doğrulanır; ayrı denetim açılmaz |

- Taslakçı her değişikliğin sınıfını, "Ne zaman" sütunundaki tetikleyiciye dayanan tek satırlık bir gerekçeyle
  yazar. Gerekçesiz ya da belirsiz satır üst sınıfa çıkar.
- Sınıf talimat imzasıyla kesinleşir. Denetçi, somut kanıtla daha yüksek kontrol gerektiren bir tetikleyici
  saptarsa sınıfı yükseltir ve gerekçesini yazar. Sınıf düşürme yalnız PI'nın yazılı kararıyla yapılır.
- Donmuş bir metni uygulayan yeni bileşen o metne madde madde eşlenir. Metnin adlandırmadığı ve kodun bir değer ya
  da okuma seçtiği her noktada yürütücü durur; konu BİLİMSEL-a olur ve PI karar verir.
- F4 … F11'in donma eyleminde henüz donmamış kural, tanım ya da literal BİLİMSEL-a'dır. Aynı kapıda daha önce
  ayrı onayla dondurulmuş bir kural uygulanarak hesaplanan kısım BİLİMSEL-b'dir. Bu sınıflama D-11 ile
  şimdiden sabitlenir.

## 3. Kod-yol kuralı (D-8 PI-3'ün genel hali)
- Kapsam: daha sonraki bir BİLİMSEL paketin koşturacağı koda — ya da koşturmayacağı bir PI kaydıyla henüz
  dışlanmamış koda — dokunan her kod maddesi. "Temizlik" görünse bile.
- Madde, bağımlı hesaplama başlamadan önce kapanır. Kapanışı bağımsız bir denetim, teslim edilen baytlar üzerinde
  doğrular.
- Düzeltme ve doğrulama ayrı bir pakette ya da aynı paketin hazırlık aşamasında yapılabilir. Doğrulama
  tamamlanana kadar bağımlı hesaplama başlamaz; gerçek-veri adımı söz konusuysa real_data_access false kalır.
- Mevcut bağlayıcı kayıtların zorunlu ön denetimleri (ör. D-9 §2 (a)) korunur; bir kayıt ayrı paket
  gerektiriyorsa o kural geçerlidir.
- Şüphede madde bu kuralın kapsamındadır.

## 4. Asgari kontrol listesi — TEKNİK ve TAM denetimlerin hepsinde (TAM ⊇ §4)
- Madde 1, 2, 6 ve 7 her denetimde uygulanır.
- Madde 3–5, bu paketin koşusunda çalışan hesaplama yollarına uygulanır — yalnız değişen yollara değil (R42A-03
  değişmemiş koddaydı). Bu pakette koşmayan yollar için "uygulanamaz" gerekçesi yeterlidir.
- v11'in ve protokol v0'ın zorunlu kontrolleri bu daraltmanın dışındadır.

1. Hash ve custody: teslim edilen her dosya = sidecar = teslim listesi; parent'lar değişmemiş. Dondurulmuş üst
   akışta uyuşmazlık STOP'tur (D-3 §2.1; protokol STOP-01). Parent ya da dispatch dosyasında uyuşmazlık B'dir
   (D-3 §2.2–2.3). Kayıt-sınıfı eksik T'dir (D-3 §2.4).
2. Depo farkı (diff) yalnız beyan edilen değişiklikleri içeriyor. Son pakette yerleştirilen kayıtlar da burada
   doğrulanır.
3. Beyan edilen testler koştu ve geçti; beklentiler koşudan ÖNCE yazılmıştı. Gerçek-veri yolu ya da D-9 §2 (a)
   kapsamındaki pakette denetçi non-regression'ı ve zorunlu testleri kendi ortamında yeniden koşar ([A-S]) ve
   ortamı bağlı ortamla alan alan karşılaştırır.
4. Bilimsel nesnelerin non-regression'ı tuttu. Beklenen kayıt farkları önceden beyan edilmişti ve gözlenenle
   eşleşiyor.
5. Bağımsız türetme (A-2 … A-4'ün kaçırdığı türden): beyan edilen plandan faz ve anahtar ailesi başına beklenen
   hesap sayısı çıkarılır.
   - Taze telemetri satırları + kaydedilen depo okumaları bu sayıya eşit olmalı.
   - Depodaki tekil birimler anahtar ailesi başına buna uymalı.
   - Ayrı beyan edilmiş iki hesap aynı anahtarı paylaşmamalı.
   - Ayrı yürütmeler arasında wall-clock dahil birebir aynı telemetri satırı kırmızı bayraktır. İki tarafı aynı
     kayıtlı birimden gelebilen bir karşılaştırma testi de kırmızı bayraktır.
6. Firewall: açılan dosyalar listesinde beyan dışı bir gerçek-veri ya da sonuç yolu yok.
7. Envanterde "kapandı" denen her madde kanıtıyla doğrulanmış; kapanış noktası gelen her madde kapanmış.
- Kırmızı bayrak denetimi büyütmez: denetçi bulguyu §5'e göre sınıflar ve denetimi bitirir.

## 5. Bulgular
- STOP (düzeltme turu değildir): beyan dışı bir bilimsel nesne farkı, firewall şüphesi ya da protokol v0 §9'daki
  herhangi bir STOP koşulu. Örnekler: v11 hash uyuşmazlığı → halt; iki aday da F3'ten kalırsa → redesign; kapı
  STOP'u → kapı kapanamaz, no run. Protokolde yazılı davranış uygulanır, konu PI'ya gider; "devam" ya da
  "kayıtlı sınırlılık" seçenekleri bunlara uygulanmaz.
- B: teslim edilen baytlarda gözlenen ya da yeniden üretilen şunlardan biri:
  - (i) yanlış bilimsel sonuç ya da karar yoluna giren yanlış değer
  - (ii) parent ya da dispatch dosyasında custody bozulması (D-3 §2.2–2.3)
  - (iii) paketin bir kusurundan doğan karşılanmamış kapı ön-koşulu
- K: henüz yanlış sonuç vermemiş kod ya da hesap kusuru. Kapanış noktası:
  - kodu daha sonraki bir BİLİMSEL paket koşturacaksa → bağımlı hesaplama başlamadan önce (§3)
  - aksi halde → sonraki pakette TEKNİK denetimle
  - deftere ertelenmez
- T: yalnız §2 KAYIT satırına giren bulgu. Düzeltmesi kodu ya da hesaplanmış bir değeri değiştiren bulgu asla T
  değildir.
- I: eylem gerektirmez.
- Bir kuralın okunması ya da PI yetkisi gerektiren bulgu (ör. R42A-02) BİLİMSEL-a'dır ve PI onayıyla kapanır.
- Eşleme: global ya da gate-specific blocker → STOP ya da B; cleanup → kod/değer ise K, kayıt ise T, kural okuması
  ise BİLİMSEL-a; informational → I. Denetçi iki etiketi birlikte yazar.
- Denetçinin sınıfı geçerlidir. PI yalnız B önerilerini ve bir sınıfın düşürülmesini kesinleştirir; her biri
  mevcut bir PI kaydında ya da bir sonraki dispatch kaydında bir satırdır.
- Yeni düzeltme turunu yalnız B açar. B düzeltmesinin denetimi:
  - Düzeltmenin farkı §2'ye göre sınıflanır: kural ya da literal değişiyorsa TAM-a, değişmiyorsa TAM-b ya da
    TEKNİK.
  - Değişmesi beklenen bilimsel nesneler önceden adıyla beyan edilir.
  - Bilimsel bir nesneyi değiştiren düzeltmeden sonra PI nitelendirmeye yeniden karar verir.

## 6. Döngünün sınırları
- Paket döngüsü kapanır: §8'deki geçme ölçütü dispatch'ten önce yazılmışsa, her maddesi denetçinin kendi
  kontrolüyle karşılanmışsa, açık B ya da STOP yoksa ve kapanış noktası gelmiş K yoksa. Ölçüt sonradan
  genişletilmez.
- Aynı paketin ikinci B düzeltmesinden sonra yeni bir B çıkarsa, yeni tur açılmadan PI karar verir: devam,
  kayıtlı sınırlılık ya da STOP. "Devam" ya da "kayıtlı sınırlılık" kararı B'yi kapatmaz ve kapıyı geçmiş saymaz:
  B, açık madde olarak envanterde kalır; kapı ancak bu B'yi adıyla anan bir PI kaydıyla geçer.
- Talimat ve PI kaydı taslakları en fazla BİR inceleme turundan geçer; aynı sürüme paralel bakan denetçiler tek
  tur sayılır.
  - İkinci tur yalnız, taslak imzalanırsa bir B ya da STOP doğuracak bir bulgu varsa yapılır; inceleyici bunu
    bulguda açıkça yazar. "must_fix" etiketi tek başına yetmez.
  - Ondan sonra kalan maddeler imzada PI'nın kararına bırakılır.
  - İstisna: bir kaydın bağımsız geçişini şart koştuğu artefaktta (STEP-1 r1 L525–526; 6B spesifikasyonu) açık
    B varken artefakt geçmiş sayılmaz; PI yeni tur ya da STOP seçer.
- PI kararları kapı başına mümkün olduğunca TEK kayıtta toplanır.
  - Kapı prosedürü bir PI eylemini bir ölçümden önce istiyorsa, o eylem bağımlı adımı başlatan dispatch kaydında
    ya da ondan önce imzalanmış bir kayıtta yer alır. Aynı adımdan önce gereken eylemler tek kayıtta
    toplanabilir. Örnekler: F3 eşik değerlerinin seçimden önce onayı (protokol L259 adım 4); F10 Delta_eq
    (L404).
  - D-9 §2 (a) bağlaması, bağımsız denetimden sonra, bağımlı paketin dispatch kaydında bir satırdır.

## 7. Açık maddeler (temizlik defteri)
- Ayrı dosya yoktur. Defter her paketin başlangıç envanterinin bir bölümüdür ve önceki envanterin SHA256'sını
  taşır. Envanter zaten yeni ve etiketli bir dosyadır; hiçbir şeyin üzerine yazılmaz.
- İlk defter, rp1 denetiminden sonraki ilk paketin envanterinde o anda açık olan K ve T maddeleriyle açılır.
- Her madde şunları taşır: kimlik, kaynak (denetim ve bulgu no), sınıf, kapanış noktası, durum, kapandığı paket ve
  kanıtı.
- Kapanış noktası:
  - T → sonraki paket. Daha geç bir nokta ancak o paketin §8 bloğunda gerekçesiyle yazılır; en geç maddenin
    dokunduğu kapının kapanışıdır. F12 hiçbir zaman kapanış noktası değildir.
  - K → §5'teki gibi.
- Kapanmayan T bir sonraki paketin §8 bloğuna taşınır, tur açmaz. Ama dokunduğu kapı açık T varken COMPLETE
  sayılmaz (protokol v0 L99).
- Kapanmayan K: bağımlı adım başlamaz (§3).

## 8. Her kapı talimatındaki blok
```text
denetim ve kapanış (D-11 r1'e göre; talimat imzasıyla kesinleşir, denetçi yükseltebilir)
  değişiklikler, sınıfları ve gerekçeleri : <değişiklik — sınıf — tetikleyici>
  denetim türü                            : TAM-a / TAM-b / TEKNİK (her durumda §4)
  geçme ölçütü                            : <adı konmuş kanıtlar ve karşılaştırmalar; sonradan genişletilmez>
  kapı prosedürünün PI onayları           : <pin — protokol v0 satırı — hangi adımdan önce>
  D-9 §2 (a) bağlaması                    : evet, paket gerçek-veri yolunda koşacak bir dosyayı ya da ortam
                                            alanını değiştiriyorsa; şüphede evet
  kod-yol maddeleri (§3)                  : <madde — kapanacağı paket>
  bu pakette kapanacak açık maddeler      : <madde — kanıt>
  korunan zorunlu kontroller              : <v11 / protokol v0 §3 ve §9 / dondurulmuş kayıtlar / D-9 §2 (a)>
```

## 9. Yürürlükteki işler
- rp1: D-10 ve rp1 §10 aynen.
- 6B spesifikasyonu: BİLİMSEL-a → TAM-a (bağımsız oturum, PI ratifikasyonu).
- rp2 (6B kodu): HESAPLAMA → TEKNİK, şunlarla birlikte:
  - 6B spesifikasyonuna madde madde eşleme
  - çıktılarının hiçbir karar ya da seçim nesnesine ulaşmadığını gösteren test
  - D-9 §2 (a) bağlaması (gerçek-veri dispatch kaydında bir satır)
- F3 gerçek-veri yürütmesi:
  - BİLİMSEL-b → TAM-b
  - F1 yeniden-üretim kapısının (rp1 C-3) gerçek koşudaki sonucu kontrol edilir
  - Eşik değerleri seçimden önce onaylanır
  - Jeneratör seçimi F3'ün kapı kaydıdır
  - İki aday da kalırsa STOP-05 (redesign) uygulanır
- F4 … F11: §2'nin son maddesine göre; alt paketler §2'ye göre.
- F12: v11 ve protokol v0'da yazıldığı gibi.

## 10. Yürütücüye (Claude Code) talimatın sınırı

```text
Bu kayıt imzalı olarak elinize ulaştığında:
  1. Kaydı ayrı .sha256 sidecar'ıyla, adını değiştirmeden p_konum_plus/prompts/ altına koyun; kendi hash'ini
     içine yazmayın. Hash'i sidecar'a ve PI'nın iletim mesajındaki değere karşı yeniden hesaplayın; eşit
     değilse durun ve PI'ya bildirin
  2. Başka hiçbir dosya yazmayın, değiştirmeyin, taşımayın, silmeyin. Yürüyen rp1 işini bu kayıt değiştirmez
     (§0, §9): rp1, D-10 ve rp1 §10 ile olduğu gibi sürer. D-11 (e42a9caf…) yerleştirilmez
  3. Gerçek veri okumayın; commit yalnız PI'nın ayrı talimatıyla
```

## 11. İmza

```text
PI                    = Öner
imza / onay           = ONAYLANDI. PI'nın 2026-10-04 tarihli mesajı, aynen:
                        «D-11 r1'i bu düzeltmelerle hazırla»
                        Düzeltmeler, PI'ya 2026-10-03'te bir dış incelemeye yanıt olarak önerilen dört değişikliktir
                        (§13); D-11'in içeriği PI'nın 2026-10-03 onayıyla zaten kabul edilmişti. Bu son metin PI'ya
                        teslim edildi; PI'nın onu yürütücüye iletmesi, metni benimsemesidir
date_time_local       = 2026-10-04, UTC+3
```

## 12. Hash'ler (bu oturumda hesaplandı; komut ve çıktı)

```text
$ git ls-remote origin refs/heads/p_konum_plus
fadf771c75396a0d242f75f0c3ce7f3f0f4ed7e7	refs/heads/p_konum_plus
$ sha256sum review_policy_v4.md p_konum_plus_lightweight_review_policy_2026-10-03.md
971813d80905ea92e1131b32ed9423bb80de01ad795ac6eeaf8c51119b29e7e2  review_policy_v4.md
e42a9cafa3ea4161dba3b9e11fe31b7ada8c07cb6a7101f58f1e9e6d0d057e0d  p_konum_plus_lightweight_review_policy_2026-10-03.md
```

## 13. D-11'e (e42a9caf…) göre değişiklikler

| # | yer | değişiklik | neden |
|---|---|---|---|
| 1 | §3, §5 K | kod maddesi "ayrı paket" yerine "bağımlı hesaplama başlamadan önce" kapanır; aynı paketin hazırlık aşamasında düzeltme + bağımsız doğrulama mümkün; D-9 §2 (a) gibi zorunlu ön denetimler korunur | dış inceleme: ayrı paket şartı gereksiz döngü üretiyordu; güvenlik doğrulama-önce-hesaplama kuralıyla korunuyor |
| 2 | §2, §8 | denetçi sınıfı somut kanıtla yükseltebilir; düşürme yalnız PI'nın yazılı kararıyla | dış inceleme: "KAYIT" sayılan bir değişikliğin hesabı etkilediği denetimde anlaşılabilir |
| 3 | §6 | "devam" / "kayıtlı sınırlılık" B'yi kapatmaz, kapıyı geçmiş saymaz | dış inceleme: açıklık |
| 4 | §4 | madde 1, 2, 6, 7 her zaman; 3–5 bu pakette koşan yollara (değişenlerle sınırlı değil); koşmayan yollar "uygulanamaz"; zorunlu protokol kontrolleri hariç | dış inceleme (aşırı yük) + R42A-03'ün değişmemiş kodda olması |
